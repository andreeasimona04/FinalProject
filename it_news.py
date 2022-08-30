import argparse
import pathlib
import sqlite3
from db import add_new_user, delete_user

ROOT = pathlib.Path(__file__).parent
DB_file = ROOT.joinpath("ForEmail.db")
conn = sqlite3.connect(DB_file)

parser = argparse.ArgumentParser(description = "Modify DB.")
parser.add_argument("email", type = str, help ="Email to delete or add.")
parser.add_argument("-d", action = "store_true", help = "Delete from DB.")
parser.add_argument("-a", action = "store_true", help = "Add to DB.")
args = parser.parse_args()

if args.a:
    add_new_user(conn, args.email)

if args.d:
    delete_user(conn, args.email)


