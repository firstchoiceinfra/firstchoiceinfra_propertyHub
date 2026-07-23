import streamlit as st
from datetime import datetime, date

# ============================================================
# PAGE 24 — SMART PROPERTY DOCUMENT VAULT
# MERGED VERSION:
# PAGE 15 + PAGE 24 + PAGE 31
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

/* ============================================================
   HERO
   ============================================================ */

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

/* ============================================================
   SECTION
   ============================================================ */

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

/* ============================================================
   CARD
   ============================================================ */

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

/* ============================================================
   AI CARD
   ============================================================ */

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

    margin-bottom: 25px;
}

/* ============================================================
   SUCCESS CARD
   ============================================================ */

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

    box-shadow:
    0 18px 50px
    rgba(5,150,105,0.25);

    margin-bottom: 25px;
}

/* ============================================================
   WARNING CARD
   ============================================================ */

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

    box-shadow:
    0 18px 50px
    rgba(245,158,11,0.22);

    margin-top: 25px;
}

/* ============================================================
   INFO CARD
   ============================================================ */

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

    min-height: 180px;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.05);

    margin-bottom: 20px;
}

/* ============================================================
   DOCUMENT CARD
   ============================================================ */

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
🗂️ Smart Property Document Vault
</h1>

<p>
A secure digital property transaction workspace to organise,
upload, verify and track important property documents.
</p>

<p>
📁 Upload • 🏷️ Categorise • 🔍 Verify • 📊 Track • 🤝 Share
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
The platform combines document vault, preliminary
verification checklist and transaction workflow management.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY PROFILE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property & Transaction Profile
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


property_location = st.text_input(
    "📍 Property Location",
    placeholder="Enter complete property location"
)


# ============================================================
# TRANSACTION WORKFLOW
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
# PRELIMINARY DOCUMENT CHECKLIST
# PAGE 15 FEATURE
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Preliminary Document Verification Checklist
</h2>

<p>
Select the documents available for this property.
</p>

</div>
""", unsafe_allow_html=True)


document_checklist = {

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


for title, description in document_checklist.items():

    checked = st.checkbox(
        f"📄 {title}",
        key=f"verification_doc_{title}"
    )

    if checked:

        selected_documents.append(
            title
        )


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

st.markdown("""
<div class="section">

<h2>
📤 Upload Property Documents
</h2>

<p>
Upload one or multiple documents for organised record keeping
and preliminary verification.
</p>

</div>
""", unsafe_allow_html=True)


uploaded_files = st.file_uploader(
    "📤 Upload PDF or Image Documents",
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "doc",
        "docx"
    ],
    accept_multiple_files=True
)


if uploaded_files:

    st.success(
        f"📁 {len(uploaded_files)} document(s) selected for upload."
    )


# ============================================================
# DOCUMENT VAULT DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🗃️ Add Document To Property Vault
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


single_uploaded_file = st.file_uploader(
    "📤 Choose Document For Vault",
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "doc",
        "docx"
    ],
    key="vault_file_uploader"
)


document_status = st.selectbox(
    "📊 Document Status",
    [
        "Pending",
        "Uploaded",
        "Under Review",
        "Verified",
        "Needs Correction",
        "Requires Attention",
        "Rejected"
    ]
)


expiry_date = st.date_input(
    "📅 Expiry / Review Date",
    value=date.today()
)


confidential = st.checkbox(
    "🔐 Mark This Document As Confidential"
)


document_notes = st.text_area(
    "📝 Document Notes",
    placeholder="Add notes about this document..."
)


# ============================================================
# SESSION STORAGE
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

    elif single_uploaded_file is None:

        st.warning(
            "⚠️ Please select a document first."
        )

    else:

        document_record = {

            "Document":
            document_name,

            "Category":
            document_category,

            "File":
            single_uploaded_file.name,

            "Status":
            document_status,

            "Expiry / Review":
            expiry_date.strftime(
                "%d-%m-%Y"
            ),

            "Confidential":
            "Yes" if confidential else "No",

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
            f"✅ {document_name} added to the Property Document Vault."
        )


# ============================================================
# DOCUMENT VAULT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🗂️ My Property Document Vault
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
        if d["Status"]
        in [
            "Needs Correction",
            "Requires Attention"
        ]
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
        "⚠️ Attention Required",
        correction_docs
    )


# ============================================================
# DOCUMENT CHECKLIST ANALYTICS
# ============================================================

total_checklist = len(
    document_checklist
)


available_checklist = len(
    selected_documents
)


missing_checklist = (

    total_checklist
    -
    available_checklist

)


if total_checklist > 0:

    checklist_progress = (

        available_checklist
        /
        total_checklist

    )

else:

    checklist_progress = 0


st.markdown("""
<div class="section">

<h2>
📈 Property Document Readiness
</h2>

</div>
""", unsafe_allow_html=True)


d1, d2, d3 = st.columns(3)


with d1:

    st.metric(
        "📄 Total Checklist",
        total_checklist
    )


with d2:

    st.metric(
        "✅ Available",
        available_checklist
    )


with d3:

    st.metric(
        "⚠️ Missing",
        missing_checklist
    )


st.progress(
    checklist_progress
)


st.caption(
    f"Document availability: "
    f"{checklist_progress * 100:.0f}%"
)


# ============================================================
# VERIFICATION REQUEST
# PAGE 15 FEATURE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔍 Request Property Verification
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
    "📝 Verification Questions / Concerns",
    placeholder=
    "Add any questions or concerns about this property..."
)


if st.button(
    "🚀 SUBMIT VERIFICATION REQUEST",
    use_container_width=True
):

    if not property_location:

        st.error(
            "⚠️ Please enter the property location."
        )

    elif not owner_name:

        st.error(
            "⚠️ Please enter the owner or seller name."
        )

    else:

        st.success(
            "🎉 Property verification request submitted successfully."
        )

        st.info(
            f"Verification Type: {verification_type}"
        )

        st.info(
            f"Priority: {priority}"
        )

        st.info(
            "Professional verification should be performed by qualified "
            "legal or property professionals where required."
        )


# ============================================================
# DOCUMENT STATUS LIST
# ============================================================

st.markdown("""
<div class="section">

<h2>
📑 Preliminary Document Status
</h2>

</div>
""", unsafe_allow_html=True)


for title, description in document_checklist.items():

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
# CONTROLLED DOCUMENT SHARING
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
            +
            ", ".join(share_role)
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
    Identify important documents that have not yet
    been added to the transaction workspace.
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

    "Property ID":
    property_id,

    "Location":
    property_location,

    "Buyer":
    buyer_name,

    "Seller":
    owner_name,

    "Current Stage":
    transaction_stage,

    "Verification Type":
    verification_type,

    "Priority":
    priority,

    "Total Vault Documents":
    total_docs,

    "Verified Vault Documents":
    verified_docs,

    "Checklist Documents Available":
    available_checklist,

    "Checklist Documents Missing":
    missing_checklist

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
The production version can add advanced document intelligence
and property risk analysis.
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
🚨 Risk Detection
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
# SECURITY & LEGAL DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Security & Legal Notice
</h2>

<p>
This page provides document organisation, checklist and
preliminary verification workflow features.
</p>

<p>
It does not currently provide guaranteed secure cloud storage,
encryption, legal certification, title certification or
digital signature services.
</p>

<p>
For production deployment, documents should be stored using
secure backend storage with authentication, authorisation,
encryption and audit logging.
</p>

<p>
Property buyers should obtain independent professional legal
and technical due diligence before completing a transaction.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="success-card">

<h2>
🌐 FirstChoice Property Hub
</h2>

<p>
Building a more transparent, secure and intelligent
real-estate experience.
</p>

</div>
""", unsafe_allow_html=True)
