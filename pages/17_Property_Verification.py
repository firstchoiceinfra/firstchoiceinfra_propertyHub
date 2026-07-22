import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 17 - PROPERTY VERIFICATION & TRUST CENTER
# ============================================================

st.set_page_config(
    page_title="Property Verification | FirstChoice Property Hub",
    page_icon="🛡️",
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

    padding: 50px;

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

/* STATUS CARD */

.status-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

/* VERIFIED */

.verified-card {

    padding: 40px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 20px 50px
    rgba(5,150,105,0.25);
}

/* TRUST */

.trust-card {

    padding: 40px;

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

/* DOCUMENT */

.document-card {

    padding: 25px;

    border-radius: 24px;

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

    margin-bottom: 15px;
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
PROPERTY HUB • TRUST • SAFETY • VERIFICATION
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🛡️ Property Verification Center
</div>

<div class="hero-subtitle">
Build trust with verified owners, verified properties
and transparent property information.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SECURITY NOTICE
# ============================================================

st.info(
    """
    🔐 **Security Notice**

    FirstChoice Property Hub should never ask users to publicly display
    sensitive identity numbers. In the production version, identity
    verification should use authorised KYC providers and secure APIs.
    Sensitive documents should be encrypted and access-controlled.
    """
)


# ============================================================
# VERIFICATION OVERVIEW
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Verification Overview
</div>

<div class="section-subtitle">
Track the verification status of your property listing.
</div>

</div>
""", unsafe_allow_html=True)


v1, v2, v3, v4 = st.columns(4)


with v1:

    st.metric(
        "🛡️ Verification Score",
        "78%"
    )


with v2:

    st.metric(
        "✅ Verified Items",
        "7"
    )


with v3:

    st.metric(
        "⏳ Under Review",
        "2"
    )


with v4:

    st.metric(
        "❌ Rejected",
        "0"
    )


# ============================================================
# SELECT PROPERTY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Select Your Property
</div>

<div class="section-subtitle">
Choose the listing you want to verify.
</div>

</div>
""", unsafe_allow_html=True)


property_name = st.selectbox(
    "Select Property",
    [
        "Premium 3 BHK Luxury Apartment — Civil Lines, Nagpur",
        "Luxury Independent Villa — Baner, Pune",
        "Premium Residential Plot — Wardha Road, Nagpur",
        "FirstChoice Premium Township — Nagpur"
    ]
)


# ============================================================
# CURRENT STATUS
# ============================================================

st.markdown("""
<div class="verified-card">

<h2>
🛡️ Verification Status
</h2>

<h1>
PARTIALLY VERIFIED
</h1>

<p>
Your property has completed several verification steps.
Complete the remaining steps to improve buyer trust.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# VERIFICATION PROGRESS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 Verification Progress
</div>

<div class="section-subtitle">
Complete all recommended verification steps.
</div>

</div>
""", unsafe_allow_html=True)


st.progress(
    0.78
)


st.write(
    "78% verification completed"
)


# ============================================================
# OWNER VERIFICATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Owner / Seller Verification
</div>

<div class="section-subtitle">
Verify the identity of the person listing the property.
</div>

</div>
""", unsafe_allow_html=True)


o1, o2 = st.columns(2)


with o1:

    st.markdown(
        """
        <div class="status-card">

        <h2>
        📱 Mobile Verification
        </h2>

        <p>
        ✅ Verified Mobile Number
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with o2:

    st.markdown(
        """
        <div class="status-card">

        <h2>
        🪪 Identity Verification
        </h2>

        <p>
        ⏳ Verification Pending
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


if st.button(
    "🛡️ START SECURE IDENTITY VERIFICATION",
    use_container_width=True
):

    st.info(
        """
        Secure identity verification will be connected
        with an authorised KYC provider in the production version.
        """
    )


# ============================================================
# PROPERTY DOCUMENTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📄 Property Document Verification
</div>

<div class="section-subtitle">
Upload documents for secure review by the verification team.
</div>

</div>
""", unsafe_allow_html=True)


documents = [

    (
        "📜 Ownership Proof",
        "✅ Verified"
    ),

    (
        "🧾 Property Tax Receipt",
        "✅ Verified"
    ),

    (
        "📄 Sale Deed / Agreement",
        "⏳ Under Review"
    ),

    (
        "🏗️ RERA Information",
        "⏳ Pending"
    ),

    (
        "🗺️ Property Location",
        "✅ Verified"
    ),

    (
        "📐 Property Details",
        "✅ Verified"
    )

]


for index, document in enumerate(documents):

    st.markdown(
        f"""
        <div class="document-card">

        <h3>
        {document[0]}
        </h3>

        <p>
        Status:
        <b>{document[1]}</b>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    uploaded_file = st.file_uploader(
        f"Upload {document[0]}",
        type=[
            "pdf",
            "jpg",
            "jpeg",
            "png"
        ],
        key=f"document_{index}"
    )


# ============================================================
# PROPERTY MEDIA VERIFICATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📸 Property Media Verification
</div>

<div class="section-subtitle">
Help buyers understand the actual property through authentic media.
</div>

</div>
""", unsafe_allow_html=True)


m1, m2 = st.columns(2)


with m1:

    property_photo = st.file_uploader(
        "📸 Upload Property Photos",
        type=[
            "jpg",
            "jpeg",
            "png"
        ],
        accept_multiple_files=True
    )


with m2:

    property_video = st.file_uploader(
        "🎥 Upload Property Video",
        type=[
            "mp4",
            "mov",
            "avi"
        ]
    )


# ============================================================
# MEDIA STATUS
# ============================================================

if property_photo:

    st.success(
        f"{len(property_photo)} property photo(s) uploaded."
    )


if property_video:

    st.success(
        "Property video uploaded successfully."
    )


# ============================================================
# LOCATION VERIFICATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📍 Location Verification
</div>

<div class="section-subtitle">
Confirm that the property location matches the listing.
</div>

</div>
""", unsafe_allow_html=True)


loc1, loc2 = st.columns(2)


with loc1:

    property_address = st.text_area(
        "Property Address",
        placeholder=
        "Enter complete property address"
    )


with loc2:

    landmark = st.text_input(
        "Nearby Landmark",
        placeholder=
        "Example: Near Metro Station"
    )


if st.button(
    "📍 VERIFY PROPERTY LOCATION",
    use_container_width=True
):

    st.success(
        "Location verification request submitted."
    )


# ============================================================
# VERIFICATION BADGES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏆 Trust Badges
</div>

<div class="section-subtitle">
Badges that can appear on verified property listings.
</div>

</div>
""", unsafe_allow_html=True)


b1, b2, b3 = st.columns(3)


with b1:

    st.success(
        """
        🛡️ **Verified Property**

        Property information reviewed.
        """
    )


with b2:

    st.info(
        """
        👤 **Verified Owner**

        Owner identity verification completed.
        """
    )


with b3:

    st.warning(
        """
        📄 **Documents Reviewed**

        Important documents reviewed by the platform.
        """
    )


# ============================================================
# BUYER TRUST VIEW
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👀 Buyer Trust Preview
</div>

<div class="section-subtitle">
This is how verification information may appear to buyers.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="trust-card">

<h2>
🏠 Premium 3 BHK Luxury Apartment
</h2>

<p>
📍 Civil Lines, Nagpur
</p>

<hr>

<p>
🛡️ Property Verification: <b>78%</b>
</p>

<p>
📱 Owner Mobile: ✅ Verified
</p>

<p>
👤 Owner Identity: ⏳ Pending
</p>

<p>
📄 Documents: 🟡 Partially Reviewed
</p>

<p>
📍 Location: ✅ Verified
</p>

<p>
📸 Media: ✅ Authenticity Review Pending
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# REPORT LISTING
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚨 Report a Suspicious Listing
</div>

<div class="section-subtitle">
Help us keep the property marketplace safe.
</div>

</div>
""", unsafe_allow_html=True)


report_reason = st.selectbox(
    "Reason for Report",
    [
        "Fake Property",
        "Incorrect Property Information",
        "Suspicious Owner",
        "Duplicate Listing",
        "Wrong Price",
        "Fraud / Scam",
        "Other"
    ]
)


report_message = st.text_area(
    "Describe the Issue",
    placeholder=
    "Please explain why you believe this listing is suspicious."
)


if st.button(
    "🚨 SUBMIT REPORT",
    use_container_width=True
):

    st.success(
        "Thank you. Your report has been submitted for review."
    )


# ============================================================
# TRUST & SAFETY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔐 FirstChoice Trust & Safety
</div>

<div class="section-subtitle">
Our future verification architecture.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="trust-card">

<h2>
🛡️ Building India's Trusted Property Marketplace
</h2>

<p>
🔐 Secure identity verification
</p>

<p>
📱 Verified mobile numbers
</p>

<p>
📄 Document review workflow
</p>

<p>
🏠 Property authenticity checks
</p>

<p>
📍 Location verification
</p>

<p>
🚨 Fraud reporting system
</p>

<p>
👥 Owner, Agent & Builder verification
</p>

<p>
⭐ Transparent trust badges
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Advanced Verification — Coming Next
</div>

<div class="section-subtitle">
Next-generation trust infrastructure.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.info(
        """
        🪪 **Secure KYC**

        Integration with authorised
        identity verification providers.
        """
    )


with f2:

    st.success(
        """
        🏛️ **RERA Verification**

        Automated verification support
        for eligible projects.
        """
    )


with f3:

    st.warning(
        """
        🤖 **AI Fraud Detection**

        Detect suspicious listings,
        duplicate photos and unusual activity.
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
