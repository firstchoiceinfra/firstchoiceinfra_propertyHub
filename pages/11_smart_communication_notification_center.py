import streamlit as st
from datetime import datetime


# ============================================================
# PAGE — SMART COMMUNICATION, NOTIFICATIONS & LEAD CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
#
# MERGED:
# PAGE 11 — NOTIFICATIONS & ALERTS
# PAGE 12 — PROPERTY ENQUIRY & LEAD MANAGEMENT
#
# FEATURES PRESERVED:
# 🔔 Notifications & Alerts
# 💬 Property Enquiry
# 📋 Lead Management
# 💬 Chat
# 📞 Call Request
# 📅 Site Visit
# 🤝 Follow-up
# ⚙️ Notification Preferences
# 📲 Notification Channels
# 🛡️ Privacy & Security
# 🤖 Smart Alert Engine
# ============================================================


st.set_page_config(
    page_title="Smart Communication, Notifications & Lead Center | FirstChoice Property Hub",
    page_icon="🔔",
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


/* =========================================================
   HERO
========================================================= */

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
    0 22px 70px
    rgba(37,99,235,0.28);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.8;
}


/* =========================================================
   SECTION
========================================================= */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 27px 32px;

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
    0 13px 38px
    rgba(79,70,229,0.20);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}


/* =========================================================
   CARD
========================================================= */

.card {
    padding: 28px;
    border-radius: 26px;

    background: white;

    box-shadow:
    0 14px 42px
    rgba(0,0,0,0.08);

    margin-bottom: 22px;
}


/* =========================================================
   NOTIFICATION CARD
========================================================= */

.notification {
    padding: 25px;

    border-radius: 24px;

    background: white;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.08);

    margin-bottom: 18px;
}

.notification:hover {
    transform: translateY(-3px);
    transition: 0.2s;
}


/* =========================================================
   UNREAD NOTIFICATION
========================================================= */

.unread {
    border-left: 6px solid #7C3AED;
}


/* =========================================================
   LEAD CARD
========================================================= */

.lead-card {
    padding: 27px;

    border-radius: 25px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border:
    1px solid #E0E7FF;

    margin-bottom: 18px;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);
}


/* =========================================================
   SUCCESS CARD
========================================================= */

.success-card {
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
    0 17px 48px
    rgba(5,150,105,0.23);
}


/* =========================================================
   INFO CARD
========================================================= */

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

    border:
    1px solid #E0E7FF;
}


/* =========================================================
   ALERT CARD
========================================================= */

.alert-card {
    padding: 28px;

    border-radius: 26px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #B45309,
        #F59E0B,
        #F97316
    );

    box-shadow:
    0 15px 45px
    rgba(245,158,11,0.22);
}


/* =========================================================
   SMART CARD
========================================================= */

.smart-card {
    padding: 30px;

    border-radius: 28px;

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


/* =========================================================
   PRIVACY CARD
========================================================= */

.privacy-card {
    padding: 30px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0369A1,
        #2563EB,
        #4F46E5
    );

    box-shadow:
    0 18px 50px
    rgba(37,99,235,0.24);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE — NOTIFICATIONS
# ============================================================

if "notifications" not in st.session_state:

    st.session_state.notifications = [

        {
            "title":
            "🏡 New Property Match Found",

            "message":
            "A new 3 BHK property matching your search preferences is available in Nagpur.",

            "type":
            "Property",

            "time":
            "10 minutes ago",

            "read":
            False
        },

        {
            "title":
            "📅 Site Visit Request",

            "message":
            "Your site visit request has been received and is awaiting confirmation.",

            "type":
            "Site Visit",

            "time":
            "1 hour ago",

            "read":
            False
        },

        {
            "title":
            "💬 Enquiry Update",

            "message":
            "The property representative has received your enquiry.",

            "type":
            "Enquiry",

            "time":
            "2 hours ago",

            "read":
            False
        },

        {
            "title":
            "🛡️ Verification Update",

            "message":
            "Your profile mobile number has been successfully verified.",

            "type":
            "Security",

            "time":
            "Yesterday",

            "read":
            True
        },

        {
            "title":
            "❤️ Property Saved",

            "message":
            "Premium Villa — Wardha Road has been added to your saved properties.",

            "type":
            "Saved",

            "time":
            "Yesterday",

            "read":
            True
        },

        {
            "title":
            "📈 Market Alert",

            "message":
            "Property prices in your preferred location have changed recently.",

            "type":
            "Market",

            "time":
            "2 days ago",

            "read":
            True
        }

    ]


# ============================================================
# SESSION STATE — PROPERTY ENQUIRIES
# ============================================================

if "property_enquiries" not in st.session_state:

    st.session_state.property_enquiries = [

        {
            "property":
            "Premium 3 BHK Luxury Apartment",

            "location":
            "Civil Lines, Nagpur",

            "name":
            "Rahul Sharma",

            "mobile":
            "98XXXXXXXX",

            "email":
            "rahul@example.com",

            "enquiry_type":
            "General Enquiry",

            "message":
            "I am interested in this property. Please share more details.",

            "status":
            "New",

            "time":
            "Today, 10:30 AM"
        },

        {
            "property":
            "Modern 4 BHK Premium Villa",

            "location":
            "Wardha Road, Nagpur",

            "name":
            "Amit Verma",

            "mobile":
            "97XXXXXXXX",

            "email":
            "amit@example.com",

            "enquiry_type":
            "Schedule Site Visit",

            "message":
            "I would like to schedule a site visit.",

            "status":
            "Follow Up",

            "time":
            "Yesterday"
        }

    ]


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🔔💬 Smart Communication, Notifications & Lead Center
</h1>

<p>
Manage your property enquiries, leads, notifications and
communication activities from one intelligent property platform.
</p>

<p>
🏡 Enquiry
&nbsp; • &nbsp;
🔔 Notifications
&nbsp; • &nbsp;
💬 Chat
&nbsp; • &nbsp;
📞 Call
&nbsp; • &nbsp;
📅 Site Visit
&nbsp; • &nbsp;
🤝 Follow-up
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# UNIFIED DASHBOARD METRICS
# ============================================================

unread_count = sum(
    1
    for n in st.session_state.notifications
    if not n["read"]
)


total_leads = len(
    st.session_state.property_enquiries
)


new_leads = sum(
    1
    for lead in st.session_state.property_enquiries
    if lead["status"] == "New"
)


followups = sum(
    1
    for lead in st.session_state.property_enquiries
    if lead["status"] == "Follow Up"
)


st.markdown("""
<div class="section">

<h2>
📊 Communication & Lead Overview
</h2>

</div>
""", unsafe_allow_html=True)


m1, m2, m3, m4 = st.columns(4)


with m1:

    st.metric(
        "🔔 Total Notifications",
        len(st.session_state.notifications)
    )


with m2:

    st.metric(
        "🟣 Unread Notifications",
        unread_count
    )


with m3:

    st.metric(
        "💬 Total Enquiries",
        total_leads
    )


with m4:

    st.metric(
        "🆕 New Enquiries",
        new_leads
    )


m5, m6, m7, m8 = st.columns(4)


with m5:

    st.metric(
        "📞 Follow Ups",
        followups
    )


with m6:

    st.metric(
        "📅 Site Visit Requests",
        sum(
            1
            for lead in st.session_state.property_enquiries
            if lead["enquiry_type"]
            ==
            "Schedule Site Visit"
        )
    )


with m7:

    st.metric(
        "📞 Call Requests",
        sum(
            1
            for lead in st.session_state.property_enquiries
            if lead["enquiry_type"]
            ==
            "Request Call Back"
        )
    )


with m8:

    st.metric(
        "✅ Read Notifications",
        len(st.session_state.notifications)
        -
        unread_count
    )


# ============================================================
# SECTION 1 — SEND NEW PROPERTY ENQUIRY
# ============================================================

st.markdown("""
<div class="section">

<h2>
✉️ Send Property Enquiry
</h2>

<p>
Interested in a property? Send your enquiry directly to the
property representative.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)


property_choice = st.selectbox(
    "🏡 Select Property",
    [
        "Premium 3 BHK Luxury Apartment",
        "Modern 4 BHK Premium Villa",
        "Premium Residential Plot",
        "Commercial Office Space",
        "Luxury Villa"
    ]
)


c1, c2 = st.columns(2)


with c1:

    buyer_name = st.text_input(
        "👤 Your Name",
        placeholder="Enter your full name"
    )


with c2:

    buyer_mobile = st.text_input(
        "📱 Mobile Number",
        max_chars=10,
        placeholder="10 digit mobile number"
    )


buyer_email = st.text_input(
    "📧 Email Address",
    placeholder="example@email.com"
)


enquiry_type = st.selectbox(
    "🎯 Enquiry Type",
    [
        "General Enquiry",
        "Request Price",
        "Request More Photos",
        "Request Property Documents",
        "Schedule Site Visit",
        "Request Call Back",
        "Investment Enquiry"
    ]
)


message = st.text_area(
    "💬 Your Message",
    placeholder="Write your enquiry or requirement here..."
)


send_enquiry = st.button(
    "🚀 SEND ENQUIRY",
    use_container_width=True
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ENQUIRY SUBMISSION
# ============================================================

if send_enquiry:

    if not buyer_name:

        st.error(
            "Please enter your name."
        )

    elif not buyer_mobile:

        st.error(
            "Please enter your mobile number."
        )

    elif (
        len(buyer_mobile) != 10
        or not buyer_mobile.isdigit()
    ):

        st.error(
            "Please enter a valid 10-digit mobile number."
        )

    else:

        new_enquiry = {

            "property":
            property_choice,

            "location":
            "Nagpur, Maharashtra",

            "name":
            buyer_name,

            "mobile":
            buyer_mobile,

            "email":
            buyer_email,

            "enquiry_type":
            enquiry_type,

            "message":
            message
            if message
            else
            "Property enquiry submitted.",

            "status":
            "New",

            "time":
            datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )

        }


        st.session_state.property_enquiries.insert(
            0,
            new_enquiry
        )


        # Create notification automatically
        st.session_state.notifications.insert(
            0,
            {
                "title":
                "💬 Enquiry Sent Successfully",

                "message":
                f"Your enquiry for {property_choice} has been submitted successfully.",

                "type":
                "Enquiry",

                "time":
                "Just now",

                "read":
                False
            }
        )


        st.markdown(
            f"""
            <div class="success-card">

            <h2>
            🎉 Enquiry Sent Successfully!
            </h2>

            <p>
            Your enquiry for
            <b>{property_choice}</b>
            has been submitted.
            </p>

            <p>
            Enquiry Type:
            <b>{enquiry_type}</b>
            </p>

            <p>
            The property representative can now contact you.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SECTION 2 — MY PROPERTY ENQUIRIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 My Property Enquiries & Lead Management
</h2>

<p>
Track your enquiries, communication status and follow-up activities.
</p>

</div>
""", unsafe_allow_html=True)


filter_status = st.selectbox(
    "📂 Filter By Status",
    [
        "All",
        "New",
        "Follow Up",
        "Contacted",
        "Closed"
    ]
)


display_count = 0


for index, lead in enumerate(
    st.session_state.property_enquiries
):

    if (
        filter_status != "All"
        and lead["status"]
        != filter_status
    ):

        continue


    display_count += 1


    st.markdown(
        f"""
        <div class="lead-card">

        <h2>
        🏡 {lead["property"]}
        </h2>

        <p>
        📍 {lead["location"]}
        </p>

        <p>
        👤 {lead["name"]}
        &nbsp; • &nbsp;
        📱 {lead["mobile"]}
        </p>

        <p>
        📧 {lead.get("email", "Not provided")}
        </p>

        <p>
        🎯 Enquiry Type:
        <b>{lead.get("enquiry_type", "General Enquiry")}</b>
        </p>

        <p>
        💬 {lead["message"]}
        </p>

        <p>
        🕐 {lead["time"]}
        </p>

        <h3>
        📌 Status: {lead["status"]}
        </h3>

        </div>
        """,
        unsafe_allow_html=True
    )


    b1, b2, b3 = st.columns(3)


    with b1:

        if st.button(
            "💬 Open Chat",
            key=f"chat_{index}",
            use_container_width=True
        ):

            st.info(
                "💬 Chat system will be connected to the real-time messaging backend."
            )


    with b2:

        if st.button(
            "📞 Request Call",
            key=f"call_{index}",
            use_container_width=True
        ):

            st.success(
                "📞 Call-back request submitted."
            )


            st.session_state.notifications.insert(
                0,
                {
                    "title":
                    "📞 Call Request Submitted",

                    "message":
                    f"Your call-back request for {lead['property']} has been submitted.",

                    "type":
                    "Enquiry",

                    "time":
                    "Just now",

                    "read":
                    False
                }
            )


    with b3:

        if st.button(
            "📅 Site Visit",
            key=f"visit_{index}",
            use_container_width=True
        ):

            st.success(
                "📅 Site visit request initiated."
            )


            st.session_state.notifications.insert(
                0,
                {
                    "title":
                    "📅 Site Visit Request",

                    "message":
                    f"Your site visit request for {lead['property']} has been initiated.",

                    "type":
                    "Site Visit",

                    "time":
                    "Just now",

                    "read":
                    False
                }
            )


if display_count == 0:

    st.info(
        "📋 No enquiries found."
    )


# ============================================================
# SECTION 3 — NOTIFICATION CENTRE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔔 Notification Centre
</h2>

<p>
Manage all your property-related notifications in one place.
</p>

</div>
""", unsafe_allow_html=True)


filter_type = st.selectbox(
    "📂 Filter Notifications",
    [
        "All",
        "Unread",
        "Property",
        "Site Visit",
        "Security",
        "Saved",
        "Market",
        "Enquiry"
    ]
)


# ============================================================
# NOTIFICATION ACTIONS
# ============================================================

a1, a2 = st.columns(2)


with a1:

    if st.button(
        "✅ Mark All As Read",
        use_container_width=True
    ):

        for n in st.session_state.notifications:

            n["read"] = True

        st.success(
            "All notifications marked as read."
        )

        st.rerun()


with a2:

    if st.button(
        "🗑️ Clear All Notifications",
        use_container_width=True
    ):

        st.session_state.notifications = []

        st.success(
            "All notifications cleared."
        )

        st.rerun()


# ============================================================
# DISPLAY NOTIFICATIONS
# ============================================================

displayed_notifications = 0


for index, notification in enumerate(
    st.session_state.notifications
):

    show = True


    if filter_type == "Unread":

        show = not notification["read"]


    elif filter_type != "All":

        show = (
            notification["type"]
            ==
            filter_type
        )


    if not show:

        continue


    displayed_notifications += 1


    css_class = (

        "notification unread"

        if not notification["read"]

        else

        "notification"

    )


    status = (

        "🟣 NEW"

        if not notification["read"]

        else

        "✓ READ"

    )


    st.markdown(
        f"""
        <div class="{css_class}">

        <h2>
        {notification["title"]}
        </h2>

        <p>
        {notification["message"]}
        </p>

        <p>
        🕐 {notification["time"]}
        &nbsp;&nbsp;
        •
        &nbsp;&nbsp;
        📂 {notification["type"]}
        &nbsp;&nbsp;
        •
        &nbsp;&nbsp;
        {status}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    n1, n2 = st.columns(2)


    with n1:

        if not notification["read"]:

            if st.button(
                "✓ Mark as Read",
                key=f"notification_read_{index}",
                use_container_width=True
            ):

                notification["read"] = True

                st.rerun()


    with n2:

        if st.button(
            "🗑️ Remove",
            key=f"notification_remove_{index}",
            use_container_width=True
        ):

            st.session_state.notifications.pop(
                index
            )

            st.rerun()


if displayed_notifications == 0:

    st.info(
        "🔔 No notifications found for this filter."
    )


# ============================================================
# SECTION 4 — NOTIFICATION PREFERENCES
# ============================================================

st.markdown("""
<div class="section">

<h2>
⚙️ Notification Preferences
</h2>

<p>
Choose which updates you would like to receive.
</p>

</div>
""", unsafe_allow_html=True)


p1, p2 = st.columns(2)


with p1:

    st.markdown(
        '<div class="notification">',
        unsafe_allow_html=True
    )


    property_alerts = st.toggle(
        "🏡 New Property Matches",
        value=True,
        key="pref_property_alerts"
    )


    price_alerts = st.toggle(
        "💰 Price Change Alerts",
        value=True,
        key="pref_price_alerts"
    )


    saved_alerts = st.toggle(
        "❤️ Saved Property Updates",
        value=True,
        key="pref_saved_alerts"
    )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


with p2:

    st.markdown(
        '<div class="notification">',
        unsafe_allow_html=True
    )


    site_visit_alerts = st.toggle(
        "📅 Site Visit Updates",
        value=True,
        key="pref_site_visit_alerts"
    )


    enquiry_alerts = st.toggle(
        "💬 Enquiry & Chat Updates",
        value=True,
        key="pref_enquiry_alerts"
    )


    security_alerts = st.toggle(
        "🛡️ Security & Login Alerts",
        value=True,
        key="pref_security_alerts"
    )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# DELIVERY CHANNELS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📲 Notification Channels
</h2>

<p>
Choose where you want to receive notifications.
</p>

</div>
""", unsafe_allow_html=True)


channels = st.multiselect(
    "📲 Receive notifications through",
    [
        "🔔 In-App Notifications",
        "📱 SMS",
        "💬 WhatsApp",
        "📧 Email",
        "🔔 Push Notifications"
    ],
    default=[
        "🔔 In-App Notifications"
    ]
)


if st.button(
    "💾 SAVE NOTIFICATION SETTINGS",
    use_container_width=True
):

    st.success(
        "🎉 Your notification preferences have been saved."
    )


# ============================================================
# SMART COMMUNICATION FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤖 Smart Communication Features
</h2>

<p>
Future versions will connect buyers and property professionals
through an intelligent communication ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.markdown("""
    <div class="info-card">

    <h3>
    💬 Real-Time Chat
    </h3>

    <p>
    Buyer and property representative
    can communicate securely.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="info-card">

    <h3>
    📞 Smart Call Request
    </h3>

    <p>
    Request a callback without
    publicly exposing mobile numbers.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="info-card">

    <h3>
    🧠 Lead Intelligence
    </h3>

    <p>
    Future AI tools can help property professionals
    prioritise genuine buyer enquiries.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# PRIVACY & SECURITY
# ============================================================

st.markdown("""
<div class="privacy-card">

<h2>
🛡️ Privacy First Communication
</h2>

<p>
Your personal contact information should remain protected.
Future versions will support secure messaging, OTP verification,
spam protection and controlled contact sharing.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY FRAUD ALERT
# ============================================================

st.markdown("""
<div class="alert-card">

<h2>
⚠️ Stay Safe From Property Fraud
</h2>

<p>
Never transfer money to an unknown person without verifying
the property, owner and documents.
</p>

<p>
FirstChoice Property Hub will introduce stronger verification
and fraud-detection tools in future versions.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART PROPERTY ALERT ENGINE
# ============================================================

st.markdown("""
<div class="smart-card">

<h2>
🤖 Smart Property Alert Engine
</h2>

<p>
Future versions will automatically analyse your searches,
saved properties, preferred locations and budget to send
personalised property recommendations.
</p>

<p>
🎯 Better Matches
&nbsp; • &nbsp;
📈 Price Alerts
&nbsp; • &nbsp;
📍 Location Alerts
&nbsp; • &nbsp;
🏡 New Listings
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="card">

<h3>
🔔💬 FirstChoice Property Hub — Smart Communication Center
</h3>

<p>
One unified place for property enquiries, leads,
notifications and communication.
</p>

</div>
""", unsafe_allow_html=True)
