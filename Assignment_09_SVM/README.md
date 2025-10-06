# 💊 Assignment 09: Support Vector Machine (SVM) - Drug Response Prediction

## 🎯 Project Goal (Maksad)
The core objective was to build and optimize a **Support Vector Machine (SVM)** classification model to accurately predict a patient's **Drug Response** (0 = No Response, 1 = Positive Response) based on various biological features. This project emphasizes the power of SVM in complex, high-dimensional classification tasks like those found in the pharmaceutical industry.

## 🛠️ Key Techniques & Optimization
* **Model:** Support Vector Classifier (SVC).
* **Hyperparameter Tuning:** Applied **GridSearchCV** with **Cross-Validation** to systematically find the optimal combination of C (Regularization) and the **Kernel** type (Linear, RBF, Polynomial).
* **Model Evaluation:** Utilized **Classification Report** metrics (**Precision, Recall, F1-Score**) and **Confusion Matrix** to comprehensively evaluate the model's predictive ability.
* **Visualization:** Visualized the feature space and classification boundaries where possible to interpret the SVM's decision-making process.

---

## 💡 Key Insights & SVM Learnings

### 1. Kernel Performance Comparison
> Testing different kernels (Linear, RBF, Polynomial) revealed that the **[Yahaan apna best performing Kernel likhiye, jaise: Radial Basis Function (RBF) Kernel]** achieved the highest performance. This suggests that the relationship between patient biomarkers and drug response is **highly non-linear**, confirming the suitability of non-linear SVMs for this task.

### 2. High-Dimensional Effectiveness
> SVM is highly effective in separating classes even when the data lies in a high-dimensional feature space. The optimization successfully identified the **Optimal Hyperplane** that maximizes the margin between the 'Positive Response' and 'No Response' patient groups.

### 3. Model Robustness (Healthcare Context)
> The final optimized SVM model showed **high Precision/Recall scores** (especially on the positive class), making it a robust predictor. In the clinical context, this model can reduce the need for long and costly traditional clinical trials by predicting patient outcomes early.

### 4. Conclusion
> The project successfully implemented, tuned, and validated an SVM model for critical binary classification in the healthcare domain. Mastery of **GridSearchCV** and **Kernel selection** demonstrates a strong command over advanced machine learning techniques.
