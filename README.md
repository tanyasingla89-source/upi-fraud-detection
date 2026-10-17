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

## Run with Docker

```bash
# Build the image
docker build -t upi-fraud-api .

# Run locally (API available at http://localhost:8000)
docker run -p 8000:8000 upi-fraud-api

# Test health endpoint
curl http://localhost:8000/

# Test predict endpoint (31 features: V1-V28, hour, is_night, Amount_scaled)
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [-1.36,-0.07,2.54,1.38,-0.34,0.46,0.24,0.10,0.36,0.09,-0.55,-0.62,-0.99,-0.31,1.47,-0.47,0.21,0.03,0.40,0.25,-0.02,0.28,-0.11,0.07,0.13,-0.19,0.13,0.0,14,0,0.24]}'
```

## Author
Tanya Singla — https://github.com/tanyasingla89-source
