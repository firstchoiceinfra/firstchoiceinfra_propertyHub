import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 02 — PROPERTY SEARCH
# ============================================================

st.set_page_config(
    page_title="Property Search | FirstChoice Property Hub",
    page_icon="🔎",
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
    radial-gradient(
        circle at 10% 10%,
        rgba(59,130,246,0.10),
        transparent 30%
    ),
    radial-gradient(
        circle at 90% 20%,
        rgba(168,85,247,0.10),
        transparent 30%
    ),
    linear-gradient(
        135deg,
        #F8FAFC,
        #EEF2FF,
        #FAF5FF,
        #F0FDFA
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
        #020617,
        #0F172A,
        #1E1B4B,
        #312E81
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}


/* HERO */

.search-hero {
    padding: 55px;
    border-radius: 40px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #172554,
        #4338CA,
        #7E22CE,
        #BE185D
    );

    box-shadow:
    0 30px 80px
    rgba(30,41,59,0.30);

    margin-bottom: 35px;
}

.search-hero h1 {
    font-size: 48px;
    font-weight: 900;
}

.search-hero p {
    font-size: 19px;
    line-height: 1.7;
}


/* SEARCH PANEL */

.search-panel {
    padding: 32px;
    border-radius: 30px;

    background:
    rgba(255,255,255,0.92);

    border:
    1px solid
    rgba(148,163,184,0.25);

    box-shadow:
    0 20px 50px
    rgba(15,23,42,0.08);

    margin-bottom: 30px;
}


/* SECTION */

.section-title {
    padding: 22px 28px;
    border-radius: 25px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4338CA,
        #7E22CE
    );

    box-shadow:
    0 15px 40px
    rgba(79,70,229,0.20);

    margin:
    30px 0 25px 0;
}

.section-title h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}


/* PROPERTY CARD */

.property-card {
    padding: 28px;
    border-radius: 30px;

    background:
    rgba(255,255,255,0.95);

    border:
    1px solid
    #E2E8F0;

    box-shadow:
    0 18px 50px
    rgba(15,23,42,0.10);

    margin-bottom: 25px;

    transition:
    transform 0.25s ease;
}

.property-card:hover {
    transform:
    translateY(-5px);
}


/* BADGE */

.badge {
    display: inline-block;

    padding:
    7px 14px;

    border-radius:
    50px;

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );

    color:
    white;

    font-size:
    13px;

    font-weight:
    700;
}


/* PRICE */

.price {
    color:
    #047857;

    font-size:
    25px;

    font-weight:
    900;
}


/* FOOTER */

.fc-footer {
    margin-top: 60px;
    padding: 40px;
    border-radius: 32px;

    color: white;
    text-align: center;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1E1B4B,
        #312E81
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:25px;
    ">

    <h1>🏠 FirstChoice</h1>

    <h3>Property Hub</h3>

    <hr>

    <p>
    India's Next-Generation<br>
    Real Estate Ecosystem
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Navigation")

    st.page_link(
        "app.py",
        label="🏠 Home"
    )

    st.page_link(
        "pages/01_Login_Register.py",
        label="🔐 Login & Registration"
    )

    st.page_link(
        "pages/02_Property_Search.py",
        label="🔎 Property Search"
    )

    st.page_link(
        "pages/03_Post_Property.py",
        label="🏡 Post Property"
    )


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="search-hero">

<h1>
🔎 Find Your Perfect Property
</h1>

<p>
Search homes, plots, apartments, commercial properties,
upcoming projects and rental properties across India.
</p>

<p>
🏠 Buy &nbsp; • &nbsp;
🏢 Commercial &nbsp; • &nbsp;
🌳 Land &nbsp; • &nbsp;
🏙️ Projects &nbsp; • &nbsp;
🔑 Rent
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH PANEL
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🔎 Advanced Property Search
</h2>

</div>
""", unsafe_allow_html=True)


with st.container(border=True):

    # --------------------------------------------------------
    # PURPOSE
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        purpose = st.selectbox(
            "🎯 Looking For",
            [
                "Buy",
                "Rent",
                "Lease",
                "Invest"
            ]
        )


    with col2:

        property_category = st.selectbox(
            "🏠 Property Category",
            [
                "Residential",
                "Commercial",
                "Plot / Land",
                "Agricultural Land",
                "Industrial Property",
                "Upcoming Project",
                "Ready to Move Project"
            ]
        )


    with col3:

        property_type = st.selectbox(
            "🏡 Property Type",
            [
                "Any",
                "Apartment",
                "Villa",
                "Independent House",
                "Builder Floor",
                "Studio Apartment",
                "Plot",
                "Farm Land",
                "Office",
                "Shop",
                "Warehouse",
                "Showroom"
            ]
        )


    # --------------------------------------------------------
    # LOCATION
    # --------------------------------------------------------

    st.markdown("### 🌍 Property Location")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        country = st.selectbox(
            "🌍 Country",
            [
                "India",
                "Other Country"
            ]
        )


    with col2:

        state = st.selectbox(
            "🗺️ State",
            [
                "Maharashtra",
                "Madhya Pradesh",
                "Delhi",
                "Gujarat",
                "Karnataka",
                "Telangana",
                "Rajasthan",
                "Uttar Pradesh",
                "Other State"
            ]
        )


    with col3:

        city = st.selectbox(
            "🏙️ City",
            [
                "Nagpur",
                "Mumbai",
                "Pune",
                "Nashik",
                "Indore",
                "Bhopal",
                "Delhi",
                "Other City"
            ]
        )


    with col4:

        area = st.selectbox(
            "📍 Area",
            [
                "Any Area",
                "Civil Lines",
                "Dharampeth",
                "Manish Nagar",
                "Wardha Road",
                "Hingna",
                "Katol Road",
                "Other Area"
            ]
        )


    # --------------------------------------------------------
    # CUSTOM AREA
    # --------------------------------------------------------

    if area == "Other Area":

        custom_area = st.text_input(
            "📍 Enter Your Area Name",
            placeholder="Example: Your specific locality / village / area"
        )

    else:

        custom_area = ""


    # --------------------------------------------------------
    # BUDGET
    # --------------------------------------------------------

    st.markdown("### 💰 Budget & Property Size")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        min_budget = st.number_input(
            "💰 Minimum Budget",
            min_value=0,
            value=0,
            step=100000
        )


    with col2:

        max_budget = st.number_input(
            "💰 Maximum Budget",
            min_value=0,
            value=10000000,
            step=100000
        )


    with col3:

        min_area = st.number_input(
            "📐 Minimum Area (Sq.Ft.)",
            min_value=0,
            value=0
        )


    with col4:

        max_area = st.number_input(
            "📐 Maximum Area (Sq.Ft.)",
            min_value=0,
            value=10000
        )


    # --------------------------------------------------------
    # PROPERTY FEATURES
    # --------------------------------------------------------

    st.markdown("### 🏗️ Property Features")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        bhk = st.selectbox(
            "🛏️ BHK",
            [
                "Any",
                "1 BHK",
                "2 BHK",
                "3 BHK",
                "4 BHK",
                "5+ BHK"
            ]
        )


    with col2:

        project_status = st.selectbox(
            "🏗️ Project Status",
            [
                "Any",
                "Upcoming",
                "Under Construction",
                "Ongoing",
                "Ready to Move"
            ]
        )


    with col3:

        possession = st.selectbox(
            "📅 Possession",
            [
                "Any",
                "Immediate",
                "Within 6 Months",
                "Within 1 Year",
                "1-2 Years",
                "2+ Years"
            ]
        )


    with col4:

        furnishing = st.selectbox(
            "🛋️ Furnishing",
            [
                "Any",
                "Unfurnished",
                "Semi Furnished",
                "Fully Furnished"
            ]
        )


    # --------------------------------------------------------
    # ADVANCED FILTER
    # --------------------------------------------------------

    st.markdown("### ⭐ Advanced Filters")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        video_available = st.checkbox(
            "🎥 Video Available"
        )


    with col2:

        location_available = st.checkbox(
            "📍 Google Location Available"
        )


    with col3:

        premium_only = st.checkbox(
            "⭐ Premium Listings Only"
        )


    with col4:

        verified_only = st.checkbox(
            "✅ Verified Properties Only"
        )


    # --------------------------------------------------------
    # SEARCH BUTTON
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)


    search_button = st.button(
        "🔎 SEARCH PROPERTIES",
        use_container_width=True
    )


# ============================================================
# SEARCH RESULT
# ============================================================

if search_button:

    st.success(
        "🔎 Property search completed successfully."
    )

    st.info(
        "Current version में demo listings दिखाई जा रही हैं. "
        "Database integration के बाद यहाँ real property listings आएँगी."
    )


# ============================================================
# SAMPLE PROPERTY LISTINGS
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🏡 Featured Property Listings
</h2>

</div>
""", unsafe_allow_html=True)


properties = [

    {
        "title":
        "Premium Residential Plot",
        "location":
        "Nagpur, Maharashtra",
        "price":
        "₹25,00,000",
        "type":
        "Residential Plot",
        "status":
        "Ready to Move",
        "area":
        "1200 Sq.Ft.",
        "verified":
        True
    },

    {
        "title":
        "Luxury 3 BHK Apartment",
        "location":
        "Pune, Maharashtra",
        "price":
        "₹85,00,000",
        "type":
        "Apartment",
        "status":
        "Ready to Move",
        "area":
        "1450 Sq.Ft.",
        "verified":
        True
    },

    {
        "title":
        "Upcoming Premium Township",
        "location":
        "Nagpur, Maharashtra",
        "price":
        "₹45,00,000",
        "type":
        "Upcoming Project",
        "status":
        "Upcoming",
        "area":
        "1000 Sq.Ft.",
        "verified":
        True
    }

]


for property_data in properties:

    st.markdown(
        f"""
        <div class="property-card">

        <span class="badge">
        ⭐ FEATURED PROPERTY
        </span>

        <h2>
        🏠 {property_data["title"]}
        </h2>

        <p>
        📍 {property_data["location"]}
        </p>

        <p>
        🏡 Type:
        <b>{property_data["type"]}</b>
        </p>

        <p>
        📐 Area:
        <b>{property_data["area"]}</b>
        </p>

        <p>
        🏗️ Status:
        <b>{property_data["status"]}</b>
        </p>

        <div class="price">
        {property_data["price"]}
        </div>

        <br>

        <p>
        ✅ Verified Property
        &nbsp;&nbsp;
        🎥 Video Tour Available
        &nbsp;&nbsp;
        📍 Google Location
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ACTION BUTTONS
# ============================================================

st.markdown("### 🚀 Quick Actions")


c1, c2, c3 = st.columns(3)


with c1:

    if st.button(
        "🏡 Post Your Property",
        use_container_width=True
    ):

        st.switch_page(
            "pages/03_Post_Property.py"
        )


with c2:

    if st.button(
        "🔐 Login / Register",
        use_container_width=True
    ):

        st.switch_page(
            "pages/01_Login_Register.py"
        )


with c3:

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.switch_page(
            "app.py"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="fc-footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

<p>
India's Next-Generation Real Estate Ecosystem
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
