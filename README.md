# UPI Fraud Detection System

An end-to-end ML system for detecting fraudulent payment transactions in real time.

## Live Demo
- Frontend: https://upi-fraud-detection-green.vercel.app
- API Docs: https://upi-fraud-api-o7or.onrender.com/docs

## Model Performance
| Model | AUC-ROC | F1 | Recall |
|-------|---------|-----|--------|
| Logistic Regression | 0.9721 | 0.1017 | 0.9082 |
| Decision Tree | 0.8869 | 0.1202 | 0.8367 |
| Random Forest | 0.9836 | 0.5139 | 0.8500 |
| XGBoost (best) | 0.9819 | 0.6391 | 0.8700 |

## Tech Stack
Python, Scikit-learn, XGBoost, SHAP, FastAPI, React, Render, Vercel

## Key Features
- 284,807 real transactions, 0.17% fraud rate
- SMOTE for class imbalance
- SHAP explainability
- FastAPI REST API
- React dashboard
- Fully deployed

## Author
Tanya Singla — https://github.com/tanyasingla89-source
