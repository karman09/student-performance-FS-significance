# Significance Analysis of Feature Selection on Student Performance

**Feature-Selection Significance Analysis on the UCI Student Performance Dataset**
*(Leak-free fold-internal feature selection + Friedman & Wilcoxon tests)*

> 📄 *Based on Cortez, P., & Silva, A. M. G. (2008).  
> “Using Data Mining to Predict Secondary School Student Performance,”  
> University of Minho, Portugal.*  
> [ResearchGate link](https://www.researchgate.net/publication/228780408) •  
> [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance)

This repository reproduces and extends **Cortez & Silva (2008)** by introducing  
a full statistical significance framework for comparing **feature selection methods**
(Varimax, LASSO, RFE, Tree Importance, etc.) across binary, five-level, and regression tasks.

--- 🔍 For the full implementation, see [full_master_v3_8_FSsignif.py](https://github.com/karman09/student-performance-FS-significance/blob/main/fs-significance-studentdata/full_master_v3_8_FSsignif.py)



## 🔹 Overview

- **Table 3** — Binary classification *(G3 ≥ 10)*  
- **Table 4** — Five-level classification *(bins: [16,14,12,10]) → 5 classes*  
- **Table 5** — Regression *(RMSE)*  
- **Setups:** A_All, B_NoG2, C_NoG1G2  
- **Feature selection:** Varimax, LASSO, RFE, TreeImp, Min2, Union_All, Intersection_All  
- **Significance tests:** Friedman χ² and pairwise Wilcoxon (p < 0.05)  
- **Leak-free:** Each fold applies inner feature selection independently  
- **Outputs:** ±95% CI, significance marks, and CSV exports

---

## ⚙️ Installation

```bash
git clone https://github.com/<your_username>/fs-significance-studentdata.git
cd fs-significance-studentdata
pip install -r requirements.txt
```

---

## ▶️ Usage Example (Colab or Local)

1️⃣ Place the original dataset [`student-mat.csv`](https://archive.ics.uci.edu/ml/datasets/Student+Performance)  
in `/content/` or your local path.

2️⃣ Run the master script:

```bash
python fs_significance/python fs_significance/full_master_v3_8_FSsignif.py
```

3️⃣ The program generates:
- `Table3_A_All.csv`, `Table4_B_NoG2.csv`, `Table5_C_NoG1G2.csv`  
- Formatted significance tables with marks and legend

---

## 🧩 Function Overview

| Function | Description |
|-----------|--------------|
| **fold_inner_fs()** | Performs *fold-internal feature selection* using PCA+Varimax, LASSO, RFE, and Random Forest importance; returns selected feature subsets and ensemble combinations (Min2, Union, Intersection). |
| **fs_significance_across_methods()** | Applies *Friedman* and *Wilcoxon signed-rank* tests across all feature selection strategies for each model and setup; adds performance marks ↑ ↓ ▲ † with detailed summary. |
| **RuleNVUniversal()** | Defines a universal rule-based baseline (NVref) based on G1/G2 grades; used as non-learning benchmark across all setups. |
| **make_models_class() / make_models_reg()** | Create benchmark ML models for classification and regression tasks (NN, SVM, DT, RF, XGB). |
| **mean_pm_ci()** | Calculates mean ± t-based confidence intervals (95%). |
| **style_table()** | Prints formatted tables in GitHub-style Markdown using `tabulate`. |

---

## 📊 Example Output

```
### TABLE 3 — Binary — A_All
| Feature Set (n) | NVref | NN | SVM | DT | RF | XGB | Time |
|------------------|-------|----|-----|----|----|-----|------|
| Varimax (29→22)  | 78.3±1.2 | 85.6±0.8↑ | 84.3±1.1 | 83.1±1.5↓ | 86.8±0.7▲† | 85.1±0.9↑ | 46.3s |

[Significance Test Summary — RF (A_All)]
→ Friedman χ²=13.48, p=0.015 ⇒ Significant overall difference  
Varimax↑, Min2_Methods↑, Union_All▲†, TreeImp↓

**Legend:**
↑ = better than ≥1 FS  
↓ = worse than ≥1 FS  
▲ = best mean performance  
† = superior to all others (p<0.05)  
(baseline) = NVref, not included in tests
```

---

## 📖 References

[1] **Cortez, P., & Silva, A. M. G. (2008).**  
*Using Data Mining to Predict Secondary School Student Performance.*  
University of Minho, Portugal.  
Published in *Proceedings of the 5th Future Business Technology Conference (FBTC 2008).*  
[ResearchGate link](https://www.researchgate.net/publication/228780408)  
[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance)

---

## ⚖️ License

Copyright (c) 2025 Kevser ARMAN TUNÇER

This project is licensed under the terms of the **MIT License (MIT)**.

You are free to use, modify, and distribute this code with attribution.  
See [LICENSE](LICENSE) for the full text.
