import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 15 — PROPERTY DOCUMENT VERIFICATION
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Document Verification | FirstChoice Property Hub",
    page_icon="🛡️",
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
    padding: 48px;
    border-radius: 34px;
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
    rgba(37,99,235,0.28);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.7;
}

/* SECTION */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 28px 32px;

    border-radius: 26px;

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
    rgba(79,70,229,0.20);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}

/* CARD */

.card {
    padding: 30px;
    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* SECURITY CARD */

.security-card {
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
    0 18px 50px
    rgba(5,150,105,0.25);
}

/* INFO CARD */

.info-card {
    padding: 25px;
    border-radius: 25px;

    background:
    linear-gradient(
        135deg,
        #EFF6FF,
        #F5F3FF,
        #FDF2F8
    );

    border: 1px solid #E0E7FF;

    min-height: 190px;
}

/* DOCUMENT CARD */

.document-card {
    padding: 24px;
    border-radius: 24px;

    background: white;

    border: 1px solid #E5E7EB;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);

    margin-bottom: 18px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🛡️ Property Document Verification Centre
</h1>

<p>
A smarter way to organise property documents and perform
preliminary due-diligence checks before moving forward.
</p>

<p>
📄 Documents • 🔍 Verification • 🛡️ Risk Awareness • ✅ Transparency
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SECURITY MESSAGE
# ============================================================

st.markdown("""
<div class="security-card">

<h2>
🛡️ Buy With Greater Confidence
</h2>

<p>
Property transactions involve important legal and financial decisions.
Our platform is designed to help users organise documents,
identify missing information and request professional verification.
</p>

<p>
🔐 Your documents should always be handled securely and shared
only with authorised professionals.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY SELECTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Property For Verification
</h2>

<p>
Start a preliminary property verification request.
</p>

</div>
""", unsafe_allow_html=True)


property_name = st.selectbox(
    "Select Property",
    [
        "Premium 3 BHK Luxury Apartment",
        "Modern 4 BHK Premium Villa",
        "Residential Plot — Wardha Road",
        "Commercial Office Space",
        "Premium Investment Property"
    ]
)


property_location = st.text_input(
    "📍 Property Location",
    placeholder="Enter complete property location"
)


owner_name = st.text_input(
    "👤 Property Owner / Seller Name",
    placeholder="Enter owner or seller name"
)


# ============================================================
# DOCUMENT CHECKLIST
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Preliminary Document Checklist
</h2>

<p>
Select the documents available for the property.
</p>

</div>
""", unsafe_allow_html=True)


documents = {

    "Sale Deed / Title Document":
    "Primary ownership document",

    "Previous Sale Deed":
    "Previous ownership history",

    "Encumbrance Certificate":
    "Helps identify registered encumbrances",

    "Property Tax Receipt":
    "Latest property tax information",

    "Approved Building Plan":
    "Building approval documentation",

    "Completion / Occupancy Certificate":
    "Applicable project completion documentation",

    "Mutation / Revenue Record":
    "Relevant land or revenue record",

    "RERA Registration Details":
    "Applicable for eligible real estate projects",

    "Society / Association Documents":
    "Applicable for apartments and societies",

    "Identity & Ownership Proof":
    "Seller identity and ownership verification"
}


selected_documents = []


for title, description in documents.items():

    checked = st.checkbox(
        f"📄 {title}",
        key=f"doc_{title}"
    )

    if checked:

        selected_documents.append(
            title
        )


# ============================================================
# UPLOAD DOCUMENTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📤 Upload Property Documents
</h2>

<p>
Upload available documents for organised record keeping.
</p>

</div>
""", unsafe_allow_html=True)


uploaded_files = st.file_uploader(
    "Upload PDF or Image Documents",
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg"
    ],
    accept_multiple_files=True
)


if uploaded_files:

    st.success(
        f"📁 {len(uploaded_files)} document(s) uploaded for preliminary review."
    )


# ============================================================
# VERIFICATION REQUEST
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔍 Request Verification
</h2>

</div>
""", unsafe_allow_html=True)


v1, v2 = st.columns(2)


with v1:

    verification_type = st.selectbox(
        "Verification Type",
        [
            "Preliminary Document Review",
            "Title & Ownership Review",
            "Legal Due Diligence",
            "RERA Verification",
            "Land Record Verification",
            "Complete Property Verification"
        ]
    )


with v2:

    priority = st.selectbox(
        "Request Priority",
        [
            "Standard",
            "Priority",
            "Urgent"
        ]
    )


additional_notes = st.text_area(
    "📝 Additional Information",
    placeholder=
    "Add any questions or concerns about this property..."
)


if st.button(
    "🚀 SUBMIT VERIFICATION REQUEST",
    use_container_width=True
):

    if not property_location:

        st.error(
            "Please enter the property location."
        )

    elif not owner_name:

        st.error(
            "Please enter the owner or seller name."
        )

    else:

        st.success(
            "🎉 Verification request submitted successfully."
        )

        st.info(
            "Your request has been recorded. "
            "Professional verification should be performed by qualified "
            "legal or property professionals where required."
        )


# ============================================================
# DOCUMENT STATUS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Document Verification Dashboard
</h2>

</div>
""", unsafe_allow_html=True)


total_documents = len(documents)

available_documents = len(
    selected_documents
)

missing_documents = (
    total_documents
    -
    available_documents
)


d1, d2, d3 = st.columns(3)


with d1:

    st.metric(
        "📄 Total Checklist",
        total_documents
    )


with d2:

    st.metric(
        "✅ Available",
        available_documents
    )


with d3:

    st.metric(
        "⚠️ Missing",
        missing_documents
    )


if total_documents > 0:

    completion = (
        available_documents
        /
        total_documents
    )


    st.progress(
        completion
    )


    st.caption(
        f"Document availability: "
        f"{completion * 100:.0f}%"
    )


# ============================================================
# DOCUMENT LIST
# ============================================================

st.markdown("""
<div class="section">

<h2>
📑 Document Status
</h2>

</div>
""", unsafe_allow_html=True)


for title, description in documents.items():

    if title in selected_documents:

        status = "✅ Available"

    else:

        status = "⚠️ Not Added"


    st.markdown(
        f"""
        <div class="document-card">

        <h3>
        📄 {title}
        </h3>

        <p>
        {description}
        </p>

        <b>
        {status}
        </b>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SMART PROPERTY SAFETY FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤖 Future Property Safety Intelligence
</h2>

<p>
Our long-term vision is to build technology that helps users
identify potential property risks before making major decisions.
</p>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    st.markdown("""
    <div class="info-card">

    <h3>
    🔍 Document OCR
    </h3>

    <p>
    Future AI systems can extract important information
    from uploaded documents for easier review.
    </p>

    </div>
    """, unsafe_allow_html=True)


with s2:

    st.markdown("""
    <div class="info-card">

    <h3>
    🚨 Risk Detection
    </h3>

    <p>
    Future tools can flag missing documents,
    inconsistent information and potential warning signs.
    </p>

    </div>
    """, unsafe_allow_html=True)


with s3:

    st.markdown("""
    <div class="info-card">

    <h3>
    👨‍⚖️ Professional Review
    </h3>

    <p>
    Users can request qualified legal and property
    professionals for detailed due diligence.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# IMPORTANT DISCLAIMER
# ============================================================

st.warning(
    "⚠️ This page is a document organisation and preliminary "
    "verification interface. It does not provide legal advice "
    "or guarantee title, ownership or regulatory compliance. "
    "Property buyers should obtain independent professional "
    "legal and technical due diligence before completing a transaction."
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="security-card">

<h2>
🌐 FirstChoice Property Hub
</h2>

<p>
Building a more transparent, secure and intelligent
real-estate experience.
</p>

</div>
""", unsafe_allow_html=True)
