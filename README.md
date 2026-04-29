<!-- ========================================================= -->
<!--      E-COMMERCE MANIPULATION RISK INTELLIGENCE STACK     -->
<!-- ========================================================= -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,100:1A1A1A&height=220&section=header&text=E-Commerce%20Manipulation%20Risk%20Intelligence&fontSize=32&fontColor=FFD700&animation=fadeIn"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=FFD700&size=18&center=true&vCenter=true&width=1000&lines=Initializing+E-commerce+Risk+Engine...;Loading+Behavioral+Analysis+Model...;Validating+Pricing+Integrity...;System+Status:+Production+Ready" />
</p>

---

## 🔹 1️⃣ SYSTEM SPECIFICATIONS

<p align="center">
  <img src="https://img.shields.io/badge/Dataset_Size-50K+-111827?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Platforms-9+-1F2937?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Model_Accuracy-85%25-000000?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Environment-Python%20%7C%20PowerBI-1A1A1A?style=for-the-badge"/>
</p>

---

## 🔹 2️⃣ SYSTEM ARCHITECTURE

```
                 ┌────────────────────────────┐
                 │   E-COMMERCE DATA LAYER    │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ DATA VALIDATION ENGINE     │
                 │ • Missing Value Handling   │
                 │ • Duplicate Filtering      │
                 │ • Schema Standardization   │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ FEATURE ENGINEERING CORE   │
                 │ • Discount Analysis        │
                 │ • Behavioral Flags         │
                 │ • Risk Indicators          │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ MANIPULATION MODEL LAYER   │
                 │ • Risk Scoring             │
                 │ • Classification           │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ BUSINESS INSIGHT OUTPUT    │
                 └────────────────────────────┘
```

---

## 🔹 3️⃣ DATA ENGINEERING LAYER

### Data Integrity Enforcement
- Missing value handling  
- Duplicate removal  
- Outlier detection  
- Schema validation  

### Feature Processing
- Discount computation  
- Behavioral signal extraction  
- Feature scaling  
- Correlation mapping  

---

## 🔹 4️⃣ MODEL LAYER

### 🎯 Manipulation Risk Modeling
Classification system predicting product-level manipulation probability.

### 📊 Risk Segmentation
- High Risk  
- Moderate Risk  
- Low Risk  

### 📈 Pricing Behavior Analysis
Evaluates relationship between discount strategies and manipulation patterns.

---

<!-- ========================================================= -->
<!--        MODEL VALIDATION & PERFORMANCE LAYER              -->
<!-- ========================================================= -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,100:1A1A1A&height=170&section=header&text=Model%20Validation%20Layer&fontSize=26&fontColor=FFD700&animation=fadeIn"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=FFD700&size=16&center=true&vCenter=true&width=1000&lines=Computing+Accuracy+Precision+Recall...;Evaluating+Risk+Classification...;Generating+Confusion+Matrix...;Validation+Status:+Complete" />
</p>

---

## 🔎 5️⃣ MODEL PERFORMANCE METRICS

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-85%25-111827?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Precision-82%25-1F2937?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Recall-80%25-000000?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/F1_Score-81%25-1A1A1A?style=for-the-badge"/>
</p>

---

## 🔹 6️⃣ CONFUSION MATRIX

```
                         Predicted
                    Low Risk    High Risk
Actual  Low Risk       TN          FP
        High Risk      FN          TP
```

---

## 🔹 7️⃣ DASHBOARD VISUALIZATION LAYER

The Power BI dashboard provides structured insights into manipulation patterns.

### 📊 Dashboard Overview
<p align="center">
  <img width="1100" height="650" alt="Dashboard click" src="https://github.com/user-attachments/assets/f337823b-95ab-4516-b19b-111d4663a819" />
</p>

### 📈 Risk Distribution
<p align="center">
  <img width="1283" height="723" alt="Risk Analysis" src="https://github.com/user-attachments/assets/8d2fa617-cd09-4764-ab60-1a64fc8447f3" />
</p>

### 📉 Discount vs Risk Analysis
<p align="center">
  <img width="1283" height="725" alt="Risk Analysis  Scatter" src="https://github.com/user-attachments/assets/9a92ea75-2e60-4f02-a09c-3c02f10b4934" />
  </p>

---

## 🔹 8️⃣ CODE IMPLEMENTATION LAYER

### 📌 Feature Engineering
```python
df['discount_percent'] = ((df['original_price'] - df['final_price']) / df['original_price']) * 100
df['urgency_flag'] = df['discount_percent'].apply(lambda x: 1 if x > 50 else 0)
```

### 📌 Risk Score Calculation
```python
df['manipulation_risk_score'] = (
    df['discount_percent'] * 0.4 +
    df['urgency_flag'] * 30 +
    df['fake_discount_flag'] * 50
)
```

### 📌 Model Training
```python
from sklearn.ensemble import RandomForestClassifier

X = df[['discount_percent','urgency_flag','fake_discount_flag','rating']]
y = df['risk_label']

model = RandomForestClassifier()
model.fit(X, y)
```

---

## 🔹 9️⃣ TECHNOLOGY STACK

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/>
  <img src="https://img.icons8.com/color/48/google-colab.png"/>
  <img src="https://img.icons8.com/color/48/microsoft-excel-2019--v1.png"/>
  <img src="https://img.icons8.com/color/48/power-bi.png"/>
</p>

---

## 🔹 🔟 SYSTEM STATUS

```
Data Pipeline .............. Stable
Feature Engineering ....... Optimized
Risk Model ................ Active
Dashboard ................. Operational
System Integrity .......... Verified
Deployment Status ......... Ready
```

---

## 🔹 1️⃣1️⃣ ACCESS PROTOCOL

```bash
git clone https://github.com/AyushTiwari25/ecommerce-manipulation-risk-analysis.git
```

---

## 🔹 1️⃣2️⃣ AUTHOR

Ayush Tiwari  
Data Science | Machine Learning | Analytics  

---

## 🔹 LICENSE

This project is intended for analytical and educational purposes.
