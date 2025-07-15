import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(to_email: str, pdf_url: str):
    from_email = os.getenv("EMAIL_FROM")
    app_password = os.getenv("EMAIL_APP_PASSWORD")

    subject = "🩺 Your Health Summary from Setu AI"
    body = f"""
    Hello,<br><br>
    Your health summary is ready.<br>
     <a href="{pdf_url}">Click here to download</a><br><br>
    Regards,<br>
    Setu AI Team
    """

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        print(" Email sent successfully.")
    except Exception as e:
        print(" Failed to send email:", e)


def send_custom_email(to_email: str, subject: str, html_body: str):
    from_email = "jayalakshmim720@gmail.com"
    app_password = "fmwu wwqg bkbb qwtm"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(html_body, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        print("Custom email sent successfully.")
    except Exception as e:
        print(" Failed to send custom email:", e)
