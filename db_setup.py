import sqlite3

# Name of the database file (will appear in your project folder)
DB_NAME = 'vision_logs.db'

def create_database():
    """Creates the logs table to store detection data."""
    conn = None
    try:
        # Connects to the database file (creates it if it doesn't exist)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create the logs table with columns for timestamp, object, and language
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                object_detected TEXT NOT NULL,
                language_used TEXT NOT NULL
            )
        """)
        conn.commit()
        print(f"Database '{DB_NAME}' and table 'logs' created successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()