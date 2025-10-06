# 🌳 Assignment 10: Decision Tree Classification - Heart Disease Prediction

## 🎯 Project Goal (Maksad)
The objective was to implement and optimize a **Decision Tree Classifier** to predict the presence of **Heart Disease** (`num` > 0 vs. `num` = 0) based on clinical data. The focus was on preprocessing the complex categorical data, tuning the model to prevent overfitting, and interpreting the final decision rules.

## 🛠️ Key Techniques & Optimization
* **Model:** Decision Tree Classifier.
* **Data Preprocessing:** Handled categorical features (e.g., `cp`, `thal`) using appropriate encoding methods.
* **Hyperparameter Tuning:** Used techniques like **GridSearchCV** to optimize hyperparameters such as `max_depth` and `min_samples_split` to balance bias and variance (prevent overfitting).
* **Model Evaluation:** Assessed performance using a full suite of metrics: **Accuracy, Precision, Recall, F1-Score,** and **ROC-AUC Score**.
* **Interpretability:** **Visualized the final decision tree** structure to understand the key diagnostic rules learned by the model.

---

## 💡 Key Insights & Decision Tree Learnings

### 1. Most Predictive Features
> The visualization of the Decision Tree clearly highlighted the **most influential features** in predicting heart disease. The top nodes, which determine the primary splits, often involved variables like **Chest Pain Type (`cp`), Maximum Heart Rate Achieved (`thalch`),** and **Exercise Induced Angina (`exang`)**.

### 2. Overfitting Mitigation
> Decision Trees are prone to overfitting. The use of **hyperparameter tuning** (specifically limiting `max_depth` to [Yahaan apni final max_depth value likhiye, jaise: 4]) and setting a minimum number of samples for splits was crucial. This pruning process resulted in a more **generalized** and **interpretable** model.

### 3. Model Performance
> The final optimized model achieved a satisfactory **Accuracy of approximately [Yahaan apni final Accuracy value likhiye, jaise: 84%]** and a **Recall score of [Yahaan apni final Recall value likhiye, jaise: 0.82]**. The high Recall is particularly important in medical diagnosis to minimize False Negatives (missing a patient with heart disease).

### 4. Conclusion
> This project successfully demonstrated the implementation and tuning of an interpretable classification model. The ability to **visualize the decision-making process** is a major strength of Decision Trees, allowing clinicians to trust and validate the model's predictions based on simple, understandable rules.
