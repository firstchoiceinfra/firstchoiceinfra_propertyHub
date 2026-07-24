# ========================================================
# NOTIFICATIONS TABLE
# ========================================================

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS notifications (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        recipient_role TEXT NOT NULL,

        recipient_user_id INTEGER,

        title TEXT NOT NULL,

        message TEXT NOT NULL,

        notification_type TEXT DEFAULT 'general',

        reference_id INTEGER,

        is_read INTEGER DEFAULT 0,

        created_at TEXT NOT NULL,

        FOREIGN KEY (
            recipient_user_id
        )
        REFERENCES users(id)

    )
    """
)
# ============================================================
# CREATE NOTIFICATION
# ============================================================

def create_notification(

    recipient_role,

    title,

    message,

    notification_type="general",

    reference_id=None,

    recipient_user_id=None

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        INSERT INTO notifications (

            recipient_role,

            recipient_user_id,

            title,

            message,

            notification_type,

            reference_id,

            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """,

        (

            recipient_role,

            recipient_user_id,

            title,

            message,

            notification_type,

            reference_id,

            datetime.now().isoformat()

        )

    )

    connection.commit()

    notification_id = cursor.lastrowid

    connection.close()

    return notification_id


# ============================================================
# GET NOTIFICATIONS
# ============================================================

def get_notifications(

    recipient_role,

    recipient_user_id=None

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT *

        FROM notifications

        WHERE

        (

            recipient_role = ?

            OR recipient_role = 'all'

        )

        AND

        (

            recipient_user_id IS NULL

            OR recipient_user_id = ?

        )

        ORDER BY created_at DESC

        """,

        (

            recipient_role,

            recipient_user_id

        )

    )

    notifications = cursor.fetchall()

    connection.close()

    return notifications


# ============================================================
# GET UNREAD NOTIFICATION COUNT
# ============================================================

def get_unread_notification_count(

    recipient_role,

    recipient_user_id=None

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT COUNT(*)

        FROM notifications

        WHERE

        is_read = 0

        AND

        (

            recipient_role = ?

            OR recipient_role = 'all'

        )

        AND

        (

            recipient_user_id IS NULL

            OR recipient_user_id = ?

        )

        """,

        (

            recipient_role,

            recipient_user_id

        )

    )

    count = cursor.fetchone()[0]

    connection.close()

    return count


# ============================================================
# MARK NOTIFICATION AS READ
# ============================================================

def mark_notification_as_read(

    notification_id

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        UPDATE notifications

        SET is_read = 1

        WHERE id = ?

        """,

        (

            notification_id,

        )

    )

    connection.commit()

    connection.close()
