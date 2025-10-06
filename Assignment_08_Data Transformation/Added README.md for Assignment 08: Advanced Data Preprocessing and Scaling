# ⚙️ Assignment 08: Data Preprocessing & Advanced Feature Engineering

## 🎯 Project Goal (Maksad)
The primary objective of this project was to master and apply crucial **Data Preprocessing** and **Feature Engineering** techniques to the **Adult Income Dataset**. The goal is to transform raw data into a clean, scaled, and feature-rich format, significantly improving its readiness for high-performance Machine Learning models aimed at predicting income level (>50K or <=50K).

## 🛠️ Key Techniques & Concepts
* **Scaling:** Applied both **Standard Scaling** and **Min-Max Scaling** to numerical features, with a clear justification for choosing the appropriate method.
* **Encoding:** Implemented **One-Hot Encoding** for low-cardinality categorical variables and **Label Encoding** for high-cardinality features, discussing the trade-offs of each.
* **Feature Engineering:** Created new, highly predictive features by combining or transforming existing variables (e.g., binning 'age', creating family-related features).
* **Transformation:** Used **Log Transformation** on highly skewed numerical features (like `capital-gain`) to stabilize variance and achieve a more normal distribution.

---

## 💡 Key Learnings & Technical Insights

### 1. The Right Scaling Technique
> Standard Scaling (Z-score normalization) was preferred for numerical features, especially for linear models and algorithms that assume a normal distribution. In contrast, Min-Max Scaling was used to demonstrate normalization when the feature range needed to be strictly confined between [0, 1] (useful for neural networks).

### 2. Handling High vs. Low Cardinality Features
> **One-Hot Encoding** was chosen for features with few unique categories to avoid introducing false order. For features with many unique values (high cardinality), **Label Encoding** was selectively applied to manage the explosion of dimensionality (too many new columns), while acknowledging the potential risk of artificial ordinality.

### 3. Impact of Feature Engineering
> **Created new features** (like **'Working Hours per Week Category'**) that capture non-linear information and greatly enhance the model's ability to learn complex patterns. This step confirms the ability to go beyond basic data cleaning to extract maximum predictive power from the dataset.

### 4. Conclusion
> This comprehensive preprocessing pipeline successfully transformed the raw Adult Income dataset into an optimized format. Mastery of these techniques is fundamental, as data quality and feature design often contribute **more to model accuracy** than the choice of the machine learning algorithm itself.
