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

# ------------------ SIDEBAR NAVIGATION ------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction"])

# ------------------ HOME PAGE ------------------
if page == "Home":
    st.title("❤️ Heart Disease Prediction System")
    st.markdown("---")

    st.write("""
    ### 🩺 Project Overview
    
    This application predicts the presence of heart disease 
    using Machine Learning techniques.
    
    The model is trained using medical attributes such as:
    - Age
    - Blood Pressure
    - Cholesterol
    - Chest Pain Type
    - Maximum Heart Rate
    
    ### 🎯 Objective
    To assist in early detection of heart disease risk 
    and support medical decision-making.
    """)

    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966481.png", width=150)

    st.success("Use the sidebar to navigate to the Prediction page.")

# ------------------ PREDICTION PAGE ------------------
elif page == "Prediction":

    st.title("🔍 Heart Disease Prediction")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
        cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Serum Cholesterol")

    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)", [0, 1])
        restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
        thalach = st.number_input("Maximum Heart Rate Achieved")
        exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
        oldpeak = st.number_input("ST Depression")

    slope = st.selectbox("Slope (0-2)", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
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
