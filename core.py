# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# CORE.PY
# Shared UI, Navigation, Security & Utility Functions
# ============================================================

import streamlit as st
from datetime import datetime


# ============================================================
# 1. GLOBAL PAGE CONFIG
# ============================================================

def configure_page(
    title="FirstChoice Infra Property Hub",
    icon="🏠"
):
    """
    Common Streamlit page configuration.
    हर page में इसी function को call किया जा सकता है.
    """

    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )


# ============================================================
# 2. PREMIUM GLOBAL UI
# ============================================================

def load_global_css():

    st.markdown(
        """
        <style>

        /* ====================================================
           MAIN APP BACKGROUND
        ==================================================== */

        .stApp {

            background:
            linear-gradient(
                135deg,
                #F7F9FF 0%,
                #FFF7F3 30%,
                #F7F1FF 65%,
                #EFFCFF 100%
            );

        }


        /* ====================================================
           HIDE DEFAULT STREAMLIT ELEMENTS
        ==================================================== */

        header {
            visibility: hidden;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }


        /* ====================================================
           SIDEBAR
        ==================================================== */

        [data-testid="stSidebar"] {

            background:
            linear-gradient(
                180deg,
                #020617,
                #0F172A,
                #1E1B4B,
                #4C1D95
            );

        }


        [data-testid="stSidebar"] * {

            color: white !important;

        }


        /* ====================================================
           MAIN HERO
        ==================================================== */

        .fc-hero {

            padding: 50px;

            border-radius: 35px;

            color: white;

            background:
            linear-gradient(
                135deg,
                #020617,
                #1D4ED8,
                #6D28D9,
                #DB2777
            );

            box-shadow:
            0 25px 70px
            rgba(37, 99, 235, 0.30);

            margin-bottom: 30px;

        }


        .fc-hero-title {

            font-size: 46px;

            font-weight: 900;

            line-height: 1.1;

            margin-bottom: 15px;

        }


        .fc-hero-subtitle {

            font-size: 18px;

            line-height: 1.7;

            color:
            rgba(255,255,255,0.90);

        }


        /* ====================================================
           SECTION HEADER
        ==================================================== */

        .fc-section {

            padding: 28px 32px;

            border-radius: 28px;

            color: white;

            background:
            linear-gradient(
                135deg,
                #0F172A,
                #1D4ED8,
                #6D28D9,
                #DB2777
            );

            box-shadow:
            0 15px 45px
            rgba(37,99,235,0.20);

            margin-top: 30px;

            margin-bottom: 25px;

        }


        .fc-section h2 {

            margin: 0;

            font-size: 28px;

            font-weight: 900;

        }


        .fc-section p {

            margin-top: 10px;

            font-size: 16px;

            color:
            rgba(255,255,255,0.90);

        }


        /* ====================================================
           PREMIUM CARD
        ==================================================== */

        .fc-card {

            padding: 28px;

            border-radius: 28px;

            background:
            rgba(255,255,255,0.92);

            border:
            1px solid
            rgba(255,255,255,0.70);

            box-shadow:
            0 15px 40px
            rgba(15,23,42,0.10);

            margin-bottom: 20px;

        }


        /* ====================================================
           3D PROPERTY CARD
        ==================================================== */

        .fc-property-card {

            padding: 25px;

            border-radius: 25px;

            background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FAFC,
                #EEF2FF
            );

            border:
            1px solid #E2E8F0;

            box-shadow:
            0 12px 25px
            rgba(15,23,42,0.08),

            0 25px 55px
            rgba(79,70,229,0.10);

            transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;

        }


        .fc-property-card:hover {

            transform:
            translateY(-7px);

            box-shadow:
            0 20px 35px
            rgba(15,23,42,0.14),

            0 35px 70px
            rgba(79,70,229,0.15);

        }


        /* ====================================================
           IMAGE CONTAINER
        ==================================================== */

        .fc-image-box {

            border-radius: 22px;

            overflow: hidden;

            box-shadow:
            0 15px 35px
            rgba(0,0,0,0.15);

        }


        /* ====================================================
           BACK BUTTON AREA
        ==================================================== */

        .fc-back-area {

            margin-top: 50px;

            padding-top: 25px;

            border-top:
            1px solid
            rgba(100,116,139,0.20);

        }


        /* ====================================================
           FOOTER
        ==================================================== */

        .fc-footer {

            margin-top: 60px;

            padding: 45px;

            border-radius: 32px;

            color: white;

            text-align: center;

            background:
            linear-gradient(
                135deg,
                #020617,
                #1E1B4B,
                #4C1D95
            );

            box-shadow:
            0 20px 50px
            rgba(15,23,42,0.20);

        }


        /* ====================================================
           MOBILE RESPONSIVE
        ==================================================== */

        @media (
            max-width: 768px
        ) {

            .fc-hero {

                padding: 30px;

            }

            .fc-hero-title {

                font-size: 32px;

            }

            .fc-section {

                padding: 22px;

            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 3. MAIN HERO FUNCTION
# ============================================================

def show_hero(
    title,
    subtitle,
    icon="🏠"
):

    st.markdown(
        f"""
        <div class="fc-hero">

            <div class="fc-hero-title">

                {icon} {title}

            </div>

            <div class="fc-hero-subtitle">

                {subtitle}

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 4. SECTION HEADER
# ============================================================

def show_section(
    title,
    description="",
    icon="🚀"
):

    st.markdown(
        f"""
        <div class="fc-section">

            <h2>
                {icon} {title}
            </h2>

            <p>
                {description}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 5. GLOBAL SIDEBAR NAVIGATION
# ============================================================

def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div
            style="
            text-align:center;
            padding:20px;
            "
            >

            <h1>
            🏠 FirstChoice
            </h1>

            <h3>
            Infra Property Hub
            </h3>

            <p>
            India's Next-Generation
            Real Estate Ecosystem
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown(
            "### 🧭 Platform Navigation"
        )

        st.page_link(
            "app.py",
            label="🏠 Home",
            use_container_width=True
        )

        st.page_link(
            "pages/01_Login_Register.py",
            label="🔐 Login & Registration",
            use_container_width=True
        )

        st.page_link(
            "pages/02_Property_Search.py",
            label="🔎 Property Search",
            use_container_width=True
        )

        st.page_link(
            "pages/03_Post_Property.py",
            label="🏠 Post Property",
            use_container_width=True
        )

        st.page_link(
            "pages/04_Projects.py",
            label="🏗️ Projects & Developments",
            use_container_width=True
        )

        st.page_link(
            "pages/05_Map_Location.py",
            label="🗺️ Maps & Location",
            use_container_width=True
        )

        st.page_link(
            "pages/06_Calculators.py",
            label="🧮 Property Calculator",
            use_container_width=True
        )

        st.page_link(
            "pages/07_Professionals.py",
            label="🏢 Agents & Professionals",
            use_container_width=True
        )

        st.page_link(
            "pages/08_Home_Services.py",
            label="🛠️ Home Services",
            use_container_width=True
        )

        st.page_link(
            "pages/09_Premium_Ads.py",
            label="💰 Premium & Advertisements",
            use_container_width=True
        )

        st.page_link(
            "pages/10_My_Dashboard.py",
            label="📊 My Dashboard",
            use_container_width=True
        )

        st.page_link(
            "pages/11_Boss_Control.py",
            label="👑 Boss Control Center",
            use_container_width=True
        )

        st.page_link(
            "pages/12_Manager_Control.py",
            label="👨‍💼 Manager Control Center",
            use_container_width=True
        )

        st.page_link(
            "pages/13_Admin_Technical.py",
            label="🛡️ Admin Technical Center",
            use_container_width=True
        )

        st.page_link(
            "pages/14_Notifications.py",
            label="🔔 Notifications & Messages",
            use_container_width=True
        )

        st.page_link(
            "pages/15_Saved_Compare.py",
            label="❤️ Saved & Compare",
            use_container_width=True
        )

        st.page_link(
            "pages/16_Feedback_Support.py",
            label="💬 Feedback & Support",
            use_container_width=True
        )

        st.markdown("---")

        st.caption(
            "© FirstChoice Infra Property Hub"
        )


# ============================================================
# 6. BACK TO HOME BUTTON
# ============================================================

def back_to_home():

    st.markdown(
        '<div class="fc-back-area">',
        unsafe_allow_html=True
    )

    if st.button(
        "⬅️ Back to Main Navigation",
        use_container_width=True
    ):

        st.switch_page(
            "app.py"
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# 7. FOOTER
# ============================================================

def show_footer():

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 8. DATE & TIME UTILITY
# ============================================================

def current_datetime():

    return datetime.now().strftime(
        "%d %B %Y, %I:%M %p"
    )


# ============================================================
# 9. SESSION USER UTILITY
# ============================================================

def get_current_user():

    return st.session_state.get(
        "current_user",
        None
    )


# ============================================================
# 10. USER ROLE UTILITY
# ============================================================

def get_user_role():

    return st.session_state.get(
        "user_role",
        "guest"
    )


# ============================================================
# 11. LOGIN CHECK
# ============================================================

def is_logged_in():

    return bool(
        st.session_state.get(
            "logged_in",
            False
        )
    )


# ============================================================
# 12. REQUIRE LOGIN
# ============================================================

def require_login():

    if not is_logged_in():

        st.warning(
            "🔐 Please login or register to continue."
        )

        if st.button(
            "Go to Login",
            use_container_width=True
        ):

            st.switch_page(
                "pages/01_Login_Register.py"
            )

        st.stop()


# ============================================================
# 13. ROLE CHECK
# ============================================================

def require_role(
    allowed_roles
):

    role = get_user_role()

    if role not in allowed_roles:

        st.error(
            "🚫 You do not have permission to access this page."
        )

        st.stop()


# ============================================================
# 14. PROPERTY LOCATION OPTIONS
# ============================================================

COUNTRIES = [
    "India",
    "Other"
]


INDIAN_STATES = [

    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Delhi",
    "Jammu & Kashmir",
    "Ladakh",
    "Other"

]


# ============================================================
# 15. COMMON PROPERTY TYPES
# ============================================================

PROPERTY_TYPES = [

    "Apartment",
    "Flat",
    "Villa",
    "Independent House",
    "Farm House",
    "Plot",
    "Land",
    "Farm Land",
    "Office",
    "Shop",
    "Showroom",
    "Warehouse",
    "Industrial Property",
    "Commercial Building",
    "Other"

]


# ============================================================
# 16. COMMON TRANSACTION TYPES
# ============================================================

TRANSACTION_TYPES = [

    "Buy",
    "Sell",
    "Rent",
    "Lease",
    "Investment"

]


# ============================================================
# END OF CORE.PY
# ============================================================
