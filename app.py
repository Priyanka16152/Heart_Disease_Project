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

# ------------------ SESSION STATE ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------ TOP NAVBAR ------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"

with col2:
    if st.button("📖 About"):
        st.session_state.page = "About"

with col3:
    if st.button("🔍 Prediction"):
        st.session_state.page = "Prediction"

with col4:
    if st.button("🤖 Model Info"):
        st.session_state.page = "Model"

with col5:
    if st.button("📩 Contact"):
        st.session_state.page = "Contact"

st.markdown("---")

# ------------------ HOME PAGE ------------------
if st.session_state.page == "Home":
    st.title("❤️ Heart Disease Prediction System")
    st.write("""
    Welcome to the Heart Disease Prediction Web Application.
    
    This system uses Machine Learning to predict the risk of heart disease 
    based on medical attributes.
    
    Early detection can help in preventive healthcare.
    """)

# ------------------ ABOUT PAGE ------------------
elif st.session_state.page == "About":
    st.title("📖 About the Project")
    st.write("""
    This project is developed using Machine Learning techniques.
    
    Dataset Used:
    - UCI Heart Disease Dataset
    
    Objective:
    - Predict presence of heart disease
    - Assist in early risk detection
    
    Technologies Used:
    - Python
    - Scikit-learn
    - Pandas & NumPy
    - Streamlit
    """)

# ------------------ MODEL INFO PAGE ------------------
elif st.session_state.page == "Model":
    st.title("🤖 Model Information")
    st.write("""
    Algorithm Used: Random Forest Classifier
    
    Why Random Forest?
    - High accuracy
    - Handles non-linear data
    - Reduces overfitting
    
    Model trained on 13 medical features.
    """)

# ------------------ CONTACT PAGE ------------------
elif st.session_state.page == "Contact":
    st.title("📩 Contact")
    st.write("""
    Developer: Priyanka
    
    This project is created for academic and learning purposes.
    
    For queries or collaboration:
    📧 chetan_sharma@gmail.com
    """)

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
