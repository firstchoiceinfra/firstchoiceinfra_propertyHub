import streamlit as st

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.database import (
    get_notifications,
    get_unread_notification_count,
    mark_notification_as_read
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 09 — NOTIFICATIONS CENTER
# ============================================================

st.set_page_config(
    page_title="Notifications | FirstChoice Property Hub",
    page_icon="🔔",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM UI
# ============================================================

load_premium_ui()


# ============================================================
# SESSION
# ============================================================

logged_in = st.session_state.get(
    "logged_in",
    False
)

user_role = st.session_state.get(
    "user_role",
    ""
)

user_id = st.session_state.get(
    "user_id",
    None
)


# ============================================================
# LOGIN CHECK
# ============================================================

if not logged_in:

    hero(
        "🔐 Login Required",
        "Please login to access your notification center."
    )

    st.warning(
        "You must login before viewing notifications."
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
# HERO
# ============================================================

hero(
    "🔔 Notifications Center",
    "Stay updated with important messages, feedback updates and platform activities."
)


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

        <h1>🔔 FirstChoice</h1>

        <h3>Notification Center</h3>

        <hr>

        <p>
        Stay Connected
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

    st.page_link(
        "pages/06_Boss_Dashboard.py",
        label="👑 Boss Dashboard"
    )

    st.page_link(
        "pages/07_Manager_Dashboard.py",
        label="👔 Manager Dashboard"
    )

    st.page_link(
        "pages/08_Feedback_Suggestions.py",
        label="💡 Feedback & Suggestions"
    )


# ============================================================
# GET NOTIFICATIONS
# ============================================================

notifications = get_notifications(

    recipient_role=user_role,

    recipient_user_id=user_id

)


unread_count = get_unread_notification_count(

    recipient_role=user_role,

    recipient_user_id=user_id

)


# ============================================================
# NOTIFICATION SUMMARY
# ============================================================

section(
    "📊 Notification Overview",
    "Your latest system and company notifications."
)


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {len(notifications)}
        </div>

        <div class="fc-stat-label">
        Total Notifications
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        f"""
        <div class="fc-warning">

        <div class="fc-stat-number">
        {unread_count}
        </div>

        <div class="fc-stat-label">
        Unread Notifications
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        f"""
        <div class="fc-success">

        <div class="fc-stat-number">
        {len(notifications) - unread_count}
        </div>

        <div class="fc-stat-label">
        Read Notifications
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# NOTIFICATION LIST
# ============================================================

section(
    "🔔 Your Notifications",
    "Click a notification to mark it as read."
)


if not notifications:

    st.info(
        "🎉 You don't have any notifications right now."
    )


else:

    for notification in notifications:

        notification_id = notification["id"]

        title = notification["title"]

        message = notification["message"]

        notification_type = notification[
            "notification_type"
        ]

        is_read = notification["is_read"]

        created_at = notification["created_at"]


        if is_read:

            st.markdown(
                f"""
                <div class="fc-card">

                <h3>
                📩 {title}
                </h3>

                <p>
                {message}
                </p>

                <small>
                🕒 {created_at}
                </small>

                </div>
                """,
                unsafe_allow_html=True
            )


        else:

            st.markdown(
                f"""
                <div class="fc-success">

                <h3>
                🔔 {title}
                </h3>

                <p>
                {message}
                </p>

                <small>
                🕒 {created_at}
                </small>

                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(

                "✅ Mark as Read",

                key=f"read_{notification_id}",

                use_container_width=True

            ):

                mark_notification_as_read(

                    notification_id

                )

                st.success(
                    "Notification marked as read."
                )

                st.rerun()


# ============================================================
# FOOTER
# ============================================================

footer()
