import sqlite3
import os
from datetime import datetime


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# CORE DATABASE SYSTEM
# ============================================================


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)


DATABASE_PATH = os.path.join(
    DATA_DIR,
    "firstchoice_property_hub.db"
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    connection = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def init_db():

    connection = get_connection()

    cursor = connection.cursor()


    # ========================================================
    # USERS TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            business_name TEXT,

            account_type TEXT NOT NULL,

            mobile_number TEXT UNIQUE NOT NULL,

            email TEXT UNIQUE NOT NULL,

            mobile_verified INTEGER DEFAULT 0,

            email_verified INTEGER DEFAULT 0,

            terms_accepted INTEGER DEFAULT 0,

            role TEXT DEFAULT 'user',

            account_status TEXT DEFAULT 'active',

            created_at TEXT NOT NULL

        )
        """
    )


    # ========================================================
    # CUSTOM AREAS TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS custom_areas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            country TEXT NOT NULL,

            state TEXT NOT NULL,

            city TEXT NOT NULL,

            village_town TEXT NOT NULL,

            area_name TEXT NOT NULL,

            created_by INTEGER,

            created_at TEXT NOT NULL,

            UNIQUE (
                country,
                state,
                city,
                village_town,
                area_name
            ),

            FOREIGN KEY (
                created_by
            )
            REFERENCES users(id)

        )
        """
    )


    # ========================================================
    # PROPERTIES TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS properties (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            owner_id INTEGER,

            purpose TEXT NOT NULL,

            category TEXT NOT NULL,

            property_type TEXT NOT NULL,

            country TEXT NOT NULL,

            state TEXT NOT NULL,

            city TEXT NOT NULL,

            village_town TEXT NOT NULL,

            area_name TEXT NOT NULL,

            property_area REAL,

            price REAL,

            bhk TEXT,

            project_status TEXT,

            possession TEXT,

            google_location TEXT,

            description TEXT,

            contact_name TEXT,

            contact_mobile TEXT,

            property_status TEXT DEFAULT 'pending',

            is_verified INTEGER DEFAULT 0,

            is_premium INTEGER DEFAULT 0,

            views INTEGER DEFAULT 0,

            created_at TEXT NOT NULL,

            updated_at TEXT,

            FOREIGN KEY (
                owner_id
            )
            REFERENCES users(id)

        )
        """
    )


    # ========================================================
    # PROPERTY MEDIA TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS property_media (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            property_id INTEGER NOT NULL,

            media_type TEXT NOT NULL,

            file_path TEXT NOT NULL,

            created_at TEXT NOT NULL,

            FOREIGN KEY (
                property_id
            )
            REFERENCES properties(id)

        )
        """
    )


    # ========================================================
    # PROPERTY VIEWS TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS property_views (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            property_id INTEGER NOT NULL,

            viewer_id INTEGER,

            viewed_at TEXT NOT NULL,

            FOREIGN KEY (
                property_id
            )
            REFERENCES properties(id),

            FOREIGN KEY (
                viewer_id
            )
            REFERENCES users(id)

        )
        """
    )


    # ========================================================
    # FEEDBACK TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            name TEXT,

            email TEXT,

            category TEXT,

            message TEXT NOT NULL,

            status TEXT DEFAULT 'new',

            created_at TEXT NOT NULL,

            FOREIGN KEY (
                user_id
            )
            REFERENCES users(id)

        )
        """
    )


    # ========================================================
    # SAVE DATABASE
    # ========================================================

    connection.commit()

    connection.close()


# ============================================================
# CREATE USER
# ============================================================

def create_user(

    full_name,

    business_name,

    account_type,

    mobile_number,

    email,

    mobile_verified=1,

    email_verified=1,

    terms_accepted=1,

    role="user"

):

    connection = get_connection()

    cursor = connection.cursor()


    created_at = datetime.now().isoformat()


    try:

        cursor.execute(
            """
            INSERT INTO users (

                full_name,

                business_name,

                account_type,

                mobile_number,

                email,

                mobile_verified,

                email_verified,

                terms_accepted,

                role,

                created_at

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,

            (

                full_name,

                business_name,

                account_type,

                mobile_number,

                email,

                mobile_verified,

                email_verified,

                terms_accepted,

                role,

                created_at

            )

        )


        connection.commit()


        user_id = cursor.lastrowid


        connection.close()


        return user_id


    except sqlite3.IntegrityError:

        connection.close()

        return None


# ============================================================
# GET USER BY MOBILE
# ============================================================

def get_user_by_mobile(

    mobile_number

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """
        SELECT *

        FROM users

        WHERE mobile_number = ?

        LIMIT 1
        """,

        (
            mobile_number,
        )

    )


    user = cursor.fetchone()


    connection.close()


    return user


# ============================================================
# GET USER BY EMAIL
# ============================================================

def get_user_by_email(

    email

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """
        SELECT *

        FROM users

        WHERE email = ?

        LIMIT 1
        """,

        (
            email,
        )

    )


    user = cursor.fetchone()


    connection.close()


    return user


# ============================================================
# SAVE CUSTOM AREA
# ============================================================

def save_custom_area(

    country,

    state,

    city,

    village_town,

    area_name,

    created_by=None

):

    connection = get_connection()

    cursor = connection.cursor()


    created_at = datetime.now().isoformat()


    try:

        cursor.execute(

            """
            INSERT OR IGNORE INTO custom_areas (

                country,

                state,

                city,

                village_town,

                area_name,

                created_by,

                created_at

            )

            VALUES (?, ?, ?, ?, ?, ?, ?)

            """,

            (

                country,

                state,

                city,

                village_town,

                area_name,

                created_by,

                created_at

            )

        )


        connection.commit()


        connection.close()


        return True


    except Exception:

        connection.close()

        return False


# ============================================================
# GET CUSTOM AREAS
# ============================================================

def get_custom_areas(

    country,

    state,

    city,

    village_town

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """
        SELECT area_name

        FROM custom_areas

        WHERE country = ?

        AND state = ?

        AND city = ?

        AND village_town = ?

        ORDER BY area_name ASC

        """,

        (

            country,

            state,

            city,

            village_town

        )

    )


    rows = cursor.fetchall()


    connection.close()


    return [

        row["area_name"]

        for row in rows

    ]


# ============================================================
# CREATE PROPERTY
# ============================================================

def create_property(

    owner_id,

    purpose,

    category,

    property_type,

    country,

    state,

    city,

    village_town,

    area_name,

    property_area,

    price,

    bhk,

    project_status,

    possession,

    google_location,

    description,

    contact_name,

    contact_mobile

):

    connection = get_connection()

    cursor = connection.cursor()


    created_at = datetime.now().isoformat()


    cursor.execute(

        """
        INSERT INTO properties (

            owner_id,

            purpose,

            category,

            property_type,

            country,

            state,

            city,

            village_town,

            area_name,

            property_area,

            price,

            bhk,

            project_status,

            possession,

            google_location,

            description,

            contact_name,

            contact_mobile,

            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            owner_id,

            purpose,

            category,

            property_type,

            country,

            state,

            city,

            village_town,

            area_name,

            property_area,

            price,

            bhk,

            project_status,

            possession,

            google_location,

            description,

            contact_name,

            contact_mobile,

            created_at

        )

    )


    connection.commit()


    property_id = cursor.lastrowid


    connection.close()


    return property_id


# ============================================================
# SAVE PROPERTY MEDIA
# ============================================================

def save_property_media(

    property_id,

    media_type,

    file_path

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """
        INSERT INTO property_media (

            property_id,

            media_type,

            file_path,

            created_at

        )

        VALUES (?, ?, ?, ?)

        """,

        (

            property_id,

            media_type,

            file_path,

            datetime.now().isoformat()

        )

    )


    connection.commit()


    connection.close()


# ============================================================
# GET PROPERTIES
# ============================================================

def get_properties(

    city=None,

    area_name=None,

    property_type=None,

    purpose=None

):

    connection = get_connection()

    cursor = connection.cursor()


    query = """

    SELECT *

    FROM properties

    WHERE property_status = 'approved'

    """

    parameters = []


    if city:

        query += """

        AND city = ?

        """

        parameters.append(
            city
        )


    if area_name:

        query += """

        AND area_name = ?

        """

        parameters.append(
            area_name
        )


    if property_type:

        query += """

        AND property_type = ?

        """

        parameters.append(
            property_type
        )


    if purpose:

        query += """

        AND purpose = ?

        """

        parameters.append(
            purpose
        )


    query += """

    ORDER BY created_at DESC

    """


    cursor.execute(

        query,

        parameters

    )


    properties = cursor.fetchall()


    connection.close()


    return properties


# ============================================================
# ADD PROPERTY VIEW
# ============================================================

def add_property_view(

    property_id,

    viewer_id=None

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """
        INSERT INTO property_views (

            property_id,

            viewer_id,

            viewed_at

        )

        VALUES (?, ?, ?)

        """,

        (

            property_id,

            viewer_id,

            datetime.now().isoformat()

        )

    )


    cursor.execute(

        """
        UPDATE properties

        SET views = views + 1

        WHERE id = ?

        """,

        (

            property_id,

        )

    )


    connection.commit()


    connection.close()


# ============================================================
# SAVE FEEDBACK
# ============================================================

def save_feedback(

    name,

    email,

    category,

    message,

    user_id=None

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """
        INSERT INTO feedback (

            user_id,

            name,

            email,

            category,

            message,

            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (

            user_id,

            name,

            email,

            category,

            message,

            datetime.now().isoformat()

        )

    )


    connection.commit()


    connection.close()


# ============================================================
# INITIALIZE DATABASE AUTOMATICALLY
# ============================================================

init_db()
