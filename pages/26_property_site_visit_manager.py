import streamlit as st
from datetime import datetime, date, time

# ============================================================
# PAGE 26 — SMART PROPERTY SITE VISIT & INSPECTION MANAGER
# FIRSTCHOICE INFRA PROPERTY HUB
# MERGED VERSION:
# PAGE 10 — SITE VISIT BOOKING
# PAGE 26 — SITE VISIT & INSPECTION MANAGER
# ============================================================

st.set_page_config(
    page_title="Site Visit Manager | FirstChoice Property Hub",
    page_icon="📍",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

if "site_visits" not in st.session_state:
    st.session_state.site_visits = []

if "visit_confirmed" not in st.session_state:
    st.session_state.visit_confirmed = False


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
    0 15px 45px
    rgba(5,150,105,0.22);
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
}

/* ============================================================
INFO CARD
============================================================ */

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

/* ============================================================
VISIT CARD
============================================================ */

.visit-card {
    padding: 25px;
    border-radius: 25px;
    background: white;
    border-left: 6px solid #7C3AED;
    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.08);
    margin-bottom: 15px;
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
📅 Schedule
&nbsp; • &nbsp;
📍 Location
&nbsp; • &nbsp;
🏠 Inspection
&nbsp; • &nbsp;
📸 Photos
&nbsp; • &nbsp;
⭐ Rating
&nbsp; • &nbsp;
📋 Report
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
# PROPERTY SELECTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Property
</h2>

<p>
Choose the property you would like to visit and inspect.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

property_name = st.selectbox(
    "🏠 Property",
    [
        "Premium 3 BHK Luxury Apartment — Civil Lines",
        "Modern 4 BHK Premium Villa — Wardha Road",
        "Premium Residential Plot — Amravati Road",
        "Commercial Office Space — MIHAN",
        "Luxury Villa — Seminary Hills",
        "Other Property"
    ]
)

if property_name == "Other Property":

    custom_property_name = st.text_input(
        "Enter Property Name"
    )

    if custom_property_name:
        property_name = custom_property_name


c1, c2 = st.columns(2)

with c1:

    property_id = st.text_input(
        "🆔 Property ID",
        value="FC-VISIT-001"
    )

with c2:

    visit_address = st.text_area(
        "📍 Property Visit Address",
        placeholder="Enter complete property address"
    )

c3, c4 = st.columns(2)

with c3:

    st.info(
        "📍 Location: Nagpur, Maharashtra"
    )

with c4:

    st.info(
        "🛡️ Verification: Available"
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# VISIT SCHEDULE
# ============================================================

st.markdown("""
<div class="section">

<h2>
📅 Schedule Your Property Visit
</h2>

<p>
Select your preferred date, time and visit type.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

s1, s2 = st.columns(2)

with s1:

    visit_date = st.date_input(
        "📅 Preferred Visit Date",
        value=date.today(),
        min_value=date.today()
    )

with s2:

    visit_time = st.time_input(
        "⏰ Preferred Visit Time",
        value=time(11, 0)
    )


visit_type = st.radio(
    "Visit Type",
    [
        "🏡 Physical Site Visit",
        "🎥 Virtual Video Tour",
        "📞 Request Property Expert Call"
    ],
    horizontal=True
)


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

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# VISITOR INFORMATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 Visitor Information
</h2>

<p>
Provide your contact details so the property team can confirm your visit.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

v1, v2 = st.columns(2)

with v1:

    visitor_name = st.text_input(
        "Full Name *",
        placeholder="Enter your full name"
    )

with v2:

    visitor_mobile = st.text_input(
        "Mobile Number *",
        max_chars=10,
        placeholder="10 digit mobile number"
    )

visitor_email = st.text_input(
    "Email Address",
    placeholder="example@email.com"
)

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

visitor_message = st.text_area(
    "Message / Special Requirement",
    placeholder=
    "Tell us if you have any specific requirement..."
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SITE VISIT SERVICES
# ============================================================

st.markdown("""
<div class="section">

<h2>
✨ Additional Visit Services
</h2>

</div>
""", unsafe_allow_html=True)

service1, service2, service3 = st.columns(3)

with service1:

    parking = st.checkbox(
        "🚗 Need Parking Assistance"
    )

with service2:

    pickup = st.checkbox(
        "🚘 Request Pickup Assistance"
    )

with service3:

    expert = st.checkbox(
        "👨‍💼 Property Expert Required"
    )


# ============================================================
# TERMS
# ============================================================

agree = st.checkbox(
    "I agree to be contacted by FirstChoice Property Hub "
    "or the property representative regarding this site visit."
)


# ============================================================
# CONFIRM SITE VISIT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Confirm Your Site Visit
</h2>

<p>
Submit your request and the property representative will confirm availability.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "📅 CONFIRM SITE VISIT",
    use_container_width=True
):

    if not visitor_name:

        st.error(
            "Please enter your full name."
        )

    elif not visitor_mobile:

        st.error(
            "Please enter your mobile number."
        )

    elif (
        len(visitor_mobile) != 10
        or not visitor_mobile.isdigit()
    ):

        st.error(
            "Please enter a valid 10-digit mobile number."
        )

    elif not agree:

        st.warning(
            "Please accept the contact confirmation."
        )

    else:

        st.session_state.visit_confirmed = True

        st.session_state.site_visits.append({

            "Property":
            property_name,

            "Property ID":
            property_id,

            "Visitor":
            visitor_name,

            "Mobile":
            visitor_mobile,

            "Email":
            visitor_email,

            "Role":
            visitor_role,

            "Visit Type":
            visit_type,

            "Date":
            str(visit_date),

            "Time":
            str(visit_time),

            "Status":
            visit_status,

            "Address":
            visit_address,

            "Parking":
            parking,

            "Pickup":
            pickup,

            "Expert":
            expert,

            "Message":
            visitor_message,

            "Created At":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        })

        st.success(
            "✅ Site visit request saved successfully."
        )


# ============================================================
# CONFIRMATION
# ============================================================

if st.session_state.visit_confirmed:

    st.markdown(
        f"""
        <div class="success-card">

        <h2>
        🎉 Site Visit Request Submitted!
        </h2>

        <p>
        <b>Property:</b>
        {property_name}
        </p>

        <p>
        <b>Property ID:</b>
        {property_id}
        </p>

        <p>
        📅 <b>Date:</b>
        {visit_date}
        </p>

        <p>
        ⏰ <b>Time:</b>
        {visit_time}
        </p>

        <p>
        👤 <b>Visitor:</b>
        {visitor_name}
        </p>

        <p>
        📞 <b>Mobile:</b>
        {visitor_mobile}
        </p>

        <p>
        🏡 <b>Visit Type:</b>
        {visit_type}
        </p>

        <p>
        Our property representative will contact you
        to confirm the visit.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SITE VISIT HISTORY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🕒 Site Visit History
</h2>

<p>
View your scheduled and completed property visits.
</p>

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


for index, item in enumerate(inspection_items):

    if st.checkbox(
        item,
        key=f"inspection_{index}"
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
    "Example: Property is close to main road. "
    "Parking is available. "
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
# BUYER DECISION
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
        <b>Property:</b>
        {property_name}
        </p>

        <p>
        <b>Property ID:</b>
        {property_id}
        </p>

        <p>
        <b>Visitor:</b>
        {visitor_name}
        </p>

        <p>
        <b>Visit Type:</b>
        {visit_type}
        </p>

        <p>
        <b>Visit Date:</b>
        {visit_date}
        </p>

        <p>
        <b>Visit Time:</b>
        {visit_time}
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

        <p>
        <b>Notes:</b>
        {visit_notes}
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
# TRUST & SAFETY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🛡️ Your Safety Matters
</h2>

</div>
""", unsafe_allow_html=True)


t1, t2, t3 = st.columns(3)


with t1:

    st.markdown("""
    <div class="info-card">

    <h3>
    🛡️ Verified Listings
    </h3>

    <p>
    We are building a trusted property ecosystem
    with verification signals.
    </p>

    </div>
    """, unsafe_allow_html=True)


with t2:

    st.markdown("""
    <div class="info-card">

    <h3>
    📍 Visit Tracking
    </h3>

    <p>
    Future versions will allow users to track
    their complete site visit history.
    </p>

    </div>
    """, unsafe_allow_html=True)


with t3:

    st.markdown("""
    <div class="info-card">

    <h3>
    🤝 Expert Assistance
    </h3>

    <p>
    Connect with property experts for
    better buying decisions.
    </p>

    </div>
    """, unsafe_allow_html=True)


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
# IMPORTANT NOTICE
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
