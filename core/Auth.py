import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# CORE AUTHENTICATION & ROLE SYSTEM
# ============================================================


# ============================================================
# ROLE DEFINITIONS
# ============================================================

ROLE_BOSS = "boss"

ROLE_MANAGER = "manager"

ROLE_ADMIN = "admin"

ROLE_USER = "user"


# ============================================================
# INITIALIZE AUTH SESSION
# ============================================================

def init_auth():

    if "logged_in" not in st.session_state:

        st.session_state.logged_in = False


    if "current_user" not in st.session_state:

        st.session_state.current_user = None


    if "user_role" not in st.session_state:

        st.session_state.user_role = None


    if "user_id" not in st.session_state:

        st.session_state.user_id = None


    if "user_name" not in st.session_state:

        st.session_state.user_name = None


    if "user_email" not in st.session_state:

        st.session_state.user_email = None


    if "user_mobile" not in st.session_state:

        st.session_state.user_mobile = None


# ============================================================
# LOGIN USER
# ============================================================

def login_user(

    user_id,

    user_name,

    user_email,

    user_mobile,

    role=ROLE_USER

):

    st.session_state.logged_in = True

    st.session_state.user_id = user_id

    st.session_state.user_name = user_name

    st.session_state.user_email = user_email

    st.session_state.user_mobile = user_mobile

    st.session_state.user_role = role

    st.session_state.current_user = {

        "id": user_id,

        "name": user_name,

        "email": user_email,

        "mobile": user_mobile,

        "role": role

    }


# ============================================================
# LOGOUT USER
# ============================================================

def logout_user():

    st.session_state.logged_in = False

    st.session_state.current_user = None

    st.session_state.user_id = None

    st.session_state.user_name = None

    st.session_state.user_email = None

    st.session_state.user_mobile = None

    st.session_state.user_role = None


    # Clear temporary OTP

    if "otp" in st.session_state:

        del st.session_state.otp


    if "otp_mobile" in st.session_state:

        del st.session_state.otp_mobile


    if "otp_email" in st.session_state:

        del st.session_state.otp_email


# ============================================================
# CHECK LOGIN
# ============================================================

def is_logged_in():

    init_auth()

    return (

        st.session_state.logged_in

        is True

    )


# ============================================================
# GET CURRENT USER
# ============================================================

def get_current_user():

    init_auth()

    return st.session_state.current_user


# ============================================================
# GET CURRENT USER ROLE
# ============================================================

def get_current_role():

    init_auth()

    return st.session_state.user_role


# ============================================================
# ROLE CHECK
# ============================================================

def has_role(

    required_role

):

    init_auth()

    return (

        st.session_state.user_role

        == required_role

    )


# ============================================================
# BOSS ACCESS
# ============================================================

def is_boss():

    init_auth()

    return (

        st.session_state.user_role

        == ROLE_BOSS

    )


# ============================================================
# MANAGER ACCESS
# ============================================================

def is_manager():

    init_auth()

    return (

        st.session_state.user_role

        == ROLE_MANAGER

    )


# ============================================================
# ADMIN ACCESS
# ============================================================

def is_admin():

    init_auth()

    return (

        st.session_state.user_role

        == ROLE_ADMIN

    )


# ============================================================
# NORMAL USER ACCESS
# ============================================================

def is_user():

    init_auth()

    return (

        st.session_state.user_role

        == ROLE_USER

    )


# ============================================================
# BOSS / MANAGER / ADMIN / USER
# ============================================================

def is_staff():

    init_auth()

    return (

        st.session_state.user_role

        in [

            ROLE_BOSS,

            ROLE_MANAGER,

            ROLE_ADMIN

        ]

    )


# ============================================================
# ACCESS CONTROL
# ============================================================

def require_login():

    """

    Page को login के बिना access करने से रोकता है.

    """

    init_auth()


    if not st.session_state.logged_in:

        st.warning(

            "🔐 Please login to access this page."

        )

        st.stop()


# ============================================================
# REQUIRE BOSS
# ============================================================

def require_boss():

    """

    केवल Boss को access.

    """

    require_login()


    if not is_boss():

        st.error(

            "🚫 Access Denied. Boss authorization required."

        )

        st.stop()


# ============================================================
# REQUIRE MANAGER
# ============================================================

def require_manager():

    """

    Manager और Boss दोनों access कर सकते हैं.

    """

    require_login()


    if st.session_state.user_role not in [

        ROLE_BOSS,

        ROLE_MANAGER

    ]:

        st.error(

            "🚫 Access Denied. Manager authorization required."

        )

        st.stop()


# ============================================================
# REQUIRE ADMIN
# ============================================================

def require_admin():

    """

    Admin और Boss access कर सकते हैं.

    """

    require_login()


    if st.session_state.user_role not in [

        ROLE_BOSS,

        ROLE_ADMIN

    ]:

        st.error(

            "🚫 Access Denied. Admin authorization required."

        )

        st.stop()


# ============================================================
# REQUIRE STAFF
# ============================================================

def require_staff():

    """

    Boss / Manager / Admin access.

    """

    require_login()


    if st.session_state.user_role not in [

        ROLE_BOSS,

        ROLE_MANAGER,

        ROLE_ADMIN

    ]:

        st.error(

            "🚫 Access Denied. Staff authorization required."

        )

        st.stop()


# ============================================================
# ROLE LABEL
# ============================================================

def get_role_label():

    init_auth()


    role = st.session_state.user_role


    role_labels = {

        ROLE_BOSS:
        "👑 Boss",

        ROLE_MANAGER:
        "🧑‍💼 Manager",

        ROLE_ADMIN:
        "🛠️ Admin",

        ROLE_USER:
        "👤 User"

    }


    return role_labels.get(

        role,

        "👤 User"

    )


# ============================================================
# USER HEADER
# ============================================================

def show_user_header():

    init_auth()


    if not is_logged_in():

        return


    col1, col2 = st.columns(

        [4, 1]

    )


    with col1:

        st.markdown(

            f"""
            ### 👋 Welcome,
            {st.session_state.user_name}

            **{get_role_label()}**
            """

        )


    with col2:

        if st.button(

            "🚪 Logout",

            use_container_width=True

        ):

            logout_user()

            st.rerun()


# ============================================================
# INITIALIZE AUTH SYSTEM
# ============================================================

init_auth()
