import streamlit as st
import joblib
import pandas as pd

# Load model
try:
    model = joblib.load('snr_regression_model.pkl')
except FileNotFoundError:
    st.error("❌ Model file not found. Make sure 'snr_regression_model.pkl' is in the same folder as this app.")
    st.stop()

st.title("📊 SNR Predictor")
st.markdown("Enter the values below to predict the **Signal-to-Noise Ratio (SNR)**.")

# Inputs
amp = st.number_input("Amplitude", format="%.4f")
rise = st.number_input("Rise Time", format="%.4f")
fdhm = st.number_input("FDHM", format="%.4f")

# Button
if st.button("🔍 Predict"):
    # Create a DataFrame with feature names
    input_df = pd.DataFrame({
        'amplitude': [amp],
        'rise_time': [rise],
        'fdhm': [fdhm]
    })

    prediction = model.predict(input_df)
    st.success(f"✅ Predicted SNR: **{prediction[0]:.2f}**")
