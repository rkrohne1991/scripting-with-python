import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Visual Studio Code"
# email["to"] - add address where to send the email
email["to"] = "email address to goes here"
email["subject"] = "You won 1,000,000 dollars!"

email.set_content(html.substitute({"name":"TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login needs 2 parameters, login and password to email account
    smtp.login("gmail account goes here", "password goes here")
    smtp.send_message(email)
    print("all good boss!")
