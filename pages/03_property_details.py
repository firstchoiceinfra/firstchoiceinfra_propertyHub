import streamlit as st

# ============================================================
# PAGE 3 — PROPERTY DETAILS
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Details | FirstChoice Property Hub",
    page_icon="🏠",
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

/* INFO CARD */

.info-card {

    padding: 28px;

    border-radius: 25px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* TRUST */

.trust {

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
🏠 Property Details
</h1>

<p>
Explore every important detail of a property before making
your next decision.
</p>

<p>
📸 Photos • 🎥 Video • 📍 Location • 💰 Price • 🛡️ Verification
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH PROPERTY ID
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔎 Find a Property
</h2>

<p>
Enter a Property ID to view complete property information.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns([3, 1])


with c1:

    property_id = st.text_input(
        "Property ID",
        placeholder="Example: FC-IND-000123"
    )


with c2:

    st.write("")
    st.write("")

    search = st.button(
        "🔎 VIEW PROPERTY",
        use_container_width=True
    )


# ============================================================
# DEMO PROPERTY DATA
# ============================================================

if search and property_id:

    # --------------------------------------------------------
    # PROPERTY HEADER
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    🌟 Premium 3 BHK Luxury Residence
    </h2>

    <p>
    📍 Civil Lines, Nagpur, Maharashtra
    </p>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # MEDIA
    # --------------------------------------------------------

    st.markdown("""
    <div class="info-card">

    <h2>
    📸 Property Gallery
    </h2>

    </div>
    """, unsafe_allow_html=True)


    media1, media2, media3 = st.columns(3)


    with media1:

        st.image(
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
            caption="Premium Exterior",
            use_container_width=True
        )


    with media2:

        st.image(
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c",
            caption="Luxury Interior",
            use_container_width=True
        )


    with media3:

        st.image(
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3",
            caption="Modern Living Space",
            use_container_width=True
        )


    # --------------------------------------------------------
    # VIDEO
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    🎥 Property Video Tour
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.video(
        "https://www.youtube.com/watch?v=ScMzIvxBSi4"
    )


    # --------------------------------------------------------
    # BASIC DETAILS
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    🏡 Property Overview
    </h2>

    </div>
    """, unsafe_allow_html=True)


    d1, d2, d3, d4 = st.columns(4)


    with d1:

        st.metric(
            "Property Type",
            "Apartment"
        )


    with d2:

        st.metric(
            "Configuration",
            "3 BHK"
        )


    with d3:

        st.metric(
            "Area",
            "1,850 Sq.Ft."
        )


    with d4:

        st.metric(
            "Property Age",
            "New"
        )


    # --------------------------------------------------------
    # PRICE
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    💰 Pricing
    </h2>

    </div>
    """, unsafe_allow_html=True)


    price1, price2, price3 = st.columns(3)


    with price1:

        st.metric(
            "Expected Price",
            "₹1.25 Cr"
        )


    with price2:

        st.metric(
            "Price / Sq.Ft.",
            "₹6,756"
        )


    with price3:

        st.metric(
            "Negotiation",
            "Available"
        )


    # --------------------------------------------------------
    # DESCRIPTION
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    📝 Property Description
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-card">

    <p>
    Experience premium urban living in this beautifully designed
    3 BHK residence located in one of Nagpur's most desirable
    neighbourhoods.
    </p>

    <p>
    The property offers spacious interiors, modern architecture,
    excellent natural lighting and convenient access to major
    city facilities.
    </p>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # AMENITIES
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    ✨ Amenities & Facilities
    </h2>

    </div>
    """, unsafe_allow_html=True)


    amenities = [
        "🚗 Covered Parking",
        "🏊 Swimming Pool",
        "🏋️ Fitness Centre",
        "🌳 Landscaped Garden",
        "🛗 High-Speed Lift",
        "🔒 24x7 Security",
        "⚡ Power Backup",
        "💧 Water Supply",
        "📶 High-Speed Internet"
    ]


    cols = st.columns(3)


    for index, amenity in enumerate(amenities):

        with cols[index % 3]:

            st.success(
                amenity
            )


    # --------------------------------------------------------
    # LOCATION
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    📍 Location & Connectivity
    </h2>

    </div>
    """, unsafe_allow_html=True)


    loc1, loc2 = st.columns(2)


    with loc1:

        st.markdown("""
        <div class="info-card">

        <h3>
        📍 Property Address
        </h3>

        <p>
        Civil Lines,<br>
        Nagpur,<br>
        Maharashtra,<br>
        India
        </p>

        </div>
        """, unsafe_allow_html=True)


    with loc2:

        st.markdown("""
        <div class="info-card">

        <h3>
        🚗 Nearby Locations
        </h3>

        <p>
        ✈️ Airport — 20 Minutes
        </p>

        <p>
        🏥 Hospital — 10 Minutes
        </p>

        <p>
        🏫 School — 5 Minutes
        </p>

        <p>
        🛒 Shopping — 8 Minutes
        </p>

        </div>
        """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # VERIFICATION
    # --------------------------------------------------------

    st.markdown("""
    <div class="trust">

    <h2>
    🛡️ FirstChoice Trust Status
    </h2>

    <p>
    ✅ Owner Identity — Verified
    </p>

    <p>
    ✅ Mobile Number — Verified
    </p>

    <p>
    ✅ Property Documents — Under Review
    </p>

    <p>
    ⭐ FirstChoice Trust Score — 85/100
    </p>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # CONTACT
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

    <h2>
    📞 Connect With Property Owner
    </h2>

    </div>
    """, unsafe_allow_html=True)


    contact1, contact2, contact3 = st.columns(3)


    with contact1:

        if st.button(
            "📞 Request Call",
            use_container_width=True
        ):

            st.success(
                "Call request submitted."
            )


    with contact2:

        if st.button(
            "💬 WhatsApp",
            use_container_width=True
        ):

            st.success(
                "WhatsApp enquiry initiated."
            )


    with contact3:

        if st.button(
            "💬 Send Enquiry",
            use_container_width=True
        ):

            st.success(
                "Your enquiry has been submitted."
            )


    # --------------------------------------------------------
    # SITE VISIT
    # --------------------------------------------------------

    st.markdown("""
    <div class="cta">

    <h2>
    🏡 Want to Visit This Property?
    </h2>

    <p>
    Schedule a property visit at your preferred date and time.
    </p>

    </div>
    """, unsafe_allow_html=True)


    visit_date = st.date_input(
        "Preferred Visit Date"
    )


    visit_time = st.time_input(
        "Preferred Visit Time"
    )


    if st.button(
        "📅 SCHEDULE SITE VISIT",
        use_container_width=True
    ):

        st.success(
            "🎉 Site visit request submitted successfully!"
        )


else:

    st.info(
        "Enter a Property ID above and click "
        "'VIEW PROPERTY' to explore property details."
    )
