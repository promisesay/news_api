import smtplib, ssl
import os


def send_email(text):
    host = "smtp.gmail.com"
    port = 465

    username = "naveedzaynali@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "naveedzaynali@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(msg=text, from_addr=username, to_addrs=receiver)

