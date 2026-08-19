import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Sales Prediction App", page_icon="📈", layout="centered")

st.title("📈 Sales Prediction Application")
st.write("Enter advertising campaign budgets below to forecast total sales using the trained **ExtraTrees** model.")

@st.cache_resource
def load_artifacts():
    model = joblib.load('extra_tree_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

try:
    model, scaler = load_artifacts()
    st.success("Model and Scaler loaded successfully!")
except Exception as e:
    st.error(f"Error loading required files: {e}")

st.divider()

st.subheader("Advertising Budgets ($ thousands):")

tv = st.number_input("TV Budget", min_value=0.0, max_value=500.0, value=150.0, step=1.0)
radio = st.number_input("Radio Budget", min_value=0.0, max_value=100.0, value=25.0, step=1.0)
newspaper = st.number_input("Newspaper Budget", min_value=0.0, max_value=150.0, value=10.0, step=1.0)

if st.button("Predict Sales 🚀", use_container_width=True):
    input_data = np.array([[tv, radio, newspaper]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    
    st.markdown("---")
    st.metric(label="Predicted Sales (Units)", value=f"{prediction[0]:.2f}")