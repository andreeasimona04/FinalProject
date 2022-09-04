import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import pathlib
from secrets import EMAIL_USER, EMAIL_PASS
from API1 import get_email_content
from db import count_emails, read_emails

ROOT = pathlib.Path(__file__).parent
DB_file = ROOT.joinpath("ForEmail.db")
conn = sqlite3.connect(DB_file)

def send_email():
    gmail_user = EMAIL_USER
    gmail_pass = EMAIL_PASS
    gmail_server = "smtp.gmail.com"
    gmail_server_port = 465
    message = MIMEMultipart("alternative")
    message["Subject"] = "IT Newsletter"
    message["From"] = gmail_user


    html = f"""
    <html>
    <body>
        <h2>Hello!Read the latest IT news!</h2>
            <p>{get_email_content()}</p>
    </body>
    </html>
    """
    part2 = MIMEText(html, "html")

    message.attach(part2)


    server = smtplib.SMTP_SSL(gmail_server, gmail_server_port)
    server.login(gmail_user, gmail_pass)
    server.sendmail(
        gmail_user,
        read_emails(conn),
        message.as_string()
    )



