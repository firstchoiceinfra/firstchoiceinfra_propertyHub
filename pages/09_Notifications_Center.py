import streamlit as st
from datetime import datetime


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 09 — NOTIFICATIONS CENTER
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Notifications | FirstChoice Property Hub",
    page_icon="🔔",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CORE UI
# ============================================================

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)


# ============================================================
# PREMIUM UI
# ============================================================

load_premium_ui()


# ============================================================
# SESSION DATA
# ============================================================

logged_in = st.session_state.get(
    "logged_in",
    False
)

user_role = st.session_state.get(
    "user_role",
    "user"
)

user_id = st.session_state.get(
    "user_id",
    None
)


# ============================================================
# SESSION NOTIFICATION STORAGE
# ============================================================

if "notifications" not in st.session_state:

    st.session_state.notifications = []


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


    st.markdown(
        "### 📌 Navigation"
    )


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
# FILTER NOTIFICATIONS FOR CURRENT USER
# ============================================================

all_notifications = st.session_state.notifications


user_notifications = []


for notification in all_notifications:

    recipient_role = notification.get(
        "recipient_role",
        "all"
    )


    recipient_user_id = notification.get(
        "recipient_user_id",
        None
    )


    role_match = (

        recipient_role == "all"

        or

        recipient_role == user_role

    )


    user_match = (

        recipient_user_id is None

        or

        recipient_user_id == user_id

    )


    if role_match and user_match:

        user_notifications.append(
            notification
        )


# ============================================================
# UNREAD COUNT
# ============================================================

unread_count = sum(

    1

    for notification

    in user_notifications

    if not notification.get(
        "is_read",
        False
    )

)


total_count = len(
    user_notifications
)


read_count = (

    total_count

    -

    unread_count

)


# ============================================================
# NOTIFICATION OVERVIEW
# ============================================================

section(
    "📊 Notification Overview",
    "Your latest system and company notifications."
)


c1, c2, c3 = st.columns(3)


# ============================================================
# TOTAL
# ============================================================

with c1:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_count}
        </div>

        <div class="fc-stat-label">
        Total Notifications
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# UNREAD
# ============================================================

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


# ============================================================
# READ
# ============================================================

with c3:

    st.markdown(
        f"""
        <div class="fc-success">

        <div class="fc-stat-number">
        {read_count}
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
    "View your latest updates and important messages."
)


# ============================================================
# EMPTY STATE
# ============================================================

if not user_notifications:

    st.info(
        "🎉 You don't have any notifications right now."
    )


# ============================================================
# SHOW NOTIFICATIONS
# ============================================================

else:

    for index, notification in enumerate(
        user_notifications
    ):

        title = notification.get(
            "title",
            "Notification"
        )


        message = notification.get(
            "message",
            ""
        )


        notification_type = notification.get(
            "notification_type",
            "general"
        )


        is_read = notification.get(
            "is_read",
            False
        )


        created_at = notification.get(
            "created_at",
            ""
        )


        notification_id = notification.get(
            "id",
            index
        )


        # ====================================================
        # UNREAD NOTIFICATION
        # ====================================================

        if not is_read:

            st.markdown(
                f"""
                <div class="fc-success">

                <h3>
                🔔 {title}
                </h3>

                <p>
                {message}
                </p>

                <p>
                <b>📌 Type:</b>
                {notification_type}
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
                key=f"read_{notification_id}_{index}",
                use_container_width=True
            ):

                # Find original notification
                for original_notification in (
                    st.session_state.notifications
                ):

                    if (
                        original_notification.get(
                            "id"
                        )
                        == notification_id
                    ):

                        original_notification[
                            "is_read"
                        ] = True

                        break


                st.success(
                    "Notification marked as read."
                )


                st.rerun()


        # ====================================================
        # READ NOTIFICATION
        # ====================================================

        else:

            st.markdown(
                f"""
                <div class="fc-card">

                <h3>
                📩 {title}
                </h3>

                <p>
                {message}
                </p>

                <p>
                <b>📌 Type:</b>
                {notification_type}
                </p>

                <small>
                🕒 {created_at}
                </small>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# DEMO NOTIFICATION
# ============================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)


with st.expander(
    "🧪 Notification System Test"
):

    st.info(
        "This section is for testing the notification UI."
    )


    if st.button(
        "🔔 Create Test Notification",
        use_container_width=True
    ):

        new_notification = {

            "id": int(
                datetime.now().timestamp()
            ),

            "recipient_role":
                user_role,

            "recipient_user_id":
                user_id,

            "title":
                "Welcome to FirstChoice Property Hub",

            "message":
                "This is a test notification. "
                "Your notification system is working successfully.",

            "notification_type":
                "system",

            "is_read":
                False,

            "created_at":
                datetime.now().strftime(
                    "%d %B %Y, %I:%M %p"
                )

        }


        st.session_state.notifications.append(
            new_notification
        )


        st.success(
            "🎉 Test notification created successfully."
        )


        st.rerun()


# ============================================================
# FOOTER
# ============================================================

footer()
