import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 11 — NOTIFICATIONS & ALERTS
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Notifications | FirstChoice Property Hub",
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

/* HERO */

.hero {
    padding: 45px;
    border-radius: 32px;
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
    0 20px 65px
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
}

/* SECTION */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 25px 30px;

    border-radius: 24px;

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
    0 12px 35px
    rgba(79,70,229,0.18);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}

/* NOTIFICATION CARD */

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

/* UNREAD */

.unread {
    border-left: 6px solid #7C3AED;
}

/* SUCCESS */

.success-card {
    padding: 28px;
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
    rgba(5,150,105,0.22);
}

/* ALERT */

.alert-card {
    padding: 25px;
    border-radius: 25px;

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
# SESSION STATE
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
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🔔 Notifications & Alerts
</h1>

<p>
Stay updated with your property journey.
Never miss a new listing, enquiry, site visit or important update.
</p>

<p>
🏡 Property Matches • 📅 Site Visits • 💬 Enquiries • 🛡️ Security
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NOTIFICATION COUNT
# ============================================================

unread_count = sum(
    1
    for n in st.session_state.notifications
    if not n["read"]
)


c1, c2, c3 = st.columns(3)


with c1:

    st.metric(
        "🔔 Total Notifications",
        len(st.session_state.notifications)
    )


with c2:

    st.metric(
        "🟣 Unread",
        unread_count
    )


with c3:

    st.metric(
        "✅ Read",
        len(st.session_state.notifications)
        - unread_count
    )


# ============================================================
# FILTER
# ============================================================

st.markdown("""
<div class="section">

<h2>
📂 Notification Centre
</h2>

<p>
Manage all your property-related notifications in one place.
</p>

</div>
""", unsafe_allow_html=True)


filter_type = st.selectbox(
    "Filter Notifications",
    [
        "All",
        "Unread",
        "Property",
        "Site Visit",
        "Security",
        "Saved",
        "Market"
    ]
)


# ============================================================
# ACTION BUTTONS
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

displayed = 0


for index, notification in enumerate(
    st.session_state.notifications
):

    show = True


    if filter_type == "Unread":

        show = not notification["read"]


    elif filter_type != "All":

        show = (
            notification["type"]
            == filter_type
        )


    if not show:

        continue


    displayed += 1


    css_class = (
        "notification unread"
        if not notification["read"]
        else "notification"
    )


    status = (
        "🟣 NEW"
        if not notification["read"]
        else "✓ READ"
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


    b1, b2 = st.columns(2)


    with b1:

        if not notification["read"]:

            if st.button(
                "✓ Mark as Read",
                key=f"read_{index}",
                use_container_width=True
            ):

                notification["read"] = True

                st.rerun()


    with b2:

        if st.button(
            "🗑️ Remove",
            key=f"remove_{index}",
            use_container_width=True
        ):

            st.session_state.notifications.pop(
                index
            )

            st.rerun()


# ============================================================
# EMPTY STATE
# ============================================================

if displayed == 0:

    st.info(
        "🔔 No notifications found for this filter."
    )


# ============================================================
# NOTIFICATION PREFERENCES
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
        value=True
    )

    price_alerts = st.toggle(
        "💰 Price Change Alerts",
        value=True
    )

    saved_alerts = st.toggle(
        "❤️ Saved Property Updates",
        value=True
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
        value=True
    )

    enquiry_alerts = st.toggle(
        "💬 Enquiry & Chat Updates",
        value=True
    )

    security_alerts = st.toggle(
        "🛡️ Security & Login Alerts",
        value=True
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

</div>
""", unsafe_allow_html=True)


channels = st.multiselect(
    "Receive notifications through",
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
# IMPORTANT ALERT
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
# FUTURE SMART NOTIFICATION ENGINE
# ============================================================

st.markdown("""
<div class="success-card">

<h2>
🤖 Smart Property Alert Engine
</h2>

<p>
Future versions will automatically analyse your searches,
saved properties, preferred locations and budget to send
personalised property recommendations.
</p>

<p>
🎯 Better Matches &nbsp; • &nbsp;
📈 Price Alerts &nbsp; • &nbsp;
📍 Location Alerts &nbsp; • &nbsp;
🏡 New Listings
</p>

</div>
""", unsafe_allow_html=True)
