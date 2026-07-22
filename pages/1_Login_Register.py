import streamlit as st
import random

# =========================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PREMIUM LOGIN & REGISTRATION
# =========================================================

st.set_page_config(
    page_title="FirstChoice Property Hub | Login",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "otp_sent": False,
    "demo_otp": None,
    "verified": False,
    "mobile": "",
    "profile_created": False,
    "firstchoice_id": "",
    "show_profile": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main Background */
    .stApp {
        background:
        linear-gradient(
            135deg,
            #f5f7fb 0%,
            #eef2f7 50%,
            #ffffff 100%
        );
    }

    /* Hide Streamlit Default */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Brand */
    .brand {
        font-size: 28px;
        font-weight: 800;
        color: #0b1f3a;
        letter-spacing: 1px;
    }

    .brand-sub {
        font-size: 13px;
        color: #b08d35;
        letter-spacing: 2px;
        font-weight: 600;
    }

    /* Hero */
    .hero {
        background:
        linear-gradient(
            135deg,
            rgba(7, 27, 52, 0.98),
            rgba(18, 63, 115, 0.95)
        );

        padding: 55px 45px;

        border-radius: 28px;

        color: white;

        box-shadow:
        0px 20px 50px rgba(11,31,58,0.20);

        margin-bottom: 35px;
    }

    .hero h1 {
        font-size: 44px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.9;
    }

    /* Cards */
    .premium-card {
        background: rgba(255,255,255,0.95);

        padding: 30px;

        border-radius: 22px;

        box-shadow:
        0px 10px 35px rgba(0,0,0,0.08);

        border: 1px solid rgba(0,0,0,0.04);

        margin-bottom: 25px;
    }

    /* Section */
    .section-title {
        color: #0b1f3a;
        font-size: 25px;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Verification */
    .verified {
        background: #eaf8f0;
        color: #18794e;
        padding: 12px 18px;
        border-radius: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .pending {
        background: #fff7e6;
        color: #9a6700;
        padding: 12px 18px;
        border-radius: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* ID Card */
    .id-card {
        background:
        linear-gradient(
            135deg,
            #0b1f3a,
            #173f70
        );

        color: white;

        padding: 30px;

        border-radius: 20px;

        box-shadow:
        0px 15px 35px rgba(11,31,58,0.25);

        margin-top: 20px;
    }

    .id-number {
        font-size: 30px;
        font-weight: 800;
        color: #e3bd63;
        letter-spacing: 2px;
    }

    /* Footer */
    .footer {
        margin-top: 60px;
        padding: 35px;
        background: #071b34;
        color: white;
        border-radius: 22px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BRAND HEADER
# =========================================================

header1, header2 = st.columns([3, 1])

with header1:

    st.markdown(
        """
        <div class="brand">
        🏠 FIRSTCHOICE INFRA
        </div>

        <div class="brand-sub">
        PROPERTY HUB
        </div>
        """,
        unsafe_allow_html=True
    )


with header2:

    st.markdown(
        """
        <div style="
        text-align:right;
        color:#0b1f3a;
        font-weight:600;
        padding-top:10px;
        ">
        🇮🇳 India's Smart Real Estate Marketplace
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <h1>Welcome to FirstChoice Property Hub</h1>

        <p>
        One trusted identity for buying, selling, renting
        and investing in real estate across India.
        </p>

        <p>
        🔐 Secure Identity &nbsp; • &nbsp;
        🏠 Verified Properties &nbsp; • &nbsp;
        🤝 Trusted Marketplace
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PROGRESS
# =========================================================

if not st.session_state.verified:

    st.progress(
        0.25,
        text="Step 1 of 4 — Mobile Verification"
    )

elif not st.session_state.profile_created:

    st.progress(
        0.60,
        text="Step 2 of 4 — Create Your Profile"
    )

else:

    st.progress(
        1.0,
        text="Step 4 of 4 — Profile Ready"
    )


# =========================================================
# STEP 1 — MOBILE LOGIN
# =========================================================

if not st.session_state.verified:

    st.markdown(
        '<div class="section-title">🔐 Secure Login & Registration</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.write(
        "Enter your current mobile number to create or access your FirstChoice Property Hub account."
    )

    mobile = st.text_input(
        "📱 Mobile Number",
        placeholder="Enter 10 digit mobile number",
        max_chars=10
    )

    if st.button(
        "📨 Send Secure OTP",
        use_container_width=True
    ):

        if len(mobile) != 10 or not mobile.isdigit():

            st.error(
                "Please enter a valid 10 digit mobile number."
            )

        else:

            otp = random.randint(
                100000,
                999999
            )

            st.session_state.mobile = mobile

            st.session_state.demo_otp = otp

            st.session_state.otp_sent = True

            st.success(
                "OTP generated successfully."
            )

            st.info(
                f"Demo OTP: {otp}"
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# STEP 1.5 — OTP VERIFICATION
# =========================================================

if (
    st.session_state.otp_sent
    and not st.session_state.verified
):

    st.markdown(
        '<div class="section-title">🔑 Verify Your Mobile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.write(
        f"OTP sent to +91 {st.session_state.mobile}"
    )

    entered_otp = st.text_input(
        "Enter 6 Digit OTP",
        max_chars=6
    )

    if st.button(
        "✅ Verify & Continue",
        use_container_width=True
    ):

        if entered_otp == str(
            st.session_state.demo_otp
        ):

            st.session_state.verified = True

            st.success(
                "Mobile number verified successfully!"
            )

            st.rerun()

        else:

            st.error(
                "Invalid OTP. Please enter the correct OTP."
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# STEP 2 — PROFILE CREATION
# =========================================================

if (
    st.session_state.verified
    and not st.session_state.profile_created
):

    st.markdown(
        '<div class="section-title">👤 Create Your FirstChoice Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )

    st.success(
        "📱 Mobile Verified Successfully"
    )

    profile_col1, profile_col2 = st.columns(2)

    with profile_col1:

        full_name = st.text_input(
            "Full Name *",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email Address",
            placeholder="yourname@email.com"
        )

        state = st.selectbox(
            "State",
            [
                "Select State",
                "Maharashtra",
                "Delhi",
                "Karnataka",
                "Gujarat",
                "Telangana",
                "Tamil Nadu",
                "Uttar Pradesh",
                "West Bengal",
                "Rajasthan",
                "Other"
            ]
        )

    with profile_col2:

        city = st.text_input(
            "City",
            placeholder="Enter your city"
        )

        account_type = st.selectbox(
            "Account Type",
            [
                "Buyer",
                "Owner / Seller",
                "Tenant",
                "Real Estate Agent / Broker",
                "Builder / Developer",
                "Business Partner"
            ]
        )

        profile_photo = st.file_uploader(
            "Profile Photo",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

    st.markdown(
        "### 🛡️ Your Verification Status"
    )

    ver1, ver2, ver3 = st.columns(3)

    with ver1:

        st.markdown(
            """
            <div class="verified">
            ✅ Mobile Verified
            </div>
            """,
            unsafe_allow_html=True
        )

    with ver2:

        st.markdown(
            """
            <div class="pending">
            ⏳ Identity Verification
            </div>
            """,
            unsafe_allow_html=True
        )

    with ver3:

        st.markdown(
            """
            <div class="pending">
            ⏳ Professional Verification
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        "Identity and professional verification will be securely completed through authorized verification services in the production version."
    )

    if st.button(
        "🚀 Create My FirstChoice ID",
        use_container_width=True
    ):

        if (
            not full_name
            or not city
            or state == "Select State"
        ):

            st.warning(
                "Please complete your Full Name, State and City."
            )

        else:

            firstchoice_id = (
                "FC-"
                + st.session_state.mobile[-4:]
                + "-"
                + str(
                    random.randint(
                        10000,
                        99999
                    )
                )
            )

            st.session_state.firstchoice_id = firstchoice_id

            st.session_state.profile_created = True

            st.success(
                "🎉 Your FirstChoice Property Hub profile has been created!"
            )

            st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# STEP 3 — PROFILE DASHBOARD
# =========================================================

if st.session_state.profile_created:

    st.markdown(
        '<div class="section-title">🎉 Welcome to Your FirstChoice Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="id-card">

            <div style="font-size:15px;">
            FIRSTCHOICE PROPERTY HUB
            </div>

            <br>

            <div style="font-size:18px;">
            Your FirstChoice ID
            </div>

            <div class="id-number">
            {st.session_state.firstchoice_id}
            </div>

            <br>

            <div>
            📱 +91 {st.session_state.mobile}
            </div>

            <br>

            <div style="color:#b9c7d8;">
            This is your unique FirstChoice Property Hub identity.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">🛡️ Verification Center</div>',
        unsafe_allow_html=True
    )

    v1, v2, v3 = st.columns(3)

    with v1:

        st.markdown(
            """
            <div class="premium-card">

            <h3>📱 Mobile</h3>

            <div class="verified">
            ✅ Verified
            </div>

            <p>
            Your mobile number is verified.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with v2:

        st.markdown(
            """
            <div class="premium-card">

            <h3>🪪 Identity</h3>

            <div class="pending">
            ⏳ Pending
            </div>

            <p>
            Secure identity verification available in production.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with v3:

        st.markdown(
            """
            <div class="premium-card">

            <h3>🏢 Professional</h3>

            <div class="pending">
            ⏳ Pending
            </div>

            <p>
            Professional verification for agents and businesses.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# QUICK ACTIONS
# =========================================================

if st.session_state.profile_created:

    st.markdown(
        '<div class="section-title">🚀 Quick Actions</div>',
        unsafe_allow_html=True
    )

    q1, q2, q3, q4 = st.columns(4)

    with q1:

        st.button(
            "🏠 Post Property",
            use_container_width=True
        )

    with q2:

        st.button(
            "🔍 Search Properties",
            use_container_width=True
        )

    with q3:

        st.button(
            "❤️ Saved Properties",
            use_container_width=True
        )

    with q4:

        st.button(
            "👤 My Profile",
            use_container_width=True
        )


# =========================================================
# SECURITY NOTICE
# =========================================================

st.markdown(
    """
    <div class="premium-card">

    <h3>🔐 Your Privacy & Security</h3>

    <p>
    FirstChoice Property Hub is designed with secure
    identity verification and privacy-first principles.
    </p>

    <p>
    Your sensitive identity information should only be
    processed through authorized verification services.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    <h2>FIRSTCHOICE INFRA PROPERTY HUB</h2>

    <p>
    India's Smart Real Estate Marketplace
    </p>

    <p>
    Buy • Sell • Rent • Invest
    </p>

    <br>

    <small>
    © FirstChoice Infra Property Hub
    </small>

    </div>
    """,
    unsafe_allow_html=True
)
