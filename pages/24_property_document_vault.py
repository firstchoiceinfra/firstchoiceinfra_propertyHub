import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 24 — SMART PROPERTY DOCUMENT VAULT
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Document Vault | FirstChoice Property Hub",
    page_icon="🗂️",
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

.success-card {
    padding: 32px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );
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
🗂️ Smart Property Document Vault
</h1>

<p>
A secure digital transaction workspace to organise,
upload and track important property documents.
</p>

<p>
📁 Upload • 🏷️ Categorise • 🔍 Track • 📊 Status • 🤝 Share
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🔐 Digital Property Transaction Room
</h2>

<p>
Keep important property transaction documents organised
in one central workspace.
</p>

<p>
Buyers, sellers, builders and authorised professionals
can manage document workflows from property evaluation
through transaction completion.
</p>

<p>
The current page provides document organisation and tracking.
Secure cloud storage, encryption and role-based access can
be connected to the production backend later.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY PROFILE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Transaction Property Profile
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_name = st.text_input(
        "🏠 Property Name",
        value="My Property"
    )


with c2:

    property_id = st.text_input(
        "🆔 Property / Transaction ID",
        value="FC-TRANS-001"
    )


c3, c4 = st.columns(2)


with c3:

    owner_name = st.text_input(
        "👤 Owner / Seller Name"
    )


with c4:

    buyer_name = st.text_input(
        "🧑 Buyer Name"
    )


# ============================================================
# TRANSACTION STAGE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔄 Transaction Workflow Stage
</h2>

</div>
""", unsafe_allow_html=True)


transaction_stage = st.selectbox(
    "Current Transaction Stage",
    [
        "Property Shortlisted",
        "Offer Submitted",
        "Negotiation",
        "Legal Verification",
        "Token Paid",
        "Loan Processing",
        "Agreement Preparation",
        "Registration",
        "Transaction Completed"
    ]
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


document_category = st.selectbox(
    "📂 Document Category",
    [
        "Identity Document",
        "Ownership Document",
        "Property Document",
        "Legal Document",
        "Loan Document",
        "Payment Document",
        "Agreement",
        "Registration Document",
        "Other"
    ]
)


document_name = st.text_input(
    "📄 Document Name",
    placeholder="Example: Sale Agreement"
)


uploaded_file = st.file_uploader(
    "📤 Choose Document",
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "doc",
        "docx"
    ]
)


document_status = st.selectbox(
    "📊 Document Status",
    [
        "Uploaded",
        "Under Review",
        "Verified",
        "Needs Correction",
        "Rejected"
    ]
)


document_notes = st.text_area(
    "📝 Document Notes",
    placeholder="Add notes about this document..."
)


# ============================================================
# SESSION DOCUMENT STORAGE
# ============================================================

if "property_documents" not in st.session_state:

    st.session_state.property_documents = []


# ============================================================
# ADD DOCUMENT
# ============================================================

if st.button(
    "➕ ADD DOCUMENT TO VAULT",
    use_container_width=True
):

    if not document_name:

        st.warning(
            "⚠️ Please enter a document name."
        )

    elif uploaded_file is None:

        st.warning(
            "⚠️ Please upload a document."
        )

    else:

        document_record = {

            "Document":
            document_name,

            "Category":
            document_category,

            "File":
            uploaded_file.name,

            "Status":
            document_status,

            "Stage":
            transaction_stage,

            "Added On":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),

            "Notes":
            document_notes

        }

        st.session_state.property_documents.append(
            document_record
        )

        st.success(
            f"✅ {document_name} added to the Document Vault."
        )


# ============================================================
# DOCUMENT VAULT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🗃️ My Property Document Vault
</h2>

</div>
""", unsafe_allow_html=True)


documents = st.session_state.property_documents


if documents:

    st.dataframe(
        documents,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "📂 No documents added yet. Upload your first property document above."
    )


# ============================================================
# DOCUMENT STATISTICS
# ============================================================

total_docs = len(
    documents
)


verified_docs = len(
    [
        d
        for d in documents
        if d["Status"] == "Verified"
    ]
)


review_docs = len(
    [
        d
        for d in documents
        if d["Status"] == "Under Review"
    ]
)


correction_docs = len(
    [
        d
        for d in documents
        if d["Status"] == "Needs Correction"
    ]
)


st.markdown("""
<div class="section">

<h2>
📊 Document Vault Analytics
</h2>

</div>
""", unsafe_allow_html=True)


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.metric(
        "📁 Total Documents",
        total_docs
    )


with a2:

    st.metric(
        "✅ Verified",
        verified_docs
    )


with a3:

    st.metric(
        "🔍 Under Review",
        review_docs
    )


with a4:

    st.metric(
        "⚠️ Needs Correction",
        correction_docs
    )


# ============================================================
# DOCUMENT PROGRESS
# ============================================================

if total_docs > 0:

    progress = (
        verified_docs
        /
        total_docs
    )

else:

    progress = 0


st.markdown("""
<div class="section">

<h2>
📈 Transaction Document Readiness
</h2>

</div>
""", unsafe_allow_html=True)


st.progress(
    progress
)


st.write(
    f"Verified Document Progress: {progress * 100:.0f}%"
)


# ============================================================
# DOCUMENT SHARING
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤝 Controlled Document Sharing
</h2>

</div>
""", unsafe_allow_html=True)


share_role = st.multiselect(
    "👥 Share Document Access With",
    [
        "Buyer",
        "Seller",
        "Builder",
        "Agent",
        "Legal Consultant",
        "Loan Consultant",
        "Admin"
    ]
)


share_expiry = st.selectbox(
    "⏳ Access Duration",
    [
        "24 Hours",
        "7 Days",
        "30 Days",
        "Until Transaction Completed"
    ]
)


if st.button(
    "🔗 CREATE SECURE SHARING REQUEST",
    use_container_width=True
):

    if not share_role:

        st.warning(
            "⚠️ Please select at least one participant."
        )

    else:

        st.success(
            "✅ Sharing request prepared for: "
            + ", ".join(share_role)
        )

        st.info(
            f"Access duration: {share_expiry}"
        )


# ============================================================
# SMART DOCUMENT ALERTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔔 Smart Document Alerts
</h2>

</div>
""", unsafe_allow_html=True)


alert1, alert2, alert3 = st.columns(3)


with alert1:

    st.markdown("""
    <div class="card">

    <h3>
    📄 Missing Documents
    </h3>

    <p>
    Identify documents that have not yet been added
    to the transaction workspace.
    </p>

    </div>
    """, unsafe_allow_html=True)


with alert2:

    st.markdown("""
    <div class="card">

    <h3>
    ⚠️ Correction Required
    </h3>

    <p>
    Quickly identify documents that require
    correction or resubmission.
    </p>

    </div>
    """, unsafe_allow_html=True)


with alert3:

    st.markdown("""
    <div class="card">

    <h3>
    🔍 Review Pending
    </h3>

    <p>
    Track documents waiting for legal or
    professional review.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# TRANSACTION SUMMARY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Transaction Document Summary
</h2>

</div>
""", unsafe_allow_html=True)


summary = {

    "Property":
    property_name,

    "Transaction ID":
    property_id,

    "Buyer":
    buyer_name,

    "Seller":
    owner_name,

    "Current Stage":
    transaction_stage,

    "Total Documents":
    total_docs,

    "Verified":
    verified_docs

}


st.json(
    summary
)


# ============================================================
# FUTURE AI DOCUMENT INTELLIGENCE
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Document Intelligence
</h2>

<p>
The production version can add advanced document intelligence.
</p>

<p>
🤖 OCR Document Reading
&nbsp; • &nbsp;
🔍 AI Document Classification
&nbsp; • &nbsp;
📑 Duplicate Detection
&nbsp; • &nbsp;
⚠️ Missing Document Alerts
&nbsp; • &nbsp;
🔐 Encryption
&nbsp; • &nbsp;
👥 Role-Based Access
&nbsp; • &nbsp;
🧾 Digital Signatures
</p>

<p>
The platform can eventually create a complete digital
transaction room where every authorised participant
can collaborate securely.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Security & Legal Notice
</h2>

<p>
This demo page provides document organisation and workflow
features. It does not currently provide guaranteed secure
cloud storage, encryption, legal certification or digital
signature services.
</p>

<p>
For production deployment, documents should be stored using
secure backend storage with authentication, authorisation,
encryption and audit logging.
</p>

</div>
""", unsafe_allow_html=True)
