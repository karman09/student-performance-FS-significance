#  Assessing the Methodological and Statistical Impact of Feature Selection in Student Performance Modeling

### 🎯 Research Aim and Scope

This study extends *Cortez & Silva (2008)* by developing a **feature-selection-based framework** that integrates *fold-inner (leak-free) feature selection (FS)*, *nested cross-validation*, and *statistical significance testing*.

The project compares six FS strategies — **Varimax, LASSO, RFE, Tree Importance, Union, and Intersection** — across multiple setups (**A_All, B_NoG2, C_NoG1G2**) and tasks (binary classification, five-level classification, and regression).

Five **machine learning models** were used to evaluate FS effects on predictive performance: *Multi-Layer Perceptron (MLP), Support Vector Machine (SVM), Decision Tree (DT), Random Forest (RF),* and *XGBoost (XGB)*.  
A rule-based **Naive Predictor (NVref)** served as a baseline for statistical comparison.

By applying **Friedman χ²** and **Wilcoxon–Holm** tests, the study provides statistically validated, reproducible, and interpretable model comparisons — offering a modernized methodological extension of the reference study.

---
### ⚙️ Cross-Validation & Significance Testing

- **Nested Evaluation:**  
  - `RepeatedStratifiedKFold` *(10×20)* for classification  
  - `RepeatedKFold` *(10×20)* for regression  
- **Significance Tests:**  
  - *Friedman χ²* for overall FS comparison  
  - *Wilcoxon (Holm-corrected)* for pairwise significance  
- **Result Markers:**  
  - ▲ (best mean), † (statistically superior), * (better than baseline)



### 🧠 Data-Driven Hypotheses

| Code | Hypothesis |
|------|-------------|
| **H1** | Models with feature selection (FS) outperform the Naive Predictor, showing higher accuracy (PCC%) and lower error (RMSE). |
| **H2** | Different feature selection methods exhibit significant performance variations, indicating that the effectiveness of FS depends on the algorithmic mechanism and selection strategy. |
| **H3** | Removing G1 and G2 grade variables significantly reduces predictive accuracy. |
| **H4** | Performance differences among FS methods are statistically significant (p < 0.05). |
| **H5** | Hybrid FS approaches (Union_All, Intersection_All) achieve the best accuracy–stability balance and demonstrate the highest cross-model consistency. |


### 📊 Hypothesis Validation Summary

| Hypothesis | Expected Outcome | Empirical Evidence (Tables 1–3) | Conclusion |
|-------------|------------------|----------------------------------|-------------|
| **H1** | FS > NVref | FS methods achieved +2–10% higher PCC and lower RMSE. | ✅ Accepted |
| **H2** | FS methods differ in effectiveness | Significant variance among FS; Intersection_All best overall. | 🟡 Partially Supported |
| **H3** | Dropping G1/G2 reduces performance | Binary PCC: 91→83→67; RMSE worsened. | ✅ Accepted |
| **H4** | FS differences significant | Very low p-values (10⁻¹¹–10⁻⁷³) confirm significance. | ✅ Accepted |
| **H5** | Hybrid FS most consistent | Intersection_All showed top accuracy & stability. | ✅ Accepted |



## 📊 Example Outputs

| Table | Task Type | Metric | Visualization |
|:------|:-----------|:--------|:---------------|
| 🟩 **Table 1** | Binary Classification | PCC% | <img src="https://raw.githubusercontent.com/karman09/student-performance-FS-significance/main/fs-significance-studentdata/fs_significance/ikili.png" width="500"><br>_Binary classification results (FS-based accuracy comparison)_ |
| 🟨 **Table 2** | Five-Level Classification | PCC% | <img src="https://raw.githubusercontent.com/karman09/student-performance-FS-significance/main/fs-significance-studentdata/fs_significance/five.png" width="500"><br>_Five-level classification performance_ |
| 🟦 **Table 3** | Regression | RMSE ↓ | <img src="https://raw.githubusercontent.com/karman09/student-performance-FS-significance/main/fs-significance-studentdata/fs_significance/reg.png" width="500"><br>_Lower RMSE indicates better performance_ |

---

## ⚙️ Run in Google Colab
Open directly in Colab 👉  
[🔗 https://colab.research.google.com/drive/1CSaIn0OdfMlOPSIHUhu0_4hA2N3VQrlN?authuser=1](https://colab.research.google.com/drive/1CSaIn0OdfMlOPSIHUhu0_4hA2N3VQrlN?authuser=1)

> _This GitHub version mirrors the active Colab notebook used above._

---

## 🧾 How to Cite This Work

Arman Tunçer, K., 2025. Assessing the Methodological and Statistical Impact of Feature Selection in Student Performance Modeling. GitHub repository.
URL: https://github.com/karman09/student-performance-FS-significance

---
### References
Cortez, P., & Silva, A. (2008). *Using Data Mining to Predict Secondary School Student Performance.*  


