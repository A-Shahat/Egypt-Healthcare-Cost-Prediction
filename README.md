#  Egypt Healthcare Cost Prediction

> Predicting annual healthcare expenditures using demographic and clinical features — built with Python and Scikit-learn.

---

## Overview

Healthcare systems face increasing financial pressure from rising treatment costs and growing chronic disease prevalence. This project builds machine learning models to predict patients' annual healthcare expenditures, helping:

- **Insurance companies** estimate risk and set fair premiums
- **Hospitals** allocate resources more efficiently
- **Policymakers** identify and address key drivers of healthcare spending

The best model — **Gradient Boosting** — achieves **R² ≈ 0.887**, an RMSE of ~2,538 EGP, and an MAE of ~1,995 EGP on held-out test data.

---

## Project Structure

```
egypt-healthcare-cost-prediction/
│
├── Egypt_healthcare_cost_prediction_enhanced.ipynb  # Main notebook
├── egypt_healthcare_synthetic_data.csv              # Dataset
│
├── eda_overview.png                                 # EDA grid
├── model_comparison.png                             # Model comparison chart
├── prediction_diagnostics.png                       # Actual vs Predicted & residuals
├── feature_importance.png                           # Feature importance plot
│
├── requirements.txt
└── README.md
```

---

## Dataset

> **This dataset is synthetically generated for educational purposes.** It does not represent real patient records.

| Feature | Type | Description |
|---|---|---|
| `age` | Numeric | Patient age |
| `bmi` | Numeric | Body mass index |
| `num_dependents` | Numeric | Number of dependents |
| `chronic_conditions` | Numeric | Number of chronic diseases |
| `visits_per_year` | Numeric | Annual healthcare visits |
| `smoker` | Binary | Smoking status |
| `diabetes` | Binary | Diabetes diagnosis |
| `hypertension` | Binary | Hypertension diagnosis |
| `obese` | Binary | Obesity status |
| `insured` | Binary | Insurance coverage |
| `sex` | Categorical | Patient sex |
| `region` | Categorical | Geographical region |
| `facility_type` | Categorical | Public or private facility |
| `annual_charges_egp` |  **Target** | Total yearly expenditure (EGP) |

---

## Methodology

### 1. Exploratory Data Analysis
- Distribution and skewness analysis of charges
- Regional and facility-type cost comparisons
- Smoking, age, and chronic condition impact visualizations
- Correlation matrix with target-correlation callout

### 2. Feature Engineering & Preprocessing
- 80/20 stratified train/test split

### 3. Model Training & Evaluation
Three models trained and compared with **5-fold cross-validation**:

| Model | R² | CV R² | RMSE (EGP) | MAE (EGP) |
|---|---|---|---|---|
| Linear Regression | — | — | — | — |
| Random Forest | — | — | — | — |
| **Gradient Boosting** | **~0.887** | — | **~2,538** | **~1,995** |

> Run the notebook to populate exact cross-validation values.

### 4. Prediction Confidence
The notebook reports the percentage of predictions falling within ±2K, ±5K, and ±10K EGP — a more business-meaningful metric than RMSE alone.

---

## Key Findings

- **Region** is the top cost driver — urban patients (Cairo, Giza, Alexandria) incur significantly higher costs.
- **Diabetes** is the strongest clinical predictor of elevated expenditure.
- **Facility type** (private vs public) has a large independent effect on costs.
- **Age and BMI** show continuous positive relationships with annual charges.
- Smokers exhibit a clearly shifted cost distribution compared to non-smokers.

---


---

## 📦 Requirements

```
pandas>=1.5
numpy>=1.23
matplotlib>=3.6
seaborn>=0.12
scikit-learn>=1.2
```

---

## Future Work

- [ ] Validate on real-world Egyptian health insurance data
- [ ] Hyperparameter tuning with `GridSearchCV`
- [ ] SHAP values for patient-level explainability
- [ ] Deploy as a REST API with FastAPI or Flask

---

## 👤 Author

**Ahmed El-Shahat**
- Data Analyst | Python · SQL · Machine Learning
- 📬 [LinkedIn](https://www.linkedin.com/in/ahmed-shahat)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

