import streamlit as st

# ============================================================
# PAGE 4 — PROPERTY SEARCH & DISCOVERY
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Search | FirstChoice Property Hub",
    page_icon="🔎",
    layout="wide"
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

/* HERO */

.hero {
    padding: 45px;
    border-radius: 32px;
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
    0 20px 65px
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
}

/* SECTION */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 25px 30px;

    border-radius: 24px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4F46E5,
        #9333EA,
        #EC4899
    );

    box-shadow:
    0 12px 35px
    rgba(79,70,229,0.18);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
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

/* PROPERTY CARD */

.property-card {
    padding: 25px;
    border-radius: 25px;
    background: white;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

/* TRUST */

.trust {
    padding: 20px;
    border-radius: 20px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );
}

/* CTA */

.cta {
    padding: 35px;
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

</style>
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
Search smarter. Explore better. Find the property
that fits your lifestyle and investment goals.
</p>

<p>
🏠 Buy • 🔑 Rent • 🏢 Commercial • 🌳 Land • 📈 Investment
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART SEARCH
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Smart Property Search
</h2>

<p>
Use multiple filters to discover properties matching your requirements.
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
        "🎯 Looking For",
        [
            "Buy",
            "Rent",
            "Lease",
            "Investment",
            "Joint Venture"
        ]
    )


with c2:

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


with c3:

    location = st.text_input(
        "📍 Location",
        placeholder="City, Area or PIN Code"
    )


c4, c5, c6 = st.columns(3)


with c4:

    min_price = st.number_input(
        "💰 Minimum Budget (₹)",
        min_value=0,
        step=100000
    )


with c5:

    max_price = st.number_input(
        "💰 Maximum Budget (₹)",
        min_value=0,
        step=100000
    )


with c6:

    bhk = st.selectbox(
        "🛏️ Configuration",
        [
            "Any",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5+ BHK"
        ]
    )


c7, c8, c9 = st.columns(3)


with c7:

    min_area = st.number_input(
        "📐 Min Area (Sq.Ft.)",
        min_value=0,
        step=100
    )


with c8:

    max_area = st.number_input(
        "📐 Max Area (Sq.Ft.)",
        min_value=0,
        step=100
    )


with c9:

    verified_only = st.checkbox(
        "🛡️ Show Verified Properties Only"
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ADVANCED FILTERS
# ============================================================

with st.expander(
    "⚙️ Advanced Search Filters"
):

    a1, a2, a3 = st.columns(3)


    with a1:

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


    with a2:

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


    with a3:

        listing_by = st.selectbox(
            "👤 Listed By",
            [
                "Everyone",
                "Owner",
                "Agent / Broker",
                "Builder / Developer"
            ]
        )


    verified_identity = st.checkbox(
        "🛡️ Identity Verified"
    )


    verified_property = st.checkbox(
        "📄 Property Documents Verified"
    )


# ============================================================
# SEARCH BUTTON
# ============================================================

if st.button(
    "🔎 SEARCH PROPERTIES",
    use_container_width=True
):

    st.session_state.search_done = True


# ============================================================
# DEMO SEARCH RESULTS
# ============================================================

if st.session_state.get(
    "search_done",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    🏡 Recommended Properties
    </h2>

    <p>
    Properties matching your search preferences.
    </p>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # PROPERTY 1
    # --------------------------------------------------------

    col1, col2 = st.columns([1, 2])


    with col1:

        st.image(
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
            caption="Premium Property",
            use_container_width=True
        )


    with col2:

        st.markdown("""
        <div class="property-card">

        <h2>
        🏡 Premium 3 BHK Luxury Apartment
        </h2>

        <p>
        📍 Civil Lines, Nagpur, Maharashtra
        </p>

        <h2>
        ₹1.25 Crore
        </h2>

        <p>
        🛏️ 3 BHK &nbsp; | &nbsp;
        📐 1,850 Sq.Ft. &nbsp; | &nbsp;
        🏗️ New Construction
        </p>

        <p>
        🛡️ Verified Mobile
        &nbsp; • &nbsp;
        ⭐ Trust Score 85/100
        </p>

        </div>
        """, unsafe_allow_html=True)


        b1, b2, b3 = st.columns(3)


        with b1:

            if st.button(
                "👁️ View Details",
                key="view1",
                use_container_width=True
            ):

                st.info(
                    "Open Property Details page."
                )


        with b2:

            if st.button(
                "❤️ Save",
                key="save1",
                use_container_width=True
            ):

                st.success(
                    "Property saved."
                )


        with b3:

            if st.button(
                "⚖️ Compare",
                key="compare1",
                use_container_width=True
            ):

                st.success(
                    "Added to comparison."
                )


    # --------------------------------------------------------
    # PROPERTY 2
    # --------------------------------------------------------

    st.divider()


    col3, col4 = st.columns([1, 2])


    with col3:

        st.image(
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d",
            caption="Modern Villa",
            use_container_width=True
        )


    with col4:

        st.markdown("""
        <div class="property-card">

        <h2>
        🏠 Modern 4 BHK Premium Villa
        </h2>

        <p>
        📍 Wardha Road, Nagpur, Maharashtra
        </p>

        <h2>
        ₹2.10 Crore
        </h2>

        <p>
        🛏️ 4 BHK &nbsp; | &nbsp;
        📐 2,800 Sq.Ft. &nbsp; | &nbsp;
        🏗️ New Construction
        </p>

        <p>
        🛡️ Owner Identity Verified
        &nbsp; • &nbsp;
        ⭐ Trust Score 92/100
        </p>

        </div>
        """, unsafe_allow_html=True)


        b4, b5, b6 = st.columns(3)


        with b4:

            if st.button(
                "👁️ View Details",
                key="view2",
                use_container_width=True
            ):

                st.info(
                    "Open Property Details page."
                )


        with b5:

            if st.button(
                "❤️ Save",
                key="save2",
                use_container_width=True
            ):

                st.success(
                    "Property saved."
                )


        with b6:

            if st.button(
                "⚖️ Compare",
                key="compare2",
                use_container_width=True
            ):

                st.success(
                    "Added to comparison."
                )


    # --------------------------------------------------------
    # PROPERTY 3
    # --------------------------------------------------------

    st.divider()


    col5, col6 = st.columns([1, 2])


    with col5:

        st.image(
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3",
            caption="Investment Property",
            use_container_width=True
        )


    with col6:

        st.markdown("""
        <div class="property-card">

        <h2>
        🌳 Premium Residential Plot
        </h2>

        <p>
        📍 Amravati Road, Nagpur, Maharashtra
        </p>

        <h2>
        ₹65 Lakh
        </h2>

        <p>
        📐 2,000 Sq.Ft. &nbsp; | &nbsp;
        🏗️ Residential Plot
        </p>

        <p>
        📄 Documents Under Verification
        &nbsp; • &nbsp;
        📈 Investment Opportunity
        </p>

        </div>
        """, unsafe_allow_html=True)


        b7, b8, b9 = st.columns(3)


        with b7:

            if st.button(
                "👁️ View Details",
                key="view3",
                use_container_width=True
            ):

                st.info(
                    "Open Property Details page."
                )


        with b8:

            if st.button(
                "❤️ Save",
                key="save3",
                use_container_width=True
            ):

                st.success(
                    "Property saved."
                )


        with b9:

            if st.button(
                "⚖️ Compare",
                key="compare3",
                use_container_width=True
            ):

                st.success(
                    "Added to comparison."
                )


# ============================================================
# SMART DISCOVERY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤖 Smart Property Discovery
</h2>

<p>
Our future AI engine will learn from your search behaviour
and recommend properties based on your preferences.
</p>

</div>
""", unsafe_allow_html=True)


d1, d2, d3 = st.columns(3)


with d1:

    st.markdown("""
    <div class="property-card">

    <h2>
    🎯 Smart Match
    </h2>

    <p>
    Find properties matching your budget,
    location and lifestyle.
    </p>

    </div>
    """, unsafe_allow_html=True)


with d2:

    st.markdown("""
    <div class="property-card">

    <h2>
    📈 Investment Insights
    </h2>

    <p>
    Future tools will help compare property
    prices and investment potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


with d3:

    st.markdown("""
    <div class="property-card">

    <h2>
    🛡️ Trust Signals
    </h2>

    <p>
    Easily identify verified owners,
    agents and property listings.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CTA
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
