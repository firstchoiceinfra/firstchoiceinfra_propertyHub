import streamlit as st

# ============================================================
# PAGE 4 — PROPERTY SEARCH & DISCOVERY
# MERGED FROM:
# 04_property_search.py
# 9_Property_Search.py
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Search | FirstChoice Property Hub",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM MULTICOLOUR UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F5F7FF 0%,
        #FFF7ED 35%,
        #FDF4FF 70%,
        #ECFEFF 100%
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
    padding: 25px 35px;
    border-radius: 28px;
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
    0 20px 60px
    rgba(37,99,235,0.25);
    margin-bottom: 25px;
}

.brand-title {
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 2px;
}

.brand-subtitle {
    margin-top: 8px;
    font-size: 13px;
    letter-spacing: 2px;
    color: #FDE68A;
}

/* ============================================================
HERO
============================================================ */

.hero {
    padding: 50px;
    border-radius: 34px;
    color: white;
    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #DB2777
    );
    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.25);
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 46px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.7;
}

/* ============================================================
SECTION
============================================================ */

.section {
    margin-top: 30px;
    margin-bottom: 22px;
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
    0 14px 40px
    rgba(37,99,235,0.20);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}

.section p {
    margin-bottom: 0;
}

/* ============================================================
SEARCH CARD
============================================================ */

.search-card {
    padding: 32px;
    border-radius: 30px;
    background: white;
    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);
    margin-bottom: 30px;
}

/* ============================================================
PROPERTY CARD
============================================================ */

.property-card {
    padding: 25px;
    border-radius: 26px;
    background: white;
    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.08);
    margin-bottom: 20px;
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
    margin-bottom: 20px;
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
TRUST CARD
============================================================ */

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
    box-shadow:
    0 15px 40px
    rgba(5,150,105,0.20);
}

/* ============================================================
AI CARD
============================================================ */

.ai-card {
    padding: 35px;
    border-radius: 30px;
    color: white;
    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #C026D3,
        #DB2777
    );
    box-shadow:
    0 20px 60px
    rgba(124,58,237,0.25);
}

/* ============================================================
CTA
============================================================ */

.cta {
    padding: 40px;
    border-radius: 30px;
    color: white;
    text-align: center;
    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );
    box-shadow:
    0 20px 60px
    rgba(124,58,237,0.25);
}

/* ============================================================
FOOTER
============================================================ */

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
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</div>

<div class="brand-subtitle">
INDIA'S SMART REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🔎 Discover Your Perfect Property
</h1>

<p>
Search smarter. Explore better. Find homes, apartments,
villas, plots, commercial spaces and investment opportunities
across India.
</p>

<p>
🏠 Buy &nbsp; • &nbsp;
🔑 Rent &nbsp; • &nbsp;
🏢 Commercial &nbsp; • &nbsp;
🌳 Land & Plot &nbsp; • &nbsp;
📈 Investment
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART PROPERTY SEARCH
# ============================================================

st.markdown("""
<div class="section">

<h2>
🇮🇳 Smart India Property Search
</h2>

<p>
Use multiple filters to discover properties matching
your budget, location, lifestyle and investment goals.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="search-card">',
    unsafe_allow_html=True
)


# ============================================================
# TRANSACTION TYPE
# ============================================================

transaction_type = st.radio(
    "🎯 I am looking to",
    [
        "🏡 Buy",
        "🔑 Rent",
        "🏢 Commercial",
        "🌱 Land / Plot",
        "📈 Investment",
        "🤝 Joint Venture"
    ],
    horizontal=True
)


# ============================================================
# LOCATION
# ============================================================

l1, l2, l3 = st.columns(3)

with l1:
    state = st.selectbox(
        "🇮🇳 State",
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
        "🌆 City",
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
        "📍 Locality / Area / PIN Code",
        placeholder="Enter locality, area or PIN Code"
    )


# ============================================================
# PROPERTY TYPE
# ============================================================

p1, p2, p3 = st.columns(3)

with p1:
    property_type = st.selectbox(
        "🏠 Property Type",
        [
            "Any Property",
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Plot",
            "Residential Land",
            "Farm Land",
            "Office",
            "Shop",
            "Warehouse",
            "Industrial Property"
        ]
    )

with p2:
    bhk = st.selectbox(
        "🛏️ Configuration / BHK",
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
    property_age = st.selectbox(
        "🏗️ Property Age",
        [
            "Any",
            "New Construction",
            "0–1 Year",
            "1–5 Years",
            "5–10 Years",
            "10+ Years"
        ]
    )


# ============================================================
# BUDGET
# ============================================================

b1, b2, b3 = st.columns(3)

with b1:
    min_price = st.number_input(
        "💰 Minimum Budget (₹)",
        min_value=0,
        step=100000
    )

with b2:
    max_price = st.number_input(
        "💰 Maximum Budget (₹)",
        min_value=0,
        step=100000
    )

with b3:
    budget_range = st.selectbox(
        "💰 Quick Budget Range",
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


# ============================================================
# AREA
# ============================================================

a1, a2, a3 = st.columns(3)

with a1:
    min_area = st.number_input(
        "📐 Minimum Area (Sq.Ft.)",
        min_value=0,
        step=100
    )

with a2:
    max_area = st.number_input(
        "📐 Maximum Area (Sq.Ft.)",
        min_value=0,
        step=100
    )

with a3:
    area_range = st.selectbox(
        "📐 Quick Area Range",
        [
            "Any Area",
            "Under 500 Sq.Ft.",
            "500 - 1000 Sq.Ft.",
            "1000 - 2000 Sq.Ft.",
            "2000 - 5000 Sq.Ft.",
            "Above 5000 Sq.Ft."
        ]
    )


# ============================================================
# VERIFICATION FILTERS
# ============================================================

v1, v2, v3 = st.columns(3)

with v1:
    verified_only = st.checkbox(
        "🛡️ Verified Properties Only"
    )

with v2:
    identity_verified = st.checkbox(
        "🪪 Identity Verified Owner"
    )

with v3:
    mobile_verified = st.checkbox(
        "📱 Mobile Verified"
    )


# ============================================================
# ADVANCED FILTERS
# ============================================================

with st.expander(
    "⚙️ Advanced Search Filters"
):

    af1, af2, af3 = st.columns(3)

    with af1:
        amenities = st.multiselect(
            "✨ Amenities",
            [
                "Parking",
                "Swimming Pool",
                "Gym",
                "Garden",
                "Security",
                "Lift",
                "Power Backup",
                "Water Supply",
                "Internet"
            ]
        )

    with af2:
        listing_by = st.selectbox(
            "👤 Listed By",
            [
                "Everyone",
                "Owner",
                "Agent / Broker",
                "Builder / Developer"
            ]
        )

    with af3:
        verified_property = st.checkbox(
            "📄 Property Documents Verified"
        )


# ============================================================
# SEARCH BUTTON
# ============================================================

search_button = st.button(
    "🔎 SEARCH PROPERTIES",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


if search_button:

    st.session_state.search_done = True

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
<div class="section">

<h2>
🌆 Explore Popular Indian Cities
</h2>

<p>
Discover high-demand real estate markets across India.
</p>

</div>
""", unsafe_allow_html=True)


cities = [
    ("🏙️", "Mumbai", "Luxury & Premium Homes"),
    ("🌆", "Pune", "IT & Residential Growth"),
    ("🏡", "Nagpur", "Plots & Investment"),
    ("🏢", "Bengaluru", "Technology & Rentals"),
    ("🌇", "Hyderabad", "IT & New Projects"),
    ("🏙️", "Delhi NCR", "Luxury & Commercial")
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


# ============================================================
# PROPERTY RESULTS
# ============================================================

if st.session_state.get(
    "search_done",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    🏆 Recommended Properties
    </h2>

    <p>
    Properties selected according to your search preferences.
    </p>

    </div>
    """, unsafe_allow_html=True)


    properties = [

        {
            "name":
            "Premium 3 BHK Luxury Apartment",

            "location":
            "Civil Lines, Nagpur, Maharashtra",

            "price":
            "₹1.25 Cr",

            "type":
            "Apartment",

            "details":
            "3 BHK • 1,850 Sq.Ft. • New Construction",

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
            "Modern 4 BHK Premium Villa",

            "location":
            "Baner, Pune, Maharashtra",

            "price":
            "₹2.80 Cr",

            "type":
            "Villa",

            "details":
            "4 BHK • 2,800 Sq.Ft. • New Construction",

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
            "Wardha Road, Nagpur, Maharashtra",

            "price":
            "₹48 Lakh",

            "type":
            "Residential Plot",

            "details":
            "2,000 Sq.Ft. • Investment Opportunity",

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

        col1, col2 = st.columns([1, 2])

        with col1:

            st.image(
                property_item["image"],
                caption=property_item["name"],
                use_container_width=True
            )

        with col2:

            badges = """
            <span class="badge verified">
            🛡️ Verified
            </span>
            """

            if property_item["premium"]:

                badges += """
                <span class="badge premium">
                ⭐ Premium
                </span>
                """

            if property_item["featured"]:

                badges += """
                <span class="badge featured">
                🔥 Featured
                </span>
                """


            st.markdown(
                f"""
                <div class="property-card">

                {badges}

                <h2>
                {property_item["name"]}
                </h2>

                <p>
                📍 {property_item["location"]}
                </p>

                <h2 style="color:#7C3AED;">
                {property_item["price"]}
                </h2>

                <p>
                🏠 {property_item["type"]}
                </p>

                <p>
                📐 {property_item["details"]}
                </p>

                <p>
                🛡️ Verified Listing
                &nbsp; • &nbsp;
                ⭐ FirstChoice Trust Signal
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


            b1, b2, b3, b4 = st.columns(4)

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

        st.divider()


# ============================================================
# VERIFIED PROPERTY TRUST
# ============================================================

st.markdown("""
<div class="section">

<h2>
🛡️ FirstChoice Verified Properties
</h2>

<p>
Our verification ecosystem will help buyers discover
trusted property listings.
</p>

</div>
""", unsafe_allow_html=True)


trust1, trust2, trust3 = st.columns(3)

with trust1:

    st.markdown("""
    <div class="trust-card">

    <h2>
    🪪 Identity Verification
    </h2>

    <p>
    Owner identity verification can be
    connected with secure KYC infrastructure.
    </p>

    </div>
    """, unsafe_allow_html=True)


with trust2:

    st.markdown("""
    <div class="trust-card">

    <h2>
    📱 Mobile Verification
    </h2>

    <p>
    Property owners and agents can verify
    their mobile number.
    </p>

    </div>
    """, unsafe_allow_html=True)


with trust3:

    st.markdown("""
    <div class="trust-card">

    <h2>
    📄 Property Verification
    </h2>

    <p>
    Property documents and ownership verification
    can be integrated with the production backend.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SMART PROPERTY DISCOVERY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤖 Smart Property Discovery
</h2>

<p>
Your future personalised real estate discovery assistant.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🎯 Find Properties That Match Your Lifestyle
</h2>

<p>
FirstChoice Property Hub can use your preferred city,
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
    "🚀 EXPLORE SMART RECOMMENDATIONS",
    use_container_width=True
):

    st.info(
        "Smart recommendation engine will be connected in the production backend."
    )


# ============================================================
# POST PROPERTY REQUIREMENT
# ============================================================

st.markdown("""
<div class="cta">

<h2>
🏡 Can't Find What You're Looking For?
</h2>

<p>
Post your requirement and let property owners,
agents and builders contact you.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "📢 POST YOUR PROPERTY REQUIREMENT",
    use_container_width=True
):

    st.success(
        "Requirement posting module will be connected to the backend."
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
