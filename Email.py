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

gmail_user = EMAIL_USER
gmail_pass = EMAIL_PASS
email_adresses = read_emails(conn)
gmail_server = "smtp.gmail.com"
gmail_server_port = 465

def send_email(sendto):
    message = MIMEMultipart("alternative")
    message["Subject"] = "IT Newsletter"
    message["From"] = gmail_user
    message["To"] = sendto


    html = f"""
    <html>
    <body>
        <h2>Hello!</h2>
        <p>Read the latest IT news!</p>
    </body>
    </html>
    """
    part2 = MIMEText(html, "html")

    message.attach(part2)


    server = smtplib.SMTP_SSL(gmail_server, gmail_server_port)
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(
        gmail_user,
        sendto,
        message.as_string()
    )

# send_welcome_email(email_adresses)

print(email_adresses)