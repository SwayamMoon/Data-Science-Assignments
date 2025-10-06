# 🚗 Assignment 06: Multiple Linear Regression - Toyota Corolla Price Prediction

## 🎯 Project Goal (Maksad)
The core objective was to develop a **Multiple Linear Regression (MLR)** model to accurately predict the used car price of a Toyota Corolla based on key attributes (Age, KM, HP, Weight, etc.). The project also focused on addressing common linear regression challenges.

## 🛠️ Key Techniques & Models
* **Data Preprocessing:** Handled categorical variables (FuelType) using **One-Hot Encoding** and managed data scaling.
* **Model Building:** Constructed and compared **three different MLR models** to find the optimal feature set.
* **Regularization:** Applied **Ridge** and **Lasso** regression to address potential **Multicollinearity** (high correlation among predictors) and prevent overfitting.
* **Evaluation Metric:** Used **R-squared ($R^2$)** to measure the model's predictive power.

---

## 💡 Key Insights & Predictive Findings

### 1. Feature Significance
> Model coefficients (Betas) clearly indicated that **Age**, **Kilometers (KM)**, and **Horsepower (HP)** were the most statistically **significant negative predictors** of price. For instance, **Age** was the strongest factor, with every extra year in age leading to the highest drop in the predicted price.

### 2. Model Performance ($R^2$ Score)
> The final optimized MLR model achieved an **R-squared ($R^2$) score of approximately [Yahaan apni final R-squared value likhiye, jaise: 0.88]** on the test dataset. This high score indicates that the model successfully explains **[Value]%** of the variation in the car's price.

### 3. Regularization Effectiveness (Lasso & Ridge)
> **Lasso Regression** proved highly effective by shrinking the coefficients of less important features to zero, thereby acting as an **automatic feature selection** tool. This resulted in a more parsimonious and stable model compared to the standard MLR model.

### 4. Conclusion
> The project successfully built a robust price prediction model that provides valuable insights into the primary drivers of car value. The application of regularization techniques confirms the ability to handle complex, real-world data where multicollinearity may exist.
