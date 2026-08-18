import streamlit as st

from version import APP_NAME, VERSION

from frontend.home import show_home
from frontend.risk_assessment import show_risk_assessment
from frontend.ai_assistant import show_ai_assistant
from frontend.model_performance import show_model_performance
from frontend.about import show_about


# ============================================
# Load Custom CSS
# ============================================

def load_css():

    with open("assets/style.css") as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


# ============================================
# Page Configuration
# ============================================

st.set_page_config(

    page_title=APP_NAME,

    page_icon="🤱",

    layout="wide",

    initial_sidebar_state="expanded"
)


# ============================================
# Load CSS
# ============================================

load_css()


# ============================================
# Sidebar Header
# ============================================

st.sidebar.title(f"🤱 {APP_NAME}")

st.sidebar.caption(f"Version {VERSION}")

st.sidebar.markdown(
    """
**Intelligent Maternal Health Decision Support System**
"""
)

st.sidebar.divider()


# ============================================
# Navigation
# ============================================

page = st.sidebar.radio(

    "📌 Navigation",

    [

        "🏠 Home",

        "🩺 Risk Assessment",

        "🤖 AI Assistant",

        "📈 Model Performance",

        "ℹ️ About"

    ]

)

st.sidebar.divider()


# ============================================
# System Information
# ============================================

with st.sidebar.expander(
    "⚙️ System Information",
    expanded=True
):

    st.markdown(
        """
### Machine Learning

- Gradient Boosting Classifier

### AI Assistant

- Groq API
- llama-3.1-8b-instant

### Framework

- Streamlit

### Version

- v1.0.0
"""
    )

st.sidebar.divider()


# ============================================
# Quick Tips
# ============================================

with st.sidebar.expander(
    "💡 Quick Tips",
    expanded=False
):

    st.write(
        """
• Enter realistic patient measurements.

• Review the AI explanation after every prediction.

• Check the Prediction Analytics dashboard.

• Remember that this application supports—not replaces—clinical judgement.
"""
    )

st.sidebar.divider()


# ============================================
# Navigation Pages
# ============================================

if page == "🏠 Home":

    show_home()

elif page == "🩺 Risk Assessment":

    show_risk_assessment()

elif page == "🤖 AI Assistant":

    show_ai_assistant()

elif page == "📈 Model Performance":

    show_model_performance()

elif page == "ℹ️ About":

    show_about()


# ============================================
# Footer
# ============================================

st.markdown("---")

st.caption(
    f"🤱 {APP_NAME} v{VERSION} | Educational Maternal Health Decision Support System | © 2026"
)
