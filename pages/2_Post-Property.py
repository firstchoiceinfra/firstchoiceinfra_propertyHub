import streamlit as st
import random

# =========================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PREMIUM PROPERTY LISTING / POST PROPERTY
# =========================================================

st.set_page_config(
    page_title="Post Your Property | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "listing_submitted": False,
    "listing_id": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
        linear-gradient(
            135deg,
            #f5f7fb 0%,
            #eef2f7 50%,
            #ffffff 100%
        );
    }

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .brand {
        font-size: 28px;
        font-weight: 800;
        color: #0b1f3a;
        letter-spacing: 1px;
    }

    .brand-sub {
        font-size: 13px;
        color: #b08d35;
        letter-spacing: 2px;
        font-weight: 600;
    }

    .hero {
        background:
        linear-gradient(
            135deg,
            rgba(7, 27, 52, 0.98),
            rgba(18, 63, 115, 0.95)
        );

        padding: 55px 45px;

        border-radius: 28px;

        color: white;

        box-shadow:
        0px 20px 50px rgba(11,31,58,0.20);

        margin-top: 25px;
        margin-bottom: 35px;
    }

    .hero h1 {
        font-size: 42px;
        font-weight: 800;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.9;
    }

    .section-title {
        color: #0b1f3a;
        font-size: 26px;
        font-weight: 800;
        margin-top: 30px;
        margin-bottom: 18px;
    }

    .premium-card {
        background: rgba(255,255,255,0.96);

        padding: 30px;

        border-radius: 22px;

        box-shadow:
        0px 10px 35px rgba(0,0,0,0.07);

        border: 1px solid rgba(0,0,0,0.04);

        margin-bottom: 25px;
    }

    .info-card {
        background:
        linear-gradient(
            135deg,
            #0b1f3a,
            #173f70
        );

        color: white;

        padding: 25px;

        border-radius: 18px;

        margin-bottom: 20px;
    }

    .verified {
        background: #eaf8f0;
        color: #18794e;

        padding: 12px 18px;

        border-radius: 12px;

        font-weight: 700;
    }

    .pending {
        background: #fff7e6;
        color: #9a6700;

        padding: 12px 18px;

        border-radius: 12px;

        font-weight: 700;
    }

    .success-card {
        background:
        linear-gradient(
            135deg,
            #0b1f3a,
            #173f70
        );

        color: white;

        padding: 40px;

        border-radius: 25px;

        text-align: center;

        box-shadow:
        0px 20px 50px rgba(11,31,58,0.25);
    }

    .listing-id {
        font-size: 32px;
        font-weight: 800;
        color: #e3bd63;
        letter-spacing: 2px;
    }

    .footer {
        margin-top: 60px;

        padding: 35px;

        background: #071b34;

        color: white;

        border-radius: 22px;

        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

header1, header2 = st.columns([3, 1])

with header1:

    st.markdown(
        """
        <div class="brand">
        🏠 FIRSTCHOICE INFRA
        </div>

        <div class="brand-sub">
        PROPERTY HUB
        </div>
        """,
        unsafe_allow_html=True
    )

with header2:

    st.markdown(
        """
        <div style="
        text-align:right;
        color:#0b1f3a;
        font-weight:600;
        padding-top:10px;
        ">
        🇮🇳 India's Smart Real Estate Marketplace
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <h1>List Your Property With Confidence</h1>

        <p>
        Reach genuine buyers, tenants and investors
        across India's growing real estate marketplace.
        </p>

        <p>
        📸 Photos &nbsp; • &nbsp;
        🎬 Property Video &nbsp; • &nbsp;
        📍 Location &nbsp; • &nbsp;
        🛡️ Verification
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PROGRESS
# =========================================================

st.progress(
    0.20,
    text="Step 1 of 5 — Property Information"
)


# =========================================================
# SECTION 1 — LISTING PURPOSE
# =========================================================

st.markdown(
    '<div class="section-title">🏠 What would you like to do?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

purpose_col1, purpose_col2 = st.columns(2)

with purpose_col1:

    listing_purpose = st.radio(
        "Listing Purpose",
        [
            "Sell Property",
            "Rent / Lease Property"
        ],
        horizontal=True
    )

with purpose_col2:

    seller_type = st.selectbox(
        "I am a",
        [
            "Property Owner",
            "Real Estate Agent / Broker",
            "Builder / Developer",
            "Business Partner"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 2 — PROPERTY CATEGORY
# =========================================================

st.markdown(
    '<div class="section-title">🏘️ Property Category</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

category_col1, category_col2 = st.columns(2)

with category_col1:

    property_category = st.selectbox(
        "Category",
        [
            "Residential",
            "Commercial",
            "Plot / Land",
            "Agricultural Land"
        ]
    )

with category_col2:

    property_type = st.selectbox(
        "Property Type",
        [
            "Apartment / Flat",
            "Villa",
            "Independent House",
            "Builder Floor",
            "Penthouse",
            "Studio Apartment",
            "Residential Plot",
            "Commercial Plot",
            "Office Space",
            "Shop / Showroom",
            "Warehouse",
            "Industrial Property",
            "Farm Land",
            "Agricultural Land"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 3 — PROPERTY LOCATION
# =========================================================

st.markdown(
    '<div class="section-title">📍 Property Location</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

location_col1, location_col2 = st.columns(2)

with location_col1:

    state = st.selectbox(
        "State",
        [
            "Select State",
            "Maharashtra",
            "Delhi",
            "Karnataka",
            "Gujarat",
            "Telangana",
            "Tamil Nadu",
            "Uttar Pradesh",
            "Rajasthan",
            "West Bengal",
            "Madhya Pradesh",
            "Other"
        ]
    )

    city = st.text_input(
        "City",
        placeholder="Enter city"
    )

with location_col2:

    locality = st.text_input(
        "Locality / Area",
        placeholder="Enter locality or area"
    )

    landmark = st.text_input(
        "Nearby Landmark",
        placeholder="Example: Near Metro Station"
    )

address = st.text_area(
    "Property Address",
    placeholder="Enter complete property address"
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 4 — PROPERTY DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">📐 Property Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

detail_col1, detail_col2, detail_col3 = st.columns(3)

with detail_col1:

    area = st.number_input(
        "Property Area (Sq.Ft.)",
        min_value=0,
        step=100
    )

with detail_col2:

    bedrooms = st.selectbox(
        "Bedrooms",
        [
            "Not Applicable",
            "1",
            "2",
            "3",
            "4",
            "5+"
        ]
    )

with detail_col3:

    bathrooms = st.selectbox(
        "Bathrooms",
        [
            "Not Applicable",
            "1",
            "2",
            "3",
            "4+"
        ]
    )

detail_col4, detail_col5, detail_col6 = st.columns(3)

with detail_col4:

    furnishing = st.selectbox(
        "Furnishing",
        [
            "Not Applicable",
            "Unfurnished",
            "Semi Furnished",
            "Fully Furnished"
        ]
    )

with detail_col5:

    parking = st.selectbox(
        "Parking",
        [
            "No Parking",
            "Bike Parking",
            "Car Parking",
            "Multiple Parking"
        ]
    )

with detail_col6:

    possession = st.selectbox(
        "Possession Status",
        [
            "Ready to Move",
            "Under Construction",
            "New Launch",
            "Resale"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 5 — PRICE
# =========================================================

st.markdown(
    '<div class="section-title">💰 Pricing & Financial Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

price_col1, price_col2 = st.columns(2)

with price_col1:

    price = st.number_input(
        "Expected Price (₹)",
        min_value=0,
        step=100000
    )

with price_col2:

    negotiable = st.radio(
        "Price Negotiable?",
        [
            "Yes",
            "No"
        ],
        horizontal=True
    )

if listing_purpose == "Rent / Lease Property":

    rent = st.number_input(
        "Monthly Rent (₹)",
        min_value=0,
        step=1000
    )

    deposit = st.number_input(
        "Security Deposit (₹)",
        min_value=0,
        step=1000
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 6 — MEDIA
# =========================================================

st.markdown(
    '<div class="section-title">📸 Property Photos & 🎬 Video</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

st.info(
    "High-quality photos and videos increase buyer confidence and property engagement."
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

if photos:

    st.success(
        f"{len(photos)} property photo(s) selected."
    )

    image_cols = st.columns(
        min(len(photos), 4)
    )

    for i, photo in enumerate(
        photos[:4]
    ):

        with image_cols[i]:

            st.image(
                photo,
                use_container_width=True
            )

if video:

    st.success(
        "Property video uploaded successfully."
    )

    st.video(
        video
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 7 — AMENITIES
# =========================================================

st.markdown(
    '<div class="section-title">✨ Property Amenities</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

amenities = st.multiselect(
    "Select Available Amenities",
    [
        "Swimming Pool",
        "Gym",
        "Club House",
        "Garden",
        "Children's Play Area",
        "24x7 Security",
        "CCTV",
        "Lift",
        "Power Backup",
        "Visitor Parking",
        "Gated Community",
        "Water Supply",
        "Internet Connectivity",
        "Fire Safety"
    ]
)

description = st.text_area(
    "Property Description",
    placeholder="Describe your property, location advantages, nearby facilities and unique features..."
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 8 — OWNER DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">👤 Contact & Ownership Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

owner_col1, owner_col2 = st.columns(2)

with owner_col1:

    owner_name = st.text_input(
        "Owner / Contact Person Name"
    )

    owner_mobile = st.text_input(
        "Mobile Number",
        max_chars=10
    )

with owner_col2:

    owner_email = st.text_input(
        "Email Address"
    )

    contact_preference = st.selectbox(
        "Preferred Contact Method",
        [
            "Phone Call",
            "WhatsApp",
            "Email",
            "Phone + WhatsApp"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 9 — VERIFICATION
# =========================================================

st.markdown(
    '<div class="section-title">🛡️ Property Verification</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="premium-card">',
    unsafe_allow_html=True
)

verify_col1, verify_col2, verify_col3 = st.columns(3)

with verify_col1:

    st.markdown(
        """
        <div class="verified">
        📱 Mobile Verification
        <br>
        Required
        </div>
        """,
        unsafe_allow_html=True
    )

with verify_col2:

    st.markdown(
        """
        <div class="pending">
        🪪 Identity Verification
        <br>
        Pending
        </div>
        """,
        unsafe_allow_html=True
    )

with verify_col3:

    st.markdown(
        """
        <div class="pending">
        📄 Property Documents
        <br>
        Verification Required
        </div>
        """,
        unsafe_allow_html=True
    )

st.info(
    "In the production version, property documents and identity information will be securely verified through authorized verification services."
)

documents = st.file_uploader(
    "Upload Supporting Property Documents (Optional Demo)",
    type=[
        "pdf",
        "jpg",
        "jpeg",
        "png"
    ],
    accept_multiple_files=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SECTION 10 — PREVIEW
# =========================================================

st.markdown(
    '<div class="section-title">👁️ Listing Preview</div>',
    unsafe_allow_html=True
)

preview_col1, preview_col2 = st.columns(2)

with preview_col1:

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.subheader(
        property_type if property_type else "Your Property"
    )

    st.write(
        f"📍 {locality}, {city}"
    )

    st.write(
        f"🏠 {property_category}"
    )

    st.write(
        f"📐 {area} Sq.Ft."
    )

    st.write(
        f"💰 ₹ {price:,}"
    )

    st.write(
        f"✨ Amenities: {', '.join(amenities) if amenities else 'Not selected'}"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

with preview_col2:

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.subheader(
        "Verification Status"
    )

    st.success(
        "📱 Mobile: Ready for Verification"
    )

    st.warning(
        "🪪 Identity: Pending"
    )

    st.warning(
        "📄 Property Documents: Pending"
    )

    st.info(
        "Your listing will be reviewed before publication."
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# SUBMIT LISTING
# =========================================================

st.markdown(
    '<div class="section-title">🚀 Submit Property Listing</div>',
    unsafe_allow_html=True
)

submit_col1, submit_col2 = st.columns(2)

with submit_col1:

    save_draft = st.button(
        "💾 Save as Draft",
        use_container_width=True
    )

with submit_col2:

    submit_listing = st.button(
        "🚀 Submit for Verification",
        use_container_width=True
    )


if save_draft:

    st.info(
        "Your property listing has been saved as a draft."
    )


if submit_listing:

    if (
        not city
        or not locality
        or not address
        or not owner_name
        or not owner_mobile
        or not price
    ):

        st.error(
            "Please complete the required property, location, pricing and contact details."
        )

    else:

        listing_id = (
            "FCPH-"
            + str(
                random.randint(
                    100000,
                    999999
                )
            )
        )

        st.session_state.listing_id = listing_id

        st.session_state.listing_submitted = True


# =========================================================
# SUCCESS
# =========================================================

if st.session_state.listing_submitted:

    st.markdown(
        """
        <div class="success-card">

        <h1>🎉 Property Submitted Successfully!</h1>

        <p>
        Your property has been submitted for verification.
        </p>

        <p>
        Once approved, your listing can be published
        on FirstChoice Infra Property Hub.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="info-card">

        <div>
        YOUR PROPERTY LISTING ID
        </div>

        <div class="listing-id">
        {st.session_state.listing_id}
        </div>

        <br>

        <div>
        Status: ⏳ Pending Verification
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "📱 Mobile Verification — Pending"
    )

    st.warning(
        "🪪 Identity Verification — Pending"
    )

    st.warning(
        "📄 Property Document Verification — Pending"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    <h2>FIRSTCHOICE INFRA PROPERTY HUB</h2>

    <p>
    India's Smart Real Estate Marketplace
    </p>

    <p>
    Buy • Sell • Rent • Invest
    </p>

    <br>

    <small>
    © FirstChoice Infra Property Hub
    </small>

    </div>
    """,
    unsafe_allow_html=True
)
