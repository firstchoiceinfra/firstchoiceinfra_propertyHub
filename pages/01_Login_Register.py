import streamlit as st
import random
import time
import re

from core.Ui import load_premium_ui, hero, section, footer


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
# LOAD PREMIUM UI
# ============================================================

load_premium_ui()


# ============================================================
# SESSION STATE
# ============================================================

if "mobile_otp" not in st.session_state:
    st.session_state.mobile_otp = None

if "email_otp" not in st.session_state:
    st.session_state.email_otp = None

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "mobile_verified" not in st.session_state:
    st.session_state.mobile_verified = False

if "email_verified" not in st.session_state:
    st.session_state.email_verified = False

if "terms_accepted" not in st.session_state:
    st.session_state.terms_accepted = False

if "account_created" not in st.session_state:
    st.session_state.account_created = False


# ============================================================
# HERO
# ============================================================

hero(
    "🔐 Welcome to FirstChoice Property Hub",
    "Secure Login & Registration — Your trusted gateway to India's next-generation real estate ecosystem."
)


# ============================================================
# PAGE INTRO
# ============================================================

st.markdown(
    """
    <div class="fc-card">

    <h3>🏠 Create Your FirstChoice Account</h3>

    <p>
    Register once and explore properties, post listings,
    connect with buyers, owners, agents, builders and
    real estate service professionals.
    </p>

    <p>
    🔐 Mobile verification and Email verification are required
    for account security.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ACCOUNT TYPE
# ============================================================

section(
    "👤 Select Your Account Type",
    "Choose the account category that best describes you."
)


account_type = st.selectbox(

    "Account Type",

    [
        "Buyer",
        "Owner / Seller",
        "Tenant",
        "Agent / Broker",
        "Builder / Developer",
        "Architect",
        "Interior Designer",
        "Building Material Supplier",
        "Painter",
        "Carpenter",
        "Plumber",
        "Electrician",
        "Fabrication Service",
        "Other Service Provider"
    ]

)


# ============================================================
# PERSONAL INFORMATION
# ============================================================

section(
    "📝 Personal & Business Information",
    "Enter your basic information to create your account."
)


col1, col2 = st.columns(2)


with col1:

    full_name = st.text_input(
        "👤 Full Name *",
        placeholder="Enter your full name"
    )


with col2:

    business_name = st.text_input(
        "🏢 Business / Company Name",
        placeholder="Enter business name if applicable"
    )


# ============================================================
# CONTACT INFORMATION
# ============================================================

section(
    "📱 Contact Verification",
    "Your mobile number and email address are required for secure account verification."
)


col1, col2 = st.columns(2)


with col1:

    mobile_number = st.text_input(
        "📱 Mobile Number *",
        placeholder="Enter your 10-digit mobile number",
        max_chars=10
    )


with col2:

    email = st.text_input(
        "📧 Email ID *",
        placeholder="Enter your active email address"
    )


# ============================================================
# VALIDATION FUNCTIONS
# ============================================================

def valid_mobile(number):

    return (
        number.isdigit()
        and len(number) == 10
        and number[0] in "6789"
    )


def valid_email(email_address):

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return re.match(
        pattern,
        email_address
    )


# ============================================================
# SEND OTP
# ============================================================

st.markdown(
    """
    <div class="fc-card">

    <h3>🔐 Secure OTP Verification</h3>

    <p>
    OTP verification will be required for both your mobile
    number and email address.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


if st.button(
    "📩 SEND MOBILE & EMAIL OTP",
    use_container_width=True
):

    if not full_name.strip():

        st.error(
            "Please enter your full name."
        )

    elif not valid_mobile(
        mobile_number
    ):

        st.error(
            "Please enter a valid 10-digit Indian mobile number."
        )

    elif not valid_email(
        email
    ):

        st.error(
            "Please enter a valid email address."
        )

    else:

        # DEMO OTP
        # Production में actual SMS और Email API जोड़ी जाएगी.

        st.session_state.mobile_otp = str(
            random.randint(
                100000,
                999999
            )
        )

        st.session_state.email_otp = str(
            random.randint(
                100000,
                999999
            )
        )

        st.session_state.otp_sent = True

        st.session_state.mobile_verified = False

        st.session_state.email_verified = False

        st.success(
            "OTP generated successfully."
        )

        st.info(
            "Demo Mode: OTP values are shown below. "
            "Production version में OTP SMS और Email पर भेजा जाएगा."
        )

        st.code(
            f"""
Mobile OTP: {st.session_state.mobile_otp}

Email OTP: {st.session_state.email_otp}
"""
        )


# ============================================================
# OTP VERIFICATION
# ============================================================

if st.session_state.otp_sent:

    section(
        "🔑 Verify Your OTP",
        "Enter the OTP received on your mobile and email."
    )


    otp_col1, otp_col2 = st.columns(2)


    with otp_col1:

        mobile_otp_input = st.text_input(
            "📱 Mobile OTP",
            placeholder="Enter 6-digit mobile OTP",
            max_chars=6
        )


        if st.button(
            "✅ VERIFY MOBILE OTP",
            use_container_width=True
        ):

            if (
                mobile_otp_input
                == st.session_state.mobile_otp
            ):

                st.session_state.mobile_verified = True

                st.success(
                    "Mobile number verified successfully."
                )

            else:

                st.error(
                    "Invalid mobile OTP."
                )


    with otp_col2:

        email_otp_input = st.text_input(
            "📧 Email OTP",
            placeholder="Enter 6-digit email OTP",
            max_chars=6
        )


        if st.button(
            "✅ VERIFY EMAIL OTP",
            use_container_width=True
        ):

            if (
                email_otp_input
                == st.session_state.email_otp
            ):

                st.session_state.email_verified = True

                st.success(
                    "Email address verified successfully."
                )

            else:

                st.error(
                    "Invalid email OTP."
                )


# ============================================================
# VERIFICATION STATUS
# ============================================================

if st.session_state.otp_sent:

    status1, status2 = st.columns(2)


    with status1:

        if st.session_state.mobile_verified:

            st.success(
                "🟢 Mobile Verified"
            )

        else:

            st.warning(
                "🟡 Mobile Verification Pending"
            )


    with status2:

        if st.session_state.email_verified:

            st.success(
                "🟢 Email Verified"
            )

        else:

            st.warning(
                "🟡 Email Verification Pending"
            )


# ============================================================
# TERMS & CONDITIONS
# ============================================================

if (
    st.session_state.mobile_verified
    and st.session_state.email_verified
):

    section(
        "📜 Terms & Conditions",
        "Please read and accept the terms before creating your account."
    )


    with st.expander(
        "📖 Read FirstChoice Property Hub Terms & Conditions"
    ):

        st.markdown(
            """
            ### 1. Account Responsibility

            The user is responsible for providing accurate,
            complete and updated information.

            ### 2. Property Information

            Any property information, photographs, videos,
            documents or location details uploaded by the user
            must be accurate and legally permitted to be shared.

            ### 3. User Conduct

            Users must not upload fraudulent, illegal,
            misleading or abusive content.

            ### 4. Property Transactions

            FirstChoice Property Hub is a technology platform
            connecting property users and service providers.
            Unless specifically stated, the platform is not
            itself a party to private property transactions.

            ### 5. Payments

            Any premium subscription or paid service must be
            used according to the applicable plan terms.

            ### 6. Refunds

            Refund eligibility, if applicable, will depend on
            the specific service and refund policy.

            ### 7. Content

            Users grant the platform permission to display
            submitted listing content for platform services.

            ### 8. Account Security

            Users must keep their account credentials secure
            and must immediately report suspicious activity.

            ### 9. Suspension

            Accounts may be suspended or restricted for
            violations of platform policies or applicable law.

            ### 10. Privacy

            Personal information will be handled according to
            the platform's applicable Privacy Policy.

            ### 11. Service Availability

            The platform may occasionally experience
            maintenance, technical issues or interruptions.

            ### 12. Legal Compliance

            Users must comply with all applicable laws,
            regulations and property-related requirements.

            ### 13. Changes

            FirstChoice Property Hub may update its terms,
            policies and services when required.

            ### 14. Acceptance

            By creating an account, the user confirms that
            they have read, understood and accepted the
            applicable Terms & Conditions and Privacy Policy.

            ---
            
            **Important:**
            
            This is a software-level draft and should be
            reviewed and finalized by a qualified legal
            professional before production launch.
            """
        )


    st.session_state.terms_accepted = st.checkbox(

        "☑️ I have read and agree to the Terms & Conditions and Privacy Policy."

    )


# ============================================================
# CREATE ACCOUNT
# ============================================================

if (
    st.session_state.mobile_verified
    and st.session_state.email_verified
):

    if st.session_state.terms_accepted:

        st.markdown(
            """
            <div class="fc-success">

            <h2>
            ✅ All Verification Completed
            </h2>

            <p>
            Your mobile number, email address and
            Terms & Conditions acceptance have been verified.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        if st.button(
            "🚀 CREATE MY FIRSTCHOICE ACCOUNT",
            use_container_width=True
        ):

            st.session_state.account_created = True

            st.success(
                "🎉 Your FirstChoice Property Hub account has been created successfully!"
            )

            st.balloons()


    else:

        st.warning(
            "⚠️ Please accept the Terms & Conditions before creating your account."
        )


# ============================================================
# ACCOUNT CREATED
# ============================================================

if st.session_state.account_created:

    st.markdown(
        """
        <div class="fc-card">

        <h2>
        🎉 Welcome to FirstChoice Property Hub
        </h2>

        <p>
        Your account registration process is complete.
        </p>

        <p>
        You can now continue to explore the platform.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button(
        "🏠 GO TO PROPERTY SEARCH",
        use_container_width=True
    ):

        st.switch_page(
            "pages/02_Property_Search.py"
        )


# ============================================================
# SECURITY NOTICE
# ============================================================

st.markdown(
    """
    <div class="fc-warning">

    <h3>🛡️ Account Security</h3>

    <p>
    Never share your OTP with anyone.
    FirstChoice Property Hub support staff will never
    ask you to share your OTP or password.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

footer()
