import streamlit as st

st.set_page_config(
    page_title="FirstChoice Property Hub",
    page_icon="🏠",
    layout="wide"
)

# ============================================================
# FIRSTCHOICE PROPERTY HUB
# MAIN APP
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F7F9FF,
        #FFF7F3,
        #F7F1FF,
        #EFFCFF
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

.hero {
    padding: 60px 45px;
    border-radius: 35px;
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
}

.hero h1 {
    font-size: 48px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
}

.card {
    padding: 30px;
    border-radius: 28px;
    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);
}

.section {
    margin-top: 30px;
    padding: 25px 30px;
    border-radius: 24px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🏠 FirstChoice Property Hub
</h1>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Discover
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUICK SEARCH
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Find Your Perfect Property
</h2>

<p>
Search properties across India with smart discovery tools.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    st.selectbox(
        "Looking For",
        [
            "Buy",
            "Rent",
            "Commercial",
            "Land & Plot",
            "Investment"
        ]
    )


with c2:

    st.text_input(
        "Location",
        placeholder="City, Area or PIN Code"
    )


with c3:

    st.selectbox(
        "Property Type",
        [
            "Any Property",
            "Apartment",
            "Villa",
            "Independent House",
            "Plot",
            "Commercial",
            "Farm Land"
        ]
    )


if st.button(
    "🔎 SEARCH PROPERTY",
    use_container_width=True
):

    st.info(
        "Property search module is ready."
    )


# ============================================================
# FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 FirstChoice Property Hub
</h2>

<p>
A powerful real estate platform designed for the Indian market.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.markdown("""
    <div class="card">

    <h2>🏠 Buy & Sell</h2>

    <p>
    Discover verified properties
    from owners, agents and builders.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="card">

    <h2>🔑 Rent</h2>

    <p>
    Find homes, apartments and
    commercial spaces for rent.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="card">

    <h2>🛡️ Verified Listings</h2>

    <p>
    Future identity and property
    verification system.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<br><br>

<div class="hero">

<h2>
FirstChoice Infra Property Hub
</h2>

<p>
Building India's trusted digital property ecosystem.
</p>

</div>
""", unsafe_allow_html=True)
