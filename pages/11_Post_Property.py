import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 11 - POST / LIST YOUR PROPERTY
# PREMIUM INDIA REAL ESTATE LISTING MODULE
# ============================================================

st.set_page_config(
    page_title="Post Your Property | FirstChoice Property Hub",
    page_icon="🏠",
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

    padding: 50px 45px;

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
    font-size: 44px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 17px;
    color: rgba(255,255,255,0.88);
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
    color: rgba(255,255,255,0.82);
}

/* CARD */

.card {
    background: white;

    padding: 30px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);
}

/* VERIFICATION */

.verify-card {
    padding: 30px;

    border-radius: 28px;

    background:
    linear-gradient(
        135deg,
        #ECFDF5,
        #EFF6FF,
        #F5F3FF
    );

    border:
    1px solid #DDE7FF;
}

/* CTA */

.cta {
    padding: 45px;

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
🏡 List Your Property
</div>

<div class="hero-subtitle">
Reach genuine buyers, tenants and investors across India.
Create your property listing in a few simple steps.
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
Complete the information below to prepare your property for publishing.
</div>

</div>
""", unsafe_allow_html=True)


step1, step2, step3, step4 = st.columns(4)

with step1:
    st.info("1️⃣ Property")

with step2:
    st.info("2️⃣ Location")

with step3:
    st.info("3️⃣ Photos & Video")

with step4:
    st.info("4️⃣ Publish")


# ============================================================
# STEP 1 - LISTING TYPE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
1️⃣ What do you want to list?
</div>

<div class="section-subtitle">
Choose the purpose of your property listing.
</div>

</div>
""", unsafe_allow_html=True)


l1, l2 = st.columns(2)


with l1:

    listing_for = st.selectbox(
        "Listing Purpose",
        [
            "Sell Property",
            "Rent Property",
            "Lease Property",
            "Commercial Sale",
            "Commercial Rent"
        ]
    )


with l2:

    seller_type = st.selectbox(
        "I am a",
        [
            "Owner",
            "Agent / Broker",
            "Builder / Developer",
            "Company / Organization"
        ]
    )


# ============================================================
# PROPERTY TYPE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Property Information
</div>

<div class="section-subtitle">
Tell buyers about the property you are listing.
</div>

</div>
""", unsafe_allow_html=True)


p1, p2, p3 = st.columns(3)


with p1:

    property_type = st.selectbox(
        "Property Type",
        [
            "Apartment",
            "Independent House",
            "Villa",
            "Residential Plot",
            "Agricultural Land",
            "Farm House",
            "Commercial Office",
            "Shop",
            "Showroom",
            "Warehouse",
            "Industrial Property",
            "Hotel / Hospitality",
            "Other"
        ]
    )


with p2:

    property_status = st.selectbox(
        "Property Status",
        [
            "Ready to Move",
            "Under Construction",
            "New Launch",
            "Resale",
            "Pre-Launch"
        ]
    )


with p3:

    ownership = st.selectbox(
        "Ownership",
        [
            "Freehold",
            "Leasehold",
            "Power of Attorney",
            "Other"
        ]
    )


# ============================================================
# BASIC DETAILS
# ============================================================

b1, b2, b3 = st.columns(3)


with b1:

    bedrooms = st.selectbox(
        "Bedrooms / BHK",
        [
            "Not Applicable",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5 BHK",
            "6+ BHK"
        ]
    )


with b2:

    bathrooms = st.selectbox(
        "Bathrooms",
        [
            "Not Applicable",
            "1",
            "2",
            "3",
            "4",
            "5+"
        ]
    )


with b3:

    furnishing = st.selectbox(
        "Furnishing",
        [
            "Unfurnished",
            "Semi-Furnished",
            "Fully Furnished"
        ]
    )


# ============================================================
# AREA
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📐 Property Size
</div>

<div class="section-subtitle">
Add accurate property measurements.
</div>

</div>
""", unsafe_allow_html=True)


a1, a2, a3 = st.columns(3)


with a1:

    built_area = st.number_input(
        "Built-up Area",
        min_value=0,
        step=100
    )


with a2:

    carpet_area = st.number_input(
        "Carpet Area",
        min_value=0,
        step=100
    )


with a3:

    area_unit = st.selectbox(
        "Area Unit",
        [
            "Sq.Ft",
            "Sq.Yard",
            "Sq.Meter",
            "Acre",
            "Hectare"
        ]
    )


# ============================================================
# PRICE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💰 Pricing Information
</div>

<div class="section-subtitle">
Set your expected property price.
</div>

</div>
""", unsafe_allow_html=True)


pr1, pr2, pr3 = st.columns(3)


with pr1:

    price = st.number_input(
        "Expected Price",
        min_value=0,
        step=100000
    )


with pr2:

    price_unit = st.selectbox(
        "Price Unit",
        [
            "₹",
            "₹ Thousand",
            "₹ Lakh",
            "₹ Crore"
        ]
    )


with pr3:

    negotiable = st.checkbox(
        "Price Negotiable"
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


loc1, loc2 = st.columns(2)


with loc1:

    state = st.selectbox(
        "State",
        [
            "Maharashtra",
            "Madhya Pradesh",
            "Delhi NCR",
            "Karnataka",
            "Telangana",
            "Gujarat",
            "Rajasthan",
            "Uttar Pradesh",
            "Tamil Nadu",
            "Goa",
            "Other"
        ]
    )


with loc2:

    city = st.text_input(
        "City",
        placeholder="Enter city"
    )


loc3, loc4 = st.columns(2)


with loc3:

    locality = st.text_input(
        "Locality / Area",
        placeholder="Enter locality"
    )


with loc4:

    landmark = st.text_input(
        "Nearby Landmark",
        placeholder="Example: Near Metro Station"
    )


# ============================================================
# DESCRIPTION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📝 Property Description
</div>

<div class="section-subtitle">
Describe what makes your property special.
</div>

</div>
""", unsafe_allow_html=True)


description = st.text_area(

    "Write a detailed description",

    height=180,

    placeholder=
    "Describe location, construction quality, amenities, connectivity and other important details..."

)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
✨ Select Amenities
</div>

<div class="section-subtitle">
Highlight the facilities available with your property.
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
        "Children's Play Area",
        "24/7 Security",
        "CCTV",
        "Power Backup",
        "Lift",
        "Covered Parking",
        "Visitor Parking",
        "Fire Safety",
        "Internet",
        "Security Gate",
        "Sports Facility"
    ]

)


# ============================================================
# PHOTOS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📸 Property Photos
</div>

<div class="section-subtitle">
Upload high-quality images to attract genuine buyers.
</div>

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


if photos:

    st.success(
        f"{len(photos)} property image(s) selected."
    )


# ============================================================
# VIDEO
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🎥 Property Video
</div>

<div class="section-subtitle">
Add a property video or virtual tour.
</div>

</div>
""", unsafe_allow_html=True)


video_url = st.text_input(

    "YouTube / Video URL",

    placeholder=
    "Paste your property video link"

)


# ============================================================
# VERIFICATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ Trust & Verification
</div>

<div class="section-subtitle">
Build buyer confidence with verified information.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="verify-card">

<h3>
🔐 FirstChoice Verification System
</h3>

<p>
Our production platform will support secure identity,
mobile and property verification.
</p>

<p>
🪪 Identity / KYC Verification
</p>

<p>
📱 Mobile Number Verification
</p>

<p>
📄 Property Document Verification
</p>

<p>
🏠 Ownership Verification
</p>

</div>
""", unsafe_allow_html=True)


v1, v2 = st.columns(2)


with v1:

    mobile = st.text_input(
        "Mobile Number",
        placeholder="Enter your 10-digit mobile number"
    )


with v2:

    email = st.text_input(
        "Email Address",
        placeholder="Enter email address"
    )


if st.button(

    "📱 SEND MOBILE OTP",

    use_container_width=True

):

    if len(mobile) == 10:

        st.success(
            "OTP verification process started."
        )

    else:

        st.warning(
            "Please enter a valid 10-digit mobile number."
        )


# ============================================================
# DOCUMENTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📄 Property Documents
</div>

<div class="section-subtitle">
Upload documents for future property verification.
</div>

</div>
""", unsafe_allow_html=True)


documents = st.file_uploader(

    "Upload Property Documents",

    type=[
        "pdf",
        "jpg",
        "jpeg",
        "png"
    ],

    accept_multiple_files=True,

    key="documents"

)


if documents:

    st.success(
        f"{len(documents)} document(s) selected."
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
Review your property listing before publishing.
</div>

</div>
""", unsafe_allow_html=True)


preview1, preview2 = st.columns(2)


with preview1:

    st.markdown("""
    <div class="card">

    <h2>
    🏡 Your Property
    </h2>

    <p>
    Buyers will see your property details,
    photos, pricing and location here.
    </p>

    </div>
    """, unsafe_allow_html=True)


with preview2:

    st.markdown("""
    <div class="card">

    <h2>
    🛡️ Verification Status
    </h2>

    <p>
    Mobile: Pending
    </p>

    <p>
    Identity: Pending
    </p>

    <p>
    Property Documents: Pending
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# PUBLISH
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Publish Your Property
</div>

<div class="section-subtitle">
Submit your listing for publishing on FirstChoice Property Hub.
</div>

</div>
""", unsafe_allow_html=True)


agree = st.checkbox(

    "I confirm that the information provided by me is accurate."

)


if st.button(

    "🚀 PUBLISH PROPERTY LISTING",

    use_container_width=True

):

    if not city or not locality:

        st.warning(
            "Please enter property city and locality."
        )

    elif not mobile:

        st.warning(
            "Please enter your mobile number."
        )

    elif not agree:

        st.warning(
            "Please confirm the information declaration."
        )

    else:

        st.success(
            "🎉 Property listing submitted successfully for verification."
        )

        st.info(
            "In the production version, your listing will be saved in the database and appear in the Property Search marketplace."
        )


# ============================================================
# PREMIUM CTA
# ============================================================

st.markdown("""
<div class="cta">

<h2>
🌟 Get Maximum Visibility
</h2>

<p>
Upgrade your property listing to Premium or Featured
to reach more buyers and investors.
</p>

<p>
⭐ Premium Listing
</p>

<p>
🔥 Featured Placement
</p>

<p>
📈 Higher Visibility
</p>

<p>
🎯 Better Buyer Reach
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

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
