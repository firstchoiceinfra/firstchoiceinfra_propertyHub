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
# PAGE 07 — MANAGER DASHBOARD
# ============================================================

st.set_page_config(
    page_title="Manager Dashboard | FirstChoice Property Hub",
    page_icon="👔",
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

        <h1>👔 FirstChoice</h1>

        <h3>Manager Dashboard</h3>

        <hr>

        <p>
        Company Operations Center
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
# MANAGER SECURITY
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
        "🔐 Manager Login Required",
        "Please login with an authorized Manager account."
    )

    st.error(
        "You must login before accessing the Manager Dashboard."
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
# MANAGER ROLE CHECK
# ============================================================

if user_role != "manager":

    hero(
        "🚫 Access Restricted",
        "This dashboard is available only to authorized company Managers."
    )

    st.error(
        "You do not have Manager level permission."
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
# MANAGER HERO
# ============================================================

hero(
    "👔 Manager Operations Dashboard",
    "Monitor company operations, property activity and platform performance."
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

connection = get_connection()

cursor = connection.cursor()


# ============================================================
# USERS
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM users
    """
)

total_users = cursor.fetchone()[0]


cursor.execute(
    """
    SELECT COUNT(*)
    FROM users
    WHERE account_status = 'active'
    """
)

active_users = cursor.fetchone()[0]


# ============================================================
# PROPERTIES
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    """
)

total_properties = cursor.fetchone()[0]


cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE property_status = 'approved'
    """
)

approved_properties = cursor.fetchone()[0]


cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE property_status = 'pending'
    """
)

pending_properties = cursor.fetchone()[0]


cursor.execute(
    """
    SELECT COUNT(*)
    FROM properties
    WHERE property_status = 'rejected'
    """
)

rejected_properties = cursor.fetchone()[0]


# ============================================================
# VIEWS
# ============================================================

cursor.execute(
    """
    SELECT COALESCE(SUM(views), 0)
    FROM properties
    """
)

total_views = cursor.fetchone()[0]


# ============================================================
# FEEDBACK
# ============================================================

cursor.execute(
    """
    SELECT COUNT(*)
    FROM feedback
    """
)

total_feedback = cursor.fetchone()[0]


cursor.execute(
    """
    SELECT COUNT(*)
    FROM feedback
    WHERE status = 'new'
    """
)

new_feedback = cursor.fetchone()[0]


connection.close()


# ============================================================
# COMPANY OPERATIONS
# ============================================================

section(
    "📊 Company Operations Overview",
    "Manager-level operational information. Confidential Boss financial data is restricted."
)


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
        Total Properties
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
        {approved_properties}
        </div>

        <div class="fc-stat-label">
        Approved Properties
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PROPERTY OPERATIONS
# ============================================================

st.write("")


section(
    "🏡 Property Operations",
    "Monitor property approval and listing activity."
)


p1, p2, p3, p4 = st.columns(4)


with p1:

    st.markdown(
        f"""
        <div class="fc-warning">

        <div class="fc-stat-number">
        {pending_properties}
        </div>

        <div class="fc-stat-label">
        Pending Properties
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with p2:

    st.markdown(
        f"""
        <div class="fc-success">

        <div class="fc-stat-number">
        {approved_properties}
        </div>

        <div class="fc-stat-label">
        Approved Properties
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with p3:

    st.markdown(
        f"""
        <div class="fc-danger">

        <div class="fc-stat-number">
        {rejected_properties}
        </div>

        <div class="fc-stat-label">
        Rejected Properties
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with p4:

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


# ============================================================
# FEEDBACK MANAGEMENT
# ============================================================

section(
    "💬 Customer Feedback",
    "Monitor feedback and suggestions submitted by users."
)


f1, f2 = st.columns(2)


with f1:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_feedback}
        </div>

        <div class="fc-stat-label">
        Total Feedback
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with f2:

    st.markdown(
        f"""
        <div class="fc-warning">

        <div class="fc-stat-number">
        {new_feedback}
        </div>

        <div class="fc-stat-label">
        New Feedback
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# QUICK MANAGEMENT ACTIONS
# ============================================================

section(
    "⚡ Quick Management Actions",
    "Access important company operations."
)


a1, a2, a3 = st.columns(3)


with a1:

    if st.button(
        "🏡 Review Properties",
        use_container_width=True
    ):

        st.switch_page(
            "pages/05_Admin_Panel.py"
        )


with a2:

    if st.button(
        "💬 Review Feedback",
        use_container_width=True
    ):

        st.info(
            "Feedback Management Center will be connected in the next module."
        )


with a3:

    if st.button(
        "📊 View Property Search",
        use_container_width=True
    ):

        st.switch_page(
            "pages/02_Property_Search.py"
        )


# ============================================================
# SECURITY NOTICE
# ============================================================

section(
    "🔒 Manager Access Policy",
    "Manager accounts can access operational information only."
)


st.info(
    """
    Manager accounts cannot access:

    • Company Revenue
    • Company Profit
    • Payment Information
    • Subscription Revenue
    • Financial Reports
    • Boss Confidential Analytics
    """
)


# ============================================================
# FOOTER
# ============================================================

footer()
