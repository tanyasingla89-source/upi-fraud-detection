from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib
import os

# Create FastAPI app
app = FastAPI(title="UPI Fraud Detection API")

# Allow React frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model only — no scaler needed
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, '..', 'model', 'fraud_model.pkl'))

# Define transaction input
class Transaction(BaseModel):
    features: list[float]

# Route 1 — check if API is running
@app.get("/")
def home():
    return {
        "message": "UPI Fraud Detection API is running",
        "status": "healthy"
    }

# Route 2 — predict fraud
@app.post("/predict")
def predict(txn: Transaction):
    # Convert to numpy array
    X = np.array(txn.features).reshape(1, -1)

    # Get fraud probability directly
    prob  = model.predict_proba(X)[0][1]
    label = int(prob >= 0.5)

    return {
        "fraud_probability": round(float(prob), 4),
        "is_fraud": label,
        "risk_level": "HIGH" if prob >= 0.7 else "MEDIUM" if prob >= 0.4 else "LOW",
        "message": "Fraudulent transaction detected" if label == 1 else "Legitimate transaction"
    }