import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# =========================
# LOAD MODEL
# =========================

model = joblib.load(
    'models/student_performance_model.pkl'
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Student Performance Prediction",
    layout="wide"
)

st.title(
    "AI-Based Student Performance Prediction System"
)

st.subheader(
    "Academic Performance Intelligence Dashboard"
)

# =========================
# USER INPUTS
# =========================

st.header(
    "Student Information"
)

studytime = st.slider(
    "Study Time",
    1,
    4,
    2
)

failures = st.slider(
    "Past Class Failures",
    0,
    4,
    0
)

absences = st.slider(
    "Absences",
    0,
    50,
    5
)

internet = st.selectbox(
    "Internet Access",
    [0, 1]
)

higher = st.selectbox(
    "Higher Education Interest",
    [0, 1]
)

G1 = st.slider(
    "First Period Grade",
    0,
    20,
    10
)

G2 = st.slider(
    "Second Period Grade",
    0,
    20,
    10
)

# =========================
# PREDICTION
# =========================

if st.button(
    "Predict Final Score"
):

    input_data = pd.DataFrame([{
        'school': 0,
        'sex': 0,
        'age': 17,
        'address': 1,
        'famsize': 0,
        'Pstatus': 1,
        'Medu': 2,
        'Fedu': 2,
        'Mjob': 0,
        'Fjob': 0,
        'reason': 0,
        'guardian': 0,
        'traveltime': 1,
        'studytime': studytime,
        'failures': failures,
        'schoolsup': 0,
        'famsup': 1,
        'paid': 0,
        'activities': 1,
        'nursery': 1,
        'higher': higher,
        'internet': internet,
        'romantic': 0,
        'famrel': 4,
        'freetime': 3,
        'goout': 3,
        'Dalc': 1,
        'Walc': 1,
        'health': 3,
        'absences': absences,
        'G1': G1,
        'G2': G2
    }])

    prediction = model.predict(
        input_data
    )[0]

    # =========================
    # OUTPUT
    # =========================

    st.header(
        "Prediction Result"
    )

    st.success(
        f"Predicted Final Grade (G3): {prediction:.2f}"
    )

    # =========================
    # PERFORMANCE CATEGORY
    # =========================

    if prediction >= 15:

        st.success(
            "Excellent Academic Performance"
        )

    elif prediction >= 10:

        st.info(
            "Average Academic Performance"
        )

    else:

        st.error(
            "Low Academic Performance"
        )

    # =========================
    # VISUALIZATION
    # =========================

    st.header(
        "Performance Analytics"
    )

    labels = [
        'G1',
        'G2',
        'Predicted G3'
    ]

    values = [
        G1,
        G2,
        prediction
    ]

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(
        labels,
        values
    )

    ax.set_title(
        "Student Academic Performance"
    )

    ax.set_ylabel(
        "Marks"
    )

    st.pyplot(fig)