import streamlit as st
import sqlite3
import os

from core.Ui import (
    load_premium_ui,
    hero,
    section,
    footer
)

from core.database import (
    get_connection
)


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 04 — ADMIN PANEL
# ============================================================


st.set_page_config(
    page_title="Admin Panel | FirstChoice Property Hub",
    page_icon="🛡️",
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

        <h1>🛡️ FirstChoice</h1>

        <h3>Admin Control Center</h3>

        <hr>

        <p>
        Secure Property Management
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
        "pages/05_Admin_Panel.py",
        label="🛡️ Admin Panel"
    )


# ============================================================
# ADMIN SECURITY CHECK
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
        "🔐 Secure Admin Access",
        "Please login with an authorized administrator account."
    )

    st.error(
        "You are not logged in."
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
# ROLE CHECK
# ============================================================

if user_role != "admin":

    hero(
        "🚫 Access Restricted",
        "This area is reserved for authorized FirstChoice Property Hub administrators."
    )

    st.error(
        "You do not have permission to access the Admin Panel."
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
# ADMIN HERO
# ============================================================

hero(
    "🛡️ Admin Control Center",
    "Manage property listings, verify submissions and maintain the FirstChoice Infra Property Hub ecosystem."
)


# ============================================================
# GET DATABASE STATISTICS
# ============================================================

connection = get_connection()

cursor = connection.cursor()


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
    WHERE property_status = 'pending'
    """
)

pending_properties = cursor.fetchone()[0]


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
    WHERE property_status = 'rejected'
    """
)

rejected_properties = cursor.fetchone()[0]


cursor.execute(
    """
    SELECT COALESCE(SUM(views), 0)
    FROM properties
    """
)

total_views = cursor.fetchone()[0]


connection.close()


# ============================================================
# DASHBOARD STATISTICS
# ============================================================

section(
    "📊 Property Management Overview",
    "Monitor the current property listing status across the platform."
)


c1, c2, c3, c4, c5 = st.columns(5)


with c1:

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


with c2:

    st.markdown(
        f"""
        <div class="fc-warning">

        <div class="fc-stat-number">
        {pending_properties}
        </div>

        <div class="fc-stat-label">
        Pending Review
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
        {approved_properties}
        </div>

        <div class="fc-stat-label">
        Approved
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c4:

    st.markdown(
        f"""
        <div class="fc-danger">

        <div class="fc-stat-number">
        {rejected_properties}
        </div>

        <div class="fc-stat-label">
        Rejected
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c5:

    st.markdown(
        f"""
        <div class="fc-stat">

        <div class="fc-stat-number">
        {total_views}
        </div>

        <div class="fc-stat-label">
        Total Views
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PROPERTY MANAGEMENT
# ============================================================

section(
    "🏡 Property Verification Center",
    "Review property listings submitted by users before they become publicly visible."
)


# ============================================================
# FILTER
# ============================================================

filter_status = st.selectbox(

    "🔎 Filter Properties",

    [

        "All",

        "Pending",

        "Approved",

        "Rejected"

    ]

)


# ============================================================
# GET PROPERTIES
# ============================================================

connection = get_connection()

cursor = connection.cursor()


query = """

SELECT *

FROM properties

"""


parameters = []


if filter_status == "Pending":

    query += """

    WHERE property_status = 'pending'

    """


elif filter_status == "Approved":

    query += """

    WHERE property_status = 'approved'

    """


elif filter_status == "Rejected":

    query += """

    WHERE property_status = 'rejected'

    """


query += """

ORDER BY created_at DESC

"""


cursor.execute(

    query,

    parameters

)


properties = cursor.fetchall()


connection.close()


# ============================================================
# NO DATA
# ============================================================

if not properties:

    st.info(
        "No properties found for the selected filter."
    )


# ============================================================
# PROPERTY LIST
# ============================================================

for property_data in properties:

    property_id = property_data["id"]

    status = property_data["property_status"]


    with st.expander(

        f"🏡 Property #{property_id} — "
        f"{property_data['property_type']} — "
        f"{property_data['city']} — "
        f"{status.upper()}"

    ):

        col1, col2 = st.columns(2)


        # ====================================================
        # PROPERTY INFORMATION
        # ====================================================

        with col1:

            st.markdown(
                "### 🏠 Property Information"
            )

            st.write(
                f"**Property ID:** {property_id}"
            )

            st.write(
                f"**Purpose:** {property_data['purpose']}"
            )

            st.write(
                f"**Category:** {property_data['category']}"
            )

            st.write(
                f"**Property Type:** {property_data['property_type']}"
            )

            st.write(
                f"**Price:** ₹{property_data['price']:,.0f}"
                if property_data["price"]
                else "**Price:** Not specified"
            )

            st.write(
                f"**Area:** {property_data['property_area']} Sq.Ft."
            )

            st.write(
                f"**BHK:** {property_data['bhk']}"
            )

            st.write(
                f"**Project Status:** {property_data['project_status']}"
            )


        # ====================================================
        # LOCATION
        # ====================================================

        with col2:

            st.markdown(
                "### 📍 Location"
            )

            st.write(
                f"**Country:** {property_data['country']}"
            )

            st.write(
                f"**State:** {property_data['state']}"
            )

            st.write(
                f"**City:** {property_data['city']}"
            )

            st.write(
                f"**Village / Town:** {property_data['village_town']}"
            )

            st.write(
                f"**Area:** {property_data['area_name']}"
            )

            st.write(
                f"**Google Maps:** "
                f"{property_data['google_location']}"
            )


        # ====================================================
        # DESCRIPTION
        # ====================================================

        st.markdown(
            "### 📝 Description"
        )

        st.write(
            property_data["description"]
            or
            "No description provided."
        )


        # ====================================================
        # CONTACT
        # ====================================================

        st.markdown(
            "### 📞 Contact"
        )

        st.write(
            f"**Name:** {property_data['contact_name']}"
        )

        st.write(
            f"**Mobile:** {property_data['contact_mobile']}"
        )


        # ====================================================
        # MEDIA
        # ====================================================

        st.markdown(
            "### 📸 Property Media"
        )


        connection = get_connection()

        cursor = connection.cursor()


        cursor.execute(

            """
            SELECT *

            FROM property_media

            WHERE property_id = ?

            ORDER BY created_at ASC

            """,

            (property_id,)

        )


        media_files = cursor.fetchall()


        connection.close()


        if media_files:

            image_files = [

                media

                for media in media_files

                if media["media_type"] == "image"

            ]


            video_files = [

                media

                for media in media_files

                if media["media_type"] == "video"

            ]


            if image_files:

                st.markdown(
                    "#### 🖼️ Photos"
                )


                image_columns = st.columns(

                    min(
                        len(image_files),
                        4
                    )

                )


                for index, media in enumerate(
                    image_files
                ):

                    file_path = media["file_path"]


                    if os.path.exists(
                        file_path
                    ):

                        with image_columns[
                            index % len(image_columns)
                        ]:

                            st.image(

                                file_path,

                                use_container_width=True

                            )


            if video_files:

                st.markdown(
                    "#### 🎥 Video"
                )


                for media in video_files:

                    file_path = media["file_path"]


                    if os.path.exists(
                        file_path
                    ):

                        st.video(
                            file_path
                        )


        else:

            st.info(
                "No media uploaded."
            )


        # ====================================================
        # ACTION BUTTONS
        # ====================================================

        st.markdown(
            "### ⚙️ Property Action"
        )


        if status == "pending":

            approve_col, reject_col = st.columns(2)


            with approve_col:

                if st.button(

                    "✅ Approve Property",

                    key=f"approve_{property_id}",

                    use_container_width=True

                ):

                    connection = get_connection()

                    cursor = connection.cursor()


                    cursor.execute(

                        """
                        UPDATE properties

                        SET property_status = 'approved',

                            is_verified = 1,

                            updated_at = datetime('now')

                        WHERE id = ?

                        """,

                        (property_id,)

                    )


                    connection.commit()

                    connection.close()


                    st.success(

                        f"Property #{property_id} approved successfully."

                    )


                    st.rerun()


            with reject_col:

                if st.button(

                    "❌ Reject Property",

                    key=f"reject_{property_id}",

                    use_container_width=True

                ):

                    connection = get_connection()

                    cursor = connection.cursor()


                    cursor.execute(

                        """
                        UPDATE properties

                        SET property_status = 'rejected',

                            is_verified = 0,

                            updated_at = datetime('now')

                        WHERE id = ?

                        """,

                        (property_id,)

                    )


                    connection.commit()

                    connection.close()


                    st.error(

                        f"Property #{property_id} rejected."

                    )


                    st.rerun()


        elif status == "approved":

            st.success(
                "✅ This property is publicly approved."
            )


        elif status == "rejected":

            st.error(
                "❌ This property has been rejected."
            )


# ============================================================
# SECURITY INFORMATION
# ============================================================

section(
    "🔐 Security Notice",
    "Administrative actions should only be performed by authorized FirstChoice Property Hub administrators."
)


st.warning(

    "Never share your administrator credentials. All future administrative actions will be recorded in the platform audit system."

)


# ============================================================
# FOOTER
# ============================================================

footer()
