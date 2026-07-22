import streamlit as st
from datetime import date, timedelta

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 16 - SMART SITE VISIT BOOKING
# ============================================================

st.set_page_config(
    page_title="Site Visit Booking | FirstChoice Property Hub",
    page_icon="📅",
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
    padding: 48px;
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
    color: rgba(255,255,255,0.88);
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
    color: rgba(255,255,255,0.82);
}

/* BOOKING CARD */

.booking-card {
    background: white;
    padding: 35px;
    border-radius: 30px;

    box-shadow:
    0 18px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* PROPERTY */

.property-card {
    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F8FAFF,
        #FDF4FF
    );

    padding: 30px;
    border-radius: 30px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);
}

/* VISIT STATUS */

.status-card {
    padding: 25px;
    border-radius: 25px;
    background: white;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);
}

/* TRUST */

.trust-card {
    padding: 35px;
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
PROPERTY HUB • SMART SITE VISIT EXPERIENCE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
📅 Book Your Property Visit
</div>

<div class="hero-subtitle">
Schedule a convenient property visit with owners,
agents and builders through FirstChoice Property Hub.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# VISIT STATISTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 My Visit Activity
</div>

<div class="section-subtitle">
Manage your upcoming and previous property visits.
</div>

</div>
""", unsafe_allow_html=True)


s1, s2, s3, s4 = st.columns(4)


with s1:

    st.metric(
        "📅 Upcoming",
        "3"
    )


with s2:

    st.metric(
        "🟢 Confirmed",
        "2"
    )


with s3:

    st.metric(
        "⏳ Pending",
        "1"
    )


with s4:

    st.metric(
        "✅ Completed",
        "8"
    )


# ============================================================
# SELECT PROPERTY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Select Property
</div>

<div class="section-subtitle">
Choose the property you want to visit.
</div>

</div>
""", unsafe_allow_html=True)


property_options = [

    "Premium 3 BHK Luxury Apartment — Civil Lines, Nagpur",

    "Luxury Independent Villa — Baner, Pune",

    "Premium Residential Plot — Wardha Road, Nagpur",

    "FirstChoice Premium Township — Nagpur"

]


selected_property = st.selectbox(
    "Select Property",
    property_options
)


# ============================================================
# PROPERTY PREVIEW
# ============================================================

st.markdown("""
<div class="property-card">

<h2>
🏡 Selected Property
</h2>

<p>
Your selected property will appear here with
photos, videos, verification status and owner information.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# BUYER DETAILS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Visitor Information
</div>

<div class="section-subtitle">
Your verified contact details help us coordinate the visit.
</div>

</div>
""", unsafe_allow_html=True)


b1, b2 = st.columns(2)


with b1:

    buyer_name = st.text_input(
        "Full Name",
        placeholder="Enter your full name"
    )


with b2:

    buyer_mobile = st.text_input(
        "Verified Mobile Number",
        placeholder="+91 XXXXX XXXXX"
    )


b3, b4 = st.columns(2)


with b3:

    buyer_email = st.text_input(
        "Email Address",
        placeholder="example@email.com"
    )


with b4:

    visitors = st.selectbox(
        "Number of Visitors",
        [
            "1 Person",
            "2 People",
            "3 People",
            "4 People",
            "5+ People"
        ]
    )


# ============================================================
# DATE AND TIME
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📅 Choose Visit Date & Time
</div>

<div class="section-subtitle">
Select your preferred date and convenient time slot.
</div>

</div>
""", unsafe_allow_html=True)


d1, d2 = st.columns(2)


with d1:

    visit_date = st.date_input(
        "Preferred Visit Date",
        value=date.today() + timedelta(days=1),
        min_value=date.today()
    )


with d2:

    visit_time = st.selectbox(
        "Preferred Time Slot",
        [
            "09:00 AM – 10:00 AM",
            "10:00 AM – 11:00 AM",
            "11:00 AM – 12:00 PM",
            "12:00 PM – 01:00 PM",
            "02:00 PM – 03:00 PM",
            "03:00 PM – 04:00 PM",
            "04:00 PM – 05:00 PM",
            "05:00 PM – 06:00 PM",
            "06:00 PM – 07:00 PM"
        ]
    )


# ============================================================
# VISIT PURPOSE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🎯 Visit Purpose
</div>

<div class="section-subtitle">
Tell the property partner what you are looking for.
</div>

</div>
""", unsafe_allow_html=True)


visit_purpose = st.selectbox(
    "I am interested in",
    [
        "Buying Property",
        "Renting Property",
        "Investment",
        "Plot / Land Purchase",
        "Commercial Property",
        "New Project",
        "Just Exploring"
    ]
)


special_request = st.text_area(
    "Special Request / Message",
    placeholder=
    "Example: I would like to understand the payment plan and property documents."
)


# ============================================================
# CONFIRMATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
✅ Confirm Site Visit Request
</div>

<div class="section-subtitle">
Review your details before submitting the request.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="booking-card">

    <h2>
    📋 Visit Summary
    </h2>

    <p>
    🏠 <b>Property:</b>
    {selected_property}
    </p>

    <p>
    👤 <b>Visitor:</b>
    {buyer_name if buyer_name else "Not entered"}
    </p>

    <p>
    📱 <b>Mobile:</b>
    {buyer_mobile if buyer_mobile else "Not entered"}
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
    🎯 <b>Purpose:</b>
    {visit_purpose}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


if st.button(
    "📅 REQUEST SITE VISIT",
    use_container_width=True
):

    if not buyer_name:

        st.error(
            "Please enter your full name."
        )

    elif not buyer_mobile:

        st.error(
            "Please enter your verified mobile number."
        )

    else:

        st.success(
            "🎉 Site visit request submitted successfully!"
        )

        st.info(
            "The property owner or agent will confirm the visit shortly."
        )


# ============================================================
# UPCOMING VISITS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📅 My Upcoming Visits
</div>

<div class="section-subtitle">
Track and manage your scheduled property visits.
</div>

</div>
""", unsafe_allow_html=True)


visits = [

    {
        "property":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "date":
        "25 July 2026",

        "time":
        "11:00 AM – 12:00 PM",

        "status":
        "🟢 Confirmed"

    },

    {
        "property":
        "Luxury Independent Villa",

        "location":
        "Baner, Pune",

        "date":
        "28 July 2026",

        "time":
        "04:00 PM – 05:00 PM",

        "status":
        "⏳ Pending Confirmation"

    }

]


for index, visit in enumerate(visits):

    st.markdown(
        f"""
        <div class="status-card">

        <h2>
        🏠 {visit['property']}
        </h2>

        <p>
        📍 {visit['location']}
        </p>

        <p>
        📅 {visit['date']}
        </p>

        <p>
        ⏰ {visit['time']}
        </p>

        <p>
        <b>{visit['status']}</b>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    v1, v2, v3 = st.columns(3)


    with v1:

        if st.button(
            "🔄 Reschedule",
            key=f"reschedule_{index}",
            use_container_width=True
        ):

            st.info(
                "Rescheduling module will open."
            )


    with v2:

        if st.button(
            "❌ Cancel Visit",
            key=f"cancel_{index}",
            use_container_width=True
        ):

            st.warning(
                "Visit cancellation confirmation required."
            )


    with v3:

        if st.button(
            "📍 View Property",
            key=f"property_{index}",
            use_container_width=True
        ):

            st.info(
                "Property details page will open."
            )


# ============================================================
# SMART REMINDER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔔 Smart Visit Reminders
</div>

<div class="section-subtitle">
Never miss your scheduled property visit.
</div>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    st.success(
        """
        🔔 24-Hour Reminder

        Receive a reminder before your
        scheduled property visit.
        """
    )


with r2:

    st.info(
        """
        📱 Mobile Notification

        Get visit updates on your
        verified mobile number.
        """
    )


with r3:

    st.warning(
        """
        📧 Email Reminder

        Receive booking confirmations
        and visit details.
        """
    )


# ============================================================
# TRUST & SAFETY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ FirstChoice Visit Safety
</div>

<div class="section-subtitle">
A trusted experience for buyers, owners and property professionals.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="trust-card">

<h2>
🛡️ Verified Property Visits
</h2>

<p>
🏠 Visit verified property listings whenever possible.
</p>

<p>
📱 Communication through verified contact information.
</p>

<p>
👤 Verified owners, agents and builders.
</p>

<p>
📍 Visit details shared securely with confirmed participants.
</p>

<p>
🚨 Report suspicious property listings or activity.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FUTURE FEATURE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Coming Next
</div>

<div class="section-subtitle">
Advanced property visit management.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.info(
        """
        🗓️ **Smart Calendar**

        Owner and buyer calendars
        will automatically sync.
        """
    )


with f2:

    st.success(
        """
        🗺️ **Live Location**

        Future visit navigation and
        property location assistance.
        """
    )


with f3:

    st.warning(
        """
        🤖 **AI Scheduling**

        Smart time suggestions based
        on availability.
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
