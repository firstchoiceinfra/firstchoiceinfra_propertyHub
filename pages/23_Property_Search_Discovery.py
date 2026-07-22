import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 23 - PROPERTY SEARCH & DISCOVERY ENGINE
# ============================================================

st.set_page_config(
    page_title="Discover Properties | FirstChoice Property Hub",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
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

/* BRAND */

.brand {

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 22px 32px;

    border-radius: 24px;

    color: white;

    box-shadow:
    0 18px 50px
    rgba(37,99,235,0.22);
}

.brand-title {

    font-size: 28px;

    font-weight: 900;

    letter-spacing: 2px;
}

.brand-subtitle {

    font-size: 11px;

    letter-spacing: 4px;

    color: #FDE68A;
}

/* HERO */

.hero {

    margin-top: 28px;

    padding: 48px;

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
}

.hero-title {

    font-size: 42px;

    font-weight: 900;
}

.hero-subtitle {

    font-size: 16px;

    color:
    rgba(255,255,255,0.88);
}

/* SEARCH */

.search-card {

    margin-top: 25px;

    padding: 30px;

    border-radius: 30px;

    background: white;

    box-shadow:
    0 20px 50px
    rgba(0,0,0,0.10);
}

/* SECTION */

.section-header {

    margin-top: 35px;

    margin-bottom: 22px;

    padding: 22px 30px;

    border-radius: 22px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    color: white;

    box-shadow:
    0 12px 35px
    rgba(37,99,235,0.18);
}

.section-title {

    font-size: 27px;

    font-weight: 900;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);
}

/* PROPERTY CARD */

.property-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

/* AI */

.ai-card {

    padding: 35px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 22px 60px
    rgba(124,58,237,0.25);
}

/* MAP */

.map-card {

    padding: 25px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #ECFEFF,
        #EEF2FF,
        #FDF4FF
    );

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);
}

/* TRUST */

.trust-card {

    padding: 25px;

    border-radius: 25px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );
}

/* FOOTER */

.footer {

    margin-top: 60px;

    padding: 45px;

    border-radius: 28px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FIRSTCHOICE INFRA
</div>

<div class="brand-subtitle">
PROPERTY HUB • INDIA PROPERTY DISCOVERY ENGINE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🔎 Discover Your Perfect Property
</div>

<div class="hero-subtitle">
Search millions of property possibilities across India.
Buy, Rent, Invest and Discover your next destination.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY PURPOSE
# ============================================================

st.markdown("""
<div class="search-card">

<h2>
🏠 What are you looking for?
</h2>

</div>
""", unsafe_allow_html=True)


purpose = st.radio(
    "Select Property Requirement",
    [
        "🏠 Buy",
        "🔑 Rent",
        "🏢 Commercial",
        "🌳 Land & Plot",
        "📈 Investment"
    ],
    horizontal=True
)


# ============================================================
# MAIN SEARCH
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Smart Property Search
</div>

<div class="section-subtitle">
Search by city, locality, project, landmark or PIN code.
</div>

</div>
""", unsafe_allow_html=True)


search_query = st.text_input(
    "Search Location",
    placeholder=
    "Example: Nagpur, Pune, Mumbai, Civil Lines, Wardha Road..."
)


s1, s2, s3 = st.columns(3)


with s1:

    state = st.selectbox(
        "Select State",
        [
            "All India",
            "Maharashtra",
            "Karnataka",
            "Telangana",
            "Delhi NCR",
            "Gujarat",
            "Rajasthan",
            "Madhya Pradesh",
            "Uttar Pradesh",
            "Tamil Nadu",
            "Other"
        ]
    )


with s2:

    city = st.selectbox(
        "Select City",
        [
            "All Cities",
            "Nagpur",
            "Mumbai",
            "Pune",
            "Bengaluru",
            "Hyderabad",
            "Delhi",
            "Gurugram",
            "Noida",
            "Nashik"
        ]
    )


with s3:

    locality = st.text_input(
        "Locality / Area",
        placeholder=
        "Example: Civil Lines"
    )


# ============================================================
# ADVANCED FILTERS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🎯 Advanced Property Filters
</div>

<div class="section-subtitle">
Refine your search and find exactly what you need.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3, f4 = st.columns(4)


with f1:

    property_type = st.selectbox(
        "Property Type",
        [
            "Any",
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


with f2:

    bhk = st.selectbox(
        "BHK",
        [
            "Any",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5+ BHK"
        ]
    )


with f3:

    furnishing = st.selectbox(
        "Furnishing",
        [
            "Any",
            "Unfurnished",
            "Semi Furnished",
            "Fully Furnished"
        ]
    )


with f4:

    possession = st.selectbox(
        "Possession",
        [
            "Any",
            "Ready to Move",
            "Under Construction",
            "New Launch"
        ]
    )


# ============================================================
# BUDGET
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💰 Budget & Area
</div>

<div class="section-subtitle">
Set your preferred price and property size.
</div>

</div>
""", unsafe_allow_html=True)


b1, b2 = st.columns(2)


with b1:

    budget = st.select_slider(
        "Maximum Budget",
        options=[
            "₹10 Lakh",
            "₹25 Lakh",
            "₹50 Lakh",
            "₹1 Crore",
            "₹2 Crore",
            "₹5 Crore",
            "₹10 Crore+"
        ],
        value="₹1 Crore"
    )


with b2:

    area_range = st.select_slider(
        "Minimum Property Area",
        options=[
            "500 Sq.Ft.",
            "750 Sq.Ft.",
            "1000 Sq.Ft.",
            "1500 Sq.Ft.",
            "2000 Sq.Ft.",
            "3000 Sq.Ft.",
            "5000+ Sq.Ft."
        ],
        value="1000 Sq.Ft."
    )


# ============================================================
# SMART FILTERS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ Smart Trust Filters
</div>

<div class="section-subtitle">
Find safer and more reliable properties.
</div>

</div>
""", unsafe_allow_html=True)


t1, t2, t3, t4 = st.columns(4)


with t1:

    verified_only = st.checkbox(
        "🛡️ Verified Properties"
    )


with t2:

    rera_only = st.checkbox(
        "📜 RERA Registered"
    )


with t3:

    owner_only = st.checkbox(
        "👤 Direct Owner"
    )


with t4:

    price_drop = st.checkbox(
        "💰 Recent Price Drop"
    )


# ============================================================
# SEARCH BUTTON
# ============================================================

if st.button(
    "🔎 SEARCH PROPERTIES",
    use_container_width=True
):

    st.success(
        "Searching properties based on your preferences..."
    )


# ============================================================
# AI PROPERTY MATCH
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 AI Property Match
</div>

<div class="section-subtitle">
Our intelligent recommendation engine finds properties matching your needs.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🎯 Your Search Intelligence
</h2>

<h1>
94% Match Found
</h1>

<p>
Based on your location, budget, property type and preferences,
we identified highly relevant properties for you.
</p>

<p>
🏠 126 properties match your requirements
</p>

<p>
🛡️ 84 verified properties
</p>

<p>
💰 21 properties recently reduced their prices
</p>

<p>
📍 63 properties are in your preferred locations
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAP DISCOVERY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🗺️ Explore Properties on Map
</div>

<div class="section-subtitle">
Discover properties visually by location.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="map-card">

<h2>
📍 Map-Based Property Discovery
</h2>

<p>
Future version will display live property listings,
price markers, neighbourhood information and nearby amenities.
</p>

</div>
""", unsafe_allow_html=True)


map_data = {
    "lat": [
        21.1458,
        21.1350,
        21.1600,
        21.1200
    ],

    "lon": [
        79.0882,
        79.0900,
        79.0800,
        79.1000
    ]
}


st.map(
    map_data
)


# ============================================================
# PROPERTY RESULTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Recommended Properties
</div>

<div class="section-subtitle">
Properties selected based on your search preferences.
</div>

</div>
""", unsafe_allow_html=True)


properties = [

    {
        "name":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "price":
        "₹1.25 Crore",

        "area":
        "1650 Sq.Ft.",

        "match":
        "94%",

        "trust":
        "98%",

        "status":
        "💰 Price Reduced"
    },

    {
        "name":
        "Luxury Independent Villa",

        "location":
        "Baner, Pune",

        "price":
        "₹2.40 Crore",

        "area":
        "2800 Sq.Ft.",

        "match":
        "91%",

        "trust":
        "95%",

        "status":
        "🛡️ Verified"
    },

    {
        "name":
        "Premium Residential Plot",

        "location":
        "Wardha Road, Nagpur",

        "price":
        "₹65 Lakh",

        "area":
        "2000 Sq.Ft.",

        "match":
        "89%",

        "trust":
        "96%",

        "status":
        "🔥 Popular"
    }

]


for index, property_data in enumerate(properties):

    st.markdown(
        f"""
        <div class="property-card">

        <h2>
        🏠 {property_data["name"]}
        </h2>

        <p>
        📍 {property_data["location"]}
        </p>

        <h2>
        💰 {property_data["price"]}
        </h2>

        <p>
        📐 Area: {property_data["area"]}
        </p>

        <p>
        🎯 AI Match Score:
        <b>{property_data["match"]}</b>
        </p>

        <p>
        🛡️ Trust Score:
        <b>{property_data["trust"]}</b>
        </p>

        <p>
        {property_data["status"]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:

        if st.button(
            "👁️ View",
            key=f"view_{index}",
            use_container_width=True
        ):

            st.info(
                "Property details selected."
            )


    with c2:

        if st.button(
            "❤️ Save",
            key=f"save_{index}",
            use_container_width=True
        ):

            st.success(
                "Property added to wishlist."
            )


    with c3:

        if st.button(
            "⚖️ Compare",
            key=f"compare_{index}",
            use_container_width=True
        ):

            st.info(
                "Property added to comparison."
            )


    with c4:

        if st.button(
            "📅 Visit",
            key=f"visit_{index}",
            use_container_width=True
        ):

            st.success(
                "Site visit request started."
            )


    with c5:

        if st.button(
            "💬 Enquiry",
            key=f"enquiry_{index}",
            use_container_width=True
        ):

            st.info(
                "Property enquiry form opened."
            )


# ============================================================
# TRUSTED PROPERTY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ FirstChoice Trusted Properties
</div>

<div class="section-subtitle">
Discover properties that have completed additional verification.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="trust-card">

<h2>
🛡️ Verified Property Network
</h2>

<p>
Properties may be verified based on available identity,
ownership and listing information.
</p>

<p>
⭐ Verified Owner
</p>

<p>
📄 Documents Reviewed
</p>

<p>
📍 Location Confirmed
</p>

<p>
🏠 Property Information Validated
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NEW LAUNCHES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 New Launches & Fresh Listings
</div>

<div class="section-subtitle">
Discover newly listed properties before everyone else.
</div>

</div>
""", unsafe_allow_html=True)


n1, n2, n3 = st.columns(3)


with n1:

    st.info(
        """
        🆕 **New Property**

        Listed 10 minutes ago

        📍 Nagpur
        """
    )


with n2:

    st.success(
        """
        🚀 **New Project**

        Premium Township

        📍 Pune
        """
    )


with n3:

    st.warning(
        """
        🔥 **Trending**

        120+ views today

        📍 Bengaluru
        """
    )


# ============================================================
# LOCATION INTELLIGENCE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📍 Location Intelligence
</div>

<div class="section-subtitle">
Understand the neighbourhood before making a decision.
</div>

</div>
""", unsafe_allow_html=True)


l1, l2, l3, l4 = st.columns(4)


with l1:

    st.metric(
        "🏫 Schools Nearby",
        "12"
    )


with l2:

    st.metric(
        "🏥 Hospitals",
        "8"
    )


with l3:

    st.metric(
        "🚇 Metro / Transit",
        "4"
    )


with l4:

    st.metric(
        "🛒 Shopping",
        "26"
    )


# ============================================================
# SMART ALERT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔔 Create Property Search Alert
</div>

<div class="section-subtitle">
Get notified instantly when matching properties are listed.
</div>

</div>
""", unsafe_allow_html=True)


alert_name = st.text_input(
    "Search Alert Name",
    placeholder=
    "Example: 3 BHK Under ₹1.5 Cr in Nagpur"
)


frequency = st.selectbox(
    "Alert Frequency",
    [
        "Instant",
        "Daily",
        "Weekly"
    ]
)


if st.button(
    "🔔 CREATE SEARCH ALERT",
    use_container_width=True
):

    if alert_name:

        st.success(
            f"Search alert '{alert_name}' created successfully."
        )

    else:

        st.warning(
            "Please enter an alert name."
        )


# ============================================================
# FUTURE INTELLIGENCE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Next-Generation Property Discovery
</div>

<div class="section-subtitle">
Features that will make FirstChoice Property Hub different.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.info(
        """
        🤖 **AI Property Advisor**

        Tell us your requirements in natural language
        and receive property recommendations.
        """
    )


with f2:

    st.success(
        """
        🗺️ **Smart Map Search**

        Draw an area on the map
        and discover properties inside it.
        """
    )


with f3:

    st.warning(
        """
        🛡️ **Fraud Risk Detection**

        Intelligent signals to identify
        suspicious property listings.
        """
    )


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

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
