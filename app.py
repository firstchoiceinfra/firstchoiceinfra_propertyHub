import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MAIN APP.PY
# ============================================================

st.set_page_config(
    page_title="FirstChoice Property Hub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM MULTINATIONAL UI
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

    padding: 35px;

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

    font-size: 48px;

    font-weight: 900;

    line-height: 1.1;
}

.brand-subtitle {

    margin-top: 15px;

    font-size: 18px;

    color:
    rgba(255,255,255,0.88);
}

/* SEARCH CARD */

.search-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 30px;
}

/* SECTION */

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
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 15px 40px
    rgba(37,99,235,0.18);
}

/* FEATURE CARD */

.card {

    padding: 30px;

    min-height: 200px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    transition:
    transform 0.2s ease;
}

.card:hover {

    transform:
    translateY(-5px);
}

/* FOOTER */

.footer {

    margin-top: 60px;

    padding: 45px;

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
    <h1>
    🏠 FirstChoice
    </h1>

    <p>
    Property Hub
    </p>

    <hr>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🚀 Explore

    Use the pages menu above to explore
    the FirstChoice Property Hub.
    """)

    st.markdown("""
    ### 🏠 Property

    • Buy Property

    • Rent Property

    • Commercial

    • Land & Plot

    • New Projects
    """)

    st.markdown("""
    ### 🛡️ Trust

    • Verified Listings

    • Verified Owners

    • Secure Enquiry

    • Property Verification
    """)

    st.markdown("""
    ### 👤 Account

    Login and registration
    modules are available
    through the application pages.
    """)


# ============================================================
# MAIN HERO
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FirstChoice Property Hub
</div>

<div class="brand-subtitle">
India's Next-Generation Real Estate Marketplace
<br><br>
Buy • Sell • Rent • Invest • Discover
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH SECTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Find Your Perfect Property
</h2>

<p>
Search homes, plots, commercial spaces and investment opportunities
across India.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="search-card">',
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)


with c1:

    looking_for = st.selectbox(
        "What are you looking for?",
        [
            "🏠 Buy",
            "🔑 Rent",
            "🏢 Commercial",
            "🌳 Land & Plot",
            "📈 Investment"
        ]
    )


with c2:

    location = st.text_input(
        "📍 Location",
        placeholder=
        "City, Locality or PIN Code"
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
        "Property search request submitted."
    )

    st.info(
        "Open the Property Search page from the Pages menu to explore all listings."
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PLATFORM FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 One Platform. Every Property Need.
</h2>

<p>
A modern property ecosystem designed for buyers,
owners, agents, builders and investors.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2, f3, f4 = st.columns(4)


with f1:

    st.markdown("""
    <div class="card">

    <h2>
    🏠 Buy
    </h2>

    <p>
    Discover apartments, villas,
    houses and plots across India.
    </p>

    <p>
    🎯 Smart Property Discovery
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="card">

    <h2>
    🔑 Rent
    </h2>

    <p>
    Find homes, apartments and
    commercial spaces for rent.
    </p>

    <p>
    📍 Location-Based Search
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="card">

    <h2>
    🚀 Sell
    </h2>

    <p>
    List your property with photos,
    videos and detailed information.
    </p>

    <p>
    📸 Premium Property Listings
    </p>

    </div>
    """, unsafe_allow_html=True)


with f4:

    st.markdown("""
    <div class="card">

    <h2>
    🛡️ Trust
    </h2>

    <p>
    Future identity and property
    verification ecosystem.
    </p>

    <p>
    ⭐ Trust Score
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# WHY FIRSTCHOICE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🌟 Why FirstChoice Property Hub?
</h2>

<p>
We are building more than a property listing website.
We are building a complete digital property ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


w1, w2, w3 = st.columns(3)


with w1:

    st.markdown("""
    <div class="card">

    <h2>
    🤖 Smart Technology
    </h2>

    <p>
    AI-powered recommendations,
    smart search and property intelligence.
    </p>

    </div>
    """, unsafe_allow_html=True)


with w2:

    st.markdown("""
    <div class="card">

    <h2>
    🛡️ Trusted Ecosystem
    </h2>

    <p>
    Identity verification,
    property verification and trust signals.
    </p>

    </div>
    """, unsafe_allow_html=True)


with w3:

    st.markdown("""
    <div class="card">

    <h2>
    🇮🇳 India-Wide Vision
    </h2>

    <p>
    Designed to scale from local property
    discovery to a nationwide marketplace.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CALL TO ACTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Ready to Find Your Next Property?
</h2>

<p>
Explore the pages from the sidebar and discover
the next generation of property search.
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
Buy • Sell • Rent • Invest • Discover
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
