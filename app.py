import streamlit as st
import sqlite3
import pickle
import numpy as np

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

# Create tables
c.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS predictions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    result TEXT
)
""")

conn.commit()

# ---------------------------
# LOAD MODEL
# ---------------------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------------------
# SIDEBAR MENU
# ---------------------------
menu = ["Home", "Login", "Signup"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------------------
# HOME PAGE
# ---------------------------
if choice == "Home":
    st.title("❤️ Heart Disease Prediction System")
    st.write("""
    This project predicts the risk of heart disease using Machine Learning.
    
    🔹 Built with Streamlit  
    🔹 Model: Logistic Regression / Random Forest  
    🔹 Backend: SQLite Database
    """)

# ---------------------------
# SIGNUP PAGE
# ---------------------------
elif choice == "Signup":
    st.subheader("Create New Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Signup"):
        c.execute("INSERT INTO users(username,password) VALUES (?,?)",
                  (new_user, new_pass))
        conn.commit()
        st.success("Account Created Successfully!")

# ---------------------------
# LOGIN PAGE
# ---------------------------
elif choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (username, password))
        data = c.fetchall()

        if data:
            st.success("Logged In Successfully!")
            st.session_state["user"] = username
        else:
            st.error("Invalid Credentials")

# ---------------------------
# AFTER LOGIN
# ---------------------------
if "user" in st.session_state:

    st.sidebar.success(f"Logged in as {st.session_state['user']}")
    page = st.sidebar.radio("Go To", ["Prediction", "My History", "Logout"])

    # ---------------------------
    # PREDICTION PAGE
    # ---------------------------
    if page == "Prediction":

        st.subheader("Enter Patient Details")

        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
        cp = st.number_input("Chest Pain Type", 0, 3)
        trestbps = st.number_input("Resting Blood Pressure")
        chol = st.number_input("Cholesterol")
        fbs = st.selectbox("Fasting Blood Sugar > 120 (1 = Yes, 0 = No)", [0, 1])
        restecg = st.number_input("Rest ECG", 0, 2)
        thalach = st.number_input("Max Heart Rate")
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("Oldpeak")
        slope = st.number_input("Slope", 0, 2)
        ca = st.number_input("Number of Major Vessels", 0, 4)
        thal = st.number_input("Thal", 0, 3)

        if st.button("Predict"):
            input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                                    restecg, thalach, exang, oldpeak,
                                    slope, ca, thal]])

            prediction = model.predict(input_data)

            if prediction[0] == 1:
                result = "High Risk of Heart Disease"
                st.error(result)
            else:
                result = "Low Risk of Heart Disease"
                st.success(result)

            # Save prediction
            c.execute("INSERT INTO predictions(username,result) VALUES (?,?)",
                      (st.session_state["user"], result))
            conn.commit()

    # ---------------------------
    # HISTORY PAGE
    # ---------------------------
    elif page == "My History":

        st.subheader("My Prediction History")

        c.execute("SELECT result FROM predictions WHERE username=?",
                  (st.session_state["user"],))
        data = c.fetchall()

        if data:
            for row in data:
                st.write("•", row[0])
        else:
            st.info("No predictions yet.")

    # ---------------------------
    # LOGOUT
    # ---------------------------
    elif page == "Logout":
        st.session_state.clear()
        st.success("Logged Out Successfully")
