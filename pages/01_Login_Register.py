import streamlit as st

from core.auth import (
    validate_email,
    validate_mobile,
    normalize_email,
    normalize_mobile,
    send_email_otp,
    send_mobile_otp,
    verify_email_otp,
    verify_mobile_otp,
    both_otp_verified,
    register_user,
    login_user,
    accept_current_user_terms,
    is_logged_in,
    logout_user,
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# LOGIN & REGISTRATION CENTER
# ============================================================

st.set_page_config(
    page_title="Login & Registration | FirstChoice Property Hub",
    page_icon="🔐",
    layout="wide",
)


# ============================================================
# PREMIUM UI CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {

    background:
    radial-gradient(
        circle at top left,
        rgba(59,130,246,0.15),
        transparent 35%
    ),

    radial-gradient(
        circle at bottom right,
        rgba(168,85,247,0.14),
        transparent 35%
    ),

    linear-gradient(
        135deg,
        #F8FAFC,
        #EEF2FF,
        #FAF5FF
    );

}


/* HIDE STREAMLIT DEFAULT UI */

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

.auth-hero {

    padding: 45px;

    border-radius: 35px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #4F46E5,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.28);

    margin-bottom: 35px;

}


.auth-hero h1 {

    font-size: 44px;

    font-weight: 900;

    margin-bottom: 10px;

}


.auth-hero p {

    font-size: 18px;

    line-height: 1.7;

    color:
    rgba(255,255,255,0.88);

}


/* AUTH CARD */

.auth-card {

    padding: 35px;

    border-radius: 30px;

    background:

    rgba(
        255,
        255,
        255,
        0.92
    );

    border:

    1px solid
    rgba(
        255,
        255,
        255,
        0.7
    );

    box-shadow:

    0 20px 60px
    rgba(
        15,
        23,
        42,
        0.10
    );

}


/* INFO CARD */

.info-card {

    padding: 30px;

    border-radius: 28px;

    color: white;

    background:

    linear-gradient(
        135deg,
        #0F172A,
        #1E3A8A,
        #4C1D95
    );

    box-shadow:

    0 20px 55px
    rgba(
        15,
        23,
        42,
        0.20
    );

}


/* OTP STATUS */

.otp-success {

    padding: 18px;

    border-radius: 18px;

    color: #065F46;

    background: #D1FAE5;

    border:
    1px solid #6EE7B7;

}


.otp-warning {

    padding: 18px;

    border-radius: 18px;

    color: #92400E;

    background: #FEF3C7;

    border:
    1px solid #FCD34D;

}


/* TERMS */

.terms-box {

    padding: 25px;

    border-radius: 22px;

    background:

    linear-gradient(
        135deg,
        #EFF6FF,
        #F5F3FF
    );

    border:
    1px solid #C7D2FE;

}


/* FOOTER */

.auth-footer {

    margin-top: 50px;

    padding: 30px;

    border-radius: 25px;

    text-align: center;

    color: white;

    background:

    linear-gradient(
        135deg,
        #020617,
        #1E1B4B,
        #4C1D95
    );

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="auth-hero">

<h1>
🏠 FirstChoice Property Hub
</h1>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Discover • Build
</p>

</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# ALREADY LOGGED IN
# ============================================================

if is_logged_in():

    st.success(
        "You are currently logged in."
    )

    user_name = st.session_state.get(
        "user_name",
        "User"
    )

    user_role = st.session_state.get(
        "user_role",
        "user"
    )

    st.markdown(
        f"""
<div class="auth-card">

<h2>
👋 Welcome, {user_name}
</h2>

<p>
Account Role:
<strong>
{user_role.upper()}
</strong>
</p>

</div>
""",
        unsafe_allow_html=True,
    )


    # ========================================================
    # TERMS ACCEPTANCE
    # ========================================================

    if st.session_state.get(
        "terms_required",
        False
    ):

        st.warning(
            "Your account requires Terms & Conditions acceptance before you can continue."
        )

        st.markdown(
            """
<div class="terms-box">

<h2>
📜 Terms & Conditions
</h2>

<p>
By using FirstChoice Property Hub, you agree to use the platform
lawfully and responsibly.
</p>

<p>
You are responsible for the accuracy of information submitted
through your account.
</p>

<p>
Property listings, images, videos, documents and other content
uploaded by users must not violate applicable laws or third-party rights.
</p>

<p>
Users must not use the platform for fraudulent, misleading,
illegal or unauthorized activities.
</p>

<p>
FirstChoice Property Hub may review, moderate, suspend or remove
content and accounts that violate platform policies or applicable law.
</p>

<p>
Paid services, subscriptions, advertising packages and premium
features are subject to their respective commercial terms,
payment conditions and refund policies.
</p>

<p>
The platform does not guarantee the accuracy, legality,
ownership or quality of every property listing posted by third parties.
Users must independently verify property documents and transaction details.
</p>

<p>
The platform may update its policies, features and terms from time
to time. Continued use after applicable updates may require renewed acceptance.
</p>

<p>
By accepting these Terms & Conditions, you confirm that you have
read and understood the applicable platform policies.
</p>

</div>
""",
            unsafe_allow_html=True,
        )


        terms_accept = st.checkbox(
            "I have read and agree to the Terms & Conditions and Privacy Policy."
        )


        if st.button(
            "✅ ACCEPT & CONTINUE",
            use_container_width=True,
        ):

            if not terms_accept:

                st.error(
                    "You must accept the Terms & Conditions to continue."
                )

            else:

                if accept_current_user_terms():

                    st.success(
                        "Terms accepted successfully."
                    )

                    st.rerun()


    else:

        st.info(
            "You can continue using FirstChoice Property Hub."
        )


    if st.button(
        "🚪 LOGOUT",
        use_container_width=True,
    ):

        logout_user()

        st.success(
            "You have been logged out successfully."
        )

        st.rerun()


    st.stop()


# ============================================================
# AUTHENTICATION LAYOUT
# ============================================================

left, right = st.columns(
    [1.05, 1.45],
    gap="large",
)


# ============================================================
# LEFT INFORMATION PANEL
# ============================================================

with left:

    st.markdown(
        """
<div class="info-card">

<h2>
🌏 One Account. Complete Property Ecosystem.
</h2>

<p>
Create your FirstChoice Property Hub account and access
a modern real estate marketplace.
</p>

<br>

<h3>
🏠 Property Discovery
</h3>

<p>
Buy, rent and discover residential,
commercial and land opportunities.
</p>

<h3>
📸 Property Listings
</h3>

<p>
Explore rich property listings with photos,
videos and location information.
</p>

<h3>
🛠️ Property Services
</h3>

<p>
Connect with architects, builders,
contractors, suppliers and other property professionals.
</p>

<h3>
🛡️ Secure Account
</h3>

<p>
Email and mobile verification helps protect
your account and platform access.
</p>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# RIGHT AUTH PANEL
# ============================================================

with right:

    st.markdown(
        """
<div class="auth-card">

<h2>
🔐 Account Access
</h2>

<p>
Login to your existing account or create a new account.
</p>

</div>
""",
        unsafe_allow_html=True,
    )


    # ========================================================
    # LOGIN / REGISTER TABS
    # ========================================================

    login_tab, register_tab = st.tabs(
        [
            "🔐 Login",
            "📝 Create New Account",
        ]
    )


    # ========================================================
    # LOGIN
    # ========================================================

    with login_tab:

        st.markdown(
            "### 🔐 Login to FirstChoice Property Hub"
        )


        login_email = st.text_input(

            "📧 Email ID",

            placeholder=
            "Enter your registered email address",

            key="login_email",

        )


        login_mobile = st.text_input(

            "📱 Mobile Number",

            placeholder=
            "Enter your registered 10-digit mobile number",

            max_chars=10,

            key="login_mobile",

        )


        st.caption(
            "Enter the same email address and mobile number used during registration."
        )


        if st.button(

            "🔐 LOGIN",

            use_container_width=True,

            key="login_button",

        ):

            email = normalize_email(
                login_email
            )

            mobile = normalize_mobile(
                login_mobile
            )


            if not validate_email(email):

                st.error(
                    "Please enter a valid email address."
                )


            elif not validate_mobile(mobile):

                st.error(
                    "Please enter a valid 10-digit mobile number."
                )


            else:

                success, message = login_user(

                    email,

                    mobile

                )


                if success:

                    st.success(
                        message
                    )

                    st.rerun()

                else:

                    st.error(
                        message
                    )


    # ========================================================
    # REGISTRATION
    # ========================================================

    with register_tab:

        st.markdown(
            "### 📝 Create Your FirstChoice Account"
        )


        full_name = st.text_input(

            "👤 Full Name",

            placeholder=
            "Enter your full legal name",

            key="register_name",

        )


        register_email = st.text_input(

            "📧 Email ID",

            placeholder=
            "Enter your email address",

            key="register_email",

        )


        register_mobile = st.text_input(

            "📱 Mobile Number",

            placeholder=
            "Enter your 10-digit mobile number",

            max_chars=10,

            key="register_mobile",

        )


        st.caption(
            "Email ID and mobile number verification are required."
        )


        # ====================================================
        # OTP SEND BUTTONS
        # ====================================================

        otp_col1, otp_col2 = st.columns(2)


        with otp_col1:

            if st.button(

                "📧 SEND EMAIL OTP",

                use_container_width=True,

            ):

                email = normalize_email(
                    register_email
                )


                if not validate_email(email):

                    st.error(
                        "Please enter a valid email address."
                    )

                else:

                    otp = send_email_otp(
                        email
                    )

                    st.session_state[
                        "dev_email_otp"
                    ] = otp

                    st.success(
                        "Email OTP generated successfully."
                    )

                    st.info(
                        "Development Mode: OTP is shown below."
                    )


        with otp_col2:

            if st.button(

                "📱 SEND MOBILE OTP",

                use_container_width=True,

            ):

                mobile = normalize_mobile(
                    register_mobile
                )


                if not validate_mobile(mobile):

                    st.error(
                        "Please enter a valid 10-digit mobile number."
                    )

                else:

                    otp = send_mobile_otp(
                        mobile
                    )

                    st.session_state[
                        "dev_mobile_otp"
                    ] = otp

                    st.success(
                        "Mobile OTP generated successfully."
                    )

                    st.info(
                        "Development Mode: OTP is shown below."
                    )


        # ====================================================
        # DEVELOPMENT OTP DISPLAY
        # ====================================================

        if "dev_email_otp" in st.session_state:

            st.warning(

                "Development Email OTP: "
                +
                st.session_state[
                    "dev_email_otp"
                ]

            )


        if "dev_mobile_otp" in st.session_state:

            st.warning(

                "Development Mobile OTP: "
                +
                st.session_state[
                    "dev_mobile_otp"
                ]

            )


        # ====================================================
        # OTP INPUT
        # ====================================================

        st.markdown(
            "### 🔑 Verify OTP"
        )


        email_otp = st.text_input(

            "📧 Email OTP",

            placeholder=
            "Enter 6-digit email OTP",

            max_chars=6,

            key="email_otp_input",

        )


        mobile_otp = st.text_input(

            "📱 Mobile OTP",

            placeholder=
            "Enter 6-digit mobile OTP",

            max_chars=6,

            key="mobile_otp_input",

        )


        verify_col1, verify_col2 = st.columns(2)


        with verify_col1:

            if st.button(

                "✅ VERIFY EMAIL OTP",

                use_container_width=True,

            ):

                if not email_otp:

                    st.error(
                        "Please enter the email OTP."
                    )

                else:

                    success, message = (
                        verify_email_otp(
                            email_otp
                        )
                    )


                    if success:

                        st.success(
                            message
                        )

                    else:

                        st.error(
                            message
                        )


        with verify_col2:

            if st.button(

                "✅ VERIFY MOBILE OTP",

                use_container_width=True,

            ):

                if not mobile_otp:

                    st.error(
                        "Please enter the mobile OTP."
                    )

                else:

                    success, message = (
                        verify_mobile_otp(
                            mobile_otp
                        )
                    )


                    if success:

                        st.success(
                            message
                        )

                    else:

                        st.error(
                            message
                        )


        # ====================================================
        # VERIFICATION STATUS
        # ====================================================

        if both_otp_verified():

            st.markdown(

                """
<div class="otp-success">

<strong>
✅ Email and Mobile Number Verified
</strong>

<br>

You can now create your account.

</div>
""",

                unsafe_allow_html=True,

            )

        else:

            st.markdown(

                """
<div class="otp-warning">

<strong>
⚠️ Verification Required
</strong>

<br>

Both Email OTP and Mobile OTP must be verified.

</div>
""",

                unsafe_allow_html=True,

            )


        # ====================================================
        # CREATE ACCOUNT
        # ====================================================

        st.markdown(
            "### 🚀 Complete Registration"
        )


        if st.button(

            "📝 CREATE ACCOUNT",

            use_container_width=True,

            type="primary",

        ):

            if not full_name.strip():

                st.error(
                    "Please enter your full name."
                )


            elif not validate_email(
                register_email
            ):

                st.error(
                    "Please enter a valid email address."
                )


            elif not validate_mobile(
                register_mobile
            ):

                st.error(
                    "Please enter a valid 10-digit mobile number."
                )


            elif not both_otp_verified():

                st.error(

                    "Please verify both Email OTP and Mobile OTP."

                )


            else:

                user_id, message = register_user(

                    full_name=full_name,

                    email=register_email,

                    mobile=register_mobile,

                )


                if user_id:

                    st.success(
                        message
                    )

                    st.info(
                        "Please review and accept the Terms & Conditions to continue."
                    )

                    st.rerun()

                else:

                    st.error(
                        message
                    )


# ============================================================
# SECURITY NOTICE
# ============================================================

st.markdown(
    """
<div class="auth-footer">

<h3>
🛡️ Your Account Security Matters
</h3>

<p>
FirstChoice Property Hub uses account verification and
role-based access controls to protect platform access.
</p>

<p>
Never share your OTP or account credentials with anyone.
</p>

</div>
""",
    unsafe_allow_html=True,
)
