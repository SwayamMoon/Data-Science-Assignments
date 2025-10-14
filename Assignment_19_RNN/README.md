# 🥛 Dairy Production Forecasting: RNN, LSTM, and GRU Deep Learning Models

## **🎯 Project Goal (Maksad)**

The objective was to develop and compare three advanced **Recurrent Neural Network (RNN)** architectures—**SimpleRNN**, **Long Short-Term Memory (LSTM)**, and **Gated Recurrent Unit (GRU)**—to accurately forecast **Monthly Milk Production**.

The model aims to provide the dairy business with reliable, long-term forecasts to optimize supply chain, manage inventory, and make strategic operational decisions.

---

## **⚙️ Key Techniques & Deep Learning Workflow**

| Stage | Focus Area | Deep Learning Technique |
| :--- | :--- | :--- |
| **Data Preparation** | Preparing time series data for sequential deep learning models. | **MinMaxScaler (Normalization)**, Creating **Time Windows (Sequences)** |
| **Model Development** | Building and training three distinct sequence-aware models. | **SimpleRNN**, **LSTM**, and **GRU** Layers (using TensorFlow/Keras) |
| **Model Tuning** | Preventing overfitting and optimizing the learning process. | **Early Stopping** (patience), **ReduceLROnPlateau** (Learning Rate Schedule) |
| **Evaluation** | Assessing the quality of the time series forecast. | Plotting Predictions vs. Actuals, **RMSE**, **MAE**, **MAPE** |
| **Prediction** | Generating actionable future forecasts. | **12-Month Out-of-Sample Forecasting** |

---

## **💡 Key Insights & Model Comparison**

### **1. LSTM: The Top Performer**
> In time series forecasting, especially with data showing **strong seasonality and long-term dependencies** (jo ki milk production mein aam hai), **LSTM** generally outperformed SimpleRNN and GRU. LSTMs excelled at retaining long-term information due to their internal *cell state* and *gates*.

### **2. Importance of Data Scaling**
> **Normalization (MinMaxScaler)** was crucial. It ensured that the deep learning models trained stably and efficiently, especially with gradient-based optimizers like Adam, leading to lower final error rates.

### **3. Business Value of Forecasts**
> The **12-month forecast** provides a critical operational roadmap. It allows the business to:
> * **Inventory Management:** High-production months ke dauran storage aur inventory badhaana.
> * **Procurement:** Expected demand ke aadhar par feed aur raw materials ki kharidari plan karna.

### **4. Conclusion**
This project successfully implemented a state-of-the-art deep learning solution for time series forecasting. The **LSTM model** is recommended for its superior ability to capture complex temporal patterns in the monthly production data.

---

## **💻 Setup and Execution**

1.  **Zaroori Libraries Install Karein:**
    ```bash
    pip install pandas numpy matplotlib scikit-learn tensorflow keras joblib
    ```
2.  **Execution:**
    * `RNN.ipynb` Jupyter Notebook kholein.
    * Ensure karein ki data file (`monthly_milk_production.csv` or similar) notebook ke saath uplabdh hai.
    * Code cells ko sequence mein run karein.
