# 📉 Assignment 02: Statistical Estimation & Confidence Intervals

## 🎯 Project Goal (Maksad)
The primary objective was to estimate the mean durability of high-value printer heads using Confidence Intervals, demonstrating the difference between using **Sample Standard Deviation** (t-distribution) and **Known Population Standard Deviation** (z-distribution) under small sample sizes.

## 🛠️ Tools and Technologies (Kaunse Tools Use Kiye)
* **Language:** Python
* **Libraries:** NumPy, SciPy (for `stats` module, `t` and `norm` distributions)

---

## 💡 Key Insights & Technical Learnings

### 1. The Crux of T-Distribution
> Project ka sabse important learning point yeh tha ki jab **Sample Size (n=15) chota** ho aur **Population Standard Deviation unknown** ho, toh hum **Z-distribution** ki jagah **T-distribution** ka use karte hain. T-distribution **larger margin of error** (wider interval) deta hai, jo uncertainty ko better handle karta hai.

### 2. Confidence Interval Interpretation
> Humne 99% confidence interval calculate kiya. Iska matlab hai ki agar hum **100 baar** yahi process repeat karein, toh 99 baar **true population mean durability** (millions of characters mein) isi calculated range ke beech mein aayegi.

### 3. Practical Application in Quality Control
> Is analysis ne manufacturer ko **destructive testing** ki zaroorat ko kam karte hue, apne print-heads ki average life ka ek reliable range de diya. Yeh **cost-saving** aur **quality assessment** mein critical role play karta hai.

### 4. Conclusion
> Successfully estimated the population mean using both methods, providing a robust range of [Aapne jo bhi final value calculate ki ho woh yahaan likh sakte hain, jaise: 1.05M - 1.45M characters]. This reinforces core concepts of **statistical inference** and small sample size handling.
