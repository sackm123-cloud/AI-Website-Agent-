import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def get_email_config():
    sender = os.getenv("GMAIL_SENDER")
    password = os.getenv("GMAIL_APP_PASSWORD")
    recipients = os.getenv("GMAIL_RECIPIENTS")

    if not sender:
        raise RuntimeError("GMAIL_SENDER is not configured")

    if not password:
        raise RuntimeError("GMAIL_APP_PASSWORD is not configured")

    if not recipients:
        raise RuntimeError("GMAIL_RECIPIENTS is not configured")

    recipient_list = [
        email.strip()
        for email in recipients.split(",")
        if email.strip()
    ]

    return sender, password, recipient_list


def send_email(
    subject: str,
    body: str,
    recipients=None,
):
    sender, password, default_recipients = get_email_config()

    recipients = recipients or default_recipients

    message = EmailMessage()

    message["From"] = sender
    message["To"] = ", ".join(recipients)
    message["Subject"] = subject

    message.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        SMTP_HOST,
        SMTP_PORT,
        context=context,
    ) as smtp:

        smtp.login(sender, password)

        smtp.send_message(message)

    return True


def send_html_email(
    subject: str,
    html_body: str,
    recipients=None,
):
    sender, password, default_recipients = get_email_config()

    recipients = recipients or default_recipients

    message = EmailMessage()

    message["From"] = sender
    message["To"] = ", ".join(recipients)
    message["Subject"] = subject

    message.set_content(
        "This email contains HTML content. "
        "Please use an HTML-capable email client."
    )

    message.add_alternative(
        html_body,
        subtype="html",
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        SMTP_HOST,
        SMTP_PORT,
        context=context,
    ) as smtp:

        smtp.login(sender, password)
        smtp.send_message(message)

    return True


if __name__ == "__main__":
    send_email(
        "AI Automation Test",
        "Gmail SMTP is working correctly.",
    )

    print("Email sent successfully.")
