import streamlit as st
from datetime import date

# ============================================================
# PAGE 30 — SMART LEGAL DUE DILIGENCE & PROPERTY VERIFICATION
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Legal Verification | FirstChoice Property Hub",
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

.danger-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #991B1B,
        #DC2626,
        #EF4444
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
⚖️ Smart Legal Due Diligence Center
</h1>

<p>
Verify important property information before moving forward
with a purchase or investment decision.
</p>

<p>
📜 Title • 👤 Ownership • 🏛️ RERA • 🗺️ Approvals • 💰 Tax • 🔒 Encumbrance
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🛡️ Property Verification Command Center
</h2>

<p>
Track the legal verification journey of a property from
initial document collection to final professional review.
</p>

<p>
Every verification item can be marked as Pending, Under Review,
Verified or Requires Attention.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY INFORMATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property Information
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    property_name = st.text_input(
        "🏠 Property / Project Name",
        value="My Property"
    )


with c2:

    property_location = st.text_input(
        "📍 Property Location"
    )


with c3:

    property_type = st.selectbox(
        "🏘️ Property Type",
        [
            "Residential Plot",
            "Apartment",
            "Villa",
            "Commercial Property",
            "Agricultural Land",
            "Industrial Property"
        ]
    )


# ============================================================
# OWNER INFORMATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 Ownership & Seller Verification
</h2>

</div>
""", unsafe_allow_html=True)


o1, o2, o3 = st.columns(3)


with o1:

    owner_name = st.text_input(
        "👤 Seller / Owner Name"
    )


with o2:

    ownership_type = st.selectbox(
        "📜 Ownership Type",
        [
            "Individual",
            "Joint Ownership",
            "Company",
            "Partnership",
            "Trust",
            "Other"
        ]
    )


with o3:

    ownership_status = st.selectbox(
        "🔍 Ownership Verification",
        [
            "Pending",
            "Under Review",
            "Verified",
            "Requires Attention"
        ]
    )


# ============================================================
# DOCUMENT VERIFICATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
📂 Legal Document Verification
</h2>

</div>
""", unsafe_allow_html=True)


documents = [

    "Sale Deed / Title Deed",

    "Previous Chain Documents",

    "Encumbrance Certificate",

    "Property Tax Receipt",

    "Mutation / Khata",

    "Approved Layout Plan",

    "Building Permission",

    "Completion / Occupancy Certificate",

    "RERA Registration",

    "NOC / Other Approvals"

]


document_status = {}


for i, document in enumerate(documents):

    c1, c2, c3 = st.columns([2, 1, 1])


    with c1:

        st.write(
            f"📄 **{document}**"
        )


    with c2:

        status = st.selectbox(
            "Status",
            [
                "Pending",
                "Under Review",
                "Verified",
                "Requires Attention"
            ],
            key=f"doc_status_{i}"
        )


    with c3:

        received = st.checkbox(
            "Document Received",
            key=f"doc_received_{i}"
        )


    document_status[document] = {

        "status":
        status,

        "received":
        received

    }


# ============================================================
# RERA VERIFICATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏛️ RERA & Government Registration
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    rera_required = st.selectbox(
        "🏛️ RERA Applicable?",
        [
            "Yes",
            "No",
            "Not Sure"
        ]
    )


with r2:

    rera_number = st.text_input(
        "🔢 RERA Registration Number"
    )


with r3:

    rera_status = st.selectbox(
        "🔍 RERA Verification Status",
        [
            "Not Checked",
            "Under Verification",
            "Verified",
            "Requires Attention"
        ]
    )


# ============================================================
# ENCUMBRANCE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔒 Encumbrance & Liability Check
</h2>

</div>
""", unsafe_allow_html=True)


e1, e2, e3 = st.columns(3)


with e1:

    encumbrance_status = st.selectbox(
        "🔒 Encumbrance Status",
        [
            "Not Checked",
            "Clear",
            "Under Review",
            "Issue Found"
        ]
    )


with e2:

    mortgage_status = st.selectbox(
        "🏦 Existing Mortgage",
        [
            "None Known",
            "Mortgage Exists",
            "Under Verification"
        ]
    )


with e3:

    litigation_status = st.selectbox(
        "⚖️ Litigation Check",
        [
            "Not Checked",
            "No Known Litigation",
            "Under Review",
            "Potential Issue"
        ]
    )


# ============================================================
# TAX & DUES
# ============================================================

st.markdown("""
<div class="section">

<h2>
💰 Tax & Outstanding Dues
</h2>

</div>
""", unsafe_allow_html=True)


t1, t2, t3 = st.columns(3)


with t1:

    property_tax_status = st.selectbox(
        "🏛️ Property Tax",
        [
            "Paid",
            "Pending",
            "Under Verification"
        ]
    )


with t2:

    outstanding_dues = st.number_input(
        "💰 Known Outstanding Dues (₹)",
        min_value=0,
        value=0,
        step=1000
    )


with t3:

    maintenance_dues = st.number_input(
        "🔧 Maintenance Dues (₹)",
        min_value=0,
        value=0,
        step=1000
    )


# ============================================================
# VERIFICATION TEAM
# ============================================================

st.markdown("""
<div class="section">

<h2>
👨‍⚖️ Professional Verification
</h2>

</div>
""", unsafe_allow_html=True)


v1, v2, v3 = st.columns(3)


with v1:

    assigned_professional = st.text_input(
        "👨‍⚖️ Assigned Lawyer / Professional"
    )


with v2:

    verification_date = st.date_input(
        "📅 Verification Target Date",
        value=date.today()
    )


with v3:

    professional_status = st.selectbox(
        "📋 Professional Review Status",
        [
            "Not Started",
            "In Progress",
            "Completed",
            "Requires Additional Documents"
        ]
    )


# ============================================================
# CALCULATE VERIFICATION SCORE
# ============================================================

verified_documents = sum(

    1
    for item in document_status.values()

    if item["status"] == "Verified"

)


attention_documents = sum(

    1
    for item in document_status.values()

    if item["status"] == "Requires Attention"

)


total_documents = len(
    documents
)


document_score = (

    verified_documents
    /
    total_documents
    *
    100

)


# Additional checks

extra_score = 0


if ownership_status == "Verified":

    extra_score += 15


if rera_status == "Verified" or rera_required == "No":

    extra_score += 15


if encumbrance_status == "Clear":

    extra_score += 15


if mortgage_status == "None Known":

    extra_score += 10


if litigation_status == "No Known Litigation":

    extra_score += 10


if property_tax_status == "Paid":

    extra_score += 5


final_score = min(

    (
        document_score * 0.50
        +
        extra_score
    ),

    100

)


# ============================================================
# STATUS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Legal Verification Score
</h2>

</div>
""", unsafe_allow_html=True)


if attention_documents > 0:

    st.markdown(
        f"""
        <div class="danger-card">

        <h2>
        🔴 Verification Requires Attention
        </h2>

        <h1>
        Score: {final_score:.1f}/100
        </h1>

        <p>
        {attention_documents} document(s) require attention.
        Do not proceed without resolving the flagged items.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

elif final_score >= 75:

    st.markdown(
        f"""
        <div class="safe-card">

        <h2>
        🟢 Verification Progress: Strong
        </h2>

        <h1>
        Score: {final_score:.1f}/100
        </h1>

        <p>
        Most important verification items appear to be completed.
        Professional legal review is still recommended.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        f"""
        <div class="warning-card">

        <h2>
        🟠 Verification In Progress
        </h2>

        <h1>
        Score: {final_score:.1f}/100
        </h1>

        <p>
        Several verification items are still pending.
        Complete the due diligence process before proceeding.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RISK FLAGS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚨 Risk Flags
</h2>

</div>
""", unsafe_allow_html=True)


risk_flags = []


if ownership_status != "Verified":

    risk_flags.append(
        "Ownership verification is not completed."
    )


if rera_required == "Yes" and rera_status != "Verified":

    risk_flags.append(
        "RERA verification is pending."
    )


if encumbrance_status != "Clear":

    risk_flags.append(
        "Encumbrance status is not confirmed clear."
    )


if mortgage_status != "None Known":

    risk_flags.append(
        "Possible existing mortgage requires verification."
    )


if litigation_status != "No Known Litigation":

    risk_flags.append(
        "Litigation status requires professional verification."
    )


if outstanding_dues > 0:

    risk_flags.append(
        f"Outstanding dues reported: ₹{outstanding_dues:,.0f}."
    )


if maintenance_dues > 0:

    risk_flags.append(
        f"Maintenance dues reported: ₹{maintenance_dues:,.0f}."
    )


if len(risk_flags) == 0:

    st.success(
        "✅ No major risk flags entered in the current checklist."
    )

else:

    for risk in risk_flags:

        st.warning(
            f"⚠️ {risk}"
        )


# ============================================================
# FINAL ACTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Verification Next Step
</h2>

</div>
""", unsafe_allow_html=True)


next_action = st.selectbox(
    "Select next action",
    [
        "📤 Upload Pending Documents",
        "👨‍⚖️ Send Documents to Legal Professional",
        "🔍 Request Title Search",
        "🏛️ Verify RERA Details",
        "🔒 Verify Encumbrance Certificate",
        "💰 Clear Outstanding Dues",
        "🤝 Proceed to Deal Room"
    ]
)


if st.button(
    "🚀 CONTINUE VERIFICATION",
    use_container_width=True
):

    st.success(
        f"✅ Next action selected: {next_action}"
    )


# ============================================================
# FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future Smart Legal Features
</h2>

<p>
Production version में आगे ये features जोड़े जा सकते हैं:
</p>

<p>
🤖 AI Document Reading
&nbsp; • &nbsp;
📄 OCR & Data Extraction
&nbsp; • &nbsp;
🔍 Document Mismatch Detection
&nbsp; • &nbsp;
🏛️ RERA Data Verification
&nbsp; • &nbsp;
🔒 Encumbrance Verification
&nbsp; • &nbsp;
🗺️ Land Record Integration
&nbsp; • &nbsp;
👨‍⚖️ Lawyer Collaboration
&nbsp; • &nbsp;
📊 Legal Risk Score
&nbsp; • &nbsp;
🔔 Verification Alerts
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
This page is a property verification checklist and tracking
tool. The verification score does not confirm that a property
is legally safe or free from disputes.
</p>

<p>
Always obtain independent legal advice and verify original
documents with the appropriate government authorities and
qualified professionals before purchasing property.
</p>

</div>
""", unsafe_allow_html=True)
