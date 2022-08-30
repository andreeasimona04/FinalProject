import pathlib
import sqlite3

ROOT = pathlib.Path(__file__).parent
DB_file = ROOT.joinpath("ForEmail.db")
conn = sqlite3.connect(DB_file)

def create_user_table(con):
    cur = con.cursor()
    cur.execute("""CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    count INTEGER DEFAULT 0
    )""")
    con.commit()

def read_emails(con):
    cur = con.cursor()
    r = cur.execute("""SELECT email FROM users""")
    con.commit()
    return r
    
    
def count_emails(con):
    cur = con.cursor()
    cur.execute("""UPDATE users SET count = count + 1""")
    con.commit()

def delete_user(con, email):
    cur = con.cursor()
    cur.execute("""DELETE FROM users WHERE email = ?""", (email,))
    con.commit()

def add_new_user(con, email):
    cur = con.cursor()
    cur.execute("""
    INSERT INTO users (email)
    VALUES
    (?)
    """, (email,))
    con.commit()

# def main():
#     conn = sqlite3.connect(DB_file)
#     # create_user_table(conn)

# if __name__ == "__main__":
#     main()


print(read_emails(conn))