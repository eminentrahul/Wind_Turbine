import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Wind Turbine Power Forecast",
    page_icon="🌬️",
    layout="centered"
)

st.title("🌬️ Wind Turbine Power Forecasting")
st.markdown("Predict wind turbine power output using weather conditions.")

# ---------------------------
# Load model (cached)
# ---------------------------
@st.cache_resource
def load_model():
    model = xgb.XGBRegressor()
    model.load_model("../models/xgboost_forecast.json")
    return model

@st.cache_resource
def load_features():
    return joblib.load("../models/model_features.pkl")

model = load_model()
FEATURES = load_features()

# ---------------------------
# User Inputs
# ---------------------------
st.subheader("🔧 Input Parameters")

wind_speed = st.slider("Wind Speed (m/s)", 0.0, 25.0, 8.0)
wind_direction = st.slider("Wind Direction (°)", 0.0, 360.0, 180.0)
temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0)

# ---------------------------
# Feature engineering (basic demo)
# ---------------------------
input_data = pd.DataFrame([{
    "WindSpeed": wind_speed,
    "WindDirection": wind_direction,
    "Temperature": temperature,
    "Humidity": humidity
}])

# Ensure feature order matches training
for col in FEATURES:
    if col not in input_data:
        input_data[col] = 0

input_data = input_data[FEATURES]

# ---------------------------
# Prediction
# ---------------------------
if st.button("⚡ Predict Power Output"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Power Output: **{prediction:.2f} kW**")
