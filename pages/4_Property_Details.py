import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 4 - PROPERTY DETAILS
# PREMIUM MULTICOLOR REAL ESTATE EXPERIENCE
# ============================================================

st.set_page_config(
    page_title="Property Details | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PROPERTY DATA
# ============================================================

property_data = {
    "title": "Luxury 3 BHK Premium Residence",
    "location": "Civil Lines, Nagpur, Maharashtra",
    "price": 12500000,
    "area": "2,150 Sq.Ft.",
    "bedrooms": "3 BHK",
    "bathrooms": "3",
    "parking": "2 Cars",
    "property_type": "Premium Apartment",
    "status": "Ready to Move",
    "owner": "FirstChoice Verified Partner",
    "phone": "+91 98765 43210",
    "image1": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1600&q=90",
    "image2": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1200&q=85",
    "image3": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=1200&q=85",
    "image4": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=85",
    "image5": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=85"
}

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #f8faff 0%,
        #fff8f5 35%,
        #f8f2ff 70%,
        #f0fbff 100%
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

    padding: 18px 30px;

    border-radius: 20px;

    color: white;

    box-shadow:
    0 15px 40px rgba(37,99,235,0.20);
}

.brand-title {
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 2px;
}

.brand-subtitle {
    font-size: 11px;
    letter-spacing: 4px;
    color: #FDE68A;
}

/* BREADCRUMB */

.breadcrumb {
    margin-top: 25px;

    color: #667085;

    font-size: 14px;
}

/* MAIN GALLERY */

.gallery-main {
    border-radius: 30px;

    overflow: hidden;

    height: 510px;

    box-shadow:
    0 20px 50px rgba(0,0,0,0.15);
}

.gallery-main img {
    width: 100%;

    height: 510px;

    object-fit: cover;
}

/* BADGES */

.badge-row {
    margin-top: -65px;

    position: relative;

    padding: 0 25px;
}

.badge {
    display: inline-block;

    padding: 9px 16px;

    border-radius: 25px;

    color: white;

    font-size: 12px;

    font-weight: 900;

    margin-right: 8px;
}

.badge-premium {
    background:
    linear-gradient(
        135deg,
        #F59E0B,
        #EF4444
    );
}

.badge-verified {
    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

/* PROPERTY INFO */

.info-panel {
    background: white;

    padding: 35px;

    border-radius: 28px;

    box-shadow:
    0 15px 45px rgba(0,0,0,0.08);
}

.property-title {
    color: #071952;

    font-size: 36px;

    font-weight: 900;

    line-height: 1.2;
}

.location {
    color: #667085;

    font-size: 16px;
}

.price {
    color: #7C3AED;

    font-size: 38px;

    font-weight: 900;
}

/* FEATURE CARDS */

.feature {
    padding: 22px;

    border-radius: 20px;

    text-align: center;

    color: white;

    min-height: 120px;
}

.feature-icon {
    font-size: 35px;
}

.feature-title {
    font-weight: 900;

    margin-top: 8px;
}

.f-blue {
    background:
    linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
}

.f-purple {
    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.f-orange {
    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

.f-green {
    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.f-gold {
    background:
    linear-gradient(
        135deg,
        #B7791F,
        #F2C94C
    );
}

.f-sky {
    background:
    linear-gradient(
        135deg,
        #0284C7,
        #38BDF8
    );
}

/* ACTION PANEL */

.action-panel {
    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    padding: 30px;

    border-radius: 28px;

    color: white;

    box-shadow:
    0 20px 50px rgba(124,58,237,0.25);
}

/* SECTION */

.section-title {
    color: #071952;

    font-size: 30px;

    font-weight: 900;

    margin-top: 45px;
}

.section-subtitle {
    color: #667085;

    margin-bottom: 25px;
}

/* AMENITIES */

.amenity {
    background: white;

    padding: 18px;

    border-radius: 18px;

    box-shadow:
    0 8px 25px rgba(0,0,0,0.06);

    text-align: center;

    font-weight: 800;

    color: #344054;
}

/* OWNER */

.owner-card {
    background:
    linear-gradient(
        135deg,
        #ECFDF5,
        #D1FAE5,
        #DBEAFE
    );

    padding: 30px;

    border-radius: 28px;
}

.owner-avatar {
    width: 90px;

    height: 90px;

    border-radius: 50%;

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 45px;

    color: white;
}

/* EMI */

.emi-box {
    background:
    linear-gradient(
        135deg,
        #FFF7ED,
        #FCE7F3,
        #EDE9FE
    );

    padding: 35px;

    border-radius: 28px;
}

/* VIDEO */

.video-box {
    background:
    linear-gradient(
        135deg,
        #071952,
        #1E3A8A
    );

    padding: 30px;

    border-radius: 28px;

    color: white;
}

/* MAP */

.map-box {
    height: 330px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #DBEAFE,
        #E0E7FF,
        #FCE7F3
    );

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    font-size: 25px;

    color: #071952;

    font-weight: 900;
}

/* SIMILAR CARD */

.similar {
    background: white;

    border-radius: 22px;

    overflow: hidden;

    box-shadow:
    0 12px 35px rgba(0,0,0,0.08);
}

.similar img {
    width: 100%;

    height: 190px;

    object-fit: cover;
}

.similar-content {
    padding: 20px;
}

/* FOOTER */

.footer {
    margin-top: 60px;

    padding: 45px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );

    color: white;

    text-align: center;
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
# BREADCRUMB
# ============================================================

st.markdown("""
<div class="breadcrumb">
Home  ›  Properties  ›  Maharashtra  ›  Nagpur  ›  Civil Lines
</div>
""", unsafe_allow_html=True)


# ============================================================
# GALLERY
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

g1, g2 = st.columns([1.8, 1])

with g1:

    st.image(
        property_data["image1"],
        use_container_width=True
    )

with g2:

    st.image(
        property_data["image2"],
        use_container_width=True
    )

    st.image(
        property_data["image3"],
        use_container_width=True
    )


# ============================================================
# BADGES
# ============================================================

st.markdown("""
<div class="badge-row">

<span class="badge badge-premium">
⭐ PREMIUM PROPERTY
</span>

<span class="badge badge-verified">
🛡️ VERIFIED LISTING
</span>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN PROPERTY INFORMATION
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

left, right = st.columns([1.5, 1])

with left:

    st.markdown(
        f"""
        <div class="info-panel">

        <div class="property-title">
        {property_data["title"]}
        </div>

        <div class="location">
        📍 {property_data["location"]}
        </div>

        <br>

        <div class="price">
        ₹ {property_data["price"]:,}
        </div>

        <p>
        💎 Premium residential property with modern architecture,
        excellent connectivity and lifestyle amenities.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.markdown("""
    <div class="action-panel">

    <h2>
    Interested in this property?
    </h2>

    <p>
    Connect directly with our verified property partner.
    </p>

    </div>
    """, unsafe_allow_html=True)

    a1, a2 = st.columns(2)

    with a1:

        st.button(
            "❤️ Save",
            use_container_width=True
        )

    with a2:

        st.button(
            "📤 Share",
            use_container_width=True
        )

    a3, a4 = st.columns(2)

    with a3:

        st.button(
            "📞 Call Now",
            use_container_width=True
        )

    with a4:

        st.button(
            "💬 WhatsApp",
            use_container_width=True
        )


# ============================================================
# PROPERTY HIGHLIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">🏡 Property Highlights</div>',
    unsafe_allow_html=True
)

h1,h2,h3,h4,h5,h6 = st.columns(6)

highlights = [
    ("🛏️","3 BHK","f-blue"),
    ("🚿","3 Baths","f-purple"),
    ("📐","2,150 Sq.Ft.","f-orange"),
    ("🚗","2 Parking","f-green"),
    ("🏢","Apartment","f-gold"),
    ("🔑","Ready","f-sky")
]

for col, item in zip(
    [h1,h2,h3,h4,h5,h6],
    highlights
):

    with col:

        st.markdown(
            f"""
            <div class="feature {item[2]}">

            <div class="feature-icon">
            {item[0]}
            </div>

            <div class="feature-title">
            {item[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DESCRIPTION
# ============================================================

st.markdown(
    '<div class="section-title">✨ About This Property</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-panel">

<h3>
A Premium Lifestyle Address
</h3>

<p>
Experience sophisticated urban living in one of Nagpur's
most desirable residential locations. This thoughtfully
designed residence combines contemporary architecture,
spacious interiors and modern amenities.
</p>

<p>
The property offers excellent connectivity to major roads,
schools, hospitals, shopping destinations and business hubs.
</p>

<p>
Whether you're searching for your dream home or a long-term
real estate investment, this property offers an exceptional
combination of lifestyle and value.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AMENITIES
# ============================================================

st.markdown(
    '<div class="section-title">✨ Premium Amenities</div>',
    unsafe_allow_html=True
)

amenities = [
    "🏊 Swimming Pool",
    "🏋️ Fitness Centre",
    "🌳 Landscaped Garden",
    "🛡️ 24x7 Security",
    "📹 CCTV Surveillance",
    "🛗 High-Speed Lift",
    "⚡ Power Backup",
    "🚗 Covered Parking",
    "🏡 Club House",
    "🧒 Kids Play Area",
    "💧 Water Supply",
    "🌐 High-Speed Internet"
]

amenity_cols = st.columns(4)

for i, amenity in enumerate(amenities):

    with amenity_cols[i % 4]:

        st.markdown(
            f"""
            <div class="amenity">
            {amenity}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# VIDEO TOUR
# ============================================================

st.markdown(
    '<div class="section-title">🎬 Virtual Property Tour</div>',
    unsafe_allow_html=True
)

v1, v2 = st.columns([1.5, 1])

with v1:

    st.video(
        "https://www.youtube.com/watch?v=ScMzIvxBSi4"
    )

with v2:

    st.markdown("""
    <div class="video-box">

    <h2>
    Walk Through Your Future Home
    </h2>

    <p>
    Explore the property virtually before planning
    your physical site visit.
    </p>

    <p>
    🎥 Property Walkthrough
    </p>

    <p>
    🏡 Interior Tour
    </p>

    <p>
    📍 Location Experience
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# OWNER / AGENT
# ============================================================

st.markdown(
    '<div class="section-title">👤 Property Partner</div>',
    unsafe_allow_html=True
)

o1, o2 = st.columns([1, 2])

with o1:

    st.markdown("""
    <div class="owner-card">

    <div class="owner-avatar">
    👤
    </div>

    <h2>
    FirstChoice Verified Partner
    </h2>

    <p>
    🛡️ Identity Verified
    </p>

    <p>
    🏠 Property Verified
    </p>

    <p>
    ⭐ Trusted Partner
    </p>

    </div>
    """, unsafe_allow_html=True)

with o2:

    st.markdown("""
    <div class="info-panel">

    <h2>
    Connect With Property Partner
    </h2>

    <p>
    Get complete property information, arrange a site visit
    or discuss pricing directly with the verified partner.
    </p>

    </div>
    """, unsafe_allow_html=True)

    o3, o4, o5 = st.columns(3)

    with o3:

        st.button(
            "📞 Call",
            use_container_width=True
        )

    with o4:

        st.button(
            "💬 WhatsApp",
            use_container_width=True
        )

    with o5:

        st.button(
            "📅 Visit",
            use_container_width=True
        )


# ============================================================
# SITE VISIT
# ============================================================

st.markdown(
    '<div class="section-title">📅 Schedule a Site Visit</div>',
    unsafe_allow_html=True
)

sv1, sv2 = st.columns(2)

with sv1:

    visit_date = st.date_input(
        "Preferred Date"
    )

with sv2:

    visit_time = st.selectbox(
        "Preferred Time",
        [
            "10:00 AM",
            "12:00 PM",
            "2:00 PM",
            "4:00 PM",
            "6:00 PM"
        ]
    )

visitor_name = st.text_input(
    "Your Name"
)

visitor_mobile = st.text_input(
    "Mobile Number"
)

if st.button(
    "📅 Request Site Visit",
    use_container_width=True
):

    st.success(
        "Your site visit request has been submitted successfully."
    )


# ============================================================
# EMI CALCULATOR
# ============================================================

st.markdown(
    '<div class="section-title">🧮 Home Loan EMI Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="emi-box">',
    unsafe_allow_html=True
)

e1,e2,e3 = st.columns(3)

with e1:

    loan_amount = st.number_input(
        "Loan Amount ₹",
        min_value=100000,
        value=8000000,
        step=100000
    )

with e2:

    interest_rate = st.number_input(
        "Interest Rate %",
        min_value=1.0,
        max_value=30.0,
        value=8.5,
        step=0.1
    )

with e3:

    loan_years = st.number_input(
        "Loan Tenure (Years)",
        min_value=1,
        max_value=40,
        value=20
    )

monthly_rate = interest_rate / 12 / 100

months = loan_years * 12

if monthly_rate > 0:

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
        /
        (
            (1 + monthly_rate) ** months
            - 1
        )
    )

else:

    emi = loan_amount / months

st.markdown(
    f"""
    <div style="
    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );

    color:white;

    padding:30px;

    border-radius:20px;

    text-align:center;
    ">

    <h2>
    Estimated Monthly EMI
    </h2>

    <div style="
    font-size:40px;
    font-weight:900;
    ">

    ₹ {emi:,.0f}

    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOCATION / MAP
# ============================================================

st.markdown(
    '<div class="section-title">📍 Explore the Location</div>',
    unsafe_allow_html=True
)

m1, m2 = st.columns([1.5, 1])

with m1:

    st.markdown("""
    <div class="map-box">

    📍

    <br>

    Interactive Map Integration Coming Soon

    <br>

    Civil Lines, Nagpur

    </div>
    """, unsafe_allow_html=True)

with m2:

    st.markdown("""
    <div class="info-panel">

    <h2>
    Nearby Essentials
    </h2>

    <p>
    🏫 Schools & Colleges
    </p>

    <p>
    🏥 Hospitals
    </p>

    <p>
    🛒 Shopping & Markets
    </p>

    <p>
    🚉 Railway Station
    </p>

    <p>
    ✈️ Airport
    </p>

    <p>
    🛣️ Major Highways
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SIMILAR PROPERTIES
# ============================================================

st.markdown(
    '<div class="section-title">🏡 You May Also Like</div>',
    unsafe_allow_html=True
)

similar_properties = [
    (
        "Modern Villa",
        "₹2.80 Cr",
        "Pune",
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1000&q=85"
    ),
    (
        "Luxury Penthouse",
        "₹4.25 Cr",
        "Bengaluru",
        "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1000&q=85"
    ),
    (
        "Premium Plot",
        "₹48 Lakh",
        "Nagpur",
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1000&q=85"
    )
]

scols = st.columns(3)

for col, item in zip(
    scols,
    similar_properties
):

    with col:

        st.markdown(
            f"""
            <div class="similar">

            <img
            src="{item[3]}"
            >

            <div class="similar-content">

            <h3>
            {item[0]}
            </h3>

            <p>
            📍 {item[2]}
            </p>

            <h2 style="color:#7C3AED;">
            {item[1]}
            </h2>

            </div>

            </div>
            """,
            unsafe_allow_html=True
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
