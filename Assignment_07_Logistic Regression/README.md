# 🚢 Assignment 07: Logistic Regression - Titanic Survival Prediction

## 🎯 Project Goal (Maksad)
The core objective was to build and evaluate a **Logistic Regression** classification model to predict the probability of a passenger's **survival (1=Survived, 0=Did Not Survive)** on the Titanic tragedy. This project involved extensive **Data Preprocessing** and rigorous **Model Evaluation**.

## 🛠️ Key Techniques & Evaluation Metrics
* **Feature Engineering:** Extracted valuable information from the **'Name'** column (e.g., Title: Mr., Mrs., Master) for better predictive power.
* **Data Preprocessing:** Handled missing values (Median Imputation for Age, Mode for Embarked) and encoded categorical features (Sex, Pclass).
* **Evaluation Metrics:** Used **Accuracy, Precision, Recall, F1-Score,** and visualized the **ROC-AUC Curve** to assess model performance beyond simple accuracy.
* **Optional:** **Streamlit Deployment** for real-time model interaction.

---

## 💡 Key Insights & Classification Learnings

### 1. Survival Predictors (Model Interpretation)
> Logistic Regression **Coefficients** ki interpretation se pata chala ki **'Sex' (female)** aur **'Pclass' (First Class)** survival ke sabse **strong positive predictors** the. Yaani, "Women and children first" ka effect data mein clearly dikhta hai.

### 2. Model Performance & Trade-offs (ROC-AUC)
> The model achieved an **Accuracy** of approximately **[Yahaan apni final Accuracy value likhiye, jaise: 81%]** on the test set. More importantly, the **ROC-AUC score of [Yahaan apni final ROC-AUC value likhiye, jaise: 0.85]** confirms the model's high capability in distinguishing between the two classes (Survived vs. Not Survived).

### 3. Feature Importance through Engineering
> Creating a new **'Title'** feature from the 'Name' column significantly improved the model's accuracy, demonstrating the importance of **domain knowledge** and **feature engineering** in classification tasks.

### 4. Conclusion
> The project successfully delivered a highly interpretable and robust Logistic Regression model for binary classification. The focus on comprehensive evaluation metrics and feature engineering confirms readiness for real-world classification challenges, like churn prediction or loan default risk.
