import streamlit as st
import random
from datetime import datetime

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.Database import (
    get_user_by_mobile,
    get_user_by_email,
    create_user
)

from core.Auth import (
    login_user,
    logout_user,
    is_logged_in,
    get_role_label
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 01 — LOGIN & REGISTRATION
# ============================================================


st.set_page_config(
    page_title="Login & Registration | FirstChoice Property Hub",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM UI
# ============================================================

load_premium_ui()


# ============================================================
# INITIALIZE SESSION STATE
# ============================================================

if "auth_mode" not in st.session_state:

    st.session_state.auth_mode = "login"


if "mobile_otp" not in st.session_state:

    st.session_state.mobile_otp = None


if "email_otp" not in st.session_state:

    st.session_state.email_otp = None


if "mobile_verified" not in st.session_state:

    st.session_state.mobile_verified = False


if "email_verified" not in st.session_state:

    st.session_state.email_verified = False


if "registration_data" not in st.session_state:

    st.session_state.registration_data = {}


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:25px;
        ">

        <h1>🏠 FirstChoice</h1>

        <h3>Property Hub</h3>

        <hr>

        <p>
        India's Next-Generation<br>
        Real Estate Ecosystem
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("### 📌 Navigation")


    st.page_link(
        "app.py",
        label="🏠 Home"
    )


    st.page_link(
        "pages/01_Login_Register.py",
        label="🔐 Login & Registration"
    )


    st.page_link(
        "pages/02_Property_Search.py",
        label="🔎 Property Search"
    )


    st.page_link(
        "pages/03_Post_Property.py",
        label="🏡 Post Property"
    )


# ============================================================
# HERO
# ============================================================

hero(
    "🔐 Welcome to FirstChoice Property Hub",
    "Securely login or create your account to access India's next-generation real estate ecosystem."
)


# ============================================================
# IF ALREADY LOGGED IN
# ============================================================

if is_logged_in():

    section(
        "👋 You Are Already Logged In",
        "Your FirstChoice Property Hub account is currently active."
    )


    st.success(
        f"Welcome {st.session_state.user_name}!"
    )


    st.info(
        f"Account Role: {get_role_label()}"
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "🏠 Go to Home",
            use_container_width=True
        ):

            st.switch_page(
                "app.py"
            )


    with col2:

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout_user()

            st.rerun()


    footer()

    st.stop()


# ============================================================
# LOGIN / REGISTER SWITCH
# ============================================================

section(
    "🔑 Account Access",
    "Choose whether you want to login or create a new account."
)


col1, col2 = st.columns(2)


with col1:

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        st.session_state.auth_mode = "login"

        st.rerun()


with col2:

    if st.button(
        "📝 Create New Account",
        use_container_width=True
    ):

        st.session_state.auth_mode = "register"

        st.rerun()


# ============================================================
# LOGIN
# ============================================================

if st.session_state.auth_mode == "login":

    section(
        "🔐 Login to Your Account",
        "Enter your registered mobile number or email address."
    )


    login_identifier = st.text_input(
        "📱 Mobile Number / 📧 Email ID",
        placeholder=
        "Enter your registered mobile number or email ID"
    )


    login_otp = st.text_input(
        "🔢 Enter OTP",
        placeholder=
        "Enter 6-digit OTP"
    )


    if st.button(
        "📨 Send Login OTP",
        use_container_width=True
    ):

        if not login_identifier.strip():

            st.error(
                "Please enter your mobile number or email ID."
            )

        else:

            user = None


            if "@" in login_identifier:

                user = get_user_by_email(
                    login_identifier.strip()
                )

            else:

                user = get_user_by_mobile(
                    login_identifier.strip()
                )


            if user is None:

                st.error(
                    "No account found. Please create a new account first."
                )

            else:

                otp = "123456"

                st.session_state.login_otp = otp

                st.session_state.login_identifier = (
                    login_identifier.strip()
                )


                st.success(
                    "OTP sent successfully."
                )


                st.info(
                    "Demo OTP for testing: 123456"
                )


    if st.button(
        "✅ Verify OTP & Login",
        use_container_width=True
    ):

        if "login_otp" not in st.session_state:

            st.error(
                "Please request OTP first."
            )

        elif login_otp != st.session_state.login_otp:

            st.error(
                "Invalid OTP."
            )

        else:

            identifier = (
                st.session_state.login_identifier
            )


            if "@" in identifier:

                user = get_user_by_email(
                    identifier
                )

            else:

                user = get_user_by_mobile(
                    identifier
                )


            if user:

                login_user(

                    user_id=user["id"],

                    user_name=user["full_name"],

                    user_email=user["email"],

                    user_mobile=user["mobile_number"],

                    role=user["role"]

                )


                st.success(
                    "🎉 Login successful!"
                )


                st.rerun()


# ============================================================
# REGISTRATION
# ============================================================

else:

    section(
        "📝 Create Your FirstChoice Account",
        "Mobile number and email verification are required."
    )


    full_name = st.text_input(
        "👤 Full Name",
        placeholder=
        "Enter your full name"
    )


    business_name = st.text_input(
        "🏢 Business / Company Name",
        placeholder=
        "Enter business or company name (optional)"
    )


    account_type = st.selectbox(

        "👤 Account Type",

        [

            "Individual Buyer",

            "Property Owner",

            "Tenant",

            "Agent / Broker",

            "Builder / Developer",

            "Architect",

            "Interior Designer",

            "Construction Professional",

            "Property Service Provider",

            "Other"

        ]

    )


    mobile_number = st.text_input(
        "📱 Mobile Number",
        placeholder=
        "Enter your 10-digit mobile number"
    )


    email = st.text_input(
        "📧 Email ID",
        placeholder=
        "Enter your active email address"
    )


    # ========================================================
    # MOBILE OTP
    # ========================================================

    st.markdown(
        "### 📱 Mobile Verification"
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "📨 Send Mobile OTP",
            use_container_width=True
        ):

            if not mobile_number.strip():

                st.error(
                    "Please enter mobile number first."
                )

            elif len(mobile_number.strip()) != 10:

                st.error(
                    "Please enter a valid 10-digit mobile number."
                )

            else:

                otp = "123456"

                st.session_state.mobile_otp = otp

                st.success(
                    "Mobile OTP sent successfully."
                )

                st.info(
                    "Demo OTP: 123456"
                )


    with col2:

        mobile_otp_input = st.text_input(
            "🔢 Mobile OTP",
            placeholder=
            "Enter 6-digit OTP"
        )


    if st.button(
        "✅ Verify Mobile OTP",
        use_container_width=True
    ):

        if (

            st.session_state.mobile_otp

            and mobile_otp_input

            == st.session_state.mobile_otp

        ):

            st.session_state.mobile_verified = True

            st.success(
                "✅ Mobile number verified."
            )

        else:

            st.error(
                "Invalid mobile OTP."
            )


    # ========================================================
    # EMAIL OTP
    # ========================================================

    st.markdown(
        "### 📧 Email Verification"
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "📨 Send Email OTP",
            use_container_width=True
        ):

            if not email.strip():

                st.error(
                    "Please enter email address first."
                )

            elif "@" not in email:

                st.error(
                    "Please enter a valid email address."
                )

            else:

                otp = "123456"

                st.session_state.email_otp = otp

                st.success(
                    "Email OTP sent successfully."
                )

                st.info(
                    "Demo OTP: 123456"
                )


    with col2:

        email_otp_input = st.text_input(
            "🔢 Email OTP",
            placeholder=
            "Enter 6-digit OTP"
        )


    if st.button(
        "✅ Verify Email OTP",
        use_container_width=True
    ):

        if (

            st.session_state.email_otp

            and email_otp_input

            == st.session_state.email_otp

        ):

            st.session_state.email_verified = True

            st.success(
                "✅ Email address verified."
            )

        else:

            st.error(
                "Invalid email OTP."
            )


    # ========================================================
    # TERMS & CONDITIONS
    # ========================================================

    section(
        "📜 Terms & Conditions",
        "You must read and accept the Terms & Conditions before creating your account."
    )


    st.markdown(
        """
        <div class="fc-card">

        <h3>
        FirstChoice Infra Property Hub — Terms of Use
        </h3>

        <p>
        By creating an account, you agree that the information
        provided by you is accurate and complete.
        </p>

        <p>
        Users are responsible for the accuracy and legality of
        property information, images, videos and documents
        uploaded by them.
        </p>

        <p>
        FirstChoice Infra Property Hub may review, moderate,
        suspend or remove listings that violate applicable
        laws, policies or platform guidelines.
        </p>

        <p>
        Property listings and advertisements are provided by
        users, owners, agents, builders or other third parties.
        FirstChoice Infra Property Hub does not automatically
        guarantee the ownership, legality, title, quality or
        authenticity of every listing.
        </p>

        <p>
        Users should independently verify property documents,
        ownership, approvals, pricing and other information
        before entering into any transaction.
        </p>

        <p>
        Paid or premium services may be subject to separate
        pricing, subscription and refund policies.
        </p>

        <p>
        Users must not misuse the platform, upload unlawful
        content, attempt unauthorized access, interfere with
        platform security or engage in fraudulent activities.
        </p>

        <p>
        The platform may collect and process account and usage
        information in accordance with its Privacy Policy.
        </p>

        <p>
        These Terms may be updated periodically. Continued use
        of the platform after an update may require acceptance
        of the revised Terms.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    terms_accepted = st.checkbox(

        "☑️ I have read, understood and agree to the Terms & Conditions and Privacy Policy."

    )


    # ========================================================
    # CREATE ACCOUNT
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)


    if st.button(

        "🚀 CREATE MY ACCOUNT",

        use_container_width=True

    ):

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not full_name.strip():

            st.error(
                "Please enter your full name."
            )

        elif not mobile_number.strip():

            st.error(
                "Please enter mobile number."
            )

        elif not email.strip():

            st.error(
                "Please enter email address."
            )

        elif not st.session_state.mobile_verified:

            st.error(
                "Please verify your mobile number."
            )

        elif not st.session_state.email_verified:

            st.error(
                "Please verify your email address."
            )

        elif not terms_accepted:

            st.error(
                "You must accept the Terms & Conditions before continuing."
            )

        else:

            # ------------------------------------------------
            # CHECK DUPLICATE MOBILE
            # ------------------------------------------------

            existing_mobile = get_user_by_mobile(

                mobile_number.strip()

            )


            if existing_mobile:

                st.error(
                    "This mobile number is already registered."
                )

                st.stop()


            # ------------------------------------------------
            # CHECK DUPLICATE EMAIL
            # ------------------------------------------------

            existing_email = get_user_by_email(

                email.strip()

            )


            if existing_email:

                st.error(
                    "This email address is already registered."
                )

                st.stop()


            # ------------------------------------------------
            # CREATE USER
            # ------------------------------------------------

            user_id = create_user(

                full_name=full_name.strip(),

                business_name=business_name.strip(),

                account_type=account_type,

                mobile_number=mobile_number.strip(),

                email=email.strip(),

                mobile_verified=1,

                email_verified=1,

                terms_accepted=1,

                role="user"

            )


            if user_id:

                st.success(
                    "🎉 Your account has been created successfully!"
                )


                # --------------------------------------------
                # AUTO LOGIN
                # --------------------------------------------

                login_user(

                    user_id=user_id,

                    user_name=full_name.strip(),

                    user_email=email.strip(),

                    user_mobile=mobile_number.strip(),

                    role="user"

                )


                st.info(
                    "Welcome to FirstChoice Infra Property Hub."
                )


                st.rerun()


            else:

                st.error(
                    "Unable to create account. Please try again."
                )


# ============================================================
# FOOTER
# ============================================================

footer()
