import streamlit as st
import random
import re


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 01 — LOGIN & REGISTRATION
# STANDALONE VERSION
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

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(
        circle at 10% 10%,
        rgba(99,102,241,0.12),
        transparent 30%
    ),
    radial-gradient(
        circle at 90% 20%,
        rgba(236,72,153,0.12),
        transparent 30%
    ),
    linear-gradient(
        135deg,
        #F8FAFC,
        #EEF2FF,
        #FAF5FF,
        #F0FDFA
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


/* SIDEBAR */

[data-testid="stSidebar"] {
    background:
    linear-gradient(
        180deg,
        #020617,
        #0F172A,
        #1E1B4B,
        #312E81
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}


/* HERO */

.fc-hero {
    padding: 55px;
    border-radius: 38px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #172554,
        #4C1D95,
        #9D174D
    );

    box-shadow:
    0 30px 80px
    rgba(30,41,59,0.30);

    margin-bottom: 35px;
}

.fc-hero h1 {
    font-size: 48px;
    font-weight: 900;
}

.fc-hero p {
    font-size: 19px;
    line-height: 1.7;
}


/* SECTION */

.fc-section {
    padding: 25px 30px;
    border-radius: 28px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4338CA,
        #7E22CE,
        #BE185D
    );

    box-shadow:
    0 18px 45px
    rgba(79,70,229,0.22);

    margin: 35px 0 25px 0;
}

.fc-section h2 {
    margin: 0;
    font-size: 30px;
    font-weight: 900;
}

.fc-section p {
    margin-top: 8px;
    font-size: 16px;
}


/* CARD */

.fc-card {
    padding: 30px;
    border-radius: 28px;

    background:
    rgba(255,255,255,0.90);

    border:
    1px solid
    rgba(148,163,184,0.20);

    box-shadow:
    0 18px 45px
    rgba(15,23,42,0.08);

    margin-bottom: 20px;
}

.fc-card h3 {
    color: #0F172A;
    font-size: 23px;
}

.fc-card p {
    color: #475569;
    line-height: 1.7;
}


/* SUCCESS */

.fc-success {
    padding: 28px;
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
    0 20px 50px
    rgba(5,150,105,0.20);
}


/* WARNING */

.fc-warning {
    padding: 28px;
    border-radius: 28px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #B45309,
        #D97706,
        #F59E0B
    );
}


/* FOOTER */

.fc-footer {
    margin-top: 60px;
    padding: 40px;
    border-radius: 32px;
    color: white;
    text-align: center;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1E1B4B,
        #312E81
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "mobile_otp": None,
    "email_otp": None,
    "otp_sent": False,
    "mobile_verified": False,
    "email_verified": False,
    "terms_accepted": False,
    "account_created": False
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
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
    """, unsafe_allow_html=True)

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

st.markdown("""
<div class="fc-hero">

<h1>
🔐 Welcome to FirstChoice Property Hub
</h1>

<p>
Secure Login & Registration
</p>

<p>
Your trusted gateway to India's next-generation
real estate ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="fc-card">

<h3>
🏠 Create Your FirstChoice Account
</h3>

<p>
Register once and explore properties, post listings,
connect with buyers, owners, agents, builders and
real estate service professionals.
</p>

<p>
🔐 Mobile verification and Email verification
are required for account security.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# ACCOUNT TYPE
# ============================================================

st.markdown("""
<div class="fc-section">

<h2>
👤 Select Your Account Type
</h2>

<p>
Choose the account category that best describes you.
</p>

</div>
""", unsafe_allow_html=True)


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

st.markdown("""
<div class="fc-section">

<h2>
📝 Personal & Business Information
</h2>

<p>
Enter your basic information to create your account.
</p>

</div>
""", unsafe_allow_html=True)


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
# CONTACT
# ============================================================

st.markdown("""
<div class="fc-section">

<h2>
📱 Contact Verification
</h2>

<p>
Mobile number and Email ID are required.
</p>

</div>
""", unsafe_allow_html=True)


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
# VALIDATION
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

if st.button(
    "📩 SEND MOBILE & EMAIL OTP",
    use_container_width=True
):

    if not full_name.strip():

        st.error(
            "Please enter your full name."
        )

    elif not valid_mobile(mobile_number):

        st.error(
            "Please enter a valid 10-digit Indian mobile number."
        )

    elif not valid_email(email):

        st.error(
            "Please enter a valid Email ID."
        )

    else:

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
            "DEMO MODE: Production में OTP SMS और Email पर भेजा जाएगा."
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

    st.markdown("""
    <div class="fc-section">

    <h2>
    🔑 Verify Your OTP
    </h2>

    <p>
    Enter the OTP received on your mobile and email.
    </p>

    </div>
    """, unsafe_allow_html=True)


    otp1, otp2 = st.columns(2)


    with otp1:

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


    with otp2:

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

    c1, c2 = st.columns(2)


    with c1:

        if st.session_state.mobile_verified:

            st.success(
                "🟢 Mobile Verified"
            )

        else:

            st.warning(
                "🟡 Mobile Verification Pending"
            )


    with c2:

        if st.session_state.email_verified:

            st.success(
                "🟢 Email Verified"
            )

        else:

            st.warning(
                "🟡 Email Verification Pending"
            )


# ============================================================
# TERMS
# ============================================================

if (
    st.session_state.mobile_verified
    and st.session_state.email_verified
):

    st.markdown("""
    <div class="fc-section">

    <h2>
    📜 Terms & Conditions
    </h2>

    <p>
    You must accept the Terms & Conditions before creating your account.
    </p>

    </div>
    """, unsafe_allow_html=True)


    with st.expander(
        "📖 Read Terms & Conditions"
    ):

        st.markdown("""
        ### 1. Account Responsibility

        Users must provide accurate and updated information.

        ### 2. Property Listings

        All property information, photos, videos and documents
        must be accurate and legally permitted.

        ### 3. Prohibited Content

        Fraudulent, misleading, illegal or abusive content
        is strictly prohibited.

        ### 4. Transactions

        FirstChoice Property Hub is a technology platform
        connecting property users and service providers.

        ### 5. Payments

        Paid services are subject to applicable plan conditions.

        ### 6. Account Security

        Users are responsible for protecting their account.

        ### 7. Suspension

        Accounts violating platform policies may be restricted.

        ### 8. Privacy

        Personal information will be handled according to
        the applicable Privacy Policy.

        ### 9. Service Availability

        The platform may experience maintenance or technical
        interruptions.

        ### 10. Legal Compliance

        Users must comply with applicable laws and regulations.

        ### 11. Policy Changes

        Terms and policies may be updated when required.

        ### 12. Acceptance

        Creating an account confirms acceptance of the
        applicable Terms & Conditions and Privacy Policy.

        **Legal Notice:**
        Production launch से पहले Terms & Conditions और
        Privacy Policy को qualified legal professional से review करवाना चाहिए.
        """)


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

        st.markdown("""
        <div class="fc-success">

        <h2>
        ✅ Verification Completed
        </h2>

        <p>
        Mobile number, Email ID and Terms & Conditions
        have been successfully verified.
        </p>

        </div>
        """, unsafe_allow_html=True)


        if st.button(
            "🚀 CREATE MY FIRSTCHOICE ACCOUNT",
            use_container_width=True
        ):

            st.session_state.account_created = True

            st.success(
                "🎉 Account created successfully!"
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

    st.markdown("""
    <div class="fc-card">

    <h2>
    🎉 Welcome to FirstChoice Property Hub
    </h2>

    <p>
    Your registration process is complete.
    </p>

    </div>
    """, unsafe_allow_html=True)


    if st.button(
        "🔎 GO TO PROPERTY SEARCH",
        use_container_width=True
    ):

        st.switch_page(
            "pages/02_Property_Search.py"
        )


# ============================================================
# SECURITY
# ============================================================

st.markdown("""
<div class="fc-warning">

<h3>
🛡️ Account Security
</h3>

<p>
Never share your OTP with anyone.
FirstChoice Property Hub support staff will never
ask you for your OTP or password.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="fc-footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
Buy • Sell • Rent • Invest • Build • Discover
</p>

<p>
India's Next-Generation Real Estate Ecosystem
</p>

<hr>

<p>
© FirstChoice Infra Property Hub
</p>

</div>
""", unsafe_allow_html=True)
