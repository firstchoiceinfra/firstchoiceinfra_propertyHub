import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 22 - POST PROPERTY
# PREMIUM PROPERTY LISTING MODULE
# ============================================================

st.set_page_config(
    page_title="Post Property | FirstChoice Property Hub",
    page_icon="🏠",
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

/* CARDS */

.card {

    padding: 32px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);

    margin-bottom: 20px;
}

/* VERIFICATION */

.verification {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 18px 45px
    rgba(5,150,105,0.22);
}

/* MEDIA */

.media-card {

    padding: 30px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F8FAFF,
        #FDF4FF
    );

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);
}

/* PREVIEW */

.preview {

    padding: 35px;

    border-radius: 30px;

    background:
    linear-gradient(
        135deg,
        #EEF2FF,
        #FDF4FF,
        #FFFFFF
    );

    border:
    1px solid #C7D2FE;

    box-shadow:
    0 18px 45px
    rgba(79,70,229,0.14);
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
PROPERTY HUB • LIST • VERIFY • CONNECT • SELL
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🏠 List Your Property
</div>

<div class="hero-subtitle">
Reach genuine buyers, tenants and investors across India
with a trusted and professionally verified property listing.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LISTING PROGRESS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Create Your Property Listing
</div>

<div class="section-subtitle">
Complete the information below to create a professional property listing.
</div>

</div>
""", unsafe_allow_html=True)


step1, step2, step3, step4, step5 = st.columns(5)


with step1:
    st.info("1️⃣ Basic Details")

with step2:
    st.info("2️⃣ Location")

with step3:
    st.info("3️⃣ Media")

with step4:
    st.info("4️⃣ Verification")

with step5:
    st.info("5️⃣ Publish")


# ============================================================
# OWNER / SELLER PROFILE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Listing Owner / Seller Profile
</div>

<div class="section-subtitle">
Tell buyers who is listing this property.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="card">

<h2>
🛡️ Trusted Property Listing
</h2>

<p>
Verified profiles receive higher trust and better buyer engagement.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    listing_by = st.selectbox(
        "I am listing as",
        [
            "Property Owner",
            "Agent / Broker",
            "Builder",
            "Developer",
            "Investor"
        ]
    )


with c2:

    seller_name = st.text_input(
        "Full Name / Business Name",
        placeholder=
        "Enter your full name or company name"
    )


c3, c4 = st.columns(2)


with c3:

    seller_mobile = st.text_input(
        "Current Mobile Number",
        placeholder=
        "Enter 10 digit mobile number"
    )


with c4:

    seller_email = st.text_input(
        "Email Address",
        placeholder=
        "Enter your email address"
    )


st.markdown("""
<div class="verification">

<h2>
📱 Identity Verification
</h2>

<p>
✅ Mobile OTP Verification — Ready
</p>

<p>
🛡️ Identity Verification — Pending
</p>

<p>
🔐 Your identity data will be handled through a secure verification workflow.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "📱 VERIFY MOBILE NUMBER",
    use_container_width=True
):

    st.success(
        "OTP verification workflow initiated."
    )


if st.button(
    "🛡️ START IDENTITY VERIFICATION",
    use_container_width=True
):

    st.info(
        "Secure KYC verification workflow will open."
    )


# ============================================================
# PROPERTY BASIC DETAILS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏡 Property Basic Details
</div>

<div class="section-subtitle">
Provide accurate information about your property.
</div>

</div>
""", unsafe_allow_html=True)


property_title = st.text_input(
    "Property Listing Title",
    placeholder=
    "Example: Premium 3 BHK Luxury Apartment Near Metro"
)


c1, c2, c3 = st.columns(3)


with c1:

    property_category = st.selectbox(
        "Property Category",
        [
            "Residential",
            "Commercial",
            "Land & Plot",
            "Agricultural Land",
            "Industrial",
            "Co-working",
            "Other"
        ]
    )


with c2:

    property_type = st.selectbox(
        "Property Type",
        [
            "Apartment",
            "Flat",
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


with c3:

    listing_purpose = st.selectbox(
        "Listing Purpose",
        [
            "For Sale",
            "For Rent",
            "For Lease",
            "For Investment"
        ]
    )


# ============================================================
# PROPERTY SPECIFICATIONS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📐 Property Specifications
</div>

<div class="section-subtitle">
Add detailed property specifications.
</div>

</div>
""", unsafe_allow_html=True)


s1, s2, s3, s4 = st.columns(4)


with s1:

    area = st.number_input(
        "Area (Sq.Ft.)",
        min_value=0,
        step=100
    )


with s2:

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        step=1
    )


with s3:

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0,
        step=1
    )


with s4:

    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        step=1
    )


c5, c6, c7 = st.columns(3)


with c5:

    property_age = st.selectbox(
        "Property Age",
        [
            "New Construction",
            "0–1 Years",
            "1–5 Years",
            "5–10 Years",
            "10+ Years"
        ]
    )


with c6:

    furnishing = st.selectbox(
        "Furnishing",
        [
            "Unfurnished",
            "Semi Furnished",
            "Fully Furnished"
        ]
    )


with c7:

    facing = st.selectbox(
        "Property Facing",
        [
            "East",
            "West",
            "North",
            "South",
            "North-East",
            "North-West",
            "South-East",
            "South-West",
            "Not Specified"
        ]
    )


# ============================================================
# PRICE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💰 Pricing & Financial Details
</div>

<div class="section-subtitle">
Set your property price and transaction preferences.
</div>

</div>
""", unsafe_allow_html=True)


p1, p2 = st.columns(2)


with p1:

    price = st.number_input(
        "Expected Price (₹)",
        min_value=0,
        step=100000
    )


with p2:

    rent = st.number_input(
        "Monthly Rent (If Applicable)",
        min_value=0,
        step=1000
    )


negotiable = st.checkbox(
    "💬 Price Negotiable"
)


maintenance = st.number_input(
    "Monthly Maintenance (₹)",
    min_value=0,
    step=500
)


# ============================================================
# LOCATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📍 Property Location
</div>

<div class="section-subtitle">
Help buyers discover your property easily.
</div>

</div>
""", unsafe_allow_html=True)


l1, l2 = st.columns(2)


with l1:

    state = st.selectbox(
        "State",
        [
            "Maharashtra",
            "Delhi",
            "Karnataka",
            "Telangana",
            "Gujarat",
            "Rajasthan",
            "Uttar Pradesh",
            "Madhya Pradesh",
            "Other"
        ]
    )


with l2:

    city = st.text_input(
        "City",
        placeholder=
        "Example: Nagpur"
    )


l3, l4 = st.columns(2)


with l3:

    locality = st.text_input(
        "Locality / Area",
        placeholder=
        "Example: Civil Lines"
    )


with l4:

    pincode = st.text_input(
        "PIN Code",
        placeholder=
        "Enter 6 digit PIN code"
    )


address = st.text_area(
    "Property Address",
    placeholder=
    "Enter complete property address"
)


# ============================================================
# RERA / LEGAL DETAILS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📜 Legal & Regulatory Information
</div>

<div class="section-subtitle">
Add regulatory information where applicable.
</div>

</div>
""", unsafe_allow_html=True)


rera_status = st.selectbox(
    "RERA Status",
    [
        "Not Applicable",
        "RERA Registered",
        "RERA Registration Pending",
        "I Don't Know"
    ]
)


rera_number = st.text_input(
    "RERA Registration Number",
    placeholder=
    "Enter RERA number if applicable"
)


ownership = st.selectbox(
    "Ownership Type",
    [
        "Freehold",
        "Leasehold",
        "Society Property",
        "Power of Attorney",
        "Other"
    ]
)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
✨ Property Amenities
</div>

<div class="section-subtitle">
Highlight the features that make your property special.
</div>

</div>
""", unsafe_allow_html=True)


amenities = st.multiselect(
    "Select Amenities",
    [
        "Swimming Pool",
        "Gym",
        "Club House",
        "Garden",
        "Children's Play Area",
        "Security",
        "CCTV",
        "Lift",
        "Power Backup",
        "Parking",
        "Visitor Parking",
        "EV Charging",
        "24x7 Water Supply",
        "Internet Connectivity",
        "Gated Community",
        "Pet Friendly",
        "Near School",
        "Near Hospital",
        "Near Metro",
        "Near Airport"
    ]
)


# ============================================================
# PROPERTY DESCRIPTION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📝 Property Description
</div>

<div class="section-subtitle">
Tell buyers what makes your property unique.
</div>

</div>
""", unsafe_allow_html=True)


description = st.text_area(
    "Detailed Property Description",
    height=180,
    placeholder=
    "Describe your property, location advantages, nearby facilities and other important information."
)


# ============================================================
# MEDIA UPLOAD
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📸 Property Photos & Video
</div>

<div class="section-subtitle">
High-quality media can significantly improve buyer engagement.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="media-card">

<h2>
🎥 Create a Premium Property Showcase
</h2>

<p>
Upload high-quality photos, property videos and future 360° tours.
</p>

</div>
""", unsafe_allow_html=True)


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


if photos:

    st.success(
        f"{len(photos)} property photos uploaded."
    )


if video:

    st.success(
        "Property video uploaded."
    )


# ============================================================
# LOCATION MAP FOUNDATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🗺️ Property Map Location
</div>

<div class="section-subtitle">
Map-based property discovery will be connected in the backend.
</div>

</div>
""", unsafe_allow_html=True)


map_lat = st.number_input(
    "Latitude",
    value=21.1458,
    format="%.6f"
)


map_lon = st.number_input(
    "Longitude",
    value=79.0882,
    format="%.6f"
)


st.map(
    {
        "lat": [map_lat],
        "lon": [map_lon]
    }
)


# ============================================================
# VERIFICATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ FirstChoice Property Verification
</div>

<div class="section-subtitle">
Verified properties will receive a trusted verification badge.
</div>

</div>
""", unsafe_allow_html=True)


verify_documents = st.checkbox(
    "I want FirstChoice Property Hub to verify my property documents."
)


verify_identity = st.checkbox(
    "I agree to complete secure identity verification."
)


st.info(
    """
    🛡️ Verification may include identity verification,
    ownership/document review and property information validation.
    """
)


# ============================================================
# PREVIEW
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👁️ Listing Preview
</div>

<div class="section-subtitle">
Review your property information before publishing.
</div>

</div>
""", unsafe_allow_html=True)


preview_title = property_title or "Your Property Title"

preview_location = (
    f"{locality}, {city}, {state}"
    if city
    else
    "Property Location"
)


st.markdown(
    f"""
    <div class="preview">

    <h1>
    🏠 {preview_title}
    </h1>

    <h3>
    📍 {preview_location}
    </h3>

    <h2>
    💰 ₹{price:,.0f}
    </h2>

    <p>
    🏡 Type: {property_type}
    </p>

    <p>
    📐 Area: {area:,.0f} Sq.Ft.
    </p>

    <p>
    🛏️ Bedrooms: {bedrooms}
    </p>

    <p>
    🚿 Bathrooms: {bathrooms}
    </p>

    <p>
    🛡️ Verification:
    {"Requested" if verify_documents else "Not Requested"}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SAVE DRAFT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💾 Save Your Listing
</div>

<div class="section-subtitle">
You can save your listing as a draft and publish it later.
</div>

</div>
""", unsafe_allow_html=True)


if st.button(
    "💾 SAVE AS DRAFT",
    use_container_width=True
):

    st.success(
        "Property listing saved as draft."
    )


# ============================================================
# PUBLISH
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Publish Property
</div>

<div class="section-subtitle">
Submit your property for publishing on FirstChoice Property Hub.
</div>

</div>
""", unsafe_allow_html=True)


publish = st.button(
    "🚀 PUBLISH PROPERTY LISTING",
    use_container_width=True
)


if publish:

    required_fields = []

    if not property_title:
        required_fields.append(
            "Property Title"
        )

    if not seller_name:
        required_fields.append(
            "Seller Name"
        )

    if not seller_mobile:
        required_fields.append(
            "Mobile Number"
        )

    if not city:
        required_fields.append(
            "City"
        )

    if price <= 0:
        required_fields.append(
            "Property Price"
        )


    if required_fields:

        st.error(
            "Please complete: "
            +
            ", ".join(required_fields)
        )

    else:

        st.success(
            """
            🎉 Property listing submitted successfully!

            Your property is now ready for verification
            and publishing workflow.
            """
        )


# ============================================================
# SMART LISTING FEATURES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Next-Generation Listing Features
</div>

<div class="section-subtitle">
Our future platform will go beyond traditional property portals.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.info(
        """
        🤖 **AI Listing Assistant**

        Automatically generate professional
        property descriptions.
        """
    )


with f2:

    st.success(
        """
        📸 **AI Photo Enhancement**

        Improve property photos and
        create premium listing visuals.
        """
    )


with f3:

    st.warning(
        """
        🛡️ **Trust Score**

        Show buyers property and
        owner verification status.
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
