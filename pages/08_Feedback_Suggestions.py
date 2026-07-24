import streamlit as st

from datetime import datetime

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.database import (
    save_feedback
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 08 — FEEDBACK & SUGGESTIONS
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Feedback & Suggestions | FirstChoice Property Hub",
    page_icon="💡",
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

user_id = st.session_state.get(
    "user_id",
    None
)

user_role = st.session_state.get(
    "user_role",
    "user"
)


# ============================================================
# NOTIFICATION STORAGE
# ============================================================

if "notifications" not in st.session_state:

    st.session_state.notifications = []


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

        <h1>💡 FirstChoice</h1>

        <h3>Feedback Center</h3>

        <hr>

        <p>
        Your Voice Helps Us Improve
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
        "pages/09_Notifications_Center.py",
        label="🔔 Notifications Center"
    )


# ============================================================
# HERO
# ============================================================

hero(
    "💡 Feedback & Suggestions",
    "Your feedback helps FirstChoice Infra Property Hub become better, faster and more powerful."
)


# ============================================================
# INTRODUCTION
# ============================================================

section(
    "🗣️ We Want To Hear From You",
    "Share your experience, report an issue or suggest a new feature."
)


st.markdown(
    """
    <div class="fc-card">

    <h3>🚀 Help Us Build The Future</h3>

    <p>
    FirstChoice Infra Property Hub is continuously improving.
    Your suggestions and feedback are important to us.
    </p>

    <p>
    You can report a technical issue, suggest a new feature,
    share your experience or send us a general message.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOGIN INFORMATION
# ============================================================

if logged_in:

    st.success(
        "✅ You are logged in. Your feedback will be linked to your account."
    )

else:

    st.info(
        "ℹ️ You can submit feedback without logging in. "
        "Please provide your correct name and email."
    )


# ============================================================
# FEEDBACK FORM
# ============================================================

section(
    "📝 Submit Your Feedback",
    "Please provide accurate information so our team can respond appropriately."
)


with st.form(
    "feedback_form",
    clear_on_submit=True
):

    col1, col2 = st.columns(2)


    # ========================================================
    # NAME
    # ========================================================

    with col1:

        name = st.text_input(
            "👤 Your Full Name",
            placeholder="Enter your full name"
        )


    # ========================================================
    # EMAIL
    # ========================================================

    with col2:

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your email address"
        )


    # ========================================================
    # CATEGORY
    # ========================================================

    category = st.selectbox(

        "📌 Feedback Type",

        [

            "General Feedback",

            "⭐ Software Review",

            "💡 New Feature Suggestion",

            "🐛 Bug Report",

            "⚠️ Complaint",

            "💳 Payment Related Issue",

            "🔐 Login / Account Issue",

            "🏡 Property Listing Issue",

            "🔎 Property Search Issue",

            "📱 Mobile / UI Issue",

            "Other"

        ]

    )


    # ========================================================
    # MESSAGE
    # ========================================================

    message = st.text_area(

        "📝 Your Message",

        placeholder=(
            "Please describe your feedback, "
            "suggestion, problem or idea in detail..."
        ),

        height=180

    )


    # ========================================================
    # RATING
    # ========================================================

    rating = st.select_slider(

        "⭐ How would you rate your experience?",

        options=[

            1,
            2,
            3,
            4,
            5

        ],

        value=5

    )


    # ========================================================
    # SUBMIT
    # ========================================================

    submit = st.form_submit_button(

        "🚀 Submit Feedback",

        use_container_width=True

    )


# ============================================================
# SUBMISSION
# ============================================================

if submit:


    # ========================================================
    # VALIDATION
    # ========================================================

    if not name.strip():

        st.error(
            "⚠️ Please enter your full name."
        )

        st.stop()


    if not email.strip():

        st.error(
            "⚠️ Please enter your email address."
        )

        st.stop()


    if "@" not in email or "." not in email:

        st.error(
            "⚠️ Please enter a valid email address."
        )

        st.stop()


    if not message.strip():

        st.error(
            "⚠️ Please enter your feedback message."
        )

        st.stop()


    # ========================================================
    # SAVE FEEDBACK
    # ========================================================

    try:

        save_feedback(

            name=name.strip(),

            email=email.strip(),

            category=category,

            message=message.strip(),

            user_id=user_id

        )


        # ====================================================
        # NOTIFICATION MESSAGE
        # ====================================================

        notification_message = (

            f"New feedback has been submitted.\n\n"

            f"Category: {category}\n\n"

            f"Submitted By: {name.strip()}\n\n"

            f"Email: {email.strip()}\n\n"

            f"Rating: {rating}/5\n\n"

            f"Message: {message.strip()}"

        )


        # ====================================================
        # UNIQUE NOTIFICATION ID
        # ====================================================

        base_id = int(
            datetime.now().timestamp() * 1000
        )


        # ====================================================
        # NOTIFICATION FUNCTION
        # ====================================================

        def create_notification(

            recipient_role,

            notification_id

        ):

            st.session_state.notifications.append(

                {

                    "id":
                        notification_id,

                    "recipient_role":
                        recipient_role,

                    "recipient_user_id":
                        None,

                    "title":
                        "💡 New Feedback Received",

                    "message":
                        notification_message,

                    "notification_type":
                        "feedback",

                    "is_read":
                        False,

                    "created_at":
                        datetime.now().strftime(
                            "%d %B %Y, %I:%M %p"
                        )

                }

            )


        # ====================================================
        # BOSS NOTIFICATION
        # ====================================================

        create_notification(

            "boss",

            base_id + 1

        )


        # ====================================================
        # MANAGER NOTIFICATION
        # ====================================================

        create_notification(

            "manager",

            base_id + 2

        )


        # ====================================================
        # ADMIN NOTIFICATION
        # ====================================================

        create_notification(

            "admin",

            base_id + 3

        )


        # ====================================================
        # SUCCESS MESSAGE
        # ====================================================

        st.success(
            "🎉 Thank you! Your feedback has been submitted successfully."
        )


        st.info(
            "📩 Your feedback has been forwarded to the appropriate management teams."
        )


        st.success(
            f"⭐ Your experience rating: {rating}/5"
        )


        st.balloons()


    except Exception as e:

        st.error(
            "❌ Unable to submit your feedback at the moment."
        )


# ============================================================
# SUGGESTION BOX
# ============================================================

section(
    "💡 Feature Suggestion Box",
    "Have an idea that can make FirstChoice Property Hub better?"
)


st.markdown(
    """
    <div class="fc-success">

    <h2>🚀 Your Idea Could Become Our Next Feature</h2>

    <p>
    Do you have an idea for a new property feature,
    better search experience, advanced dashboard,
    AI-powered property recommendation or anything else?
    </p>

    <p>
    Send your suggestion using the form above and our
    management and technology team will review it.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MANAGEMENT COMMUNICATION
# ============================================================

section(
    "📩 Management Communication",
    "Important feedback can be reviewed by authorized company teams."
)


st.info(
    """
    Your submitted feedback will be stored securely in the
    FirstChoice Infra Property Hub system.

    Depending on the category, the feedback may be reviewed
    by the appropriate authorized team.

    Important feedback and complaints may be forwarded to
    authorized management personnel for further action.
    """
)


# ============================================================
# FOOTER
# ============================================================

footer()
