## 🔍 Key Features
- **284,807 real transactions** from Kaggle Credit Card Fraud dataset
- **Extreme class imbalance** handled with SMOTE (0.17% fraud rate)
- **4 models compared** — XGBoost wins with AUC-ROC 0.98
- **SHAP explainability** — explains why each transaction was flagged
- **REST API** — FastAPI endpoint for real-time predictions
- **React dashboard** — live fraud checker with risk level display

## 🏃 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/tanyasingla89-source/upi-fraud-detection.git
cd upi-fraud-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download dataset
Download `creditcard.csv` from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place in `data/` folder.

### 4. Run the notebook
```bash
cd notebooks
jupyter notebook fraud_detection.ipynb
```

### 5. Start the API
```bash
cd api
uvicorn main:app --reload --port 8000
```

### 6. Start the frontend
```bash
cd frontend
npm install
npm start
```

## 📬 API Usage
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [...]}'
```

Response:
```json
{
  "fraud_probability": 0.9231,
  "is_fraud": 1,
  "risk_level": "HIGH",
  "message": "Fraudulent transaction detected"
}
```

## 👩‍💻 Author
**Tanya Singla** — [GitHub](https://github.com/tanyasingla89-source)