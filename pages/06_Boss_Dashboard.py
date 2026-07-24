import streamlit as st

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.database import get_connection


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 06 — BOSS / OWNER DASHBOARD
# ============================================================

st.set_page_config(
    page_title="Boss Dashboard | FirstChoice Property Hub",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM UI
# ============================================================

load_premium_ui()


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

        <h1>👑 FirstChoice</h1>

        <h3>Boss Dashboard</h3>

        <hr>

        <p>
        Executive Business Intelligence
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

    st.page_link(
        "pages/04_Property_Details.py",
        label="📋 Property Details"
    )

    st.page_link(
        "pages/05_Admin_Panel.py",
        label="🛡️ Admin Panel"
    )


# ============================================================
# BOSS SECURITY CHECK
# ============================================================

logged_in = st.session_state.get(
    "logged_in",
    False
)

user_role = st.session_state.get(
    "user_role",
    ""
)


if not logged_in:

    hero(
        "🔐 Secure Boss Access",
        "This dashboard is restricted to authorized company owners."
    )

    st.error(
        "Please login to access the Boss Dashboard."
    )

    if st.button(
        "🔐 Go to Login",
        use_container_width=True
    ):

        st.switch_page(
            "pages/01_Login_Register.py"
        )

    footer()

    st.stop()


# ============================================================
# BOSS ROLE CHECK
# ============================================================

if user_role not in [
    "boss",
    "owner"
]:

    hero(
        "🚫 Confidential Area",
        "This dashboard contains confidential company-level information."
    )

    st.error(
        "You do not have Boss / Owner level permission."
    )

    st.info(
        f"Current Role: {user_role or 'Unknown'}"
    )

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.switch_page(
            "app.py"
        )

    footer()

    st.stop()


# ============================================================
# BOSS HERO
# ============================================================

hero(
    "👑 Boss Executive Dashboard",
    "Confidential business intelligence and company performance overview."
)


# ============================================================
# DATABASE STATISTICS
# ============================================================

connection = get_connection()

cursor = connection.cursor()


# ============================================================
# TOTAL USERS
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM users
    """
)

total_users = cursor.fetchone()[0]


# ============================================================
# ACTIVE USERS
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM users
    WHERE account_status = 'active'
    """
)

active_users = cursor.fetchone()[0]


# ============================================================
# TOTAL PROPERTIES
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    """
)

total_properties = cursor.fetchone()[0]


# ============================================================
# ACTIVE / APPROVED PROPERTIES
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE property_status = 'approved'
    """
)

active_ads = cursor.fetchone()[0]


# ============================================================
# INACTIVE PROPERTIES
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE property_status != 'approved'
    """
)

inactive_ads = cursor.fetchone()[0]


# ============================================================
# TOTAL VIEWS
# ============================================================

cursor.execute(
    """
    SELECT COALESCE(SUM(views), 0)
    FROM properties
    """
)

total_views = cursor.fetchone()[0]


# ============================================================
# PREMIUM PROPERTY COUNT
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE is_premium = 1
    """
)

premium_properties = cursor.fetchone()[0]


# ============================================================
# NON PREMIUM PROPERTY COUNT
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE is_premium = 0
    """
)

non_premium_properties = cursor.fetchone()[0]


connection.close()


# ============================================================
# BUSINESS OVERVIEW
# ============================================================

section(
    "📊 Company Business Overview",
    "Confidential performance information available only to Boss / Owner."
)


# ============================================================
# ROW 1
# ============================================================

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_users}
        </div>

        <div class="fc-stat-label">
        Total Users
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        f"""
        <div class="fc-success">

        <div class="fc-stat-number">
        {active_users}
        </div>

        <div class="fc-stat-label">
        Active Users
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_properties}
        </div>

        <div class="fc-stat-label">
        Total Ads
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c4:

    st.markdown(
        f"""
        <div class="fc-success">

        <div class="fc-stat-number">
        {active_ads}
        </div>

        <div class="fc-stat-label">
        Active Ads
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ROW 2
# ============================================================

st.write("")


c5, c6, c7, c8 = st.columns(4)


with c5:

    st.markdown(
        f"""
        <div class="fc-warning">

        <div class="fc-stat-number">
        {inactive_ads}
        </div>

        <div class="fc-stat-label">
        Inactive Ads
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c6:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_views}
        </div>

        <div class="fc-stat-label">
        Total Property Views
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c7:

    st.markdown(
        f"""
        <div class="fc-success">

        <div class="fc-stat-number">
        {premium_properties}
        </div>

        <div class="fc-stat-label">
        Premium Listings
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c8:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {non_premium_properties}
        </div>

        <div class="fc-stat-label">
        Non-Premium Listings
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PREMIUM BUSINESS SECTION
# ============================================================

section(
    "⭐ Premium Business Intelligence",
    "Premium subscription and revenue analytics will be connected here."
)


p1, p2, p3 = st.columns(3)


with p1:

    st.markdown(
        """
        <div class="fc-card">

        <h3>⭐ Premium Users</h3>

        <p>
        Premium subscription users will be displayed here.
        </p>

        <h2>
        Coming Soon
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with p2:

    st.markdown(
        """
        <div class="fc-card">

        <h3>💰 Total Revenue</h3>

        <p>
        Subscription and premium listing revenue
        will be connected to the payment system.
        </p>

        <h2>
        ₹ 0
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with p3:

    st.markdown(
        """
        <div class="fc-card">

        <h3>📈 Company Profit</h3>

        <p>
        Net company profit will be calculated
        after connecting revenue and expense data.
        </p>

        <h2>
        ₹ 0
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# VIEWER ANALYTICS
# ============================================================

section(
    "👁️ Viewer Analytics",
    "Track how users interact with property listings."
)


v1, v2, v3 = st.columns(3)


with v1:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_views}
        </div>

        <div class="fc-stat-label">
        Total Property Views
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with v2:

    st.markdown(
        """
        <div class="fc-success">

        <div class="fc-stat-number">
        --
        </div>

        <div class="fc-stat-label">
        Active Viewers
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with v3:

    st.markdown(
        """
        <div class="fc-warning">

        <div class="fc-stat-number">
        --
        </div>

        <div class="fc-stat-label">
        Inactive Viewers
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CONFIDENTIALITY
# ============================================================

section(
    "🔒 Confidentiality & Security",
    "This dashboard is intended only for authorized Boss / Owner accounts."
)


st.warning(
    """
    ⚠️ Revenue, profit, payment and company financial information
    must never be displayed to Manager, Admin or regular User accounts.
    """
)


# ============================================================
# FOOTER
# ============================================================

footer()
