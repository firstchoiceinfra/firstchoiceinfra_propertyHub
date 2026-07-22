import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 6 - USER PROFILE / MY ACCOUNT
# PREMIUM MULTINATIONAL REAL ESTATE DESIGN
# ============================================================

st.set_page_config(
    page_title="My Account | FirstChoice Property Hub",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
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

/* =========================================================
BRAND
========================================================= */

.brand {

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 20px 32px;

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

/* =========================================================
PAGE HEADER
========================================================= */

.page-header {

    margin-top: 28px;

    padding: 35px 40px;

    border-radius: 28px;

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
    0 20px 55px
    rgba(124,58,237,0.22);

    position: relative;

    overflow: hidden;
}

.page-header::after {

    content: "";

    position: absolute;

    width: 240px;

    height: 240px;

    right: -80px;

    top: -120px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.13);
}

.page-title {

    font-size: 40px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.page-subtitle {

    font-size: 16px;

    color:
    rgba(255,255,255,0.85);

    position: relative;

    z-index: 2;
}

/* =========================================================
SECTION HEADER
========================================================= */

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

    position: relative;

    overflow: hidden;
}

.section-header::after {

    content: "";

    position: absolute;

    width: 140px;

    height: 140px;

    right: -45px;

    top: -70px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.12);
}

.section-title {

    font-size: 27px;

    font-weight: 900;

    position: relative;

    z-index: 2;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);

    margin-top: 5px;

    position: relative;

    z-index: 2;
}

/* =========================================================
PROFILE CARD
========================================================= */

.profile-card {

    background: white;

    padding: 32px;

    border-radius: 28px;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);
}

.avatar {

    width: 110px;

    height: 110px;

    border-radius: 50%;

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    display: flex;

    align-items: center;

    justify-content: center;

    color: white;

    font-size: 52px;

    margin-bottom: 18px;
}

/* =========================================================
STATUS CARD
========================================================= */

.status-card {

    padding: 25px;

    border-radius: 22px;

    color: white;

    min-height: 145px;

    box-shadow:
    0 12px 30px
    rgba(0,0,0,0.10);
}

.blue {

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
}

.green {

    background:
    linear-gradient(
        135deg,
        #059669,
        #22C55E
    );
}

.purple {

    background:
    linear-gradient(
        135deg,
        #7C3AED,
        #EC4899
    );
}

.orange {

    background:
    linear-gradient(
        135deg,
        #F97316,
        #EF4444
    );
}

/* =========================================================
PROPERTY CARD
========================================================= */

.property-card {

    background: white;

    border-radius: 24px;

    overflow: hidden;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.08);

    margin-bottom: 20px;
}

.property-image {

    width: 100%;

    height: 200px;

    object-fit: cover;
}

.property-content {

    padding: 22px;
}

/* =========================================================
ACTIVITY
========================================================= */

.activity-card {

    background: white;

    padding: 22px;

    border-radius: 20px;

    margin-bottom: 14px;

    box-shadow:
    0 8px 25px
    rgba(0,0,0,0.06);
}

/* =========================================================
PREMIUM CARD
========================================================= */

.premium-card {

    padding: 35px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 20px 50px
    rgba(124,58,237,0.25);
}

/* =========================================================
FOOTER
========================================================= */

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
PROPERTY HUB • INDIA'S SMART REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown("""
<div class="page-header">

<div class="page-title">
👤 My Account
</div>

<div class="page-subtitle">
Manage your profile, properties, favourites,
verification and real estate activities from one place.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROFILE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
👤 Personal Profile
</div>

<div class="section-subtitle">
Your FirstChoice Property Hub identity and account information.
</div>

</div>
""", unsafe_allow_html=True)

p1, p2 = st.columns([1, 2])

with p1:

    st.markdown("""
    <div class="profile-card">

    <div class="avatar">
    👤
    </div>

    <h2>
    Welcome, Property User
    </h2>

    <p>
    🟢 Active Account
    </p>

    </div>
    """, unsafe_allow_html=True)

with p2:

    name = st.text_input(
        "Full Name",
        value="Property User"
    )

    mobile = st.text_input(
        "Mobile Number",
        value="+91 XXXXX XXXXX"
    )

    email = st.text_input(
        "Email Address",
        value="user@example.com"
    )

    location = st.text_input(
        "City",
        value="Nagpur, Maharashtra"
    )

    if st.button(
        "💾 Save Profile",
        use_container_width=True
    ):

        st.success(
            "Profile information updated successfully."
        )


# ============================================================
# VERIFICATION STATUS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🛡️ Verification & Trust
</div>

<div class="section-subtitle">
Verified profiles help build confidence between property owners and buyers.
</div>

</div>
""", unsafe_allow_html=True)

v1,v2,v3,v4 = st.columns(4)

statuses = [
    ("📱","Mobile","Verified","green"),
    ("✉️","Email","Verified","blue"),
    ("🛡️","Identity","Pending","orange"),
    ("🏠","Owner Profile","Not Verified","purple")
]

for col, item in zip(
    [v1,v2,v3,v4],
    statuses
):

    with col:

        st.markdown(
            f"""
            <div class="status-card {item[3]}">

            <div style="font-size:35px;">
            {item[0]}
            </div>

            <h3>
            {item[1]}
            </h3>

            <b>
            {item[2]}
            </b>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DASHBOARD STATS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📊 My Property Dashboard
</div>

<div class="section-subtitle">
Track your property activity and marketplace engagement.
</div>

</div>
""", unsafe_allow_html=True)

d1,d2,d3,d4 = st.columns(4)

stats = [
    ("🏡","My Listings","3"),
    ("❤️","Saved Properties","12"),
    ("👁️","Total Views","1,245"),
    ("💬","Enquiries","27")
]

for col, item in zip(
    [d1,d2,d3,d4],
    stats
):

    with col:

        st.metric(
            label=f"{item[0]} {item[1]}",
            value=item[2]
        )


# ============================================================
# MY LISTINGS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏡 My Property Listings
</div>

<div class="section-subtitle">
Manage the properties you have listed on FirstChoice Property Hub.
</div>

</div>
""", unsafe_allow_html=True)

properties = [

    (
        "Premium 3 BHK Apartment",
        "Nagpur, Maharashtra",
        "₹1.25 Cr",
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1000&q=85"
    ),

    (
        "Luxury Independent Villa",
        "Pune, Maharashtra",
        "₹2.80 Cr",
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1000&q=85"
    ),

    (
        "Premium Residential Plot",
        "Nagpur, Maharashtra",
        "₹48 Lakh",
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1000&q=85"
    )
]

cols = st.columns(3)

for col, property_item in zip(
    cols,
    properties
):

    with col:

        st.markdown(
            f"""
            <div class="property-card">

            <img
            class="property-image"
            src="{property_item[3]}"
            >

            <div class="property-content">

            <h3>
            {property_item[0]}
            </h3>

            <p>
            📍 {property_item[1]}
            </p>

            <h2 style="color:#7C3AED;">
            {property_item[2]}
            </h2>

            <p>
            🟢 Active Listing
            </p>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        c1,c2 = st.columns(2)

        with c1:

            st.button(
                "✏️ Edit",
                use_container_width=True,
                key=f"edit_{property_item[0]}"
            )

        with c2:

            st.button(
                "📊 Analytics",
                use_container_width=True,
                key=f"analytics_{property_item[0]}"
            )


# ============================================================
# SAVED PROPERTIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
❤️ Saved Properties
</div>

<div class="section-subtitle">
Properties you have saved for future consideration.
</div>

</div>
""", unsafe_allow_html=True)

saved = st.selectbox(
    "Select Saved Property",
    [
        "Luxury 3 BHK Apartment — Nagpur",
        "Premium Villa — Pune",
        "Residential Plot — Bengaluru",
        "Commercial Office — Mumbai"
    ]
)

if st.button(
    "🏡 View Saved Property",
    use_container_width=True
):

    st.info(
        f"Opening: {saved}"
    )


# ============================================================
# SITE VISITS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📅 My Site Visits
</div>

<div class="section-subtitle">
Track upcoming and previous property visits.
</div>

</div>
""", unsafe_allow_html=True)

visit1, visit2 = st.columns(2)

with visit1:

    st.markdown("""
    <div class="activity-card">

    <h3>
    🏡 Premium 3 BHK Apartment
    </h3>

    <p>
    📍 Civil Lines, Nagpur
    </p>

    <p>
    📅 25 July 2026
    </p>

    <p>
    ⏰ 11:00 AM
    </p>

    <b style="color:#059669;">
    🟢 Confirmed
    </b>

    </div>
    """, unsafe_allow_html=True)

with visit2:

    st.markdown("""
    <div class="activity-card">

    <h3>
    🏠 Luxury Villa
    </h3>

    <p>
    📍 Pune, Maharashtra
    </p>

    <p>
    📅 30 July 2026
    </p>

    <p>
    ⏰ 4:00 PM
    </p>

    <b style="color:#F97316;">
    🟡 Pending Confirmation
    </b>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# ENQUIRIES
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
💬 My Property Enquiries
</div>

<div class="section-subtitle">
Manage conversations and enquiries related to properties.
</div>

</div>
""", unsafe_allow_html=True)

enquiry = st.selectbox(
    "Select Enquiry",
    [
        "Premium 3 BHK Apartment",
        "Luxury Villa",
        "Residential Plot"
    ]
)

message = st.text_area(
    "Message",
    placeholder="Write your message..."
)

if st.button(
    "📤 Send Message",
    use_container_width=True
):

    st.success(
        "Message sent successfully."
    )


# ============================================================
# PREMIUM LISTING
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⭐ Premium Listing
</div>

<div class="section-subtitle">
Increase your property's visibility across the marketplace.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="premium-card">

<h2>
🚀 Boost Your Property
</h2>

<p>
Featured properties can receive higher visibility,
priority placement and premium badges.
</p>

<h3>
✨ Featured Listing
</h3>

<p>
Your property can appear in premium discovery sections.
</p>

</div>
""", unsafe_allow_html=True)

if st.button(
    "⭐ Explore Premium Listing",
    use_container_width=True
):

    st.info(
        "Premium listing plans will be connected to the payment system in the production version."
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
Manage your account preferences and security.
</div>

</div>
""", unsafe_allow_html=True)

settings = st.selectbox(
    "Account Option",
    [
        "Edit Profile",
        "Change Mobile Number",
        "Change Email",
        "Privacy Settings",
        "Notification Preferences",
        "Security Settings"
    ]
)

if st.button(
    "⚙️ Open Settings",
    use_container_width=True
):

    st.info(
        f"Opening: {settings}"
    )


# ============================================================
# LOGOUT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚪 Account Access
</div>

<div class="section-subtitle">
Securely manage your current session.
</div>

</div>
""", unsafe_allow_html=True)

if st.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state.clear()

    st.success(
        "You have been logged out successfully."
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
