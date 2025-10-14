# 💬 Automated Sentiment Analysis System: E-commerce Customer Review Classification

## **🎯 Project Goal (Maksad)**

The primary objective was to build an automated **Text Classification model** to analyze Amazon product reviews and classify the sentiment as either **Positive (`pos`)** or **Negative (`neg`)**.

This system aims to improve customer satisfaction by providing real-time feedback monitoring and quickly flagging products with adverse trends in negative reviews.

---

## **⚙️ Key Techniques & Workflow**

| Stage | Focus Area | NLP Techniques Used |
| :--- | :--- | :--- |
| **Data Cleaning** | Text preprocessing to ensure model stability and feature accuracy. | **Lowercasing**, HTML/URL Removal, Punctuation/Stopwords Removal |
| **Exploratory Analysis** | Understanding the distribution of sentiments and identifying key drivers. | Sentiment Distribution Check, **Word Clouds** (for most frequent words) |
| **Feature Extraction** | Converting unstructured text into a numerical format for machine learning. | **TF-IDF Vectorization** (Term Frequency-Inverse Document Frequency) |
| **Model Development** | Training robust linear models suitable for high-dimensional text data. | **Logistic Regression**, **Linear SVM (LinearSVC)** |
| **Evaluation** | Measuring the system's ability to generalize on unseen reviews. | **Accuracy**, **F1-Score**, Classification Report (80/20 Split) |

---

## **💡 Key Insights & Model Performance**

### **1. Feature Extraction Power**
> The **TF-IDF Vectorizer** (using unigrams and bigrams) proved highly effective in assigning greater weight to rare but sentiment-defining words (e.g., 'disappointed', 'excellent') over common words, resulting in highly predictive features.

### **2. Top Predictive Words**
> Analysis of model coefficients identified strong positive indicators like **'great', 'love',** and strong negative indicators like **'bad', 'waste', 'poor'**, validating the model's linguistic understanding.

### **3. Model Performance**
> The **Logistic Regression** model emerged as the best classifier, achieving superior performance due to its efficiency with linearly separable, sparse, high-dimensional TF-IDF features.

| Metric | Logistic Regression |
| :--- | :--- |
| **Accuracy** | **~85.5%** |
| **F1-Score** | **~0.85** |

### **4. Conclusion**
This project successfully implemented an efficient and accurate NLP pipeline for real-time sentiment monitoring. The combination of meticulous text cleaning and powerful **TF-IDF + Logistic Regression** provides a scalable solution for handling thousands of customer reviews daily.

---

## **💻 Setup and Execution**

1.  **Zaroori Libraries Install Karein:**
    ```bash
    pip install pandas numpy scikit-learn nltk re
    ```
2.  **Execution:**
    * `NLP.ipynb` Jupyter Notebook kholein.
    * Ensure karein ki data file (`reviews.csv` or similar) notebook ke saath uplabdh hai.
    * Code cells ko sequence mein run karein to perform the analysis and train the models.
