from fastapi import FastAPI
from pydantic import BaseModel, Field
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -------------------------------------------------
# App Initialization
# -------------------------------------------------
app = FastAPI(
    title="Wind Power Forecast API",
    version="1.0.0"
)

# -------------------------------------------------
# Load Model (ROBUST PATH)
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent / "models"

model = joblib.load(MODEL_DIR / "xgboost_forecast.pkl")

# ✅ THIS IS THE SOURCE OF TRUTH
EXPECTED_FEATURES = model.get_booster().feature_names

# -------------------------------------------------
# Input Schema
# -------------------------------------------------
class PredictionRequest(BaseModel):
    location: int = 1
    temp_2m: float
    relhum_2m: float
    dp_2m: float
    ws_10m: float
    ws_100m: float
    wd_10m: float
    wd_100m: float
    wg_10m: float

# -------------------------------------------------
# Feature Builder
# -------------------------------------------------
def build_feature_row(req: PredictionRequest):
    now = datetime.now()

    return {
        "Unnamed: 0": 0,
        "Location": req.location,

        "Temp_2m": req.temp_2m,
        "RelHum_2m": req.relhum_2m,
        "DP_2m": req.dp_2m,
        "WS_10m": req.ws_10m,
        "WS_100m": req.ws_100m,
        "WD_10m": req.wd_10m,
        "WD_100m": req.wd_100m,
        "WG_10m": req.wg_10m,

        "hour": now.hour,
        "day": now.day,
        "month": now.month,
        "weekday": now.weekday(),

        # Stateful features (documented limitation)
        "lag_1h": 0.0,
        "lag_24h": 0.0,
        "rolling_24h": 0.0,
        "rolling_168h": 0.0,

        "wind_energy": req.ws_100m ** 3,
        "wind_direction_effect": req.ws_100m * np.sin(np.deg2rad(req.wd_100m)),
        "sin_hour": np.sin(2 * np.pi * now.hour / 24),
        "cos_hour": np.cos(2 * np.pi * now.hour / 24),
    }

# -------------------------------------------------
# Prediction Endpoint (FIXED)
# -------------------------------------------------
@app.post("/predict")
def predict_power(request: PredictionRequest):

    row = build_feature_row(request)

    df = pd.DataFrame([row])

    # ✅ ALIGN EXACTLY WITH BOOSTER FEATURES
    df = df[EXPECTED_FEATURES]

    # ✅ Force numeric matrix
    X = df.to_numpy(dtype=float)

    prediction = model.predict(X)[0]

    return {
        "predicted_power": round(float(prediction), 4),
        "unit": "MW",
        "note": "Lag/rolling features are zero-filled. Retrain stateless model for real-time accuracy."
    }
