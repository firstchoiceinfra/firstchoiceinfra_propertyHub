import streamlit as st
from datetime import date

# ============================================================
# PAGE 31 — SMART PROPERTY DOCUMENT VAULT
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Document Vault | FirstChoice Property Hub",
    page_icon="📁",
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

.hero {
    padding: 52px;
    border-radius: 36px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 24px 75px
    rgba(37,99,235,0.32);

    margin-bottom: 32px;
}

.hero h1 {
    font-size: 46px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.8;
}

.section {
    margin-top: 32px;
    margin-bottom: 22px;

    padding: 30px 34px;

    border-radius: 28px;

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
    0 14px 40px
    rgba(79,70,229,0.22);
}

.section h2 {
    margin: 0;
    font-size: 29px;
    font-weight: 900;
}

.card {
    padding: 28px;
    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    margin-bottom: 20px;
}

.ai-card {
    padding: 32px;
    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #C026D3
    );

    box-shadow:
    0 18px 55px
    rgba(124,58,237,0.25);
}

.safe-card {
    padding: 35px;
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
    0 20px 60px
    rgba(5,150,105,0.25);
}

.warning-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #B45309,
        #F59E0B,
        #F97316
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
📁 Smart Property Document Vault
</h1>

<p>
Securely organize, track and manage all important property
documents in one centralized digital workspace.
</p>

<p>
📄 Upload • 🔍 Verify • 🏷️ Categorize • 🔐 Secure • 🤝 Share
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🔐 Your Property Documents — Organized in One Place
</h2>

<p>
Keep sale deeds, title documents, tax receipts, approvals,
RERA certificates, loan papers and other important documents
organized by property.
</p>

<p>
The production version can connect this vault with the
Legal Verification Center and Deal Room.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Property
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    property_name = st.text_input(
        "🏠 Property Name",
        value="My Property"
    )


with c2:

    property_id = st.text_input(
        "🆔 Property ID",
        value="FC-PROP-001"
    )


with c3:

    owner_name = st.text_input(
        "👤 Owner / Buyer Name"
    )


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

st.markdown("""
<div class="section">

<h2>
📤 Upload Property Document
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    document_category = st.selectbox(
        "📂 Document Category",
        [
            "Ownership & Title",
            "Government Records",
            "RERA & Approvals",
            "Tax & Financial",
            "Loan & Mortgage",
            "Sale & Purchase",
            "Legal Documents",
            "Construction Documents",
            "Identity Documents",
            "Other"
        ]
    )


with c2:

    document_name = st.text_input(
        "📄 Document Name",
        value="Property Document"
    )


uploaded_file = st.file_uploader(
    "📤 Choose Document",
    type=[
        "pdf",
        "jpg",
        "jpeg",
        "png",
        "doc",
        "docx"
    ]
)


c1, c2, c3 = st.columns(3)


with c1:

    document_status = st.selectbox(
        "🔍 Verification Status",
        [
            "Pending",
            "Under Review",
            "Verified",
            "Requires Attention"
        ]
    )


with c2:

    expiry_date = st.date_input(
        "📅 Expiry / Review Date",
        value=date.today()
    )


with c3:

    confidential = st.checkbox(
        "🔐 Mark as Confidential"
    )


if st.button(
    "📤 ADD DOCUMENT TO VAULT",
    use_container_width=True
):

    if uploaded_file:

        st.success(
            f"✅ {document_name} added to Property Document Vault."
        )

    else:

        st.warning(
            "⚠️ Please select a document first."
        )


# ============================================================
# DOCUMENT CATEGORIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
📚 Document Categories
</h2>

</div>
""", unsafe_allow_html=True)


categories = [

    ("📜", "Ownership & Title", "Sale Deed, Title Deed, Chain Documents"),

    ("🏛️", "Government Records", "Mutation, Khata, Land Records"),

    ("🏗️", "RERA & Approvals", "RERA, Layout, Building Permissions"),

    ("💰", "Tax & Financial", "Tax Receipts, Dues, Payment Records"),

    ("🏦", "Loan & Mortgage", "Loan Sanction, Mortgage, NOC"),

    ("🤝", "Sale & Purchase", "Agreement, Token, Receipts"),

    ("⚖️", "Legal Documents", "Legal Opinions, Notices, Court Records"),

    ("🏠", "Construction", "Completion, Occupancy, Architect Documents")

]


for icon, title, description in categories:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        {icon} {title}
        </h3>

        <p>
        {description}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DOCUMENT STATUS DASHBOARD
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Document Verification Dashboard
</h2>

</div>
""", unsafe_allow_html=True)


d1, d2, d3, d4 = st.columns(4)


with d1:

    st.metric(
        "📁 Total Documents",
        "0"
    )


with d2:

    st.metric(
        "✅ Verified",
        "0"
    )


with d3:

    st.metric(
        "⏳ Pending",
        "0"
    )


with d4:

    st.metric(
        "⚠️ Attention",
        "0"
    )


# ============================================================
# SEARCH DOCUMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔍 Search Your Documents
</h2>

</div>
""", unsafe_allow_html=True)


search_query = st.text_input(
    "Search by document name, category or property ID"
)


filter_status = st.selectbox(
    "Filter by Status",
    [
        "All",
        "Pending",
        "Under Review",
        "Verified",
        "Requires Attention"
    ]
)


if search_query:

    st.info(
        f"🔍 Searching documents for: {search_query}"
    )


# ============================================================
# SHARING CENTER
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤝 Secure Document Sharing
</h2>

</div>
""", unsafe_allow_html=True)


s1, s2 = st.columns(2)


with s1:

    share_with = st.selectbox(
        "👤 Share With",
        [
            "Property Buyer",
            "Property Owner",
            "Agent",
            "Builder / Developer",
            "Lawyer",
            "Bank / Lender",
            "Chartered Accountant",
            "Other"
        ]
    )


with s2:

    permission = st.selectbox(
        "🔐 Permission",
        [
            "View Only",
            "View & Download",
            "Edit / Replace"
        ]
    )


if st.button(
    "🔗 CREATE SECURE SHARING LINK",
    use_container_width=True
):

    st.success(
        f"✅ Secure sharing permission created for {share_with}."
    )


# ============================================================
# SECURITY
# ============================================================

st.markdown("""
<div class="safe-card">

<h2>
🔐 Document Security
</h2>

<p>
Production version में documents को encrypted storage,
role-based access control और audit logs के साथ secure किया जा सकता है।
</p>

<p>
हर document के लिए यह track किया जा सकता है कि
किस user ने कब document upload, view, download या share किया।
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FUTURE AI FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Future AI Document Intelligence
</h2>

<p>
Production version में आगे:
</p>

<p>
🧠 AI Document Reading
&nbsp; • &nbsp;
📄 OCR Text Extraction
&nbsp; • &nbsp;
🔍 Duplicate Detection
&nbsp; • &nbsp;
⚠️ Missing Document Detection
&nbsp; • &nbsp;
📝 Automatic Document Summary
&nbsp; • &nbsp;
🔎 Document Mismatch Detection
&nbsp; • &nbsp;
📅 Expiry Alerts
&nbsp; • &nbsp;
🔐 Digital Audit Trail
</p>

<p>
AI automatically important dates, names, survey numbers,
plot numbers and other relevant information identify कर सकता है।
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NEXT ACTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Next Step
</h2>

</div>
""", unsafe_allow_html=True)


next_action = st.selectbox(
    "Choose your next action",
    [
        "⚖️ Open Legal Verification",
        "🤝 Open Property Deal Room",
        "👨‍⚖️ Share With Lawyer",
        "🏦 Share With Lender",
        "📤 Upload More Documents",
        "🏡 Return to Property Dashboard"
    ]
)


if st.button(
    "🚀 CONTINUE",
    use_container_width=True
):

    st.success(
        f"✅ Selected action: {next_action}"
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Notice
</h2>

<p>
This page is a digital document organization and tracking
interface. Uploading a document does not mean that the document
has been legally verified.
</p>

<p>
Always verify original documents with qualified legal and
financial professionals before completing a property transaction.
</p>

</div>
""", unsafe_allow_html=True)
