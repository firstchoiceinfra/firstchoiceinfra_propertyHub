import streamlit as st
from datetime import datetime

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 19 - NOTIFICATIONS CENTER
# ============================================================

st.set_page_config(
    page_title="Notifications | FirstChoice Property Hub",
    page_icon="🔔",
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

/* NOTIFICATION */

.notification-card {
    padding: 26px;

    border-radius: 26px;

    background: white;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    margin-bottom: 15px;

    border-left:
    6px solid #7C3AED;
}

.notification-unread {
    padding: 26px;

    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #EEF2FF,
        #FDF4FF,
        #FFFFFF
    );

    box-shadow:
    0 15px 40px
    rgba(124,58,237,0.14);

    margin-bottom: 15px;

    border-left:
    6px solid #EC4899;
}

/* SUMMARY */

.summary-card {
    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);
}

/* SECURITY */

.security-card {
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
    0 20px 50px
    rgba(5,150,105,0.22);
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
PROPERTY HUB • SMART NOTIFICATIONS • REAL-TIME ALERTS
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🔔 Notification Center
</div>

<div class="hero-subtitle">
Stay updated with property enquiries, site visits,
verification, price changes and important account alerts.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SUMMARY
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Notification Overview
</div>

<div class="section-subtitle">
Your latest property marketplace activity.
</div>

</div>
""", unsafe_allow_html=True)


n1, n2, n3, n4 = st.columns(4)


with n1:

    st.metric(
        "🔔 Total",
        "32"
    )


with n2:

    st.metric(
        "🔴 Unread",
        "7"
    )


with n3:

    st.metric(
        "💬 Enquiries",
        "8"
    )


with n4:

    st.metric(
        "📅 Site Visits",
        "4"
    )


# ============================================================
# FILTER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Filter Notifications
</div>

<div class="section-subtitle">
Find important alerts quickly.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2 = st.columns(2)


with f1:

    notification_filter = st.selectbox(
        "Notification Type",
        [
            "All Notifications",
            "Property Updates",
            "Enquiries",
            "Site Visits",
            "Verification",
            "Price Alerts",
            "Security",
            "Recommendations"
        ]
    )


with f2:

    read_filter = st.selectbox(
        "Notification Status",
        [
            "All",
            "Unread",
            "Read"
        ]
    )


# ============================================================
# ACTION BAR
# ============================================================

a1, a2 = st.columns(2)


with a1:

    if st.button(
        "✅ MARK ALL AS READ",
        use_container_width=True
    ):

        st.success(
            "All notifications marked as read."
        )


with a2:

    if st.button(
        "🗑️ CLEAR ALL NOTIFICATIONS",
        use_container_width=True
    ):

        st.warning(
            "Clear all confirmation required."
        )


# ============================================================
# NOTIFICATION DATA
# ============================================================

notifications = [

    {
        "icon": "💬",
        "title": "New Property Enquiry",
        "message":
        "A property advisor has responded to your enquiry about Premium 3 BHK Luxury Apartment.",
        "time": "5 minutes ago",
        "type": "Enquiries",
        "unread": True
    },

    {
        "icon": "📅",
        "title": "Site Visit Confirmed",
        "message":
        "Your site visit for Luxury Independent Villa has been confirmed for 28 July 2026.",
        "time": "1 hour ago",
        "type": "Site Visits",
        "unread": True
    },

    {
        "icon": "💰",
        "title": "Price Drop Alert",
        "message":
        "The price of a property saved in your wishlist has been reduced.",
        "time": "3 hours ago",
        "type": "Price Alerts",
        "unread": True
    },

    {
        "icon": "🛡️",
        "title": "Property Verification Update",
        "message":
        "Your property document verification is currently under review.",
        "time": "Yesterday",
        "type": "Verification",
        "unread": True
    },

    {
        "icon": "🏠",
        "title": "New Property Match",
        "message":
        "5 new properties matching your saved search are now available.",
        "time": "Yesterday",
        "type": "Recommendations",
        "unread": True
    },

    {
        "icon": "📱",
        "title": "Security Alert",
        "message":
        "Your mobile number was successfully verified.",
        "time": "2 days ago",
        "type": "Security",
        "unread": False
    },

    {
        "icon": "❤️",
        "title": "Saved Property Update",
        "message":
        "The owner of a property in your wishlist has updated the property details.",
        "time": "3 days ago",
        "type": "Property Updates",
        "unread": False
    }

]


# ============================================================
# NOTIFICATION LIST
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📬 Your Notifications
</div>

<div class="section-subtitle">
All your important property activity in one place.
</div>

</div>
""", unsafe_allow_html=True)


for index, notification in enumerate(notifications):

    show_notification = True

    if (
        notification_filter !=
        "All Notifications"
        and
        notification["type"] !=
        notification_filter
    ):

        show_notification = False


    if (
        read_filter == "Unread"
        and
        not notification["unread"]
    ):

        show_notification = False


    if (
        read_filter == "Read"
        and
        notification["unread"]
    ):

        show_notification = False


    if show_notification:

        card_class = (
            "notification-unread"
            if notification["unread"]
            else
            "notification-card"
        )


        unread_label = (
            "🔴 NEW"
            if notification["unread"]
            else
            "✓ READ"
        )


        st.markdown(
            f"""
            <div class="{card_class}">

            <h2>
            {notification["icon"]}
            {notification["title"]}
            </h2>

            <p>
            {notification["message"]}
            </p>

            <small>
            🕒 {notification["time"]}
            &nbsp;&nbsp;
            •
            &nbsp;&nbsp;
            {unread_label}
            </small>

            </div>
            """,
            unsafe_allow_html=True
        )


        b1, b2, b3 = st.columns(3)


        with b1:

            if st.button(
                "✓ Mark Read",
                key=f"read_{index}",
                use_container_width=True
            ):

                st.success(
                    "Notification marked as read."
                )


        with b2:

            if st.button(
                "👁️ View",
                key=f"view_{index}",
                use_container_width=True
            ):

                st.info(
                    "Related activity will open."
                )


        with b3:

            if st.button(
                "🗑️ Delete",
                key=f"delete_{index}",
                use_container_width=True
            ):

                st.warning(
                    "Notification deleted."
                )


# ============================================================
# PRICE ALERTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💰 Smart Price Alerts
</div>

<div class="section-subtitle">
Get notified when saved properties change their price.
</div>

</div>
""", unsafe_allow_html=True)


p1, p2, p3 = st.columns(3)


with p1:

    st.success(
        """
        📉 **Price Reduced**

        Premium 3 BHK Apartment

        ₹1.35 Cr → ₹1.25 Cr
        """
    )


with p2:

    st.info(
        """
        📈 **Price Updated**

        Luxury Villa

        New price information available.
        """
    )


with p3:

    st.warning(
        """
        🔔 **Price Watch**

        You are watching 8 properties.
        """
    )


# ============================================================
# PROPERTY MATCH ALERT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 New Property Match
</div>

<div class="section-subtitle">
Properties matching your preferences.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="summary-card">

<h2>
🎯 We Found New Properties For You
</h2>

<p>
Based on your recent searches and saved properties,
FirstChoice Property Hub found new listings matching your preferences.
</p>

<p>
🏠 12 Residential Properties
</p>

<p>
📍 8 Properties Near Your Preferred Location
</p>

<p>
💰 6 Properties Within Your Budget
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "🔎 VIEW MATCHED PROPERTIES",
    use_container_width=True
):

    st.info(
        "Property discovery page will open."
    )


# ============================================================
# SECURITY ALERTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔐 Security & Account Alerts
</div>

<div class="section-subtitle">
Important notifications related to your account security.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="security-card">

<h2>
🛡️ Your Account is Secure
</h2>

<p>
📱 Mobile number verification completed.
</p>

<p>
🔐 No suspicious login activity detected.
</p>

<p>
🛡️ Account security is active.
</p>

<p>
⚠️ Never share your OTP or password with anyone.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NOTIFICATION PREFERENCES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚙️ Notification Preferences
</div>

<div class="section-subtitle">
Choose how you want to receive important updates.
</div>

</div>
""", unsafe_allow_html=True)


pref1, pref2 = st.columns(2)


with pref1:

    st.checkbox(
        "📱 Mobile / SMS Notifications",
        value=True
    )

    st.checkbox(
        "📧 Email Notifications",
        value=True
    )

    st.checkbox(
        "💬 Enquiry & Chat Alerts",
        value=True
    )


with pref2:

    st.checkbox(
        "📅 Site Visit Reminders",
        value=True
    )

    st.checkbox(
        "💰 Price Drop Alerts",
        value=True
    )

    st.checkbox(
        "🏠 New Property Matches",
        value=True
    )


if st.button(
    "💾 SAVE NOTIFICATION SETTINGS",
    use_container_width=True
):

    st.success(
        "Notification preferences saved successfully."
    )


# ============================================================
# SMART NOTIFICATION ENGINE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 Smart Notification Engine
</div>

<div class="section-subtitle">
Future AI-powered notification intelligence.
</div>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    st.info(
        """
        🤖 **AI Recommendations**

        Smart property alerts based
        on your search behaviour.
        """
    )


with s2:

    st.success(
        """
        📊 **Personalized Alerts**

        Receive only relevant
        property notifications.
        """
    )


with s3:

    st.warning(
        """
        🚨 **Fraud Detection**

        Get alerts when suspicious
        activity is detected.
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
