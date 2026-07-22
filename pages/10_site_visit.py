import streamlit as st
from datetime import date, time

# ============================================================
# PAGE 10 — SITE VISIT BOOKING
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Schedule Site Visit | FirstChoice Property Hub",
    page_icon="📅",
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

.card {
    padding: 30px;
    border-radius: 28px;
    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

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
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
📅 Schedule Your Property Visit
</h1>

<p>
See it. Feel it. Experience it.
Book a convenient site visit before making your property decision.
</p>

<p>
🏡 Personal Visit &nbsp; • &nbsp;
📍 Location Assistance &nbsp; • &nbsp;
🤝 Property Expert Support
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
Choose the property you would like to visit.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)


property_name = st.selectbox(
    "Property",
    [
        "Premium 3 BHK Luxury Apartment — Civil Lines",
        "Modern 4 BHK Premium Villa — Wardha Road",
        "Premium Residential Plot — Amravati Road",
        "Commercial Office Space — MIHAN",
        "Luxury Villa — Seminary Hills"
    ]
)


c1, c2 = st.columns(2)


with c1:

    st.info(
        "📍 Location: Nagpur, Maharashtra"
    )


with c2:

    st.info(
        "🛡️ Verification: Available"
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# VISIT DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🗓️ Choose Your Visit Schedule
</h2>

<p>
Select your preferred date and time.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)


c3, c4 = st.columns(2)


with c3:

    visit_date = st.date_input(
        "📅 Preferred Visit Date",
        min_value=date.today()
    )


with c4:

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


c5, c6 = st.columns(2)


with c5:

    visitor_name = st.text_input(
        "Full Name *",
        placeholder="Enter your full name"
    )


with c6:

    visitor_mobile = st.text_input(
        "Mobile Number *",
        max_chars=10,
        placeholder="10 digit mobile number"
    )


visitor_email = st.text_input(
    "Email Address",
    placeholder="example@email.com"
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
# SMART VISIT OPTIONS
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
    "I agree to be contacted by FirstChoice Property Hub or the property representative regarding this site visit."
)


# ============================================================
# SUBMIT
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

        st.markdown(
            f"""
            <div class="success-card">

            <h2>
            🎉 Site Visit Request Submitted!
            </h2>

            <p>
            Your request for:
            <b>{property_name}</b>
            </p>

            <p>
            📅 Date: {visit_date}
            </p>

            <p>
            ⏰ Time: {visit_time}
            </p>

            <p>
            👤 Visitor: {visitor_name}
            </p>

            <p>
            📞 Mobile: {visitor_mobile}
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
# TRUST & SAFETY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🛡️ Your Safety Matters
</h2>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

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


with s2:

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


with s3:

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
