#  Assessing the Methodological and Statistical Impact of Feature Selection in Student Performance Modeling

**Author:** Kevser ARMAN TUNÇER • **Year:** 2025  
📜 License: [MIT License](LICENSE)
📖 **How to Cite:**  
Arman Tunçer, K. (2025). *Assessing the Methodological and Statistical Impact of Feature Selection in Student Performance Modeling.*  
GitHub Repository: [https://github.com/karman09/student-performance-FS-significance](https://github.com/karman09/student-performance-FS-significance)


---

## 🎯 Research Aim and Hypotheses

This study replicates and extends *Cortez & Silva (2008)* by integrating **feature-selection-based modeling**  
and **statistical significance testing** to improve interpretability and reliability of student performance prediction.

### Main Objectives
- Evaluate how different **feature selection strategies** (Varimax, LASSO, RFE, Tree Importance, Union, Intersection)  
  affect model performance across multiple setups (A, B, C).  
- Determine whether FS-based models provide **statistically significant improvements**  
  over baseline (Naive) predictors.  
- Assess consistency of model rankings using **Friedman and Wilcoxon Holm-corrected tests**.  

### Data-Driven Hypotheses
- **H1:** FS-based models outperform the Naive Predictor (higher PCC%, lower RMSE).  
- **H2:** Varimax and LASSO outperform other FS methods.  
- **H3:** Removing G1 and G2 grade variables significantly reduces model performance.  
- **H4:** Performance differences among FS methods are statistically significant (p < 0.05).  
- **H5:** Hybrid FS methods (Union / Intersection) provide the best accuracy–stability trade-off.  

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


---

> 💡 *Overall, this research bridges methodological robustness with empirical interpretability —  
> offering both replication and meaningful extension of the original 2008 study.*

## 📊 Results & Hypothesis Validation

Based on the empirical results obtained from `FULL MASTER v3.9_FSbased` (Tables 1–3):

| **Hypothesis** | **Expected Outcome** | **Empirical Evidence (Tables 1–3)** | **Conclusion** |
|:----------------|:---------------------|:------------------------------------|:----------------|
| **H1** | FS > NVref | FS methods achieved higher PCC (+2–10%) and lower RMSE. | ✅ **Accepted** |
| **H2** | Varimax/LASSO as top performers | Varimax & LASSO strong, but Intersection_All best overall. | ⚖️ **Partially Accepted** |
| **H3** | Drop in PCC, ↑ RMSE after removing G1/G2 | Binary PCC: 91→83→67; Regression worsens similarly. | ✅ **Accepted** |
| **H4** | Significant Friedman/Wilcoxon p-values | p-values extremely small (10⁻¹¹ – 10⁻⁷³). | ✅ **Accepted** |
| **H5** | Hybrid methods competitive | Intersection_All shows highest consistency and significance. | ✅ **Accepted** |

### 🔬 Summary Interpretation
- **Intersection_All** emerges as the most statistically consistent and best overall FS strategy.  
- **Varimax** and **LASSO** remain highly competitive but not always dominant.  
- Excluding grade variables (G1, G2) significantly reduces predictive power.  
- All FS-based models outperform the Naive Predictor in both classification and regression.  

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


