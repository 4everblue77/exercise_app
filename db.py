
import sqlite3

DB_NAME = 'fitness_app.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, goal TEXT, days_per_week INTEGER, equipment TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    cursor.execute("CREATE TABLE IF NOT EXISTS programs (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, date DATE, block_type TEXT, exercise TEXT, sets INTEGER, reps INTEGER, rest INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))")

    cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, date DATE, exercise TEXT, weight REAL, sets INTEGER, reps INTEGER, time TEXT, rpe INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))")

    conn.commit()
    conn.close()
