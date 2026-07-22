import streamlit as st
from datetime import date, timedelta

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 18 - MY ENQUIRIES & CRM
# ============================================================

st.set_page_config(
    page_title="My Enquiries | FirstChoice Property Hub",
    page_icon="💬",
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

    color:
    rgba(255,255,255,0.88);
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

    color:
    rgba(255,255,255,0.82);
}

/* CRM CARD */

.crm-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

/* PRIORITY */

.priority-card {

    padding: 28px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #DC2626,
        #EC4899,
        #7C3AED
    );

    box-shadow:
    0 18px 45px
    rgba(236,72,153,0.25);
}

/* CHAT */

.chat-card {

    padding: 25px;

    border-radius: 25px;

    background:
    linear-gradient(
        135deg,
        #F8FAFF,
        #FFFFFF,
        #FDF4FF
    );

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);
}

/* TIMELINE */

.timeline-card {

    padding: 25px;

    border-left:
    5px solid #7C3AED;

    background: white;

    border-radius: 15px;

    margin-bottom: 12px;

    box-shadow:
    0 8px 25px
    rgba(0,0,0,0.06);
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
PROPERTY HUB • SMART CRM • PROPERTY COMMUNICATION
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
💬 My Enquiries & Property CRM
</div>

<div class="hero-subtitle">
Manage your property enquiries, conversations, site visits
and follow-ups from one powerful dashboard.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CRM OVERVIEW
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Enquiry Overview
</div>

<div class="section-subtitle">
Track every property enquiry from first contact to final decision.
</div>

</div>
""", unsafe_allow_html=True)


c1, c2, c3, c4, c5 = st.columns(5)


with c1:

    st.metric(
        "💬 Total",
        "24"
    )


with c2:

    st.metric(
        "🆕 New",
        "6"
    )


with c3:

    st.metric(
        "📞 Contacted",
        "8"
    )


with c4:

    st.metric(
        "⭐ Interested",
        "7"
    )


with c5:

    st.metric(
        "✅ Closed",
        "3"
    )


# ============================================================
# FILTER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔎 Manage Your Enquiries
</div>

<div class="section-subtitle">
Search and filter your property conversations.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    search = st.text_input(
        "Search Property",
        placeholder=
        "Search by property or location"
    )


with f2:

    status_filter = st.selectbox(
        "Enquiry Status",
        [
            "All",
            "New",
            "Contacted",
            "Interested",
            "Negotiation",
            "Site Visit",
            "Closed"
        ]
    )


with f3:

    priority_filter = st.selectbox(
        "Priority",
        [
            "All",
            "High Priority",
            "Normal",
            "Low"
        ]
    )


# ============================================================
# PRIORITY LEADS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔥 Priority Follow-ups
</div>

<div class="section-subtitle">
Important enquiries that may need your immediate attention.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="priority-card">

<h2>
🔥 High Priority Property Enquiry
</h2>

<p>
🏠 Premium 3 BHK Luxury Apartment
</p>

<p>
📍 Civil Lines, Nagpur
</p>

<p>
💰 Budget: ₹1 Crore – ₹1.5 Crore
</p>

<p>
📅 Follow-up Due: Tomorrow
</p>

<p>
⭐ Buyer is highly interested
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "📞 FOLLOW UP NOW",
    use_container_width=True
):

    st.info(
        "Follow-up communication module will open."
    )


# ============================================================
# ENQUIRY LIST
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📋 My Property Enquiries
</div>

<div class="section-subtitle">
All your property enquiries in one place.
</div>

</div>
""", unsafe_allow_html=True)


enquiries = [

    {
        "property":
        "Premium 3 BHK Luxury Apartment",

        "location":
        "Civil Lines, Nagpur",

        "contact":
        "FirstChoice Property Advisor",

        "status":
        "⭐ Interested",

        "priority":
        "🔥 High",

        "date":
        "22 July 2026"

    },

    {
        "property":
        "Luxury Independent Villa",

        "location":
        "Baner, Pune",

        "contact":
        "Premium Realty Partner",

        "status":
        "📞 Contacted",

        "priority":
        "Normal",

        "date":
        "20 July 2026"

    },

    {
        "property":
        "Premium Residential Plot",

        "location":
        "Wardha Road, Nagpur",

        "contact":
        "Verified Property Owner",

        "status":
        "📅 Site Visit",

        "priority":
        "🔥 High",

        "date":
        "18 July 2026"

    }

]


for index, enquiry in enumerate(enquiries):

    st.markdown(
        f"""
        <div class="crm-card">

        <h2>
        🏠 {enquiry['property']}
        </h2>

        <p>
        📍 {enquiry['location']}
        </p>

        <p>
        👤 Contact:
        <b>{enquiry['contact']}</b>
        </p>

        <p>
        📊 Status:
        <b>{enquiry['status']}</b>
        </p>

        <p>
        🎯 Priority:
        <b>{enquiry['priority']}</b>
        </p>

        <p>
        📅 Last Activity:
        {enquiry['date']}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    b1, b2, b3, b4 = st.columns(4)


    with b1:

        if st.button(
            "💬 Chat",
            key=f"chat_{index}",
            use_container_width=True
        ):

            st.session_state[
                "selected_enquiry"
            ] = index

            st.success(
                "Chat panel selected."
            )


    with b2:

        if st.button(
            "📞 Callback",
            key=f"callback_{index}",
            use_container_width=True
        ):

            st.info(
                "Callback request sent."
            )


    with b3:

        if st.button(
            "📅 Site Visit",
            key=f"site_{index}",
            use_container_width=True
        ):

            st.info(
                "Site visit booking module opened."
            )


    with b4:

        if st.button(
            "⭐ Priority",
            key=f"priority_{index}",
            use_container_width=True
        ):

            st.success(
                "Enquiry marked as priority."
            )


# ============================================================
# CHAT & COMMUNICATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💬 Secure Property Communication
</div>

<div class="section-subtitle">
Connect with owners, agents and builders regarding your enquiry.
</div>

</div>
""", unsafe_allow_html=True)


selected_contact = st.selectbox(
    "Select Conversation",
    [
        "FirstChoice Property Advisor",
        "Premium Realty Partner",
        "Verified Property Owner"
    ]
)


st.markdown("""
<div class="chat-card">

<h3>
💬 Conversation Preview
</h3>

<p>
👤 <b>Property Advisor:</b>
Hello! Thank you for your interest in the property.
How can we help you?
</p>

<p>
🧑 <b>You:</b>
I would like to know the final price and payment plan.
</p>

<p>
👤 <b>Property Advisor:</b>
We can arrange a site visit and discuss the payment options.
</p>

</div>
""", unsafe_allow_html=True)


message = st.text_area(
    "Write a Message",
    placeholder=
    "Ask about price, documents, payment plan or site visit."
)


if st.button(
    "📤 SEND MESSAGE",
    use_container_width=True
):

    if message:

        st.success(
            "Your message has been sent."
        )

    else:

        st.warning(
            "Please enter a message."
        )


# ============================================================
# CALLBACK REQUEST
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📞 Request a Callback
</div>

<div class="section-subtitle">
Choose a convenient time to receive a call.
</div>

</div>
""", unsafe_allow_html=True)


cb1, cb2 = st.columns(2)


with cb1:

    callback_date = st.date_input(
        "Preferred Callback Date",
        value=date.today()
    )


with cb2:

    callback_time = st.selectbox(
        "Preferred Callback Time",
        [
            "09:00 AM – 11:00 AM",
            "11:00 AM – 01:00 PM",
            "02:00 PM – 04:00 PM",
            "04:00 PM – 06:00 PM",
            "06:00 PM – 08:00 PM"
        ]
    )


callback_reason = st.text_input(
    "Reason for Callback",
    placeholder=
    "Example: Discuss final price and payment plan"
)


if st.button(
    "📞 REQUEST CALLBACK",
    use_container_width=True
):

    st.success(
        "Callback request submitted successfully."
    )


# ============================================================
# FOLLOW-UP REMINDER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔔 Follow-up Reminder
</div>

<div class="section-subtitle">
Never forget an important property follow-up.
</div>

</div>
""", unsafe_allow_html=True)


r1, r2 = st.columns(2)


with r1:

    reminder_date = st.date_input(
        "Reminder Date",
        value=date.today() + timedelta(days=1)
    )


with r2:

    reminder_note = st.text_input(
        "Reminder Note",
        placeholder=
        "Example: Call owner for negotiation"
    )


if st.button(
    "🔔 CREATE REMINDER",
    use_container_width=True
):

    st.success(
        "Follow-up reminder created."
    )


# ============================================================
# ACTIVITY TIMELINE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🕒 Enquiry Activity Timeline
</div>

<div class="section-subtitle">
See the complete history of your property enquiry.
</div>

</div>
""", unsafe_allow_html=True)


timeline = [

    (
        "Today",
        "💬",
        "You sent a message to the property advisor."
    ),

    (
        "Yesterday",
        "📞",
        "Property advisor contacted you."
    ),

    (
        "20 July 2026",
        "📅",
        "Site visit was scheduled."
    ),

    (
        "18 July 2026",
        "❤️",
        "Property added to your saved list."
    ),

    (
        "17 July 2026",
        "🏠",
        "You submitted a property enquiry."
    )

]


for item in timeline:

    st.markdown(
        f"""
        <div class="timeline-card">

        <b>
        {item[1]} {item[0]}
        </b>

        <p>
        {item[2]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# LEAD ANALYTICS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 Your Property Search Analytics
</div>

<div class="section-subtitle">
Understand your property search behaviour.
</div>

</div>
""", unsafe_allow_html=True)


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.metric(
        "🏠 Properties Viewed",
        "67"
    )


with a2:

    st.metric(
        "❤️ Properties Saved",
        "18"
    )


with a3:

    st.metric(
        "💬 Enquiries",
        "24"
    )


with a4:

    st.metric(
        "📅 Site Visits",
        "11"
    )


# ============================================================
# SMART CRM INSIGHTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 Smart Property Search Insights
</div>

<div class="section-subtitle">
AI-powered recommendations for your property journey.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="priority-card">

<h2>
🧠 Your Property Search Profile
</h2>

<p>
📍 You are mostly exploring properties in Nagpur.
</p>

<p>
💰 Your most viewed budget range is ₹50 Lakh – ₹1.5 Crore.
</p>

<p>
🏠 You are showing high interest in residential properties.
</p>

<p>
📅 You have scheduled multiple property visits.
</p>

<p>
🎯 Recommendation: Compare your shortlisted properties
before making your final decision.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Advanced CRM — Coming Next
</div>

<div class="section-subtitle">
Next-generation real estate communication and lead management.
</div>

</div>
""", unsafe_allow_html=True)


x1, x2, x3 = st.columns(3)


with x1:

    st.info(
        """
        🤖 **AI Lead Assistant**

        Smart follow-up suggestions
        and conversation assistance.
        """
    )


with x2:

    st.success(
        """
        💬 **Real-Time Chat**

        Secure buyer-owner-agent
        communication.
        """
    )


with x3:

    st.warning(
        """
        📊 **Lead Intelligence**

        Track enquiry conversion,
        response time and activity.
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
