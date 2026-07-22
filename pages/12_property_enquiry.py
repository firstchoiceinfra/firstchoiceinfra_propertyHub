import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 12 — PROPERTY ENQUIRY & LEAD MANAGEMENT
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Enquiry | FirstChoice Property Hub",
    page_icon="💬",
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

/* CARD */

.card {
    padding: 28px;
    border-radius: 25px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* LEAD CARD */

.lead-card {
    padding: 25px;
    border-radius: 24px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    margin-bottom: 18px;
}

/* SUCCESS */

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
    0 15px 45px
    rgba(5,150,105,0.22);
}

/* INFO */

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

    border: 1px solid #E0E7FF;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
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
💬 Property Enquiry Centre
</h1>

<p>
Connect buyers, owners, agents and builders
through one intelligent property communication platform.
</p>

<p>
🏡 Enquiry • 💬 Chat • 📞 Call • 📅 Site Visit • 🤝 Follow-up
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DASHBOARD METRICS
# ============================================================

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


c1, c2, c3 = st.columns(3)


with c1:

    st.metric(
        "💬 Total Enquiries",
        total_leads
    )


with c2:

    st.metric(
        "🟣 New Enquiries",
        new_leads
    )


with c3:

    st.metric(
        "📞 Follow Ups",
        followups
    )


# ============================================================
# SEND NEW ENQUIRY
# ============================================================

st.markdown("""
<div class="section">

<h2>
✉️ Send Property Enquiry
</h2>

<p>
Interested in a property? Send your enquiry directly to the property representative.
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


c4, c5 = st.columns(2)


with c4:

    buyer_name = st.text_input(
        "👤 Your Name",
        placeholder="Enter your full name"
    )


with c5:

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
    placeholder=
    "Write your enquiry or requirement here..."
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
            The property representative can now contact you.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# MY ENQUIRIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 My Property Enquiries
</h2>

<p>
Track your enquiries and communication status.
</p>

</div>
""", unsafe_allow_html=True)


filter_status = st.selectbox(
    "Filter By Status",
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


    c6, c7, c8 = st.columns(3)


    with c6:

        if st.button(
            "💬 Open Chat",
            key=f"chat_{index}",
            use_container_width=True
        ):

            st.info(
                "Chat system will be connected to the real-time messaging backend."
            )


    with c7:

        if st.button(
            "📞 Request Call",
            key=f"call_{index}",
            use_container_width=True
        ):

            st.success(
                "Call-back request submitted."
            )


    with c8:

        if st.button(
            "📅 Site Visit",
            key=f"visit_{index}",
            use_container_width=True
        ):

            st.success(
                "Site visit request initiated."
            )


if display_count == 0:

    st.info(
        "No enquiries found."
    )


# ============================================================
# SMART COMMUNICATION
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
<div class="success-card">

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
