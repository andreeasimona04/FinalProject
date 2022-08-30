import smtplib
import sqlite3
import pathlib
from secrets import EMAIL_USER, EMAIL_PASS
from API1 import get_email_content
from db import count_emails, read_emails

ROOT = pathlib.Path(__file__).parent
DB_file = ROOT.joinpath("ForEmail.db")
conn = sqlite3.connect(DB_file)

gmail_user = EMAIL_USER
gmail_pass = EMAIL_PASS
to = read_emails(conn)
subject = "Latest IT news!"
body = get_email_content()

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_pass)
    smtp_server.sendmail(gmail_user, to, email_text)
    smtp_server.close()
    print("Email was sent.")
except Exception as ex:
    print("Something went wrong.", ex)



# count_emails()



