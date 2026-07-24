import streamlit as st

st.set_page_config(
    page_title="FirstChoice Infra Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏠 FirstChoice Infra Property Hub")

st.write("Welcome to FirstChoice Property Hub")

st.sidebar.title("📌 Navigation")

st.sidebar.success(
    "Pages folder में Login, Property Search और Post Property pages available हैं."
)

st.info(
    "👈 Left Sidebar में Pages दिखाई देने चाहिए."
)
