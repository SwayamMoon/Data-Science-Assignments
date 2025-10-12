# 📈 Currency Exchange Rate Forecasting: ARIMA & Exponential Smoothing

## **🌟 Project Overview**

Is project ka mukhya uddeshya (main objective) **USD ➡️ Australian Dollar (USD_AUD)** exchange rate ki historical time series par **advanced forecasting techniques** ka upyog karna hai.

Humne do powerful models—**ARIMA** aur **Exponential Smoothing (Holt-Winters)**—ko lagoo kiya, unki kshamataon ka mulyankan (evaluation) kiya, aur sabse accurate model chuna.

---

## **🛠️ Methodology and Techniques**

| Step | Objective | Key Techniques |
| :--- | :--- | :--- |
| **Data Preparation** | Data loading, date parsing, aur missing values (NaN) ko handle karna. | `Pandas`, **Forward Fill (`ffill`)** |
| **ARIMA Modeling** | Time series ki stationarity jaanchana aur optimal parameters (p, d, q) chunna. | **ADFuller Test**, **ACF/PACF Plots** |
| **Exponential Smoothing**| Time series ke trend aur seasonality ko smooth karke forecast karna. | `Holt-Winters Exponential Smoothing` |
| **Evaluation** | Models ki performance ka tulnatmak vishleshan (comparative analysis). | **80/20 Train/Test Split**, **RMSE**, MAE, MAPE |

---

## **🎯 Key Results & Insights**

Dono models ne kafi acche parinaam (good results) diye, lekin unki strengths alag-alag hain:

| Model | Performance Strength | Best Suited For |
| :--- | :--- | :--- |
| **ARIMA** | Short-term fluctuations ko behtar dhang se capture karna. | **Financial Trading & Short-Term Decisions** |
| **Exponential Smoothing**| Stable, smoother forecasts dena. | **Long-Term Budgeting & Planning** |

> ✅ **Conclusion:** Is dataset mein, **ARIMA** model ne **lowest Root Mean Squared Error (RMSE)** prapt kiya. Yeh isliye kyunki currency exchange rates ki tarah financial time series mein autoregressive aur moving average components ko model karne ki ARIMA ki kshamta ise behtar chayan banati hai.

---

## **🚀 Setup and Execution**

1.  **Libraries Install Karein:**
    ```bash
    pip install pandas numpy matplotlib seaborn statsmodels scikit-learn
    ```
2.  **Notebook Run Karein:**
    * `Time_Series.ipynb` Jupyter Notebook kholein.
    * Ensure karein ki data file (`exchange_rate.csv`) ka path sahi hai.
    * Code cells ko sequence mein run karein.
