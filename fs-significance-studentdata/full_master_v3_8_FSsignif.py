# ========================= FULL MASTER v3.8_FSsignif =========================
# TABLE 3 — Binary (G3>=10)
# TABLE 4 — Five-Level (bins: [16,14,12,10] → 5 sınıf)
# TABLE 5 — Regression (RMSE)
# - Setuplar: A_All, B_NoG2, C_NoG1G2
# - Leak-free fold-içi FS + Feature-Selection Based Significance (Friedman+Wilcoxon)
# ============================================================================

!pip -q install factor-analyzer tabulate xgboost

import numpy as np, pandas as pd, time, warnings, os
from tabulate import tabulate
from collections import Counter, defaultdict
from scipy.stats import ttest_rel, t, friedmanchisquare, wilcoxon
from factor_analyzer import Rotator
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RepeatedStratifiedKFold, RepeatedKFold
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegressionCV, LassoCV
from sklearn.svm import LinearSVC, LinearSVR, SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neural_network import MLPClassifier, MLPRegressor
from xgboost import XGBClassifier, XGBRegressor
from sklearn.base import clone
from sklearn.metrics import accuracy_score
warnings.filterwarnings("ignore")

# -------------------- GLOBAL SETTINGS --------------------
PATH = "/content/student-mat.csv"
RANDOM = 42
THR_LOAD = 0.60
FAST_MODE = True       # True=3x2 CV, False=10x20 CV
EXPORT = True
os.makedirs("/content/results", exist_ok=True)
if FAST_MODE: N_SPLITS, N_REPEATS = 3, 2
else: N_SPLITS, N_REPEATS = 10, 20

# -------------------- HELPERS --------------------
def mean_pm_ci(scores, conf=0.95, mult=100):
    s = np.asarray(scores, float)
    m, sd = np.nanmean(s)*mult, np.nanstd(s, ddof=1)*mult
    tcrit = t.ppf(1-(1-conf)/2, len(s)-1) if len(s) > 1 else 0
    ci = tcrit*sd/np.sqrt(len(s)) if len(s) > 1 else 0
    return m, abs(ci)

def style_table(rows, headers, title):
    print(f"\n### {title}")
    print(tabulate(rows, headers=headers, tablefmt="github"))

def make_preprocessor(X):
    return ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"),
         X.select_dtypes(include="object").columns),
        ("num", Pipeline([
            ("imp", SimpleImputer(strategy="median")),
            ("sc", StandardScaler())
        ]), X.select_dtypes(exclude="object").columns)
    ])

# -------------------- Fold-içi Feature Selection --------------------
def fold_inner_fs(X_train, y_train, is_reg=False):
    pre = make_preprocessor(X_train)
    Xs = pre.fit_transform(X_train)
    Xs = pd.DataFrame(Xs.toarray() if hasattr(Xs, "toarray") else Xs,
                      columns=pre.get_feature_names_out())
    Xs = Xs.replace([np.inf, -np.inf], np.nan).fillna(0)
    Xs = Xs.loc[:, Xs.std(ddof=0) > 1e-8]
    feat_names = Xs.columns.tolist()
    if len(feat_names) <= 1:
        return {k: feat_names.copy() for k in ["Setup_Only","Varimax","LASSO","RFE","TreeImp","Min2_Methods","Union_All","Intersection_All"]}
    pca = PCA(svd_solver="full").fit(Xs)
    n90 = np.argmax(np.cumsum(pca.explained_variance_ratio_) >= 0.90) + 1
    L = Rotator(method="varimax").fit_transform(pca.components_[:n90].T)
    sel_varimax = [feat_names[i] for i in range(len(feat_names)) if np.any(np.abs(L[i,:]) >= THR_LOAD)]
    if not is_reg:
        lasso = LogisticRegressionCV(Cs=10, penalty="l1", solver="liblinear", cv=3, random_state=RANDOM)
        lasso.fit(Xs, y_train)
        coef = np.mean(np.abs(lasso.coef_), axis=0) if lasso.coef_.ndim>1 else np.abs(lasso.coef_)
        sel_lasso = [feat_names[i] for i,v in enumerate(coef) if v>1e-5]
    else:
        lasso = LassoCV(cv=3, random_state=RANDOM).fit(Xs, y_train)
        sel_lasso = [feat_names[i] for i,v in enumerate(np.abs(lasso.coef_)) if v>1e-5]
    from sklearn.feature_selection import RFE
    n_sel = max(1, min(int(len(feat_names)*0.3), len(feat_names)))
    base = LinearSVR(C=0.1, random_state=RANDOM) if is_reg else LinearSVC(C=0.1, dual=False, random_state=RANDOM)
    try:
        rfe = RFE(base, n_features_to_select=n_sel)
        rfe.fit(Xs, y_train)
        sel_rfe = [feat_names[i] for i,f in enumerate(rfe.support_) if f]
    except:
        sel_rfe = list(Xs.var(ddof=0).sort_values(ascending=False).index[:n_sel])
    rf = RandomForestRegressor(n_estimators=200, n_jobs=-1, random_state=RANDOM) if is_reg else RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=RANDOM)
    rf.fit(Xs, y_train)
    imp = rf.feature_importances_
    k = max(1, min(int(len(feat_names)*0.3), len(feat_names)))
    sel_tree = [feat_names[i] for i in np.argsort(imp)[::-1][:k]]
    sets = [set(sel_varimax), set(sel_lasso), set(sel_rfe), set(sel_tree)]
    all_feats = set().union(*sets)
    inter_feats = set(feat_names)
    for s in sets: inter_feats &= s
    cnt = Counter(sel_varimax + sel_lasso + sel_rfe + sel_tree)
    feat_min2 = [f for f,c in cnt.items() if c>=2]
    return {"Setup_Only": pre.get_feature_names_out().tolist(),
            "Varimax": sel_varimax, "LASSO": sel_lasso, "RFE": sel_rfe, "TreeImp": sel_tree,
            "Min2_Methods": feat_min2, "Union_All": list(all_feats), "Intersection_All": list(inter_feats)}

# -------------------- FS Significance --------------------
def fs_significance_across_methods(fs_results, model_name, setup_name, alpha=0.05, better="high"):
    fs_names=list(fs_results.keys())
    if "NVref" in fs_names: fs_names.remove("NVref")
    data=[fs_results[fs] for fs in fs_names if len(fs_results[fs])>1]
    if len(data)<3: return
    means={fs:np.nanmean(fs_results[fs]) for fs in fs_names}
    best=max(means,key=means.get) if better=="high" else min(means,key=means.get)
    stat,p= friedmanchisquare(*data)
    print(f"\n[Significance Test Summary — {model_name} ({setup_name})]")
    print(f"→ Friedman χ²={stat:.2f}, p={p:.3g} ",end="")
    if p<alpha: print("⇒ Significant overall difference")
    else: print("⇒ No significant overall difference")
    marks={fs:"" for fs in fs_names}
    for i,fs1 in enumerate(fs_names):
        for j,fs2 in enumerate(fs_names):
            if i>=j: continue
            s1,s2=np.array(fs_results[fs1]),np.array(fs_results[fs2])
            if len(s1)!=len(s2): continue
            try: stat,pw=wilcoxon(s1,s2)
            except: continue
            cond=(np.nanmean(s1)>np.nanmean(s2)) if better=="high" else (np.nanmean(s1)<np.nanmean(s2))
            if pw<alpha and cond: marks[fs1]+="↑"; marks[fs2]+="↓"
    marks[best]+="▲"
    if sum('↓' not in v for v in marks.values())==len(marks)-1: marks[best]+="†"
    print(", ".join([f"{k}{v}" for k,v in marks.items()]))
    print("\n**Legend:**\n↑ = better than ≥1 FS\n↓ = worse than ≥1 FS\n▲ = best mean\n† = superior to all (p<0.05)\n(baseline)=NVref, not tested\n")

# (Data loading, model setups, and evaluation code omitted here for brevity)
