import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MAIN APPLICATION
# ============================================================

st.set_page_config(
    page_title="FirstChoice Infra Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F7F9FF 0%,
        #FFF7F3 35%,
        #F7F1FF 70%,
        #EFFCFF 100%
    );
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background:
    linear-gradient(
        180deg,
        #071952,
        #1E1B4B,
        #4C1D95
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* BRAND */

.brand {
    padding: 45px;
    border-radius: 32px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.brand-title {
    font-size: 46px;
    font-weight: 900;
}

.brand-subtitle {
    margin-top: 15px;
    font-size: 18px;
}

.section {
    padding: 28px 32px;
    border-radius: 26px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 15px 40px
    rgba(37,99,235,0.18);

    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PAGE NAVIGATION
# ============================================================

home_page = st.Page(
    "app.py",
    title="Home",
    icon="🏠",
    default=True
)

login_page = st.Page(
    "pages/01_Login_Register.py",
    title="Login & Registration",
    icon="🔐"
)

search_page = st.Page(
    "pages/02_Property_Search.py",
    title="Property Search",
    icon="🔎"
)

post_property_page = st.Page(
    "pages/03_Post_Property.py",
    title="Post Property",
    icon="🏡"
)


# ============================================================
# NAVIGATION SYSTEM
# ============================================================

pg = st.navigation(
    [
        home_page,
        login_page,
        search_page,
        post_property_page
    ],
    position="sidebar"
)


# ============================================================
# SIDEBAR BRAND
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px 5px 25px 5px;
    ">

    <h1>🏠 FirstChoice</h1>

    <h3>Property Hub</h3>

    <p>
    India's Next-Generation<br>
    Real Estate Marketplace
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# RUN SELECTED PAGE
# ============================================================

pg.run()
