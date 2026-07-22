import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 9 - INDIA PROPERTY SEARCH ENGINE
# PREMIUM REAL ESTATE DISCOVERY PLATFORM
# ============================================================

st.set_page_config(
    page_title="Search Properties | FirstChoice Property Hub",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM CSS
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

/* ============================================================
BRAND
============================================================ */

.brand {

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 20px 32px;

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

/* ============================================================
HERO SEARCH
============================================================ */

.hero {

    margin-top: 28px;

    padding: 55px 45px;

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

    position: relative;

    overflow: hidden;
}

.hero::after {

    content: "";

    position: absolute;

    width: 350px;

    height: 350px;

    right: -100px;

    top: -170px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.12);
}

.hero-title {

    font-size: 46px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.hero-subtitle {

    font-size: 17px;

    color:
    rgba(255,255,255,0.88);

    position: relative;

    z-index: 2;
}

/* ============================================================
SECTION HEADER
============================================================ */

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

    position: relative;

    overflow: hidden;
}

.section-header::after {

    content: "";

    position: absolute;

    width: 150px;

    height: 150px;

    right: -50px;

    top: -75px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.12);
}

.section-title {

    font-size: 27px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);

    position: relative;

    z-index: 2;
}

/* ============================================================
PROPERTY CARD
============================================================ */

.property-card {

    background: white;

    border-radius: 28px;

    overflow: hidden;

    margin-bottom: 25px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);
}

.property-image {

    width: 100%;

    height: 230px;

    object-fit: cover;
}

.property-content {

    padding: 25px;
}

/* ============================================================
BADGES
============================================================ */

.badge {

    display: inline-block;

    padding: 7px 14px;

    border-radius: 30px;

    font-size: 11px;

    font-weight: 800;

    color: white;

    margin-right: 5px;
}

.verified {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.premium {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.featured {

    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

/* ============================================================
SEARCH BOX
============================================================ */

.search-box {

    background: white;

    padding: 30px;

    border-radius: 28px;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);
}

/* ============================================================
CITY CARD
============================================================ */

.city-card {

    padding: 30px;

    border-radius: 25px;

    color: white;

    min-height: 170px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED
    );

    box-shadow:
    0 12px 35px
    rgba(37,99,235,0.18);
}

/* ============================================================
PREMIUM
============================================================ */

.premium-card {

    padding: 40px;

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

/* ============================================================
FOOTER
============================================================ */

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
PROPERTY HUB • INDIA'S SMART REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🔎 Find Your Perfect Property
</div>

<div class="hero-subtitle">
Discover verified homes, plots, villas, apartments,
commercial spaces and investment opportunities across India.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH ENGINE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🇮🇳 India Property Search
</div>

<div class="section-subtitle">
Search thousands of real estate opportunities across India.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="search-box">',
    unsafe_allow_html=True
)


# BUY / RENT / COMMERCIAL

transaction_type = st.radio(

    "I am looking to",

    [
        "🏡 Buy",
        "🔑 Rent",
        "🏢 Commercial",
        "🌱 Land / Plot"
    ],

    horizontal=True

)


# LOCATION

l1,l2,l3 = st.columns(3)


with l1:

    state = st.selectbox(

        "State",

        [
            "All India",
            "Maharashtra",
            "Delhi NCR",
            "Karnataka",
            "Telangana",
            "Gujarat",
            "Rajasthan",
            "Madhya Pradesh",
            "Uttar Pradesh",
            "West Bengal",
            "Tamil Nadu",
            "Goa"
        ]

    )


with l2:

    city = st.selectbox(

        "City",

        [
            "All Cities",
            "Nagpur",
            "Mumbai",
            "Pune",
            "Bengaluru",
            "Hyderabad",
            "Delhi",
            "Noida",
            "Gurugram",
            "Ahmedabad",
            "Jaipur"
        ]

    )


with l3:

    locality = st.text_input(

        "Locality / Area",

        placeholder="Enter locality or landmark"

    )


# PROPERTY TYPE

p1,p2,p3,p4 = st.columns(4)


with p1:

    property_type = st.selectbox(

        "Property Type",

        [
            "All Types",
            "Apartment",
            "Villa",
            "Independent House",
            "Plot",
            "Farm Land",
            "Office",
            "Shop",
            "Warehouse",
            "Industrial Property"
        ]

    )


with p2:

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


with p3:

    budget = st.selectbox(

        "Budget",

        [
            "Any Budget",
            "Under ₹25 Lakh",
            "₹25 - ₹50 Lakh",
            "₹50 Lakh - ₹1 Crore",
            "₹1 - ₹3 Crore",
            "₹3 - ₹5 Crore",
            "Above ₹5 Crore"
        ]

    )


with p4:

    area = st.selectbox(

        "Area",

        [
            "Any Area",
            "Under 500 Sq.Ft",
            "500 - 1000 Sq.Ft",
            "1000 - 2000 Sq.Ft",
            "2000 - 5000 Sq.Ft",
            "Above 5000 Sq.Ft"
        ]

    )


# VERIFICATION

v1,v2,v3 = st.columns(3)


with v1:

    verified_only = st.checkbox(

        "🛡️ Verified Listings Only"

    )


with v2:

    aadhaar_verified = st.checkbox(

        "🪪 Identity Verified Owner"

    )


with v3:

    mobile_verified = st.checkbox(

        "📱 Mobile Verified"

    )


search_button = st.button(

    "🔎 SEARCH PROPERTIES",

    use_container_width=True

)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


if search_button:

    st.success(

        f"""
        Searching properties for:
        {transaction_type} •
        {state} •
        {city} •
        {property_type}
        """

    )


# ============================================================
# POPULAR CITIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🌆 Explore Popular Indian Cities
</div>

<div class="section-subtitle">
Discover high-demand real estate markets across India.
</div>

</div>
""", unsafe_allow_html=True)


cities = [

    ("🏙️","Mumbai","Luxury & Premium Homes"),

    ("🌆","Pune","IT & Residential Growth"),

    ("🏡","Nagpur","Plots & Investment"),

    ("🏢","Bengaluru","Technology & Rentals"),

    ("🌇","Hyderabad","IT & New Projects"),

    ("🏙️","Delhi NCR","Luxury & Commercial")

]


city_cols = st.columns(3)


for index, city_item in enumerate(cities):

    with city_cols[index % 3]:

        st.markdown(
            f"""
            <div class="city-card">

            <div style="font-size:38px;">
            {city_item[0]}
            </div>

            <h2>
            {city_item[1]}
            </h2>

            <p>
            {city_item[2]}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")


# ============================================================
# PROPERTY RESULTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏆 Recommended Properties
</div>

<div class="section-subtitle">
Premium properties selected for your discovery.
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
        "₹1.25 Cr",

        "type":
        "Apartment",

        "verified":
        True,

        "premium":
        True,

        "featured":
        True,

        "image":
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=85"

    },

    {

        "name":
        "Modern Luxury Villa",

        "location":
        "Baner, Pune",

        "price":
        "₹2.80 Cr",

        "type":
        "Villa",

        "verified":
        True,

        "premium":
        True,

        "featured":
        False,

        "image":
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85"

    },

    {

        "name":
        "Premium Residential Plot",

        "location":
        "Wardha Road, Nagpur",

        "price":
        "₹48 Lakh",

        "type":
        "Plot",

        "verified":
        True,

        "premium":
        False,

        "featured":
        True,

        "image":
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"

    }

]


for index, property_item in enumerate(properties):


    st.markdown(

        f"""
        <div class="property-card">

        <img
        class="property-image"
        src="{property_item['image']}"
        >

        <div class="property-content">

        <span class="badge verified">
        🛡️ Verified
        </span>

        {
        '<span class="badge premium">⭐ Premium</span>'
        if property_item["premium"]
        else ""
        }

        {
        '<span class="badge featured">🔥 Featured</span>'
        if property_item["featured"]
        else ""
        }

        <h2>
        {property_item['name']}
        </h2>

        <p>
        📍 {property_item['location']}
        </p>

        <h2 style="color:#7C3AED;">
        {property_item['price']}
        </h2>

        <p>
        🏠 {property_item['type']}
        </p>

        </div>

        </div>
        """,

        unsafe_allow_html=True

    )


    b1,b2,b3,b4 = st.columns(4)


    with b1:

        if st.button(

            "🏡 View Details",

            key=f"view_{index}",

            use_container_width=True

        ):

            st.info(

                f"Opening {property_item['name']}"

            )


    with b2:

        if st.button(

            "❤️ Save",

            key=f"save_{index}",

            use_container_width=True

        ):

            st.success(

                "Property saved to your favourites."

            )


    with b3:

        if st.button(

            "⚖️ Compare",

            key=f"compare_{index}",

            use_container_width=True

        ):

            st.info(

                "Property added to comparison."

            )


    with b4:

        if st.button(

            "📅 Site Visit",

            key=f"visit_{index}",

            use_container_width=True

        ):

            st.success(

                "Site visit request started."

            )


# ============================================================
# VERIFIED PROPERTY TRUST
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ FirstChoice Verified Properties
</div>

<div class="section-subtitle">
Our future verification system will help buyers discover trusted listings.
</div>

</div>
""", unsafe_allow_html=True)


trust1,trust2,trust3 = st.columns(3)


with trust1:

    st.info(

        """
        🪪 **Identity Verification**

        Owner identity verification
        will be connected with secure
        KYC infrastructure.
        """

    )


with trust2:

    st.success(

        """
        📱 **Mobile Verification**

        Property owners and agents
        can verify their mobile number.
        """

    )


with trust3:

    st.warning(

        """
        📄 **Property Verification**

        Property documents and ownership
        verification will be integrated
        in the production backend.
        """

    )


# ============================================================
# SMART PROPERTY DISCOVERY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 Smart Property Discovery
</div>

<div class="section-subtitle">
Your future personalised real estate discovery assistant.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="premium-card">

<h2>
🎯 Find Properties That Match Your Lifestyle
</h2>

<p>
FirstChoice Property Hub will use your preferred city,
budget, property type, location and saved properties
to recommend relevant listings.
</p>

<h3>
🇮🇳 Built for India's Real Estate Market
</h3>

<p>
From local residential plots to luxury apartments,
commercial properties and investment opportunities.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(

    "🚀 Explore Smart Recommendations",

    use_container_width=True

):

    st.info(

        "Smart recommendation engine will be connected in the production backend."

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
