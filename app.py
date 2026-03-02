import streamlit as st
import pickle
import numpy as np

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ------------------ LOAD MODEL ------------------
model = pickle.load(open("heart_model.pkl", "rb"))

# ------------------ CUSTOM NAVBAR STYLE ------------------
st.markdown("""
    <style>
    .nav-button {
        background-color: #0E1117;
        color: white;
        border: none;
        padding: 10px 30px;
        margin: 5px;
        font-size: 18px;
        border-radius: 8px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ SESSION STATE ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------ TOP NAVBAR ------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("🏠 Home"):
            st.session_state.page = "Home"
    with nav2:
        if st.button("🔍 Prediction"):
            st.session_state.page = "Prediction"

st.markdown("---")

# ------------------ HOME PAGE ------------------
if st.session_state.page == "Home":
    st.title("❤️ Heart Disease Prediction System")

    st.write("""
    ### 🩺 About the Project
    
    This application predicts the presence of heart disease 
    using a Machine Learning model trained on medical data.
    
    The system analyzes 13 clinical features and provides 
    an instant prediction result.
    
    ### 🎯 Objective
    To assist in early risk detection and promote preventive healthcare.
    """)

    st.success("Click on Prediction to check heart disease risk.")

# ------------------ PREDICTION PAGE ------------------
elif st.session_state.page == "Prediction":

    st.title("🔍 Heart Disease Prediction")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
        cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Serum Cholesterol")

    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.selectbox("Resting ECG (0-2)", [0, 1, 2])
        thalach = st.number_input("Maximum Heart Rate")
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("ST Depression")

    slope = st.selectbox("Slope (0-2)", [0, 1, 2])
    ca = st.selectbox("Major Vessels (0-3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (0-3)", [0, 1, 2, 3])

    if st.button("Predict"):
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                                restecg, thalach, exang, oldpeak,
                                slope, ca, thal]])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")
