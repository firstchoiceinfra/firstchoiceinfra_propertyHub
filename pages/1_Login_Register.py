import streamlit as st
import random

st.set_page_config(
    page_title="Login | FirstChoice Property Hub",
    page_icon="🔐",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fb;
    }

    .login-title {
        text-align: center;
        color: #0b1f3a;
        font-size: 32px;
        font-weight: bold;
    }

    .login-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 25px;
    }

    .info-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SESSION STATE
# -----------------------------

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "demo_otp" not in st.session_state:
    st.session_state.demo_otp = None

if "verified" not in st.session_state:
    st.session_state.verified = False

if "mobile" not in st.session_state:
    st.session_state.mobile = ""

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="login-title">🔐 Property Hub Login</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="login-subtitle">Login or create your FirstChoice Property Hub account</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="info-box">', unsafe_allow_html=True)

# -----------------------------
# MOBILE NUMBER
# -----------------------------

mobile = st.text_input(
    "📱 Enter Mobile Number",
    placeholder="Enter 10 digit mobile number",
    max_chars=10
)

# -----------------------------
# SEND OTP
# -----------------------------

if st.button(
    "📨 Send OTP",
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

# -----------------------------
# OTP VERIFICATION
# -----------------------------

if st.session_state.otp_sent:

    st.markdown("---")

    st.subheader("🔑 Verify OTP")

    entered_otp = st.text_input(
        "Enter 6 digit OTP",
        max_chars=6
    )

    if st.button(
        "✅ Verify OTP",
        use_container_width=True
    ):

        if entered_otp == str(
            st.session_state.demo_otp
        ):

            st.session_state.verified = True

            st.success(
                "Mobile number verified successfully!"
            )

        else:

            st.error(
                "Invalid OTP. Please try again."
            )

# -----------------------------
# USER REGISTRATION
# -----------------------------

if st.session_state.verified:

    st.markdown("---")

    st.subheader(
        "👤 Create Your FirstChoice Profile"
    )

    full_name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email Address"
    )

    user_type = st.selectbox(
        "Select Account Type",
        [
            "Buyer",
            "Owner / Seller",
            "Tenant",
            "Real Estate Agent",
            "Builder / Developer",
            "Business Partner"
        ]
    )

    city = st.text_input(
        "City"
    )

    if st.button(
        "🚀 Create My FirstChoice ID",
        use_container_width=True
    ):

        if not full_name or not city:

            st.warning(
                "Please enter your name and city."
            )

        else:

            firstchoice_id = (
                "FC-"
                + st.session_state.mobile[-4:]
                + "-"
                + str(random.randint(1000, 9999))
            )

            st.success(
                "🎉 Your FirstChoice Property Hub ID has been created!"
            )

            st.info(
                f"Your FirstChoice ID: {firstchoice_id}"
            )

            st.write(
                f"Account Type: **{user_type}**"
            )

            st.write(
                f"Mobile: **+91 {st.session_state.mobile}**"
            )

# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
    """
    <br>
    <center>
    <small>
    FirstChoice Infra Property Hub<br>
    India's Smart Real Estate Marketplace
    </small>
    </center>
    """,
    unsafe_allow_html=True
)
