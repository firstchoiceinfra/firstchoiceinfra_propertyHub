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
