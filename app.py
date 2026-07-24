import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MAIN HOME PAGE
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
# SIDEBAR BRAND
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
    ">

    <h1>🏠 FirstChoice</h1>

    <h3>Property Hub</h3>

    <hr>

    <p>
    India's Next-Generation<br>
    Real Estate Marketplace
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MAIN HERO
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FirstChoice Infra Property Hub
</div>

<div class="brand-subtitle">

India's Next-Generation Real Estate Marketplace

<br><br>

Buy • Sell • Rent • Invest • Build • Discover

</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# WELCOME
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Welcome to FirstChoice Property Hub
</h2>

<p>
Your complete digital property ecosystem.
</p>

<p>
Buy, sell, rent, invest and discover properties
across India.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUICK ACCESS
# ============================================================

st.subheader("🚀 Quick Access")

c1, c2, c3 = st.columns(3)


with c1:

    if st.button(
        "🔐 Login / Register",
        use_container_width=True
    ):

        st.switch_page(
            "pages/01_Login_Register.py"
        )


with c2:

    if st.button(
        "🔎 Property Search",
        use_container_width=True
    ):

        st.switch_page(
            "pages/02_Property_Search.py"
        )


with c3:

    if st.button(
        "🏠 Post Property",
        use_container_width=True
    ):

        st.switch_page(
            "pages/03_Post_Property.py"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<br><br>

<div style="
padding:30px;
border-radius:25px;
background:linear-gradient(
135deg,
#071952,
#1E1B4B,
#4C1D95
);
color:white;
text-align:center;
">

<h3>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h3>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

</div>

""", unsafe_allow_html=True)
