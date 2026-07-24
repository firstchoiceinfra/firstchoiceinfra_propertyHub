import re
import secrets
import hashlib
from datetime import datetime, timedelta

import streamlit as st

from core.database import (
    get_connection,
    create_user,
    get_user_by_email,
    get_user_by_mobile,
    has_accepted_terms,
    accept_terms,
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# AUTHENTICATION & ACCESS CONTROL SYSTEM
# ============================================================

OTP_EXPIRY_MINUTES = 5

MAX_OTP_ATTEMPTS = 5


# ============================================================
# EMAIL VALIDATION
# ============================================================

def validate_email(email):

    if not email:

        return False

    pattern = (
        r"^[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    return bool(
        re.match(
            pattern,
            email.strip()
        )
    )


# ============================================================
# MOBILE VALIDATION
# ============================================================

def validate_mobile(mobile):

    if not mobile:

        return False

    mobile = str(mobile).strip()

    pattern = r"^[6-9][0-9]{9}$"

    return bool(
        re.match(
            pattern,
            mobile
        )
    )


# ============================================================
# NORMALIZE EMAIL
# ============================================================

def normalize_email(email):

    if not email:

        return ""

    return email.strip().lower()


# ============================================================
# NORMALIZE MOBILE
# ============================================================

def normalize_mobile(mobile):

    if not mobile:

        return ""

    mobile = str(mobile)

    mobile = re.sub(
        r"\D",
        "",
        mobile
    )

    if mobile.startswith("91") and len(mobile) == 12:

        mobile = mobile[2:]

    return mobile


# ============================================================
# SECURE HASH
# ============================================================

def hash_value(value):

    if not value:

        return ""

    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()


# ============================================================
# GENERATE OTP
# ============================================================

def generate_otp():

    return str(
        secrets.randbelow(900000) + 100000
    )


# ============================================================
# CREATE OTP SESSION
# ============================================================

def create_otp_session():

    if "otp_data" not in st.session_state:

        st.session_state.otp_data = {

            "email_otp": None,

            "mobile_otp": None,

            "email": None,

            "mobile": None,

            "created_at": None,

            "email_verified": False,

            "mobile_verified": False,

            "attempts": 0

        }


# ============================================================
# SEND EMAIL OTP
# ============================================================

def send_email_otp(email):

    create_otp_session()

    otp = generate_otp()

    st.session_state.otp_data["email_otp"] = hash_value(
        otp
    )

    st.session_state.otp_data["email"] = normalize_email(
        email
    )

    st.session_state.otp_data["created_at"] = datetime.utcnow()

    st.session_state.otp_data["email_verified"] = False

    st.session_state.otp_data["attempts"] = 0

    # --------------------------------------------------------
    # DEVELOPMENT MODE
    # --------------------------------------------------------
    # In production this OTP must be sent through
    # a secure email provider such as SMTP,
    # SendGrid, Amazon SES, Resend or similar service.
    #
    # The OTP is NOT displayed to the user in production.
    # --------------------------------------------------------

    return otp


# ============================================================
# SEND MOBILE OTP
# ============================================================

def send_mobile_otp(mobile):

    create_otp_session()

    otp = generate_otp()

    st.session_state.otp_data["mobile_otp"] = hash_value(
        otp
    )

    st.session_state.otp_data["mobile"] = normalize_mobile(
        mobile
    )

    st.session_state.otp_data["created_at"] = datetime.utcnow()

    st.session_state.otp_data["mobile_verified"] = False

    st.session_state.otp_data["attempts"] = 0

    # --------------------------------------------------------
    # DEVELOPMENT MODE
    # --------------------------------------------------------
    # In production this OTP must be sent through
    # a secure SMS provider.
    #
    # Example:
    # Twilio
    # MSG91
    # AWS SNS
    # Fast2SMS
    # --------------------------------------------------------

    return otp


# ============================================================
# CHECK OTP EXPIRY
# ============================================================

def is_otp_expired():

    create_otp_session()

    created_at = (
        st.session_state
        .otp_data
        .get("created_at")
    )

    if not created_at:

        return True

    expiry_time = (
        created_at
        +
        timedelta(
            minutes=OTP_EXPIRY_MINUTES
        )
    )

    return datetime.utcnow() > expiry_time


# ============================================================
# VERIFY EMAIL OTP
# ============================================================

def verify_email_otp(user_otp):

    create_otp_session()

    if is_otp_expired():

        return False, "Email OTP has expired."

    if (
        st.session_state
        .otp_data
        .get("attempts", 0)
        >= MAX_OTP_ATTEMPTS
    ):

        return False, (
            "Maximum OTP attempts exceeded."
        )

    st.session_state.otp_data["attempts"] += 1

    stored_hash = (
        st.session_state
        .otp_data
        .get("email_otp")
    )

    if (
        stored_hash
        and
        hash_value(
            str(user_otp).strip()
        )
        == stored_hash
    ):

        st.session_state.otp_data[
            "email_verified"
        ] = True

        return True, (
            "Email verified successfully."
        )

    return False, (
        "Invalid email OTP."
    )


# ============================================================
# VERIFY MOBILE OTP
# ============================================================

def verify_mobile_otp(user_otp):

    create_otp_session()

    if is_otp_expired():

        return False, "Mobile OTP has expired."

    if (
        st.session_state
        .otp_data
        .get("attempts", 0)
        >= MAX_OTP_ATTEMPTS
    ):

        return False, (
            "Maximum OTP attempts exceeded."
        )

    st.session_state.otp_data["attempts"] += 1

    stored_hash = (
        st.session_state
        .otp_data
        .get("mobile_otp")
    )

    if (
        stored_hash
        and
        hash_value(
            str(user_otp).strip()
        )
        == stored_hash
    ):

        st.session_state.otp_data[
            "mobile_verified"
        ] = True

        return True, (
            "Mobile number verified successfully."
        )

    return False, (
        "Invalid mobile OTP."
    )


# ============================================================
# CHECK BOTH OTP VERIFICATIONS
# ============================================================

def both_otp_verified():

    create_otp_session()

    return (

        st.session_state
        .otp_data
        .get("email_verified", False)

        and

        st.session_state
        .otp_data
        .get("mobile_verified", False)

    )


# ============================================================
# CLEAR OTP SESSION
# ============================================================

def clear_otp_session():

    if "otp_data" in st.session_state:

        del st.session_state["otp_data"]


# ============================================================
# REGISTER NEW USER
# ============================================================

def register_user(

    full_name,

    email,

    mobile

):

    email = normalize_email(
        email
    )

    mobile = normalize_mobile(
        mobile
    )


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not full_name.strip():

        return None, (
            "Full name is required."
        )


    if not validate_email(email):

        return None, (
            "Please enter a valid email address."
        )


    if not validate_mobile(mobile):

        return None, (
            "Please enter a valid 10-digit mobile number."
        )


    # --------------------------------------------------------
    # CHECK EXISTING EMAIL
    # --------------------------------------------------------

    existing_email = (
        get_user_by_email(
            email
        )
    )


    if existing_email:

        return None, (
            "An account with this email already exists."
        )


    # --------------------------------------------------------
    # CHECK EXISTING MOBILE
    # --------------------------------------------------------

    existing_mobile = (
        get_user_by_mobile(
            mobile
        )
    )


    if existing_mobile:

        return None, (
            "An account with this mobile number already exists."
        )


    # --------------------------------------------------------
    # BOTH OTP VERIFICATION REQUIRED
    # --------------------------------------------------------

    if not both_otp_verified():

        return None, (
            "Both email and mobile number must be verified."
        )


    # --------------------------------------------------------
    # CREATE USER
    # --------------------------------------------------------

    user_id = create_user(

        full_name=full_name.strip(),

        email=email,

        mobile=mobile,

        role="user"

    )


    if not user_id:

        return None, (
            "Unable to create the account."
        )


    # --------------------------------------------------------
    # SESSION
    # --------------------------------------------------------

    st.session_state[
        "logged_in"
    ] = True


    st.session_state[
        "user_id"
    ] = user_id


    st.session_state[
        "user_role"
    ] = "user"


    st.session_state[
        "user_email"
    ] = email


    st.session_state[
        "user_mobile"
    ] = mobile


    st.session_state[
        "user_name"
    ] = full_name.strip()


    # --------------------------------------------------------
    # TERMS MUST BE ACCEPTED BEFORE CONTINUING
    # --------------------------------------------------------

    st.session_state[
        "terms_required"
    ] = True


    clear_otp_session()


    return user_id, (
        "Account created successfully."
    )


# ============================================================
# LOGIN USER
# ============================================================

def login_user(

    email,

    mobile

):

    email = normalize_email(
        email
    )

    mobile = normalize_mobile(
        mobile
    )


    if not validate_email(email):

        return False, (
            "Please enter a valid email address."
        )


    if not validate_mobile(mobile):

        return False, (
            "Please enter a valid mobile number."
        )


    user = get_user_by_email(
        email
    )


    if not user:

        return False, (
            "No account was found with these credentials."
        )


    if user["mobile"] != mobile:

        return False, (
            "Email and mobile number do not match."
        )


    if not user["is_active"]:

        return False, (
            "This account is currently inactive."
        )


    # --------------------------------------------------------
    # SESSION
    # --------------------------------------------------------

    st.session_state[
        "logged_in"
    ] = True


    st.session_state[
        "user_id"
    ] = user["id"]


    st.session_state[
        "user_role"
    ] = user["role"]


    st.session_state[
        "user_name"
    ] = user["full_name"]


    st.session_state[
        "user_email"
    ] = user["email"]


    st.session_state[
        "user_mobile"
    ] = user["mobile"]


    # --------------------------------------------------------
    # TERMS CHECK
    # --------------------------------------------------------

    if not has_accepted_terms(
        user["id"]
    ):

        st.session_state[
            "terms_required"
        ] = True

    else:

        st.session_state[
            "terms_required"
        ] = False


    return True, (
        "Login successful."
    )


# ============================================================
# ACCEPT TERMS FOR CURRENT USER
# ============================================================

def accept_current_user_terms():

    user_id = (
        st.session_state
        .get("user_id")
    )


    if not user_id:

        return False


    accept_terms(
        user_id
    )


    st.session_state[
        "terms_required"
    ] = False


    return True


# ============================================================
# CHECK LOGIN STATUS
# ============================================================

def is_logged_in():

    return bool(
        st.session_state.get(
            "logged_in",
            False
        )
    )


# ============================================================
# GET CURRENT ROLE
# ============================================================

def get_current_role():

    return st.session_state.get(
        "user_role",
        None
    )


# ============================================================
# ROLE ACCESS CONTROL
# ============================================================

def has_role(

    allowed_roles

):

    current_role = get_current_role()


    if not current_role:

        return False


    return current_role in allowed_roles


# ============================================================
# BOSS ACCESS
# ============================================================

def is_boss():

    return has_role(
        [
            "boss"
        ]
    )


# ============================================================
# MANAGER ACCESS
# ============================================================

def is_manager():

    return has_role(
        [
            "boss",
            "manager"
        ]
    )


# ============================================================
# ADMIN TEAM ACCESS
# ============================================================

def is_admin():

    return has_role(
        [
            "boss",
            "admin"
        ]
    )


# ============================================================
# FULL SYSTEM ACCESS
# ============================================================

def has_full_access():

    return has_role(
        [
            "boss",
            "manager",
            "admin"
        ]
    )


# ============================================================
# LOGOUT
# ============================================================

def logout_user():

    protected_keys = [

        "logged_in",

        "user_id",

        "user_role",

        "user_name",

        "user_email",

        "user_mobile",

        "terms_required",

        "otp_data"

    ]


    for key in protected_keys:

        if key in st.session_state:

            del st.session_state[key]


# ============================================================
# REQUIRE LOGIN
# ============================================================

def require_login():

    if not is_logged_in():

        st.warning(
            "Please log in to continue."
        )

        st.stop()


# ============================================================
# REQUIRE TERMS ACCEPTANCE
# ============================================================

def require_terms_acceptance():

    if not is_logged_in():

        return


    if st.session_state.get(

        "terms_required",

        False

    ):

        st.warning(
            "Please review and accept the Terms & Conditions before continuing."
        )

        st.stop()
