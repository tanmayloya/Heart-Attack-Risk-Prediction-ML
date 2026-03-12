import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Attack Risk Predictor", layout="centered")
st.title("💓 Heart Attack Risk Predictor - Analyst Mode")

st.markdown("Enter clinical values to assess heart attack risk using ML.")

# Real Inputs
age = st.number_input("Age (years)", 18, 100, value=45)
gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
hr = st.number_input("Heart Rate (bpm)", 40, 200, value=80)
sys_bp = st.number_input("Systolic BP (mm Hg)", 90, 200, value=120)
dia_bp = st.number_input("Diastolic BP (mm Hg)", 60, 140, value=80)
sugar = st.number_input("Blood Sugar (mg/dL)", 50, 300, value=110)
ckmb = st.number_input("CK-MB (ng/mL)", 0.0, 100.0, value=12.0, step=0.1)
troponin = st.number_input("Troponin (ng/mL)", 0.0, 50.0, value=0.5, step=0.01)

# Predict button
if st.button("🔍 Predict"):
    input_data = np.array([[age, gender, hr, sys_bp, dia_bp, sugar, ckmb, troponin]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")
    st.subheader("📈 Prediction Result")

    if prediction == 1:
        st.error(f"⚠ High Risk of Heart Attack")
    else:
        st.success(f"✅ Low Risk / No Immediate Threat")

    st.markdown(f"🧪 Model Probability:** {prob:.4f} ")
    st.progress(prob)

    st.markdown("---")
    st.subheader("🧠 Analyst Summary")
    st.markdown(f"""
    - *Age:* {age}  
    - *Gender:* {"Male" if gender==1 else "Female"}  
    - *Heart Rate:* {hr} bpm  
    - *Systolic BP:* {sys_bp} mm Hg  
    - *Diastolic BP:* {dia_bp} mm Hg  
    - *Blood Sugar:* {sugar} mg/dL  
    - *CK-MB:* {ckmb} ng/mL  
    - *Troponin:* {troponin} ng/mL  
    """)

    st.caption("📌 This is a predictive result and not a diagnosis. Always consult a healthcare professional.")