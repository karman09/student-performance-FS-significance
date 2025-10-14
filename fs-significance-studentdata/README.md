#  Assessing the Methodological and Statistical Impact of Feature Selection in Student Performance Modeling

**Author:** Kevser ARMAN TUNÇER • **Year:** 2025  
📜 License: [MIT License](LICENSE)
📖 **How to Cite:**  
Arman Tunçer, K. (2025). *Assessing the Methodological and Statistical Impact of Feature Selection in Student Performance Modeling.*  
GitHub Repository: [https://github.com/karman09/student-performance-FS-significance](https://github.com/karman09/student-performance-FS-significance)

🎯 Research Aim and Scope

This study replicates and extends Cortez & Silva (2008) by developing a feature-selection-based analytical framework that integrates fold-inner (leak-free) feature selection, nested cross-validation, and statistical significance testing.

The overarching aim is to establish a statistically validated, interpretable, and reproducible benchmark for student performance prediction.

Unlike prior studies, which primarily relied on descriptive accuracy metrics, this research emphasizes methodological robustness and empirical interpretability by systematically comparing multiple feature selection mechanisms under consistent, leak-free experimental conditions.

Specifically, the study addresses three methodological limitations observed in prior replication efforts:

Feature redundancy and data leakage: Previous frameworks applied full-feature models without inner-fold filtering, leading to inflated estimates.

Lack of statistical inference: Model differences were reported descriptively without testing statistical significance.

Inconsistent FS validation: The relative stability and reliability of feature selection techniques across models were not systematically examined.

🎯 Main Research Objectives

To evaluate the impact of different feature selection strategies — Varimax, LASSO, RFE, Tree Importance, Union, and Intersection — on predictive performance across multiple setups (A_All, B_NoG2, C_NoG1G2) for binary, five-level, and regression tasks.

To determine whether feature-selection-based (FS-based) models produce statistically significant improvements over baseline (Naive) predictors in terms of both accuracy (PCC %) and error (RMSE).

To assess the stability and consistency of FS-driven model rankings using Friedman χ² and Wilcoxon–Holm corrected significance tests.

🧩 Theoretical and Methodological Contributions
1. Leak-Free Nested Evaluation

Implements a fold-inner feature selection procedure within nested cross-validation to prevent data leakage and obtain unbiased, reproducible estimates of model performance.

2. Comparative FS Mechanism Analysis

Provides a unified evaluation environment for four distinct FS mechanisms — statistical loading (Varimax), regularization (LASSO), recursive elimination (RFE), and ensemble importance (TreeImp) — and their hybrid combinations (Union_All, Intersection_All).

3. Significance-Based Model Validation

Extends beyond descriptive metrics by applying Friedman χ² and Wilcoxon–Holm tests to verify whether performance differences among FS-based models are statistically meaningful.

4. Cross-Task Generalizability

Evaluates the consistency of FS effects across binary classification, five-level classification, and regression (RMSE) tasks, ensuring robustness across problem types.

💡 In summary, this research bridges methodological rigor with empirical interpretability, offering a statistically validated and reproducible methodological extension of Cortez & Silva (2008) — grounded in modern feature-selection and significance-testing practices.


## 🎯 Research Aim and Hypotheses

This study replicates and extends Cortez & Silva (2008) by integrating feature-selection-based modeling and statistical significance testing to enhance the interpretability, 
robustness, and reliability of student performance prediction.

### Main Objectives
- Evaluate how different **feature selection strategies** (Varimax, LASSO, RFE, Tree Importance, Union, Intersection)  
  affect model performance across multiple setups (A, B, C).  
- Determine whether FS-based models provide **statistically significant improvements**  
  over baseline (Naive) predictors.  
- Assess consistency of model rankings using **Friedman and Wilcoxon Holm-corrected tests**.  


## 🧩 Theoretical and Methodological Contributions

1. **Methodological Extension:**  
   This work builds upon *Cortez & Silva (2008)* by incorporating advanced **feature selection (FS)** strategies  
   and **statistical validation** techniques, offering a more rigorous evaluation pipeline.

2. **Leak-Free Nested CV Framework:**  
   Introduces a **fold-inner feature selection** procedure to ensure leak-free evaluation,  
   strengthening the statistical validity and reproducibility of the original framework.

3. **Comparative FS Evaluation:**  
   Conducts a systematic comparison of multiple FS algorithms (Varimax, LASSO, RFE, TreeImp, Union, Intersection),  
   highlighting their relative influence on predictive performance and interpretability.

4. **Significance-Based Model Assessment:**  
   Extends beyond accuracy metrics by employing **Friedman χ² and Wilcoxon-Holm** tests  
   to statistically confirm differences in performance, rather than relying on descriptive means alone.


> 💡 *Overall, this research bridges methodological robustness with empirical interpretability —  
> offering  meaningful extension of the original 2008 study.*

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

Cortez, P., & Silva, A. (2008). *Using Data Mining to Predict Secondary School Student Performance.*  
Arman Tunçer, K. (2025). *Student Performance – Feature Selection & Significance (Extension of Cortez & Silva, 2008).* GitHub Repository.

---

## 📁 Repository Structure


