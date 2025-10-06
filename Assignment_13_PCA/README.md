# Principal Component Analysis (PCA) with Clustering

## 📌 Objective
This project explores the use of **Principal Component Analysis (PCA)** for dimensionality reduction and compares clustering performance on both the **original dataset** and the **PCA-transformed dataset**.

## 📂 Files Included
- **PCA.ipynb** → Jupyter Notebook with complete code implementation.  
- **PCA.docx** → Assignment documentation with step-by-step tasks.  
- **wine.csv** → Dataset used for PCA and clustering.  

## 📝 Tasks Performed
1. **Exploratory Data Analysis (EDA)**
   - Data loading, cleaning, and visualization (histograms, boxplots, correlations).  

2. **Dimensionality Reduction (PCA)**
   - Standardization of features.  
   - Implementation of PCA.  
   - Selection of optimal components (scree plot, explained variance).  
   - Transformation into new principal components.  

3. **Clustering with Original Data**
   - Applied **K-Means clustering**.  
   - Visualized cluster distribution.  
   - Evaluated using **Silhouette Score / Davies–Bouldin Index**.  

4. **Clustering with PCA Data**
   - Applied K-Means on PCA-transformed data.  
   - Compared clustering performance with original dataset.  

5. **Comparison & Analysis**
   - Observed performance differences.  
   - Analyzed trade-offs between high-dimensional vs reduced-dimension clustering.  

6. **Conclusion**
   - PCA simplifies data while retaining variance.  
   - PCA-based clustering may perform better in terms of efficiency and visualization.  

## 🚀 Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

## 📊 Key Insights
- PCA helps reduce noise and improves clustering visualization.  
- Clustering on PCA data may slightly reduce accuracy but increases interpretability.  
- Dimensionality reduction is beneficial for large datasets with many correlated features.  

---
