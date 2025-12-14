import sqlite3
from datetime import datetime

DB_NAME = "sky_ai.db"

def get_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            message TEXT,
            response TEXT,
            timestamp TEXT
        )
    """)

    db.commit()
    db.close()

def save_message(user, message, response):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO conversations (user, message, response, timestamp)
        VALUES (?, ?, ?, ?)
    """, (user, message, response, datetime.now().isoformat()))

    db.commit()
    db.close()
