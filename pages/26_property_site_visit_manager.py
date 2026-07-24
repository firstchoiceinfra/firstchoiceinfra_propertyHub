import streamlit as st
from datetime import datetime, date, time
import uuid

# ============================================================
# NAVIGATION IMPORT
# ============================================================

from navigation import show_navigation, set_current_page


# ============================================================
# PAGE 26 — SMART PROPERTY SITE VISIT & INSPECTION MANAGER
# FIRSTCHOICE INFRA PROPERTY HUB
#
# FEATURES:
# ✅ Back Button
# ✅ Home Button
# ✅ Page Menu
# ✅ Property ID System
# ✅ Site Visit Booking
# ✅ Visit Confirmation
# ✅ Visit History
# ✅ Reschedule / Cancel
# ✅ Inspection Checklist
# ✅ Inspection Progress
# ✅ Property Rating
# ✅ Visit Notes
# ✅ Site Visit Photos
# ✅ Buyer Decision
# ✅ Site Visit Report
# ✅ Smart Recommendation
# ✅ Safety & Verification
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Site Visit Manager | FirstChoice Property Hub",
    page_icon="📍",
    layout="wide"
)


# ============================================================
# CURRENT PAGE NAVIGATION
# ============================================================

set_current_page(
    "26_property_site_visit_manager.py"
)

show_navigation()


# ============================================================
# SESSION STATE
# ============================================================

if "site_visits" not in st.session_state:
    st.session_state.site_visits = []

if "visit_confirmed" not in st.session_state:
    st.session_state.visit_confirmed = False

if "selected_visit_id" not in st.session_state:
    st.session_state.selected_visit_id = None

if "visit_report_generated" not in st.session_state:
    st.session_state.visit_report_generated = False


# ============================================================
# PREMIUM UI
# ============================================================

st.markdown(
    """
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
    0 15px 45px
    rgba(5,150,105,0.22);

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

    margin-bottom: 25px;
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

    box-shadow:
    0 18px 50px
    rgba(3,105,161,0.22);

    margin-bottom: 25px;
}


/* ============================================================
VISIT CARD
============================================================ */

.visit-card {
    padding: 25px;

    border-radius: 25px;

    background: white;

    border-left:
    6px solid #7C3AED;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.08);

    margin-bottom: 15px;
}


/* ============================================================
PROPERTY ID
============================================================ */

.property-id {
    padding: 25px;

    border-radius: 25px;

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
    rgba(5,150,105,0.25);

    margin-bottom: 25px;
}


/* ============================================================
REPORT CARD
============================================================ */

.report-card {
    padding: 35px;

    border-radius: 30px;

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
    0 20px 60px
    rgba(124,58,237,0.25);

    margin-top: 25px;
}


/* ============================================================
NAVIGATION
============================================================ */

.nav-note {
    padding: 12px 20px;

    border-radius: 14px;

    background:
    linear-gradient(
        135deg,
        #E0E7FF,
        #F5F3FF
    );

    color: #1E1B4B;

    text-align: center;

    font-weight: 700;

    margin-bottom: 25px;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
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
""",
    unsafe_allow_html=True
)


# ============================================================
# SMART INTRO
# ============================================================

st.markdown(
    """
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
Every site visit is connected with a unique Visit ID
and Property ID for better tracking.
</p>

<p>
🏡 Property → 🆔 Property ID → 📅 Site Visit
→ 🔍 Inspection → ⭐ Rating → 📋 Report
→ 🎯 Buyer Decision
</p>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY SELECTION
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🏡 Step 1 — Select Property
</h2>

<p>
Choose the property you would like to visit and inspect.
</p>

</div>
""",
    unsafe_allow_html=True
)


property_list = [
    "Premium 3 BHK Luxury Apartment — Civil Lines",
    "Modern 4 BHK Premium Villa — Wardha Road",
    "Premium Residential Plot — Amravati Road",
    "Commercial Office Space — MIHAN",
    "Luxury Villa — Seminary Hills",
    "Other Property"
]


property_name = st.selectbox(
    "🏠 Property",
    property_list
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
        value="FC-PROP-001"
    )


with c2:

    property_status = st.selectbox(
        "📊 Property Status",
        [
            "Available",
            "Under Discussion",
            "Hold",
            "Booked",
            "Sold"
        ]
    )


c3, c4 = st.columns(2)


with c3:

    visit_address = st.text_area(
        "📍 Property Visit Address",
        placeholder="Enter complete property address"
    )


with c4:

    property_location = st.text_input(
        "🗺️ Google Maps / Location Link",
        placeholder="Paste Google Maps link"
    )


l1, l2 = st.columns(2)


with l1:

    st.info(
        "📍 Location: Nagpur, Maharashtra"
    )


with l2:

    st.success(
        "🛡️ Verification: Available"
    )


# ============================================================
# VISIT SCHEDULE
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
📅 Step 2 — Schedule Your Property Visit
</h2>

<p>
Select your preferred date, time and visit type.
</p>

</div>
""",
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


visit_priority = st.selectbox(
    "🚦 Visit Priority",
    [
        "Normal",
        "High Priority",
        "Urgent"
    ]
)


# ============================================================
# VISITOR INFORMATION
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
👤 Step 3 — Visitor Information
</h2>

<p>
Provide your contact details so the property team can confirm your visit.
</p>

</div>
""",
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
        "Builder",
        "Other"
    ]
)


visitor_message = st.text_area(
    "Message / Special Requirement",
    placeholder="Tell us if you have any specific requirement..."
)


# ============================================================
# ADDITIONAL SERVICES
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
✨ Step 4 — Additional Visit Services
</h2>

</div>
""",
    unsafe_allow_html=True
)


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
# CONFIRM VISIT
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🚀 Step 5 — Confirm Your Site Visit
</h2>

<p>
Submit your request and the property representative will confirm availability.
</p>

</div>
""",
    unsafe_allow_html=True
)


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

    elif not property_id:

        st.error(
            "Please enter Property ID."
        )

    elif not agree:

        st.warning(
            "Please accept the contact confirmation."
        )

    else:

        visit_id = (
            "FC-VISIT-"
            +
            uuid.uuid4().hex[:8].upper()
        )


        new_visit = {

            "Visit ID":
            visit_id,

            "Property":
            property_name,

            "Property ID":
            property_id,

            "Property Status":
            property_status,

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

            "Priority":
            visit_priority,

            "Status":
            visit_status,

            "Address":
            visit_address,

            "Location Link":
            property_location,

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

        }


        st.session_state.site_visits.append(
            new_visit
        )


        st.session_state.visit_confirmed = True

        st.session_state.selected_visit_id = visit_id


        st.success(
            "✅ Site visit request saved successfully."
        )


# ============================================================
# CONFIRMATION
# ============================================================

if st.session_state.visit_confirmed:

    latest_visit = None


    for item in reversed(
        st.session_state.site_visits
    ):

        if (
            item["Visit ID"]
            ==
            st.session_state.selected_visit_id
        ):

            latest_visit = item

            break


    if latest_visit:

        st.markdown(
            f"""
<div class="success-card">

<h2>
🎉 Site Visit Request Submitted Successfully!
</h2>

<p>
<b>Visit ID:</b>
{latest_visit["Visit ID"]}
</p>

<p>
<b>Property:</b>
{latest_visit["Property"]}
</p>

<p>
<b>Property ID:</b>
{latest_visit["Property ID"]}
</p>

<p>
📅 <b>Date:</b>
{latest_visit["Date"]}
</p>

<p>
⏰ <b>Time:</b>
{latest_visit["Time"]}
</p>

<p>
👤 <b>Visitor:</b>
{latest_visit["Visitor"]}
</p>

<p>
📞 <b>Mobile:</b>
{latest_visit["Mobile"]}
</p>

<p>
🏡 <b>Visit Type:</b>
{latest_visit["Visit Type"]}
</p>

<p>
📊 <b>Status:</b>
{latest_visit["Status"]}
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
# VISIT DASHBOARD
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
📊 Site Visit Dashboard
</h2>

</div>
""",
    unsafe_allow_html=True
)


total_visits = len(
    st.session_state.site_visits
)


scheduled_visits = len(

    [
        x

        for x
        in st.session_state.site_visits

        if x["Status"]
        in
        [
            "Scheduled",
            "Confirmed"
        ]

    ]

)


completed_visits = len(

    [
        x

        for x
        in st.session_state.site_visits

        if x["Status"]
        ==
        "Completed"

    ]

)


cancelled_visits = len(

    [
        x

        for x
        in st.session_state.site_visits

        if x["Status"]
        ==
        "Cancelled"

    ]

)


d1, d2, d3, d4 = st.columns(4)


with d1:

    st.metric(
        "📅 Total Visits",
        total_visits
    )


with d2:

    st.metric(
        "🕒 Scheduled",
        scheduled_visits
    )


with d3:

    st.metric(
        "✅ Completed",
        completed_visits
    )


with d4:

    st.metric(
        "❌ Cancelled",
        cancelled_visits
    )


# ============================================================
# SITE VISIT HISTORY
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🕒 Site Visit History
</h2>

<p>
View and manage your scheduled and completed property visits.
</p>

</div>
""",
    unsafe_allow_html=True
)


if st.session_state.site_visits:

    st.dataframe(
        st.session_state.site_visits,
        use_container_width=True,
        hide_index=True
    )


    visit_ids = [

        x["Visit ID"]

        for x
        in st.session_state.site_visits

    ]


    selected_history_visit = st.selectbox(
        "🔍 Select Visit for Management",
        visit_ids
    )


    selected_history = next(

        (
            x

            for x
            in st.session_state.site_visits

            if x["Visit ID"]
            ==
            selected_history_visit
        ),

        None

    )


    if selected_history:

        st.markdown(
            f"""
<div class="visit-card">

<h3>
📍 {selected_history["Property"]}
</h3>

<p>
<b>Visit ID:</b>
{selected_history["Visit ID"]}
</p>

<p>
<b>Property ID:</b>
{selected_history["Property ID"]}
</p>

<p>
<b>Visitor:</b>
{selected_history["Visitor"]}
</p>

<p>
<b>Date:</b>
{selected_history["Date"]}
</p>

<p>
<b>Time:</b>
{selected_history["Time"]}
</p>

<p>
<b>Status:</b>
{selected_history["Status"]}
</p>

</div>
""",
            unsafe_allow_html=True
        )


        management_status = st.selectbox(

            "🔄 Update Visit Status",

            [
                "Scheduled",
                "Confirmed",
                "Completed",
                "Rescheduled",
                "Cancelled"
            ],

            key="management_status"

        )


        if st.button(
            "🔄 UPDATE VISIT STATUS",
            use_container_width=True
        ):

            for item in st.session_state.site_visits:

                if (
                    item["Visit ID"]
                    ==
                    selected_history_visit
                ):

                    item["Status"] = management_status


            st.success(
                "✅ Site visit status updated successfully."
            )


else:

    st.info(
        "📅 No site visits recorded yet."
    )


# ============================================================
# INSPECTION CHECKLIST
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🔍 Property Inspection Checklist
</h2>

<p>
Check the important aspects observed during the site visit.
</p>

</div>
""",
    unsafe_allow_html=True
)


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


for index, item in enumerate(
    inspection_items
):

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

st.markdown(
    """
<div class="section">

<h2>
⭐ Property Experience Rating
</h2>

</div>
""",
    unsafe_allow_html=True
)


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

st.markdown(
    """
<div class="section">

<h2>
📝 Site Visit Notes
</h2>

</div>
""",
    unsafe_allow_html=True
)


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

st.markdown(
    """
<div class="section">

<h2>
📸 Site Visit Photos
</h2>

</div>
""",
    unsafe_allow_html=True
)


visit_photos = st.file_uploader(

    "Upload Site Visit Photos",

    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
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

st.markdown(
    """
<div class="section">

<h2>
🎯 Buyer Decision
</h2>

</div>
""",
    unsafe_allow_html=True
)


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

    st.session_state.visit_report_generated = True


if st.session_state.visit_report_generated:

    st.markdown(

        f"""
<div class="report-card">

<h2>
📋 Property Site Visit Report
</h2>

<hr>

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

<p>
<b>Inspection Items Checked:</b>
{len(checked_items)} / {len(inspection_items)}
</p>

</div>
""",

        unsafe_allow_html=True

    )


    st.success(
        "✅ Site Visit Report generated successfully."
    )


# ============================================================
# SMART RECOMMENDATION
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🤖 Smart Property Visit Recommendation
</h2>

</div>
""",
    unsafe_allow_html=True
)


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
# NEXT STEP RECOMMENDATION
# ============================================================

if decision == "❤️ Highly Interested":

    st.success(
        "🚀 Recommended Next Step: Proceed to Property Legal Verification "
        "and Investment Finance evaluation."
    )

elif decision == "👍 Interested":

    st.info(
        "📊 Recommended Next Step: Compare this property with shortlisted "
        "properties and review pricing."
    )

elif decision == "💰 Need Better Price":

    st.warning(
        "💰 Recommended Next Step: Start price negotiation with the "
        "property owner or authorised representative."
    )

elif decision == "📄 Need Legal Verification":

    st.info(
        "⚖️ Recommended Next Step: Complete legal due diligence "
        "before making any booking decision."
    )

elif decision == "❌ Not Interested":

    st.warning(
        "🔍 Recommended Next Step: Explore other properties matching "
        "your requirements."
    )


# ============================================================
# TRUST & SAFETY
# ============================================================

st.markdown(
    """
<div class="section">

<h2>
🛡️ Your Safety Matters
</h2>

</div>
""",
    unsafe_allow_html=True
)


t1, t2, t3 = st.columns(3)


with t1:

    st.markdown(
        """
<div class="info-card">

<h3>
🛡️ Verified Listings
</h3>

<p>
We are building a trusted property ecosystem
with verification signals.
</p>

</div>
""",
        unsafe_allow_html=True
    )


with t2:

    st.markdown(
        """
<div class="info-card">

<h3>
📍 Visit Tracking
</h3>

<p>
Every visit can be connected to a unique
Property ID and Visit ID.
</p>

</div>
""",
        unsafe_allow_html=True
    )


with t3:

    st.markdown(
        """
<div class="info-card">

<h3>
🤝 Expert Assistance
</h3>

<p>
Connect with property experts for
better buying decisions.
</p>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# FUTURE AI FEATURES
# ============================================================

st.markdown(
    """
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
""",
    unsafe_allow_html=True
)


# ============================================================
# IMPORTANT NOTICE
# ============================================================

st.markdown(
    """
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
""",
    unsafe_allow_html=True
)


# ============================================================
# FINAL NAVIGATION
# ============================================================

st.markdown(
    """
<div class="nav-note">

🏠 FirstChoice Infra Property Hub
&nbsp; | &nbsp;
📍 Page 26 — Site Visit & Inspection Manager

</div>
""",
    unsafe_allow_html=True
)

show_navigation()
