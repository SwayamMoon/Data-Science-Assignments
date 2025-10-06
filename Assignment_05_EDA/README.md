# 🔬 Assignment 05: Exploratory Data Analysis (EDA) on Fetal Health

## 🎯 Project Goal (Maksad)
The main goal of this assignment was to conduct a comprehensive **Exploratory Data Analysis (EDA)** on the **Cardiotocographic (CTG)** dataset, which contains features extracted from fetal heart rate monitoring.
This analysis aims to:
1.  Uncover underlying patterns and relationships among medical variables.
2.  Perform **robust data cleaning** (Missing Value Handling, Outlier Detection).
3.  Prepare the dataset for subsequent **Machine Learning classification models** for fetal health prediction.

## 🛠️ Tools and Techniques
* **Language:** Python
* **Libraries:** Pandas, NumPy, **Matplotlib, Seaborn** (for Advanced Visualization)
* **Techniques:** Statistical Summaries, **Correlation Heatmaps**, Pair Plots, IQR-based Outlier Detection.

---

## 💡 Key Insights & Data-Driven Findings

### 1. Robust Data Cleaning
> Dataset mein **Missing Values** ko check kiya gaya aur **Median Imputation** ka use karke successfully handle kiya gaya. Additionally, **Boxplots** aur **IQR method** se outliers ko identify kiya gaya, jisse data quality aur reliability ensure ki gayi.

### 2. Critical Feature Relationships (Correlation)
> **Correlation Heatmap** se pata chala ki **Baseline Fetal Heart Rate (LB)** ka **Mean Short Term Variability (MSTV)** aur **Percentage of Time with Abnormal Short Term Variability (ASTV)** jaise variables ke saath **significant inverse correlation** hai. Yeh relationship **Fetal Distress** ki condition ko directly highlight karti hai.

### 3. Feature Distribution and Skewness
> **Histograms** ne reveal kiya ki kaafi variables **Non-Normal** aur **highly skewed** hain (jaise Accelerations - AC, Decelerations - DL). Is finding ne yeh conclusion diya ki Machine Learning models mein **non-linear algorithms** ya **feature transformation (log/sqrt)** ki zaroorat pad sakti hai.

### 4. Conclusion
> The thorough EDA process provided a deep understanding of the CTG data's structure, helping to validate data quality and identify **key features** (like FHR Variability) that are most relevant for predicting the final **NSP (Fetal State Class)**. This prepared the foundation for high-accuracy predictive modeling.
