import pathlib
import sqlite3

ROOT = pathlib.Path(__file__).parent
DB_file = ROOT.joinpath("ForEmail.db")

conn = sqlite3.connect(DB_file)

class DataBase:
    def create_user_table(conn):
        cur = conn.cursor()
        cur.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
        count INTEGER DEFAULT 0
        )""")
        conn.commit()

    def add_new_user(conn, name, email):
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO users (name, email)
        VALUES
        (?,?)
        """, (name, email))
        conn.commit()

    def delete_user(conn, id):
        cur = conn.cursor()
        cur.execute("""DELETE FROM users WHERE id = ?""", (id,))
        conn.commit()

    def read_email(conn, email):
        pass
    
    def count_emails(conn, count):
        cur = conn.cursor()
        cur.execute("""UPDATE users SET count = 1""")
        conn.commit()