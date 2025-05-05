
import streamlit as st
import joblib
import numpy as np

# Load the trained model and label encoder
model = joblib.load("discount_model_v4.pkl")
label_encoders = joblib.load("label_encoders_v4.pkl")
subcat_encoder = label_encoders["sub-category"]

# UI
st.title("💸 Max Discount Profitability Checker")
st.write("Estimate whether a discount is **profitable or loss-making** based on pricing inputs.")

# Inputs
sub_category = st.selectbox("Sub-Category", list(subcat_encoder.classes_))
original_price = st.number_input("Original Sales Price (€)", min_value=0.0, value=100.0)
cost_pp = st.number_input("Cost per Piece (€)", min_value=0.0, value=50.0)
discount_pct = st.slider("Discount Percentage", 0.0, 0.9, 0.1, step=0.01)

# Encode sub-category
subcat_encoded = subcat_encoder.transform([sub_category])[0]

# Predict
if st.button("Predict Profitability"):
    X = np.array([[discount_pct, subcat_encoded, original_price, cost_pp]])
    prediction = model.predict(X)[0]
    label = "High Profit ✅" if prediction == 1 else "Low Profit ❌"
    st.success(f"Prediction: {label}")
