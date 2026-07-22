import streamlit as st
from datetime import datetime

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 5 - POST PROPERTY
# PREMIUM PROPERTY LISTING EXPERIENCE
# ============================================================

st.set_page_config(
    page_title="Post Your Property | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #f7f9ff 0%,
        #fff7f3 35%,
        #f7f1ff 70%,
        #effcff 100%
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

    padding: 20px 30px;

    border-radius: 22px;

    color: white;

    box-shadow:
    0 18px 45px rgba(37,99,235,0.20);
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
    margin-top: 25px;

    min-height: 320px;

    border-radius: 32px;

    padding: 55px;

    color: white;

    background:
    linear-gradient(
        90deg,
        rgba(7,25,82,0.97),
        rgba(76,29,149,0.85),
        rgba(236,72,153,0.55)
    ),
    url("https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1800&q=90");

    background-size: cover;

    background-position: center;

    box-shadow:
    0 25px 60px rgba(7,25,82,0.22);
}

.hero h1 {
    font-size: 45px;

    font-weight: 900;
}

.hero p {
    font-size: 18px;

    max-width: 750px;

    line-height: 1.7;
}

/* PROGRESS */

.progress-card {
    background: white;

    padding: 22px;

    border-radius: 22px;

    margin-top: 25px;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.07);
}

.step {
    text-align: center;

    font-weight: 800;

    color: #667085;
}

.step-active {
    color: #7C3AED;
}

/* SECTION */

.section {
    background: white;

    padding: 32px;

    border-radius: 28px;

    margin-top: 25px;

    box-shadow:
    0 12px 35px rgba(0,0,0,0.06);
}

.section-title {
    color: #071952;

    font-size: 27px;

    font-weight: 900;
}

.section-subtitle {
    color: #667085;

    margin-bottom: 25px;
}

/* COLOR CATEGORY CARDS */

.category {
    padding: 25px;

    border-radius: 22px;

    text-align: center;

    color: white;

    min-height: 140px;

    box-shadow:
    0 12px 30px rgba(0,0,0,0.10);
}

.blue {
    background:
    linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
}

.purple {
    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.orange {
    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

.green {
    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

/* UPLOAD */

.upload-box {
    background:
    linear-gradient(
        135deg,
        #EEF2FF,
        #FCE7F3,
        #ECFEFF
    );

    padding: 30px;

    border-radius: 25px;

    border: 2px dashed #7C3AED;
}

/* VERIFY */

.verify-box {
    background:
    linear-gradient(
        135deg,
        #ECFDF5,
        #DBEAFE
    );

    padding: 30px;

    border-radius: 25px;
}

/* PREMIUM */

.premium-box {
    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    padding: 35px;

    border-radius: 28px;

    color: white;

    box-shadow:
    0 20px 50px rgba(124,58,237,0.25);
}

/* PUBLISH */

.publish-box {
    background:
    linear-gradient(
        135deg,
        #059669,
        #2563EB,
        #7C3AED
    );

    padding: 35px;

    border-radius: 28px;

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
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🏡 List Your Property With Confidence
</h1>

<p>
Reach genuine buyers, tenants and investors across India.
Create a professional property listing with photos, videos
and verified ownership information.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROGRESS
# ============================================================

st.markdown("""
<div class="progress-card">

<div style="font-size:18px;font-weight:900;color:#071952;">
Create Your Property Listing
</div>

<br>

</div>
""", unsafe_allow_html=True)

p1,p2,p3,p4 = st.columns(4)

steps = [
    "① Property Details",
    "② Location & Price",
    "③ Photos & Verification",
    "④ Publish"
]

for col, step in zip(
    [p1,p2,p3,p4],
    steps
):

    with col:

        st.markdown(
            f"""
            <div class="step step-active">
            {step}
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SECTION 1
# PROPERTY PURPOSE
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
🏠 What do you want to do?
</div>

<div class="section-subtitle">
Choose the purpose of your property listing.
</div>

</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

categories = [
    ("🏷️","Sell","blue"),
    ("🔑","Rent","purple"),
    ("🤝","Lease","orange"),
    ("📈","Invest","green")
]

for col, item in zip(
    [c1,c2,c3,c4],
    categories
):

    with col:

        st.markdown(
            f"""
            <div class="category {item[2]}">

            <div style="font-size:40px;">
            {item[0]}
            </div>

            <div style="font-size:20px;font-weight:900;">
            {item[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


listing_purpose = st.radio(
    "Select Listing Purpose",
    [
        "Sell Property",
        "Rent Property",
        "Lease Property"
    ],
    horizontal=True
)


# ============================================================
# SECTION 2
# PROPERTY TYPE
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
🏡 Property Information
</div>

<div class="section-subtitle">
Tell buyers what kind of property you are listing.
</div>

</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:

    property_type = st.selectbox(
        "Property Category",
        [
            "Residential",
            "Commercial",
            "Plot / Land",
            "Agricultural Land",
            "Industrial",
            "Farmhouse"
        ]
    )

with c2:

    property_subtype = st.selectbox(
        "Property Type",
        [
            "Apartment",
            "Independent House",
            "Villa",
            "Builder Floor",
            "Penthouse",
            "Studio",
            "Office",
            "Shop",
            "Warehouse",
            "Residential Plot"
        ]
    )

with c3:

    property_status = st.selectbox(
        "Property Status",
        [
            "Ready to Move",
            "Under Construction",
            "New Launch",
            "Resale"
        ]
    )


property_title = st.text_input(
    "Property Title",
    placeholder="Example: Premium 3 BHK Luxury Apartment in Civil Lines"
)

property_description = st.text_area(
    "Property Description",
    placeholder="Describe the property, location, features and nearby facilities...",
    height=160
)


# ============================================================
# SECTION 3
# LOCATION
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
📍 Property Location
</div>

<div class="section-subtitle">
Help buyers discover your property easily.
</div>

</div>
""", unsafe_allow_html=True)

l1,l2,l3 = st.columns(3)

with l1:

    state = st.selectbox(
        "State",
        [
            "Maharashtra",
            "Delhi",
            "Karnataka",
            "Telangana",
            "Gujarat",
            "Madhya Pradesh",
            "Rajasthan",
            "Uttar Pradesh"
        ]
    )

with l2:

    city = st.text_input(
        "City",
        placeholder="Example: Nagpur"
    )

with l3:

    locality = st.text_input(
        "Locality / Area",
        placeholder="Example: Civil Lines"
    )

address = st.text_area(
    "Complete Address",
    height=100
)


# ============================================================
# SECTION 4
# PRICE & AREA
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
💰 Price & Property Size
</div>

</div>
""", unsafe_allow_html=True)

p1,p2,p3,p4 = st.columns(4)

with p1:

    price = st.number_input(
        "Price ₹",
        min_value=0,
        step=100000
    )

with p2:

    area = st.number_input(
        "Area Sq.Ft.",
        min_value=0,
        step=100
    )

with p3:

    area_type = st.selectbox(
        "Area Type",
        [
            "Carpet Area",
            "Built-up Area",
            "Super Built-up Area",
            "Plot Area"
        ]
    )

with p4:

    negotiable = st.checkbox(
        "Price Negotiable"
    )


# ============================================================
# SECTION 5
# PROPERTY FEATURES
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
✨ Property Features
</div>

</div>
""", unsafe_allow_html=True)

f1,f2,f3,f4 = st.columns(4)

with f1:

    bedrooms = st.selectbox(
        "Bedrooms",
        [
            "Studio",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5+ BHK",
            "Not Applicable"
        ]
    )

with f2:

    bathrooms = st.selectbox(
        "Bathrooms",
        [
            "1",
            "2",
            "3",
            "4",
            "5+",
            "Not Applicable"
        ]
    )

with f3:

    parking = st.selectbox(
        "Parking",
        [
            "None",
            "1 Car",
            "2 Cars",
            "3+ Cars"
        ]
    )

with f4:

    floor = st.selectbox(
        "Floor",
        [
            "Ground Floor",
            "1st Floor",
            "2nd Floor",
            "3rd Floor",
            "4th Floor",
            "5th+ Floor",
            "Not Applicable"
        ]
    )


# ============================================================
# SECTION 6
# AMENITIES
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
🌟 Select Amenities
</div>

</div>
""", unsafe_allow_html=True)

amenities = st.multiselect(
    "Available Amenities",
    [
        "Swimming Pool",
        "Gym / Fitness Centre",
        "Club House",
        "Garden",
        "Kids Play Area",
        "24x7 Security",
        "CCTV",
        "Power Backup",
        "Lift",
        "Visitor Parking",
        "Internet",
        "Water Supply",
        "Fire Safety",
        "EV Charging"
    ]
)


# ============================================================
# SECTION 7
# PHOTOS & VIDEO
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
📸 Property Photos & Video
</div>

<div class="section-subtitle">
High-quality photos and videos help your property receive more attention.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="upload-box">',
    unsafe_allow_html=True
)

photos = st.file_uploader(
    "Upload Property Photos",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ],
    accept_multiple_files=True
)

video = st.file_uploader(
    "Upload Property Video",
    type=[
        "mp4",
        "mov",
        "avi"
    ]
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 8
# OWNER / PARTNER
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
👤 Listing Owner / Partner
</div>

</div>
""", unsafe_allow_html=True)

o1,o2,o3 = st.columns(3)

with o1:

    owner_type = st.selectbox(
        "I am",
        [
            "Property Owner",
            "Agent",
            "Builder / Developer",
            "Company"
        ]
    )

with o2:

    owner_name = st.text_input(
        "Full Name"
    )

with o3:

    mobile = st.text_input(
        "Mobile Number"
    )


email = st.text_input(
    "Email Address"
)


# ============================================================
# SECTION 9
# MOBILE OTP VERIFICATION
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
📱 Mobile Verification
</div>

<div class="section-subtitle">
Verify your current mobile number before publishing your listing.
</div>

</div>
""", unsafe_allow_html=True)

if st.button(
    "📲 Send OTP",
    use_container_width=True
):

    st.session_state.otp_sent = True

    st.info(
        "Demo OTP sent. Production version will connect to an SMS OTP provider."
    )

if st.session_state.get(
    "otp_sent",
    False
):

    otp = st.text_input(
        "Enter OTP",
        max_chars=6
    )

    if st.button(
        "✅ Verify Mobile",
        use_container_width=True
    ):

        st.session_state.mobile_verified = True

        st.success(
            "Mobile verification completed."
        )


# ============================================================
# SECTION 10
# IDENTITY VERIFICATION
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
🛡️ Identity & Ownership Verification
</div>

<div class="section-subtitle">
Build trust with verified property listings.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="verify-box">

<h3>
🛡️ Secure Verification
</h3>

<p>
For production, FirstChoice Property Hub will use a secure,
consent-based identity verification provider.
</p>

<p>
Your identity information will not be publicly displayed
on the property listing.
</p>

</div>
""", unsafe_allow_html=True)

v1,v2 = st.columns(2)

with v1:

    identity_consent = st.checkbox(
        "I consent to identity verification for this listing."
    )

with v2:

    ownership_document = st.file_uploader(
        "Upload Ownership Document",
        type=[
            "pdf",
            "jpg",
            "jpeg",
            "png"
        ]
    )


# ============================================================
# SECTION 11
# PREMIUM LISTING
# ============================================================

st.markdown("""
<div class="premium-box">

<h2>
⭐ Boost Your Property Listing
</h2>

<p>
Get higher visibility with premium placement,
featured badges and priority discovery.
</p>

</div>
""", unsafe_allow_html=True)

premium_listing = st.checkbox(
    "⭐ Make this a Featured Property"
)


# ============================================================
# PREVIEW
# ============================================================

st.markdown("""
<div class="section">

<div class="section-title">
👁️ Listing Preview
</div>

</div>
""", unsafe_allow_html=True)

preview_col1, preview_col2 = st.columns([1, 1])

with preview_col1:

    st.markdown(
        f"""
        ### 🏡 {property_title or "Your Property Title"}

        📍 {locality or "Locality"}, {city or "City"}, {state}

        💰 ₹ {price:,.0f}

        📐 {area:,.0f} Sq.Ft.

        🏠 {property_type}

        🛏️ {bedrooms}

        🚿 {bathrooms} Bathrooms

        🚗 {parking}

        ⭐ {"Featured Listing" if premium_listing else "Standard Listing"}
        """
    )

with preview_col2:

    if photos:

        st.image(
            photos[0],
            use_container_width=True
        )

    else:

        st.info(
            "Your first property photo will appear here."
        )


# ============================================================
# PUBLISH
# ============================================================

st.markdown("""
<div class="publish-box">

<h2>
🚀 Ready to Publish?
</h2>

<p>
Review your information carefully before publishing.
</p>

</div>
""", unsafe_allow_html=True)

agree = st.checkbox(
    "I confirm that the information provided is accurate and I have the right to list this property."
)

if st.button(
    "🚀 Publish Property",
    use_container_width=True
):

    if not property_title:

        st.error(
            "Please enter a property title."
        )

    elif not city:

        st.error(
            "Please enter the property city."
        )

    elif not mobile:

        st.error(
            "Please enter your mobile number."
        )

    elif not agree:

        st.error(
            "Please confirm the declaration before publishing."
        )

    else:

        st.success(
            "🎉 Property listing created successfully! "
            "Production version will save this listing to the central database."
        )

        st.balloons()


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div style="
margin-top:60px;
padding:45px;
border-radius:28px;
background:
linear-gradient(
135deg,
#071952,
#1E1B4B
);
color:white;
text-align:center;
">

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
