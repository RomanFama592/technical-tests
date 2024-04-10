import base64
from email.mime.text import MIMEText

def create_mail(to, subject, message) -> dict[str, str]:
    message = MIMEText(message)
    message["to"] = to
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_mail(service, message: dict[str, str]):
    return service.users().messages().send(userId="me", body=message).execute()
