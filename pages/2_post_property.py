import streamlit as st

# ============================================================
# PAGE 2 — POST PROPERTY
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Post Your Property | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide"
)

# ============================================================
# PREMIUM MULTICOLOUR DESIGN
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

/* MAIN TITLE */

.main-title {
    padding: 40px;
    border-radius: 30px;
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
    0 20px 60px
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.main-title h1 {
    font-size: 42px;
    font-weight: 900;
}

.main-title p {
    font-size: 17px;
}

/* SECTION TITLE */

.section-title {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 22px 28px;

    border-radius: 22px;

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

.section-title h2 {
    margin: 0;
    font-size: 27px;
    font-weight: 900;
}

.section-title p {
    margin: 8px 0 0;
    color: #E0E7FF;
}

/* CARD */

.form-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* TRUST CARD */

.trust-card {

    padding: 28px;

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
    0 15px 45px
    rgba(5,150,105,0.22);
}

/* FINAL CARD */

.final-card {

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
<div class="main-title">

<h1>
🏡 Post Your Property
</h1>

<p>
List your property on India's next-generation real estate marketplace.
Reach genuine buyers, tenants and investors.
</p>

<p>
📸 Photos &nbsp; • &nbsp;
🎥 Video &nbsp; • &nbsp;
📍 Location &nbsp; • &nbsp;
🛡️ Verification
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LISTING TYPE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
👤 Who are you?
</h2>

<p>
Select your profile type to create your property listing.
</p>

</div>
""", unsafe_allow_html=True)


profile_type = st.radio(
    "Listing Profile",
    [
        "👤 Owner",
        "🏢 Agent / Broker",
        "🏗️ Builder / Developer",
        "🏛️ Company / Organization"
    ],
    horizontal=True
)


# ============================================================
# PROPERTY PURPOSE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🎯 What do you want to do?
</h2>

<p>
Choose the purpose of your property listing.
</p>

</div>
""", unsafe_allow_html=True)


purpose = st.radio(
    "Property Requirement",
    [
        "🏠 Sell",
        "🔑 Rent",
        "📈 Lease",
        "🤝 Joint Venture"
    ],
    horizontal=True
)


# ============================================================
# PROPERTY BASIC INFORMATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🏠 Property Information
</h2>

<p>
Tell buyers and tenants about your property.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


c1, c2 = st.columns(2)


with c1:

    property_title = st.text_input(
        "Property Title *",
        placeholder=
        "Example: Premium 3 BHK Luxury Apartment"
    )


with c2:

    property_type = st.selectbox(
        "Property Type *",
        [
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Plot",
            "Residential Land",
            "Farm Land",
            "Commercial Office",
            "Shop",
            "Warehouse",
            "Industrial Property",
            "Other"
        ]
    )


c3, c4, c5 = st.columns(3)


with c3:

    bhk = st.selectbox(
        "BHK",
        [
            "Not Applicable",
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "5 BHK",
            "5+ BHK"
        ]
    )


with c4:

    area = st.number_input(
        "Property Area (Sq.Ft.)",
        min_value=0,
        step=100
    )


with c5:

    property_age = st.selectbox(
        "Property Age",
        [
            "New Construction",
            "0–1 Year",
            "1–5 Years",
            "5–10 Years",
            "10+ Years"
        ]
    )


description = st.text_area(
    "Property Description",
    height=150,
    placeholder=
    "Describe your property, features, surroundings and unique benefits..."
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOCATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📍 Property Location
</h2>

<p>
Accurate location helps buyers discover your property.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


l1, l2 = st.columns(2)


with l1:

    state = st.selectbox(
        "State *",
        [
            "Maharashtra",
            "Madhya Pradesh",
            "Gujarat",
            "Karnataka",
            "Telangana",
            "Delhi",
            "Uttar Pradesh",
            "Rajasthan",
            "Tamil Nadu",
            "Other"
        ]
    )


with l2:

    city = st.text_input(
        "City *",
        placeholder="Example: Nagpur"
    )


l3, l4 = st.columns(2)


with l3:

    locality = st.text_input(
        "Locality / Area *",
        placeholder="Example: Civil Lines"
    )


with l4:

    pincode = st.text_input(
        "PIN Code *",
        max_chars=6,
        placeholder="440001"
    )


address = st.text_area(
    "Complete Property Address",
    placeholder=
    "Enter complete address..."
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PRICE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
💰 Pricing & Financial Details
</h2>

<p>
Set your expected property value.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


p1, p2, p3 = st.columns(3)


with p1:

    price = st.number_input(
        "Expected Price (₹)",
        min_value=0,
        step=100000
    )


with p2:

    price_negotiable = st.checkbox(
        "Price Negotiable"
    )


with p3:

    maintenance = st.number_input(
        "Monthly Maintenance (₹)",
        min_value=0,
        step=500
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
✨ Property Amenities
</h2>

<p>
Select facilities available with your property.
</p>

</div>
""", unsafe_allow_html=True)


amenities = st.multiselect(
    "Available Amenities",
    [
        "🚗 Parking",
        "🏊 Swimming Pool",
        "🏋️ Gym",
        "🌳 Garden",
        "🔒 Security",
        "🛗 Lift",
        "⚡ Power Backup",
        "💧 Water Supply",
        "🔥 Gas Pipeline",
        "📶 Internet",
        "🏫 School Nearby",
        "🏥 Hospital Nearby",
        "🛒 Market Nearby",
        "🚇 Public Transport"
    ]
)


# ============================================================
# MEDIA UPLOAD
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📸 Property Photos & 🎥 Video
</h2>

<p>
High-quality media increases buyer interest and trust.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="form-card">',
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


video_url = st.text_input(
    "Or paste YouTube / Property Video URL",
    placeholder=
    "https://youtube.com/..."
)


if photos:

    st.success(
        f"{len(photos)} property photo(s) selected."
    )


if video:

    st.success(
        "Property video selected successfully."
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# VERIFICATION
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
🛡️ Identity & Property Verification
</h2>

<p>
Verification will help create a trusted property ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="trust-card">

<h2>
🛡️ Build Trust With Verified Listings
</h2>

<p>
Verified profiles may receive stronger trust signals
and better visibility in future versions.
</p>

<p>
✅ Mobile Number Verification
</p>

<p>
✅ Identity Verification
</p>

<p>
✅ Property Ownership Verification
</p>

<p>
✅ RERA Verification for Applicable Projects
</p>

</div>
""", unsafe_allow_html=True)


v1, v2 = st.columns(2)


with v1:

    mobile = st.text_input(
        "Current Mobile Number *",
        max_chars=10,
        placeholder="10 digit mobile number"
    )


with v2:

    identity_type = st.selectbox(
        "Identity Verification",
        [
            "Verify Later",
            "Aadhaar-based Verification",
            "Other Government ID"
        ]
    )


st.info(
    "🔐 Aadhaar numbers should not be stored directly in the application. "
    "For production, we will integrate a compliant third-party KYC/identity "
    "verification provider and store only the required verification status/reference."
)


# ============================================================
# CONTACT PREFERENCE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>
📞 Contact Preferences
</h2>

<p>
Choose how interested users can contact you.
</p>

</div>
""", unsafe_allow_html=True)


contact_options = st.multiselect(
    "Preferred Contact Methods",
    [
        "📞 Phone Call",
        "💬 WhatsApp",
        "✉️ Email",
        "💬 In-App Chat"
    ]
)


# ============================================================
# TERMS
# ============================================================

agree = st.checkbox(
    "I confirm that the information provided is accurate and I have the right to list this property."
)


# ============================================================
# SUBMIT
# ============================================================

st.markdown("""
<div class="final-card">

<h2>
🚀 Ready to Publish Your Property?
</h2>

<p>
Review your information and submit your listing.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "🚀 SUBMIT PROPERTY LISTING",
    use_container_width=True
):

    if not property_title:

        st.error(
            "Please enter the Property Title."
        )

    elif not city:

        st.error(
            "Please enter the City."
        )

    elif not mobile:

        st.error(
            "Please enter your current mobile number."
        )

    elif len(mobile) != 10 or not mobile.isdigit():

        st.error(
            "Please enter a valid 10-digit mobile number."
        )

    elif not agree:

        st.warning(
            "Please confirm the declaration before submitting."
        )

    else:

        st.success(
            "🎉 Your property listing has been submitted successfully!"
        )

        st.info(
            "Next step: Mobile OTP verification and listing review."
        )
