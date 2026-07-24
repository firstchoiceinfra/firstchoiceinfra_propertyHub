import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# CENTRAL NAVIGATION SYSTEM
# ============================================================


PAGES = {

    "🏠 Home": "app.py",

    "🔐 Login & Registration":
        "pages/01_Login_Register.py",

    "🔎 Property Search":
        "pages/02_Property_Search.py",

    "🏡 Post Property":
        "pages/03_Post_Property.py",

}


def show_navigation():

    st.sidebar.markdown(
        """
        <div style="
            padding:20px;
            text-align:center;
            border-radius:20px;
            background:
            linear-gradient(
                135deg,
                #1E3A8A,
                #4C1D95,
                #9D174D
            );
            margin-bottom:20px;
        ">

        <h2>
        🏠 FirstChoice
        </h2>

        <p>
        Property Hub
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.sidebar.markdown(
        "## 📌 Main Navigation"
    )


    selected_page = st.sidebar.radio(

        "Select Page",

        list(PAGES.keys()),

        index=0

    )


    return PAGES[selected_page]
