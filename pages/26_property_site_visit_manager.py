import streamlit as st
from datetime import datetime, date

# ============================================================
# PAGE 26 — SMART PROPERTY SITE VISIT & INSPECTION MANAGER
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Site Visit Manager | FirstChoice Property Hub",
    page_icon="📍",
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

.info-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0369A1,
        #0284C7,
        #06B6D4
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
📍 Smart Property Site Visit Manager
</h1>

<p>
Schedule, manage and evaluate property site visits
with a complete digital inspection workflow.
</p>

<p>
📅 Schedule • 📍 Location • 🏠 Inspection • 📸 Photos • ⭐ Rating • 📋 Report
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Site Visit & Inspection Centre
</h2>

<p>
A buyer can shortlist a property, schedule a visit,
inspect important features and record observations
before making a purchase decision.
</p>

<p>
This creates a structured property inspection history
instead of relying only on memory or scattered notes.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property Visit Profile
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
        "🆔 Property ID",
        value="FC-VISIT-001"
    )


c3, c4 = st.columns(2)


with c3:

    visitor_name = st.text_input(
        "👤 Visitor Name"
    )


with c4:

    visitor_role = st.selectbox(
        "👥 Visitor Role",
        [
            "Buyer",
            "Family Member",
            "Investor",
            "Agent",
            "Executive",
            "Builder"
        ]
    )


# ============================================================
# SITE VISIT SCHEDULING
# ============================================================

st.markdown("""
<div class="section">

<h2>
📅 Schedule Site Visit
</h2>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    visit_date = st.date_input(
        "📅 Visit Date",
        value=date.today()
    )


with s2:

    visit_time = st.time_input(
        "⏰ Visit Time"
    )


with s3:

    visit_status = st.selectbox(
        "📊 Visit Status",
        [
            "Scheduled",
            "Confirmed",
            "Completed",
            "Rescheduled",
            "Cancelled"
        ]
    )


visit_address = st.text_area(
    "📍 Property Visit Address"
)


contact_person = st.text_input(
    "📞 Site Visit Contact Person"
)


# ============================================================
# SAVE VISIT
# ============================================================

if "site_visits" not in st.session_state:

    st.session_state.site_visits = []


if st.button(
    "📅 SAVE SITE VISIT",
    use_container_width=True
):

    st.session_state.site_visits.append({

        "Property":
        property_name,

        "Property ID":
        property_id,

        "Visitor":
        visitor_name,

        "Role":
        visitor_role,

        "Date":
        str(visit_date),

        "Time":
        str(visit_time),

        "Status":
        visit_status,

        "Address":
        visit_address,

        "Contact":
        contact_person

    })

    st.success(
        "✅ Site visit saved successfully."
    )


# ============================================================
# VISIT HISTORY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🕒 Site Visit History
</h2>

</div>
""", unsafe_allow_html=True)


if st.session_state.site_visits:

    st.dataframe(
        st.session_state.site_visits,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "📅 No site visits recorded yet."
    )


# ============================================================
# INSPECTION CHECKLIST
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔍 Property Inspection Checklist
</h2>

<p>
Check the important aspects observed during the site visit.
</p>

</div>
""", unsafe_allow_html=True)


inspection_items = [

    "🏗️ Building Structure",

    "🚰 Water Supply",

    "⚡ Electricity",

    "🚗 Parking",

    "🛣️ Road Access",

    "🌳 Surrounding Environment",

    "🏫 Nearby Schools",

    "🏥 Nearby Hospitals",

    "🛒 Nearby Markets",

    "🔐 Security",

    "🛗 Lift / Elevator",

    "🔥 Fire Safety",

    "🌧️ Drainage",

    "📡 Internet / Mobile Network",

    "☀️ Natural Light",

    "🌬️ Ventilation"

]


checked_items = []


for item in inspection_items:

    if st.checkbox(
        item,
        key=f"inspection_{item}"
    ):

        checked_items.append(
            item
        )


inspection_percentage = (

    len(checked_items)
    /
    len(inspection_items)
    *
    100

)


st.progress(
    inspection_percentage / 100
)


st.write(
    f"Inspection Checklist Progress: "
    f"{inspection_percentage:.0f}%"
)


# ============================================================
# PROPERTY RATINGS
# ============================================================

st.markdown("""
<div class="section">

<h2>
⭐ Property Experience Rating
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    location_rating = st.slider(
        "📍 Location",
        1,
        5,
        3
    )


with r2:

    property_rating = st.slider(
        "🏠 Property Condition",
        1,
        5,
        3
    )


with r3:

    value_rating = st.slider(
        "💰 Value for Money",
        1,
        5,
        3
    )


overall_rating = (

    location_rating
    +
    property_rating
    +
    value_rating

) / 3


st.markdown(
    f"""
    <div class="success-card">

    <h2>
    ⭐ Overall Property Rating
    </h2>

    <h1>
    {overall_rating:.1f} / 5
    </h1>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# VISIT NOTES
# ============================================================

st.markdown("""
<div class="section">

<h2>
📝 Site Visit Notes
</h2>

</div>
""", unsafe_allow_html=True)


visit_notes = st.text_area(
    "Write your observations",
    placeholder=
    "Example: Property is close to main road. Parking is available. "
    "Need to verify drainage during monsoon."
)


# ============================================================
# PROPERTY PHOTOS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📸 Site Visit Photos
</h2>

</div>
""", unsafe_allow_html=True)


visit_photos = st.file_uploader(
    "Upload Site Visit Photos",
    type=[
        "jpg",
        "jpeg",
        "png"
    ],
    accept_multiple_files=True
)


if visit_photos:

    st.success(
        f"✅ {len(visit_photos)} photos selected."
    )


# ============================================================
# DECISION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Buyer Decision
</h2>

</div>
""", unsafe_allow_html=True)


decision = st.radio(
    "What is your decision after the site visit?",
    [
        "❤️ Highly Interested",
        "👍 Interested",
        "🤔 Need More Information",
        "💰 Need Better Price",
        "📄 Need Legal Verification",
        "❌ Not Interested"
    ]
)


# ============================================================
# GENERATE VISIT REPORT
# ============================================================

if st.button(
    "📋 GENERATE SITE VISIT REPORT",
    use_container_width=True
):

    st.markdown(
        f"""
        <div class="info-card">

        <h2>
        📋 Property Site Visit Report
        </h2>

        <p>
        <b>Property:</b> {property_name}
        </p>

        <p>
        <b>Property ID:</b> {property_id}
        </p>

        <p>
        <b>Visitor:</b> {visitor_name}
        </p>

        <p>
        <b>Visit Date:</b> {visit_date}
        </p>

        <p>
        <b>Inspection Progress:</b>
        {inspection_percentage:.0f}%
        </p>

        <p>
        <b>Overall Rating:</b>
        {overall_rating:.1f}/5
        </p>

        <p>
        <b>Decision:</b>
        {decision}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SMART RECOMMENDATION
# ============================================================

if overall_rating >= 4:

    st.success(
        "🤖 Smart Insight: This property received a strong visit rating. "
        "You may proceed to the next evaluation stage after completing "
        "legal and financial checks."
    )

elif overall_rating >= 3:

    st.info(
        "🤖 Smart Insight: The property appears moderately suitable. "
        "Consider comparing it with other shortlisted properties."
    )

else:

    st.warning(
        "🤖 Smart Insight: The property received a lower visit rating. "
        "Consider reviewing concerns before proceeding."
    )


# ============================================================
# FUTURE AI FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Site Visit Intelligence
</h2>

<p>
The production version can add:
</p>

<p>
📍 GPS Check-In
&nbsp; • &nbsp;
📸 AI Photo Analysis
&nbsp; • &nbsp;
🏠 Defect Detection
&nbsp; • &nbsp;
🌧️ Weather-Based Visit Insights
&nbsp; • &nbsp;
🗺️ Nearby Amenity Analysis
&nbsp; • &nbsp;
🤖 AI Visit Summary
</p>

<p>
AI could automatically analyse uploaded site photos,
identify visible issues and generate a structured
property inspection report.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NOTICE
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Notice
</h2>

<p>
Site visit ratings and observations are user-generated
and should not be treated as professional engineering,
structural or legal certification.
</p>

</div>
""", unsafe_allow_html=True)
