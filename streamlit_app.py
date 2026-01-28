import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="Wind Power Forecasting",
    layout="centered"
)

st.title("🌬️ Wind Power Generation Forecast")
st.markdown("Predict renewable energy generation using ML")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("xgboost_forecast.pkl")
    features = joblib.load("model_features.pkl")
    return model, features

model, feature_cols = load_model()

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Input Parameters")

ws_100m = st.slider("Wind Speed at 100m (m/s)", 0.0, 25.0, 8.0)
wd_100m = st.slider("Wind Direction at 100m (degrees)", 0, 360, 180)
temp = st.slider("Temperature at 2m (°C)", -10.0, 45.0, 25.0)

selected_time = st.time_input("Select Time", datetime.now().time())

# -----------------------------
# Feature Engineering (Inference)
# -----------------------------
hour = selected_time.hour
month = datetime.now().month
weekday = datetime.now().weekday()

input_data = {
    "WS_100m": ws_100m,
    "WD_100m": wd_100m,
    "Temp_2m": temp,
    "hour": hour,
    "month": month,
    "weekday": weekday,
    "wind_energy": ws_100m ** 3,
    "wind_direction_effect": ws_100m * np.sin(np.deg2rad(wd_100m)),
    "sin_hour": np.sin(2 * np.pi * hour / 24),
    "cos_hour": np.cos(2 * np.pi * hour / 24),
}

input_df = pd.DataFrame([input_data])

# Ensure column order matches training
input_df = input_df.reindex(columns=feature_cols, fill_value=0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Power ⚡ Output"):
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Power Output: **{prediction:.3f} MW**")

