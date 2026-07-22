import streamlit as st
from datetime import date

# ============================================================
# PAGE 22 — AI PROPERTY LEGAL & DUE DILIGENCE CENTRE
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Legal Due Diligence | FirstChoice Property Hub",
    page_icon="⚖️",
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
    padding: 52px;
    border-radius: 36px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1E3A8A,
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

/* SECTION */

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

/* CARD */

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

    margin-bottom: 22px;
}

/* AI CARD */

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

/* SUCCESS */

.success-card {
    padding: 35px;
    border-radius: 30px;

    color: white;
    text-align: center;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 20px 55px
    rgba(5,150,105,0.25);
}

/* WARNING */

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
}

/* INFO */

.info-card {
    padding: 28px;
    border-radius: 26px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0369A1,
        #0284C7,
        #06B6D4
    );

    box-shadow:
    0 15px 45px
    rgba(2,132,199,0.22);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
⚖️ Property Legal & Due-Diligence Centre
</h1>

<p>
Organise your property documents, verification checklist
and legal due-diligence process in one professional dashboard.
</p>

<p>
📄 Documents • 🔍 Verification • 🏛️ Ownership • 📑 Approvals • ⚖️ Legal Review
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Verification Assistant
</h2>

<p>
Before purchasing a property, buyers should verify ownership,
title, approvals, taxes, encumbrances and other relevant documents.
</p>

<p>
This dashboard helps organise the process and track document
status. It does not replace professional legal advice or
official verification by a qualified lawyer or authority.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY INFORMATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property Verification Profile
</h2>

<p>
Create a verification profile for the property you are evaluating.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_name = st.text_input(
        "🏷️ Property Name",
        value="My Property"
    )


with c2:

    property_location = st.text_input(
        "📍 Property Location",
        value=""
    )


c3, c4 = st.columns(2)


with c3:

    property_type = st.selectbox(
        "🏡 Property Type",
        [
            "Apartment",
            "Villa",
            "Independent House",
            "Residential Plot",
            "Commercial Property",
            "Agricultural Land"
        ]
    )


with c4:

    ownership_type = st.selectbox(
        "👤 Ownership Type",
        [
            "Individual",
            "Joint Ownership",
            "Company",
            "Trust",
            "Society",
            "Developer / Builder"
        ]
    )


# ============================================================
# DOCUMENT CHECKLIST
# ============================================================

st.markdown("""
<div class="section">

<h2>
📄 Property Document Verification Checklist
</h2>

<p>
Select documents that have been collected and verified.
</p>

</div>
""", unsafe_allow_html=True)


documents = [

    "📜 Sale Deed / Conveyance Deed",

    "🏛️ Title Documents",

    "🔍 Encumbrance Certificate",

    "🏠 Previous Sale Agreement",

    "🧾 Property Tax Receipts",

    "📐 Approved Building Plan",

    "🏗️ Building Permission",

    "🏢 Occupancy Certificate",

    "🏡 Completion Certificate",

    "📋 Mutation / Property Record",

    "🗺️ Property Survey / Site Plan",

    "💳 No Dues Certificate",

    "🏦 Bank / Mortgage Clearance",

    "📄 Society NOC",

    "🪪 Seller Identity Documents"

]


verified_documents = []


for document in documents:

    if st.checkbox(
        document,
        key=f"doc_{document}"
    ):

        verified_documents.append(
            document
        )


# ============================================================
# VERIFICATION SCORE
# ============================================================

total_documents = len(
    documents
)


verified_count = len(
    verified_documents
)


verification_percentage = (

    verified_count
    /
    total_documents
    *
    100

)


st.markdown("""
<div class="section">

<h2>
📊 Document Verification Progress
</h2>

</div>
""", unsafe_allow_html=True)


st.progress(
    verification_percentage / 100
)


st.write(
    f"### {verified_count} / {total_documents} documents marked as collected"
)


if verification_percentage >= 80:

    st.markdown(
        f"""
        <div class="success-card">

        <h2>
        🟢 Strong Document Readiness
        </h2>

        <p>
        {verification_percentage:.0f}% of the checklist
        has been marked as completed.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

elif verification_percentage >= 50:

    st.info(
        f"🟡 Moderate Document Readiness — "
        f"{verification_percentage:.0f}% completed."
    )

else:

    st.warning(
        f"🔴 Document Verification Incomplete — "
        f"Only {verification_percentage:.0f}% completed."
    )


# ============================================================
# SELLER VERIFICATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 Seller & Ownership Verification
</h2>

</div>
""", unsafe_allow_html=True)


s1, s2 = st.columns(2)


with s1:

    seller_name = st.text_input(
        "👤 Seller / Owner Name"
    )


with s2:

    seller_mobile = st.text_input(
        "📱 Seller Contact Number"
    )


s3, s4 = st.columns(2)


with s3:

    seller_id_verified = st.checkbox(
        "🪪 Seller Identity Verified"
    )


with s4:

    ownership_verified = st.checkbox(
        "🏠 Ownership Details Verified"
    )


# ============================================================
# LEGAL REVIEW
# ============================================================

st.markdown("""
<div class="section">

<h2>
⚖️ Legal Review Status
</h2>

</div>
""", unsafe_allow_html=True)


legal_status = st.selectbox(
    "Select Current Legal Review Status",
    [
        "Not Started",
        "Documents Collected",
        "Under Legal Review",
        "Additional Documents Required",
        "Legal Review Completed"
    ]
)


lawyer_name = st.text_input(
    "⚖️ Lawyer / Legal Consultant Name"
)


review_date = st.date_input(
    "📅 Legal Review Date",
    value=date.today()
)


legal_notes = st.text_area(
    "📝 Legal Review Notes",
    placeholder="Enter important observations or pending items..."
)


# ============================================================
# PROPERTY RISK INDICATORS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚦 Property Risk Indicators
</h2>

</div>
""", unsafe_allow_html=True)


risk1, risk2, risk3 = st.columns(3)


with risk1:

    title_risk = st.selectbox(
        "📜 Title Status",
        [
            "Not Checked",
            "Clear",
            "Needs Review",
            "Potential Issue"
        ]
    )


with risk2:

    encumbrance_risk = st.selectbox(
        "🔍 Encumbrance Status",
        [
            "Not Checked",
            "Clear",
            "Needs Review",
            "Potential Issue"
        ]
    )


with risk3:

    approval_risk = st.selectbox(
        "🏛️ Approval Status",
        [
            "Not Checked",
            "Approved",
            "Needs Review",
            "Potential Issue"
        ]
    )


# ============================================================
# RISK SCORE
# ============================================================

risk_score = 0


if title_risk == "Potential Issue":

    risk_score += 40

elif title_risk == "Needs Review":

    risk_score += 20


if encumbrance_risk == "Potential Issue":

    risk_score += 35

elif encumbrance_risk == "Needs Review":

    risk_score += 20


if approval_risk == "Potential Issue":

    risk_score += 25

elif approval_risk == "Needs Review":

    risk_score += 15


st.markdown("""
<div class="section">

<h2>
🚦 Preliminary Risk Overview
</h2>

</div>
""", unsafe_allow_html=True)


if risk_score == 0:

    st.markdown("""
    <div class="success-card">

    <h2>
    🟢 No Risk Flags Entered
    </h2>

    <p>
    No potential risk has been manually flagged in the dashboard.
    </p>

    </div>
    """, unsafe_allow_html=True)

elif risk_score <= 30:

    st.info(
        "🟡 Some items require additional verification."
    )

elif risk_score <= 60:

    st.warning(
        "🟠 Multiple items require professional review."
    )

else:

    st.error(
        "🔴 Significant potential risk indicators entered. "
        "Professional legal advice is strongly recommended."
    )


# ============================================================
# DUE DILIGENCE REPORT
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Due-Diligence Summary
</h2>

</div>
""", unsafe_allow_html=True)


summary_data = {

    "Property": [
        property_name
    ],

    "Location": [
        property_location
    ],

    "Property Type": [
        property_type
    ],

    "Ownership": [
        ownership_type
    ],

    "Documents Completed": [
        f"{verified_count}/{total_documents}"
    ],

    "Legal Status": [
        legal_status
    ],

    "Risk Score": [
        risk_score
    ],

    "Review Date": [
        str(review_date)
    ]

}


st.dataframe(
    summary_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# SAVE REPORT
# ============================================================

if st.button(
    "💾 SAVE DUE-DILIGENCE RECORD",
    use_container_width=True
):

    st.success(
        "✅ Due-diligence record created for "
        f"{property_name}."
    )


# ============================================================
# AI FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Legal Intelligence
</h2>

<p>
The future version of Property Hub can provide advanced
document intelligence features.
</p>

<p>
🤖 AI Document Reading
&nbsp; • &nbsp;
🔍 OCR Verification
&nbsp; • &nbsp;
📑 Document Comparison
&nbsp; • &nbsp;
⚠️ Risk Flag Detection
&nbsp; • &nbsp;
🔐 Secure Document Vault
&nbsp; • &nbsp;
⚖️ Lawyer Collaboration
</p>

<p>
Users could upload property documents and receive a structured
verification checklist, missing-document alerts and a
professional review workflow.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Legal Disclaimer
</h2>

<p>
This dashboard is designed only for document organisation
and preliminary due-diligence tracking.
</p>

<p>
It does not provide legal advice, certify ownership,
guarantee title clearance or replace verification by a
qualified lawyer, government authority or other competent
professional.
</p>

</div>
""", unsafe_allow_html=True)
