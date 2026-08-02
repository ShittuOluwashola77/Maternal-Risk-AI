import streamlit as st


def show_home():

    # ============================================
    # Title
    # ============================================

    st.title("🤱 MaternalAI")

    st.subheader(
        "Intelligent Maternal Health Decision Support System"
    )

    st.write(
        """
Welcome to **MaternalAI**, an AI-powered application that predicts maternal
health risk using a trained **Gradient Boosting Machine Learning model** and
provides educational explanations with a **Large Language Model (LLM)**.

This application is intended for educational and research purposes.
"""
    )

    st.divider()

    # ============================================
    # Dashboard Cards
    # ============================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Machine Learning",
            "Gradient Boosting"
        )

    with col2:

        st.metric(
            "AI Assistant",
            "Groq LLM"
        )

    with col3:

        st.metric(
            "Application",
            "MaternalAI"
        )

    with col4:

        st.metric(
            "Version",
            "1.0"
        )

    st.divider()

    # ============================================
    # Features
    # ============================================

    st.subheader("🚀 Features")

    st.success("✔ Maternal Risk Prediction")

    st.success("✔ AI-powered Explanation")

    st.success("✔ Prediction History")

    st.success("✔ Interactive Dashboard")

    st.divider()

    # ============================================
    # How to Use
    # ============================================

    st.subheader("📖 How to Use")

    with st.expander("Click to view instructions", expanded=True):

        st.markdown(
            """
1. Open **Risk Assessment**

2. Enter the patient's clinical information.

3. Click **Predict Maternal Risk**.

4. Review the predicted risk level.

5. Read the AI-generated explanation.

6. View your prediction history.
"""
        )

    st.divider()

    # ============================================
    # Disclaimer
    # ============================================

    st.warning(
        """
**Disclaimer**

MaternalAI provides educational information only.

It should **not** be used as a substitute for professional
medical diagnosis, treatment, or clinical decision-making.
"""
    )