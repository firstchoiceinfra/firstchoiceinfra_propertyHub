import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MAIN APP
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

/* HERO */

.hero {
    padding: 50px;
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

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.8;
}

/* SECTION */

.section {
    padding: 25px 30px;
    border-radius: 25px;
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

    margin-top: 30px;
    margin-bottom: 25px;
}

/* CARD */

.card {
    padding: 30px;
    border-radius: 25px;
    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    min-height: 180px;
}

/* FOOTER */

.footer {
    margin-top: 60px;
    padding: 40px;
    border-radius: 30px;

    color: white;
    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B,
        #4C1D95
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;">

    <h1>🏠 FirstChoice</h1>

    <h3>Property Hub</h3>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    ### 🚀 Welcome

    Use the menu below to explore
    FirstChoice Infra Property Hub.
    """)

    st.divider()

    st.markdown("""
    ### 📌 Available Pages

    👤 Login / Register

    🔎 Property Search

    🏠 Post Property
    """)

    st.divider()

    st.info(
        "Select any page from the left sidebar menu."
    )


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🏠 FirstChoice Infra Property Hub
</h1>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Find Your Perfect Property
</h2>

<p>
Search properties, plots, land, commercial spaces
and local property services.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    looking_for = st.selectbox(
        "🏠 What are you looking for?",
        [
            "Buy Property",
            "Rent Property",
            "Commercial Property",
            "Land & Plot",
            "New Project",
            "Investment"
        ]
    )


with c2:

    location = st.text_input(
        "📍 Location",
        placeholder="City, Town, Village or Area"
    )


with c3:

    property_type = st.selectbox(
        "🏡 Property Type",
        [
            "Any Property",
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Plot",
            "Farm Land",
            "Office",
            "Shop",
            "Warehouse"
        ]
    )


if st.button(
    "🔎 SEARCH PROPERTY",
    use_container_width=True
):

    st.success(
        "Search request submitted successfully."
    )

    st.info(
        "Please select 🔎 Property Search from the left sidebar to explore properties."
    )


# ============================================================
# PLATFORM FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 One Platform. Complete Property Ecosystem.
</h2>

<p>
Everything related to real estate in one place.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2, f3, f4 = st.columns(4)


with f1:

    st.markdown("""
    <div class="card">

    <h2>🏠 Buy</h2>

    <p>
    Find homes, apartments,
    villas and plots.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="card">

    <h2>🔑 Rent</h2>

    <p>
    Find residential and
    commercial rental properties.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="card">

    <h2>📢 Post Property</h2>

    <p>
    Post your property with
    photos, videos and location.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f4:

    st.markdown("""
    <div class="card">

    <h2>🛡️ Trusted</h2>

    <p>
    Build a trusted property
    ecosystem for India.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
