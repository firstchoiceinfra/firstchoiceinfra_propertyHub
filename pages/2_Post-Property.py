import streamlit as st
import random

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# MULTICOLOR PREMIUM POST PROPERTY PAGE
# ============================================================

st.set_page_config(
    page_title="Post Property | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

if "listing_submitted" not in st.session_state:
    st.session_state.listing_submitted = False

if "listing_id" not in st.session_state:
    st.session_state.listing_id = ""


# ============================================================
# PREMIUM MULTICOLOR CSS
# ============================================================

st.markdown("""
<style>

/* ================= GLOBAL ================= */

.stApp {
    background:
    linear-gradient(
        135deg,
        #f7f9ff 0%,
        #fff7f2 35%,
        #f7f2ff 70%,
        #f1fbff 100%
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

/* ================= BRAND HEADER ================= */

.brand-box {
    background:
    linear-gradient(
        135deg,
        #071952,
        #088395,
        #35A29F
    );

    padding: 20px 30px;

    border-radius: 20px;

    color: white;

    box-shadow:
    0 12px 35px rgba(7,25,82,0.22);

    margin-bottom: 25px;
}

.brand-name {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 2px;
}

.brand-tagline {
    color: #DFFFD8;
    font-size: 13px;
    letter-spacing: 3px;
}

/* ================= HERO ================= */

.hero {
    background:
    linear-gradient(
        120deg,
        #071952,
        #088395 45%,
        #35A29F 75%,
        #F2C94C
    );

    padding: 55px 45px;

    border-radius: 32px;

    color: white;

    margin-bottom: 30px;

    box-shadow:
    0 25px 60px rgba(7,25,82,0.25);

    position: relative;

    overflow: hidden;
}

.hero:before {
    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    background:
    rgba(255,255,255,0.12);

    border-radius: 50%;

    right: -80px;
    top: -100px;
}

.hero:after {
    content: "";

    position: absolute;

    width: 180px;
    height: 180px;

    background:
    rgba(242,201,76,0.30);

    border-radius: 50%;

    right: 180px;
    bottom: -100px;
}

.hero h1 {
    font-size: 46px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.hero p {
    font-size: 17px;

    line-height: 1.7;

    max-width: 750px;

    position: relative;

    z-index: 2;
}

.hero-badge {
    display: inline-block;

    background:
    rgba(255,255,255,0.18);

    padding: 9px 18px;

    border-radius: 30px;

    font-weight: 700;

    margin-bottom: 15px;
}

/* ================= SECTION TITLE ================= */

.section-title {
    font-size: 29px;

    font-weight: 900;

    color: #071952;

    margin-top: 35px;
}

.section-subtitle {
    color: #667085;

    font-size: 15px;

    margin-bottom: 22px;
}

/* ================= COLOR CARDS ================= */

.color-card {
    padding: 28px 20px;

    border-radius: 22px;

    color: white;

    min-height: 145px;

    box-shadow:
    0 12px 30px rgba(0,0,0,0.10);

    text-align: center;
}

.card-blue {
    background:
    linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
}

.card-purple {
    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.card-orange {
    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

.card-green {
    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.card-gold {
    background:
    linear-gradient(
        135deg,
        #B7791F,
        #F2C94C
    );
}

.card-sky {
    background:
    linear-gradient(
        135deg,
        #0284C7,
        #38BDF8
    );
}

.card-icon {
    font-size: 42px;
}

.card-title {
    font-weight: 900;

    font-size: 18px;

    margin-top: 8px;
}

/* ================= WHITE PANEL ================= */

.panel {
    background:
    rgba(255,255,255,0.95);

    padding: 30px;

    border-radius: 25px;

    box-shadow:
    0 12px 40px rgba(31,41,55,0.08);

    border:
    1px solid rgba(255,255,255,0.7);

    margin-bottom: 25px;
}

/* ================= MEDIA ================= */

.media-photo {
    background:
    linear-gradient(
        135deg,
        #DBEAFE,
        #E0E7FF
    );

    padding: 28px;

    border-radius: 22px;

    text-align: center;

    border:
    2px dashed #6366F1;
}

.media-video {
    background:
    linear-gradient(
        135deg,
        #FCE7F3,
        #F3E8FF
    );

    padding: 28px;

    border-radius: 22px;

    text-align: center;

    border:
    2px dashed #EC4899;
}

.media-icon {
    font-size: 48px;
}

.media-title {
    font-size: 20px;

    font-weight: 900;

    color: #071952;
}

/* ================= TRUST ================= */

.trust {
    background:
    linear-gradient(
        135deg,
        #064E3B,
        #059669,
        #34D399
    );

    padding: 30px;

    color: white;

    border-radius: 25px;

    box-shadow:
    0 15px 40px rgba(5,150,105,0.25);
}

/* ================= PREVIEW ================= */

.preview {
    background: white;

    border-radius: 25px;

    overflow: hidden;

    box-shadow:
    0 15px 45px rgba(0,0,0,0.12);
}

.preview-top {
    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #2563EB,
        #06B6D4
    );

    color: white;

    padding: 30px;
}

.preview-price {
    color: #FDE047;

    font-size: 30px;

    font-weight: 900;
}

.feature-box {
    background:
    linear-gradient(
        135deg,
        #FFF7ED,
        #FFEDD5
    );

    padding: 15px;

    border-radius: 15px;

    text-align: center;

    color: #9A3412;

    font-weight: 800;
}

/* ================= SUCCESS ================= */

.success {
    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    color: white;

    padding: 55px;

    border-radius: 30px;

    text-align: center;

    box-shadow:
    0 25px 60px rgba(124,58,237,0.30);
}

.listing-id {
    font-size: 34px;

    color: #FDE047;

    font-weight: 900;

    letter-spacing: 3px;
}

/* ================= FOOTER ================= */

.footer {
    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );

    color: white;

    padding: 45px;

    border-radius: 25px;

    text-align: center;

    margin-top: 60px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand-box">

<div class="brand-name">
🏠 FIRSTCHOICE INFRA
</div>

<div class="brand-tagline">
PROPERTY HUB • INDIA'S NEXT-GENERATION REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-badge">
🚀 LIST YOUR PROPERTY • REACH INDIA
</div>

<h1>
Turn Your Property Into Opportunity
</h1>

<p>
Showcase your home, plot, commercial space or land
to genuine buyers, tenants and investors through
the FirstChoice Infra Property Hub.
</p>

<p>
📸 Premium Photos &nbsp;&nbsp;
🎬 Video Listings &nbsp;&nbsp;
📍 Smart Location &nbsp;&nbsp;
🛡️ Verified Profiles
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUICK STATS
# ============================================================

q1, q2, q3, q4 = st.columns(4)

quick_cards = [
    ("🏡", "Residential", "Homes & Apartments", "card-blue"),
    ("🏢", "Commercial", "Shops & Offices", "card-purple"),
    ("🌳", "Plots", "Land & Development", "card-orange"),
    ("🌾", "Agricultural", "Farm & Agriculture", "card-green")
]

for col, item in zip(
    [q1, q2, q3, q4],
    quick_cards
):

    with col:

        st.markdown(
            f"""
            <div class="color-card {item[3]}">

            <div class="card-icon">
            {item[0]}
            </div>

            <div class="card-title">
            {item[1]}
            </div>

            <div>
            {item[2]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# BASIC INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🏠 Property Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Tell us what you want to list.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="panel">',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    listing_purpose = st.selectbox(
        "What do you want to do?",
        [
            "Sell Property",
            "Rent / Lease Property"
        ]
    )

with c2:

    listed_by = st.selectbox(
        "You are",
        [
            "Property Owner",
            "Real Estate Agent / Broker",
            "Builder / Developer",
            "Business Partner"
        ]
    )

c3, c4 = st.columns(2)

with c3:

    property_category = st.selectbox(
        "Property Category",
        [
            "Residential",
            "Commercial",
            "Plot / Land",
            "Agricultural Land"
        ]
    )

with c4:

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


# ============================================================
# LOCATION
# ============================================================

st.markdown(
    '<div class="section-title">📍 Property Location</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Help buyers discover your property.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="panel">',
    unsafe_allow_html=True
)

l1, l2, l3 = st.columns(3)

with l1:

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
            "Madhya Pradesh",
            "Other"
        ]
    )

with l2:

    city = st.text_input(
        "City",
        placeholder="Example: Nagpur"
    )

with l3:

    locality = st.text_input(
        "Locality",
        placeholder="Example: Civil Lines"
    )

landmark = st.text_input(
    "Nearby Landmark",
    placeholder="Example: Near Airport / Metro / Highway"
)

address = st.text_area(
    "Complete Property Address"
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown(
    '<div class="section-title">📐 Property Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="panel">',
    unsafe_allow_html=True
)

d1, d2, d3, d4 = st.columns(4)

with d1:

    area = st.number_input(
        "Area Sq.Ft.",
        min_value=0,
        step=100
    )

with d2:

    bedrooms = st.selectbox(
        "Bedrooms",
        [
            "N/A",
            "1",
            "2",
            "3",
            "4",
            "5+"
        ]
    )

with d3:

    bathrooms = st.selectbox(
        "Bathrooms",
        [
            "N/A",
            "1",
            "2",
            "3",
            "4+"
        ]
    )

with d4:

    furnishing = st.selectbox(
        "Furnishing",
        [
            "N/A",
            "Unfurnished",
            "Semi Furnished",
            "Fully Furnished"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MEDIA
# ============================================================

st.markdown(
    '<div class="section-title">📸 Create a Powerful Listing</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Properties with great photos and videos attract more attention.</div>',
    unsafe_allow_html=True
)

m1, m2 = st.columns(2)

with m1:

    st.markdown("""
    <div class="media-photo">

    <div class="media-icon">
    📸
    </div>

    <div class="media-title">
    Upload Property Photos
    </div>

    <p>
    Showcase rooms, exterior, interiors and surroundings.
    </p>

    </div>
    """, unsafe_allow_html=True)

    photos = st.file_uploader(
        "Choose Photos",
        type=[
            "jpg",
            "jpeg",
            "png",
            "webp"
        ],
        accept_multiple_files=True
    )

with m2:

    st.markdown("""
    <div class="media-video">

    <div class="media-icon">
    🎬
    </div>

    <div class="media-title">
    Upload Property Video
    </div>

    <p>
    Give buyers a virtual walkthrough of your property.
    </p>

    </div>
    """, unsafe_allow_html=True)

    video = st.file_uploader(
        "Choose Video",
        type=[
            "mp4",
            "mov",
            "avi"
        ]
    )


# ============================================================
# PHOTO PREVIEW
# ============================================================

if photos:

    st.markdown(
        "### 🖼️ Your Property Gallery"
    )

    image_columns = st.columns(
        min(len(photos), 4)
    )

    for i, image in enumerate(
        photos[:4]
    ):

        with image_columns[i]:

            st.image(
                image,
                use_container_width=True
            )


if video:

    st.markdown(
        "### 🎬 Property Video Preview"
    )

    st.video(
        video
    )


# ============================================================
# PRICE
# ============================================================

st.markdown(
    '<div class="section-title">💰 Pricing & Investment</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="panel">',
    unsafe_allow_html=True
)

pr1, pr2 = st.columns(2)

with pr1:

    price = st.number_input(
        "Expected Price ₹",
        min_value=0,
        step=100000
    )

with pr2:

    negotiable = st.selectbox(
        "Price Negotiable?",
        [
            "Yes",
            "No"
        ]
    )

if listing_purpose == "Rent / Lease Property":

    rr1, rr2 = st.columns(2)

    with rr1:

        rent = st.number_input(
            "Monthly Rent ₹",
            min_value=0,
            step=1000
        )

    with rr2:

        deposit = st.number_input(
            "Security Deposit ₹",
            min_value=0,
            step=1000
        )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# AMENITIES
# ============================================================

st.markdown(
    '<div class="section-title">✨ Premium Property Features</div>',
    unsafe_allow_html=True
)

amenities = st.multiselect(
    "Choose Property Amenities",
    [
        "🏊 Swimming Pool",
        "🏋️ Gym",
        "🏡 Club House",
        "🌳 Garden",
        "🧒 Children's Play Area",
        "🛡️ 24x7 Security",
        "📹 CCTV",
        "🛗 Lift",
        "⚡ Power Backup",
        "🚗 Visitor Parking",
        "🏘️ Gated Community",
        "💧 Water Supply",
        "🌐 Internet Connectivity",
        "🔥 Fire Safety"
    ]
)

description = st.text_area(
    "Property Description",
    placeholder="Describe the property's location, features, connectivity and unique advantages..."
)


# ============================================================
# COLORFUL FEATURE STRIP
# ============================================================

f1, f2, f3, f4 = st.columns(4)

features = [
    ("📍", "Prime Location", "card-blue"),
    ("🛡️", "Trust & Safety", "card-green"),
    ("📸", "Visual Listing", "card-purple"),
    ("💎", "Premium Reach", "card-gold")
]

for col, feature in zip(
    [f1, f2, f3, f4],
    features
):

    with col:

        st.markdown(
            f"""
            <div class="color-card {feature[2]}">

            <div class="card-icon">
            {feature[0]}
            </div>

            <div class="card-title">
            {feature[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# TRUST
# ============================================================

st.markdown(
    '<div class="section-title">🛡️ FirstChoice Verification</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="trust">

<h2>
Build Buyer Confidence
</h2>

<p>
FirstChoice Property Hub is designed to create a trusted
real estate marketplace where property owners, buyers,
agents and developers can connect.
</p>

<p>
📱 Mobile Verification
&nbsp;&nbsp; • &nbsp;&nbsp;
🪪 Identity Verification
&nbsp;&nbsp; • &nbsp;&nbsp;
📄 Property Verification
&nbsp;&nbsp; • &nbsp;&nbsp;
🛡️ Trusted Listing
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

documents = st.file_uploader(
    "Upload Supporting Property Documents",
    type=[
        "pdf",
        "jpg",
        "jpeg",
        "png"
    ],
    accept_multiple_files=True
)


# ============================================================
# LIVE PREVIEW
# ============================================================

st.markdown(
    '<div class="section-title">👁️ Live Listing Preview</div>',
    unsafe_allow_html=True
)

pv1, pv2 = st.columns([1.4, 1])

with pv1:

    if photos:

        st.image(
            photos[0],
            use_container_width=True
        )

    else:

        st.markdown("""
        <div style="
        height:350px;
        background:
        linear-gradient(
            135deg,
            #DBEAFE,
            #E0E7FF,
            #FCE7F3
        );
        border-radius:25px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:80px;
        ">
        🏡
        </div>
        """, unsafe_allow_html=True)

with pv2:

    st.markdown(
        f"""
        <div class="preview">

        <div class="preview-top">

        <h2>
        {property_type}
        </h2>

        <p>
        📍 {locality if locality else "Your Locality"},
        {city if city else "Your City"}
        </p>

        <div class="preview-price">
        ₹ {price:,}
        </div>

        </div>

        <div style="padding:25px;">

        <div class="feature-box">
        📐 {area} Sq.Ft.
        </div>

        <br>

        <div class="feature-box">
        🛏️ {bedrooms} Bedrooms
        </div>

        <br>

        <div class="feature-box">
        🛁 {bathrooms} Bathrooms
        </div>

        <br>

        <div class="feature-box">
        ✨ {len(amenities)} Amenities
        </div>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SUBMIT
# ============================================================

st.markdown(
    '<div class="section-title">🚀 Publish Your Property</div>',
    unsafe_allow_html=True
)

agree = st.checkbox(
    "I confirm that the information provided is accurate and I agree to property verification."
)

b1, b2 = st.columns(2)

with b1:

    save_draft = st.button(
        "💾 SAVE AS DRAFT",
        use_container_width=True
    )

with b2:

    submit = st.button(
        "🚀 SUBMIT PROPERTY",
        use_container_width=True
    )


if save_draft:

    st.success(
        "💾 Property saved as draft."
    )


if submit:

    if not agree:

        st.warning(
            "⚠️ Please confirm the information before submitting."
        )

    elif not city or not locality or not address or not price:

        st.error(
            "❌ Please complete location, address and pricing information."
        )

    else:

        st.session_state.listing_id = (
            "FCPH-"
            + str(
                random.randint(
                    100000,
                    999999
                )
            )
        )

        st.session_state.listing_submitted = True


# ============================================================
# SUCCESS
# ============================================================

if st.session_state.listing_submitted:

    st.markdown(
        f"""
        <div class="success">

        <h1>
        🎉 Your Property Is On Its Way!
        </h1>

        <p>
        Your listing has been successfully submitted
        for FirstChoice verification.
        </p>

        <div class="listing-id">
        {st.session_state.listing_id}
        </div>

        <p>
        ⏳ Verification Pending
        </p>

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
