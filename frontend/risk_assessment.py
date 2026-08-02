import pandas as pd
from datetime import datetime
import streamlit as st

from prediction.predictor import predict_risk
from ai.grok_client import ask_grok
from ai.prompts import build_prediction_prompt


def show_risk_assessment():

    # ============================================
    # Initialize Session State
    # ============================================

    history = st.session_state.setdefault("prediction_history", [])

    st.title("🩺 Maternal Risk Assessment")

    st.write(
        "Enter the patient's clinical information below."
    )

    st.divider()

    # ============================================
    # Patient Information
    # ============================================

    st.subheader("👤 Patient Information")

    age = st.number_input(
        "Age (Years)",
        min_value=10,
        max_value=60,
        value=25
    )

    st.divider()

    # ============================================
    # Blood Pressure
    # ============================================

    st.subheader("🩸 Blood Pressure")

    col1, col2 = st.columns(2)

    with col1:
        systolic = st.number_input(
            "Systolic Blood Pressure (mmHg)",
            min_value=70,
            max_value=250,
            value=120
        )

    with col2:
        diastolic = st.number_input(
            "Diastolic Blood Pressure (mmHg)",
            min_value=40,
            max_value=180,
            value=80
        )

    st.divider()

    # ============================================
    # Clinical Measurements
    # ============================================

    st.subheader("🧪 Clinical Measurements")

    col3, col4, col5 = st.columns(3)

    with col3:
        blood_sugar = st.number_input(
            "Blood Sugar (mmol/L)",
            min_value=2.0,
            max_value=25.0,
            value=6.5
        )

    with col4:
        body_temp = st.number_input(
            "Body Temperature (°F)",
            min_value=95.0,
            max_value=110.0,
            value=98.6
        )

    with col5:
        heart_rate = st.number_input(
            "Heart Rate (bpm)",
            min_value=40,
            max_value=200,
            value=80
        )

    st.divider()

    # ============================================
    # Prediction Button
    # ============================================

    predict = st.button(
        "🩺 Predict Maternal Risk",
        use_container_width=True,
        type="primary"
    )

    if predict:

        # ============================================
        # Make Prediction
        # ============================================

        try:
            risk, confidence, probabilities = predict_risk(
                age,
                systolic,
                diastolic,
                blood_sugar,
                body_temp,
                heart_rate
            )

        except Exception as e:
            st.error("Prediction failed.")
            st.exception(e)
            st.stop()

        # ============================================
        # Save Prediction History
        # ============================================

        history.append(
            {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Risk Level": risk,
                "Confidence (%)": round(confidence * 100, 2)
            }
        )

        st.divider()

        st.subheader("📋 Prediction Result")

        if risk.lower() == "low risk":

            color = "low-risk"
            icon = "🟢"
            title = "LOW RISK"

            message = (
                "The patient currently appears to have a relatively low maternal health risk."
            )

        elif risk.lower() == "mid risk":

            color = "mid-risk"
            icon = "🟡"
            title = "MID RISK"

            message = (
                "The patient has a moderate maternal health risk. Closer monitoring is recommended."
            )

        else:

            color = "high-risk"
            icon = "🔴"
            title = "HIGH RISK"

            message = (
                "The patient appears to have a high maternal health risk. Immediate clinical assessment is recommended."
            )

        st.markdown(
            f"""
<div class="result-card {color}">
    <h2>{icon} {title}</h2>
    <p>{message}</p>
    <h3>Confidence: {confidence*100:.2f}%</h3>
</div>
""",
            unsafe_allow_html=True
        )

        st.progress(float(confidence))

        st.toast("✅ Prediction completed successfully!")

        # ============================================
        # Build AI Prompt
        # ============================================

        prompt = build_prediction_prompt(
            age,
            systolic,
            diastolic,
            blood_sugar,
            body_temp,
            heart_rate,
            risk,
            confidence * 100
        )

        # ============================================
        # AI Explanation
        # ============================================

        try:

            with st.spinner(
                "🧠 MaternalAI is analysing the patient's clinical information..."
            ):

                explanation = ask_grok(prompt)

        except Exception as e:

            st.error("AI explanation failed.")
            st.exception(e)

            explanation = (
                "AI explanation is currently unavailable."
            )

        st.divider()

        st.subheader("🤖 AI Explanation")

        with st.expander(
            "Click to view AI explanation",
            expanded=True
        ):

            st.info(explanation)

        st.caption(
            "This explanation is generated by AI for educational purposes only "
            "and does not replace professional medical advice."
        )

    # ============================================
    # Prediction History
    # ============================================

    st.divider()

    st.subheader("📋 Prediction History")

    if history:

        history_df = pd.DataFrame(history)

        st.dataframe(
            history_df,
            use_container_width=True
        )

    else:

        st.info(
            "No predictions have been made yet."
        )

    # ============================================
    # Clear Prediction History
    # ============================================

    if st.button("🗑 Clear Prediction History"):

        history.clear()

        st.success(
            "Prediction history cleared successfully."
        )

        st.rerun()
