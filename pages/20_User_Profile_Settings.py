import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 20 - USER PROFILE & SETTINGS
# ============================================================

st.set_page_config(
    page_title="My Profile | FirstChoice Property Hub",
    page_icon="👤",
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

/* PROFILE */

.profile-card {
    padding: 40px;

    border-radius: 30px;

    background: white;

    box-shadow:
    0 18px 50px
    rgba(0,0,0,0.08);
}

/* VERIFICATION */

.verification-card {
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

/* SETTINGS */

.settings-card {
    padding: 30px;

    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F8FAFF,
        #FDF4FF
    );

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    margin-bottom: 20px;
}

/* SECURITY */

.security-card {
    padding: 35px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E3A8A,
        #4C1D95,
        #7C3AED
    );

    box-shadow:
    0 22px 60px
    rgba(76,29,149,0.25);
}

/* DANGER */

.danger-card {
    padding: 30px;

    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFF1F2,
        #FFF7F7
    );

    border:
    1px solid #FDA4AF;
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
PROPERTY HUB • PROFESSIONAL PROFILE • ACCOUNT CENTER
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
👤 My Profile & Account
</div>

<div class="hero-subtitle">
Manage your professional identity, property preferences,
verification status and account security.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROFILE OVERVIEW
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🌟 Profile Overview
</div>

<div class="section-subtitle">
Build a trusted profile to improve your property experience.
</div>

</div>
""", unsafe_allow_html=True)


p1, p2, p3, p4 = st.columns(4)


with p1:

    st.metric(
        "📊 Profile Completion",
        "82%"
    )


with p2:

    st.metric(
        "🛡️ Verification",
        "3 / 5"
    )


with p3:

    st.metric(
        "⭐ Trust Score",
        "78"
    )


with p4:

    st.metric(
        "🏠 Properties",
        "4"
    )


# ============================================================
# PROFILE INFORMATION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Personal & Professional Information
</div>

<div class="section-subtitle">
Keep your profile information accurate and up to date.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="profile-card">

<h2>
👤 Your Professional Profile
</h2>

<p>
Create a trusted identity that can be used across the FirstChoice
Property Hub ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    full_name = st.text_input(
        "Full Name",
        value="Jitendra Parate"
    )


with c2:

    user_type = st.selectbox(
        "Account Type",
        [
            "Buyer",
            "Property Owner",
            "Agent",
            "Builder",
            "Developer",
            "Investor"
        ]
    )


c3, c4 = st.columns(2)


with c3:

    mobile = st.text_input(
        "Mobile Number",
        value="+91 XXXXX XXXXX"
    )


with c4:

    email = st.text_input(
        "Email Address",
        placeholder="yourname@email.com"
    )


c5, c6 = st.columns(2)


with c5:

    city = st.text_input(
        "City",
        placeholder="Example: Nagpur"
    )


with c6:

    state = st.text_input(
        "State",
        placeholder="Example: Maharashtra"
    )


about = st.text_area(
    "About You",
    placeholder=
    "Tell buyers, owners or property professionals about yourself."
)


if st.button(
    "💾 SAVE PROFILE",
    use_container_width=True
):

    st.success(
        "Profile information saved successfully."
    )


# ============================================================
# PROFILE PHOTO
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📸 Profile Photo
</div>

<div class="section-subtitle">
A professional profile photo helps build trust.
</div>

</div>
""", unsafe_allow_html=True)


profile_photo = st.file_uploader(
    "Upload Profile Photo",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


if profile_photo:

    st.success(
        "Profile photo uploaded successfully."
    )


# ============================================================
# VERIFICATION STATUS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ Identity & Verification
</div>

<div class="section-subtitle">
Verification status of your FirstChoice Property Hub account.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="verification-card">

<h2>
🛡️ Your Trust Profile
</h2>

<p>
📱 Mobile Number — ✅ Verified
</p>

<p>
📧 Email Address — ⏳ Pending
</p>

<p>
👤 Identity Verification — ⏳ Pending
</p>

<p>
🏠 Property Verification — ✅ 2 Properties Verified
</p>

<p>
📄 Documents — 🟡 Under Review
</p>

</div>
""", unsafe_allow_html=True)


v1, v2, v3 = st.columns(3)


with v1:

    if st.button(
        "📱 VERIFY MOBILE",
        use_container_width=True
    ):

        st.success(
            "Mobile verification is already completed."
        )


with v2:

    if st.button(
        "📧 VERIFY EMAIL",
        use_container_width=True
    ):

        st.info(
            "Email verification link will be sent."
        )


with v3:

    if st.button(
        "🛡️ START KYC",
        use_container_width=True
    ):

        st.info(
            "Secure KYC verification module will open."
        )


# ============================================================
# PREFERENCES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Property Preferences
</div>

<div class="section-subtitle">
Tell us what type of property you are interested in.
</div>

</div>
""", unsafe_allow_html=True)


pref1, pref2 = st.columns(2)


with pref1:

    property_type = st.multiselect(
        "Preferred Property Types",
        [
            "Apartment",
            "Villa",
            "Independent House",
            "Plot",
            "Land",
            "Commercial",
            "Office",
            "Shop",
            "Warehouse",
            "Farm Land"
        ]
    )


with pref2:

    preferred_locations = st.multiselect(
        "Preferred Locations",
        [
            "Nagpur",
            "Pune",
            "Mumbai",
            "Bengaluru",
            "Hyderabad",
            "Delhi NCR",
            "Gurugram",
            "Noida",
            "Nashik",
            "Other"
        ]
    )


budget = st.select_slider(
    "Preferred Budget Range",
    options=[
        "Under ₹25 Lakh",
        "₹25–50 Lakh",
        "₹50 Lakh–₹1 Crore",
        "₹1–2 Crore",
        "₹2–5 Crore",
        "₹5 Crore+"
    ]
)


if st.button(
    "💾 SAVE PROPERTY PREFERENCES",
    use_container_width=True
):

    st.success(
        "Property preferences updated."
    )


# ============================================================
# ACCOUNT SETTINGS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚙️ Account Settings
</div>

<div class="section-subtitle">
Manage your account and marketplace experience.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="settings-card">

<h2>
🔔 Notification Settings
</h2>

<p>
Choose how you receive property alerts,
enquiries, site visits and important updates.
</p>

</div>
""", unsafe_allow_html=True)


notification1 = st.checkbox(
    "📱 Mobile / SMS Alerts",
    value=True
)

notification2 = st.checkbox(
    "📧 Email Alerts",
    value=True
)

notification3 = st.checkbox(
    "💬 Enquiry & Chat Notifications",
    value=True
)

notification4 = st.checkbox(
    "💰 Price Drop Alerts",
    value=True
)

notification5 = st.checkbox(
    "🏠 New Property Recommendations",
    value=True
)


if st.button(
    "💾 SAVE NOTIFICATION SETTINGS",
    use_container_width=True
):

    st.success(
        "Notification settings saved."
    )


# ============================================================
# PRIVACY SETTINGS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔒 Privacy Controls
</div>

<div class="section-subtitle">
Control what other users can see on your profile.
</div>

</div>
""", unsafe_allow_html=True)


privacy1 = st.checkbox(
    "Show my profile to verified property professionals",
    value=True
)

privacy2 = st.checkbox(
    "Allow property owners and agents to contact me",
    value=True
)

privacy3 = st.checkbox(
    "Show my preferred locations",
    value=False
)

privacy4 = st.checkbox(
    "Show my profile photo",
    value=True
)


if st.button(
    "🔒 SAVE PRIVACY SETTINGS",
    use_container_width=True
):

    st.success(
        "Privacy settings updated."
    )


# ============================================================
# SECURITY CENTER
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🔐 Security Center
</div>

<div class="section-subtitle">
Protect your account and monitor your security.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="security-card">

<h2>
🛡️ Account Security
</h2>

<p>
📱 Mobile Authentication — Active
</p>

<p>
🔐 OTP Login — Enabled
</p>

<p>
🚨 Suspicious Login Detection — Active
</p>

<p>
🛡️ Secure Session Management — Active
</p>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    if st.button(
        "📱 CHANGE MOBILE",
        use_container_width=True
    ):

        st.info(
            "Secure mobile change verification will open."
        )


with s2:

    if st.button(
        "🔐 SECURITY ACTIVITY",
        use_container_width=True
    ):

        st.info(
            "Your recent security activity will appear here."
        )


with s3:

    if st.button(
        "🚪 LOGOUT ALL DEVICES",
        use_container_width=True
    ):

        st.warning(
            "All active sessions will be logged out."
        )


# ============================================================
# TRUST BADGES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏆 Your Trust Badges
</div>

<div class="section-subtitle">
Build credibility across the FirstChoice Property Hub.
</div>

</div>
""", unsafe_allow_html=True)


b1, b2, b3, b4 = st.columns(4)


with b1:

    st.success(
        """
        📱

        **Mobile Verified**
        """
    )


with b2:

    st.info(
        """
        🏠

        **Property Owner**
        """
    )


with b3:

    st.warning(
        """
        📄

        **Documents Reviewed**
        """
    )


with b4:

    st.success(
        """
        ⭐

        **Trusted Member**
        """
    )


# ============================================================
# PROFILE COMPLETION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 Complete Your Profile
</div>

<div class="section-subtitle">
A complete profile helps you build more trust.
</div>

</div>
""", unsafe_allow_html=True)


st.progress(
    0.82
)


st.write(
    "82% Profile Completed"
)


st.info(
    """
    💡 Complete your email verification,
    identity verification and professional details
    to reach 100% profile completion.
    """
)


# ============================================================
# DANGER ZONE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚠️ Account Management
</div>

<div class="section-subtitle">
Manage your account lifecycle.
</div>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="danger-card">

<h3>
⚠️ Important Account Actions
</h3>

<p>
Deleting your account may permanently remove
your saved properties, enquiries and account data.
</p>

</div>
""", unsafe_allow_html=True)


d1, d2 = st.columns(2)


with d1:

    if st.button(
        "🚪 LOGOUT",
        use_container_width=True
    ):

        st.success(
            "Logout request initiated."
        )


with d2:

    if st.button(
        "🗑️ REQUEST ACCOUNT DELETION",
        use_container_width=True
    ):

        st.warning(
            "Account deletion confirmation required."
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
