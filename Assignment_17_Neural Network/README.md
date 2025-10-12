# 🌊 SONAR System Classifier: Mine vs. Rock Detection using Artificial Neural Networks (ANN)

## **🎯 Project Goal**

Is project ka mukhya uddeshya (main objective) **Artificial Neural Networks (ANN)** ka upyog karke underwater **SONAR** signals ko vargikrit (classify) karna hai. System ka lakshya (aim) hai ki woh pahchaan sake ki sonar return ek **metallic mine (M)** se hai ya ek **harmless rock (R)** se.

Yeh samundri suraksha (maritime safety) aur naval defense ke liye ek mahatvapurna **binary classification** samasya (problem) hai.

---

## **📂 Dataset Snapshot**

| Feature | Description | Details |
| :--- | :--- | :--- |
| **Data Source** | SONAR, Mines vs. Rocks Dataset | 208 Instances |
| **Inputs (Features)** | 60 Continuous Numeric Variables | Har feature ek frequency band mein signal energy hai (V1 to V60). |
| **Output (Target)** | Categorical (M / R) | 111 Mines (M), 97 Rocks (R) |

---

## **⚙️ Methodology and Implementation**

Project ko **Keras/TensorFlow** framework ka upyog karke nimnlikhit charanon (steps) mein poora kiya gaya:

### **1. Data Preprocessing**
* **Normalization:** 60 numeric features par **Standard Scaling (Normalization)** lagoo kiya gaya, jo ki gradient-based learning (jaise ki Neural Networks) ke liye critical hai.
* **Encoding:** Target variable (M/R) ko binary numeric format mein **Label Encoding** kiya gaya.
* **Splitting:** Data ko model training aur testing ke liye **Train-Test Split** mein baanta gaya.

### **2. Model Architecture (ANN)**
* Ek **Sequential Model** banaya gaya jismein kam se kam **ek Hidden Layer** shamil tha.
* **Activation Functions:** Hidden layers ke liye **ReLU** aur Output layer ke liye **Sigmoid** ka upyog kiya gaya (binary classification ke liye).
* **Optimizer:** Model ko **Adam** optimizer ka upyog karke compile kiya gaya.

### **3. Hyperparameter Tuning**
* Model ki performance ko behtar banane ke liye hyperparameters (jaise ki **number of neurons**, **number of hidden layers**, aur **dropout rate**) ko badal kar dekha gaya.
* **Grid Search** ya ek structured approach ka upyog tuning methodology ko systematic banata hai.

### **4. Evaluation**
Model ka parikshan (testing) test set par kiya gaya aur classification performance ko nimn metrics ka upyog karke measure kiya gaya:
* **Accuracy**
* **Precision** (Mine predictions ki vishwasniyata/reliability)
* **Recall** (Kitne mines sahi tarah se detect kiye gaye)
* **F1-Score** aur **Confusion Matrix**

---

## **📊 Key Findings**

* **Accuracy:** Tuned ANN model ne aam taur par **~76% - 80% tak ki classification accuracy** prapt ki.
* **Tuning Impact:** Hyperparameter tuning ne model ki **generalization kshamta** (generalization ability) ko thoda sudhaar diya, overfitting ko kam kiya.
* **Criticality:** Mine detection (Recall of 'M') par focus karna bahut zaroori hai.

---

## **💻 Setup and Usage**

1.  **Zaroori Libraries:**
    ```bash
    pip install pandas numpy scikit-learn tensorflow keras
    ```
2.  **Execution:**
    * `Neural_Network.ipynb` ko Jupyter ya Google Colab mein kholein.
    * Ensure karein ki `sonardataset.csv` file sahi location par uplabdh hai.
    * Code cells ko anukram (sequence) mein run karein.
