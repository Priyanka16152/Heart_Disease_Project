import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("heart_model.pkl", "rb"))

# ---------------- SIDEBAR ----------------
st.sidebar.title("❤️ Heart Disease App")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📖 About Project", "🔍 Prediction", "🤖 Model Info", "📩 Contact"]
)

st.sidebar.markdown("---")
st.sidebar.info("Developed using Machine Learning & Streamlit")

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.title("❤️ Heart Disease Prediction System")
    st.markdown("---")

    st.write("""
    Welcome to the Heart Disease Prediction Web Application.

    This system uses Machine Learning to analyze medical parameters 
    and predict the risk of heart disease.

    Early detection plays a crucial role in preventive healthcare 
    and timely medical intervention.
    """)

    st.success("Use the left sidebar to navigate through the application.")

# ---------------- ABOUT PAGE ----------------
elif page == "📖 About Project":
    st.title("📖 About the Project")
    st.markdown("---")

    st.write("""
    ### 📊 Dataset Used
    UCI Heart Disease Dataset

    ### 🎯 Objective
    - Predict presence of heart disease
    - Assist in early diagnosis
    - Support medical decision-making

    ### 🛠 Technologies Used
    - Python
    - Pandas & NumPy
    - Scikit-learn
    - Streamlit
    """)

# ---------------- MODEL INFO PAGE ----------------
elif page == "🤖 Model Info":
    st.title("🤖 Model Information")
    st.markdown("---")

    st.write("""
    ### Algorithm Used:
    Random Forest Classifier

    ### Why Random Forest?
    - High prediction accuracy
    - Handles non-linear relationships
    - Reduces overfitting
    - Works well with structured medical data

    The model is trained on 13 clinical features 
    such as age, cholesterol, blood pressure, 
    chest pain type, and more.
    """)

# ---------------- CONTACT PAGE ----------------
elif page == "📩 Contact":
    st.title("📩 Contact Information")
    st.markdown("---")

    st.write("""
    👩‍💻 Developer: Priyanka  

    This project is developed for academic and learning purposes.

    📧 Email: your_email@example.com  
    🌐 GitHub: Your GitHub Profile Link
    """)

# ---------------- PREDICTION PAGE ----------------
elif page == "🔍 Prediction":

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
