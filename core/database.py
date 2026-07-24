import sqlite3
from pathlib import Path
from datetime import datetime


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# CENTRAL DATABASE MODULE
# ============================================================

# ------------------------------------------------------------
# DATABASE PATH
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DB_PATH = DATA_DIR / "property_hub.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    connection = sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# DATABASE INITIALIZATION
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

            email TEXT UNIQUE NOT NULL,

            mobile TEXT UNIQUE NOT NULL,

            role TEXT DEFAULT 'user',

            is_active INTEGER DEFAULT 1,

            terms_accepted INTEGER DEFAULT 0,

            terms_accepted_at TEXT,

            created_at TEXT NOT NULL

        )
        """
    )


    # ========================================================
    # LOCATIONS TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS locations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            country TEXT NOT NULL,

            state TEXT NOT NULL,

            city TEXT NOT NULL,

            village_town TEXT NOT NULL,

            area TEXT NOT NULL,

            created_at TEXT NOT NULL,

            UNIQUE (
                country,
                state,
                city,
                village_town,
                area
            )

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

            title TEXT NOT NULL,

            description TEXT,

            purpose TEXT NOT NULL,

            property_type TEXT NOT NULL,

            country TEXT NOT NULL,

            state TEXT NOT NULL,

            city TEXT NOT NULL,

            village_town TEXT NOT NULL,

            area TEXT NOT NULL,

            address TEXT,

            latitude REAL,

            longitude REAL,

            price REAL,

            bedrooms INTEGER,

            bathrooms INTEGER,

            area_sqft REAL,

            status TEXT DEFAULT 'Pending',

            verification_status TEXT DEFAULT 'Pending',

            created_at TEXT NOT NULL,

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

            media_path TEXT NOT NULL,

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

            feedback_type TEXT NOT NULL,

            subject TEXT,

            message TEXT NOT NULL,

            status TEXT DEFAULT 'New',

            created_at TEXT NOT NULL,

            FOREIGN KEY (
                user_id
            )
            REFERENCES users(id)

        )
        """
    )


    # ========================================================
    # AUDIT LOG TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            action TEXT NOT NULL,

            target_type TEXT,

            target_id INTEGER,

            details TEXT,

            created_at TEXT NOT NULL,

            FOREIGN KEY (
                user_id
            )
            REFERENCES users(id)

        )
        """
    )


    connection.commit()

    connection.close()


# ============================================================
# USER FUNCTIONS
# ============================================================

def create_user(
    full_name,
    email,
    mobile,
    role="user"
):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    try:

        cursor.execute(
            """
            INSERT INTO users (

                full_name,
                email,
                mobile,
                role,
                created_at

            )

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                full_name,
                email,
                mobile,
                role,
                now
            )
        )

        connection.commit()

        user_id = cursor.lastrowid

        return user_id


    except sqlite3.IntegrityError:

        return None


    finally:

        connection.close()


# ============================================================
# GET USER BY EMAIL
# ============================================================

def get_user_by_email(email):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM users

        WHERE email = ?

        LIMIT 1
        """,
        (email,)
    )


    user = cursor.fetchone()

    connection.close()


    if user:

        return dict(user)

    return None


# ============================================================
# GET USER BY MOBILE
# ============================================================

def get_user_by_mobile(mobile):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM users

        WHERE mobile = ?

        LIMIT 1
        """,
        (mobile,)
    )


    user = cursor.fetchone()

    connection.close()


    if user:

        return dict(user)

    return None


# ============================================================
# ACCEPT TERMS
# ============================================================

def accept_terms(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    cursor.execute(
        """
        UPDATE users

        SET

            terms_accepted = 1,

            terms_accepted_at = ?

        WHERE id = ?
        """,
        (
            now,
            user_id
        )
    )


    connection.commit()

    connection.close()


# ============================================================
# CHECK TERMS STATUS
# ============================================================

def has_accepted_terms(user_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT terms_accepted

        FROM users

        WHERE id = ?

        LIMIT 1
        """,
        (user_id,)
    )


    result = cursor.fetchone()

    connection.close()


    if result:

        return bool(
            result["terms_accepted"]
        )


    return False


# ============================================================
# SAVE LOCATION
# ============================================================

def save_location(

    country,

    state,

    city,

    village_town,

    area

):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    cursor.execute(
        """
        INSERT OR IGNORE INTO locations (

            country,

            state,

            city,

            village_town,

            area,

            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (

            country,

            state,

            city,

            village_town,

            area,

            now

        )
    )


    connection.commit()

    connection.close()


# ============================================================
# GET SAVED AREAS
# ============================================================

def get_areas(

    country,

    state,

    city,

    village_town

):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT DISTINCT area

        FROM locations

        WHERE country = ?

        AND state = ?

        AND city = ?

        AND village_town = ?

        ORDER BY area ASC
        """,
        (

            country,

            state,

            city,

            village_town

        )
    )


    results = cursor.fetchall()

    connection.close()


    return [

        row["area"]

        for row in results

    ]


# ============================================================
# SAVE PROPERTY
# ============================================================

def create_property(

    owner_id,

    title,

    description,

    purpose,

    property_type,

    country,

    state,

    city,

    village_town,

    area,

    address,

    latitude,

    longitude,

    price,

    bedrooms,

    bathrooms,

    area_sqft

):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    cursor.execute(
        """
        INSERT INTO properties (

            owner_id,

            title,

            description,

            purpose,

            property_type,

            country,

            state,

            city,

            village_town,

            area,

            address,

            latitude,

            longitude,

            price,

            bedrooms,

            bathrooms,

            area_sqft,

            created_at

        )

        VALUES (

            ?, ?, ?, ?, ?,

            ?, ?, ?, ?, ?,

            ?, ?, ?, ?, ?,

            ?, ?, ?

        )
        """,
        (

            owner_id,

            title,

            description,

            purpose,

            property_type,

            country,

            state,

            city,

            village_town,

            area,

            address,

            latitude,

            longitude,

            price,

            bedrooms,

            bathrooms,

            area_sqft,

            now

        )
    )


    connection.commit()

    property_id = cursor.lastrowid

    connection.close()


    # Save location automatically

    save_location(

        country,

        state,

        city,

        village_town,

        area

    )


    return property_id


# ============================================================
# ADD PROPERTY MEDIA
# ============================================================

def add_property_media(

    property_id,

    media_type,

    media_path

):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    cursor.execute(
        """
        INSERT INTO property_media (

            property_id,

            media_type,

            media_path,

            created_at

        )

        VALUES (?, ?, ?, ?)
        """,
        (

            property_id,

            media_type,

            media_path,

            now

        )
    )


    connection.commit()

    connection.close()


# ============================================================
# ADD PROPERTY VIEW
# ============================================================

def add_property_view(

    property_id,

    viewer_id=None

):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


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

            now

        )
    )


    connection.commit()

    connection.close()


# ============================================================
# ADD FEEDBACK
# ============================================================

def add_feedback(

    user_id,

    feedback_type,

    subject,

    message

):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    cursor.execute(
        """
        INSERT INTO feedback (

            user_id,

            feedback_type,

            subject,

            message,

            created_at

        )

        VALUES (?, ?, ?, ?, ?)
        """,
        (

            user_id,

            feedback_type,

            subject,

            message,

            now

        )
    )


    connection.commit()

    connection.close()


# ============================================================
# AUDIT LOG
# ============================================================

def add_audit_log(

    user_id,

    action,

    target_type=None,

    target_id=None,

    details=None

):

    connection = get_connection()

    cursor = connection.cursor()

    now = datetime.utcnow().isoformat()


    cursor.execute(
        """
        INSERT INTO audit_logs (

            user_id,

            action,

            target_type,

            target_id,

            details,

            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (

            user_id,

            action,

            target_type,

            target_id,

            details,

            now

        )
    )


    connection.commit()

    connection.close()


# ============================================================
# INITIALIZE DATABASE
# ============================================================

init_db()
