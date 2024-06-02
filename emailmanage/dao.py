from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from fastapi import File, Form, UploadFile
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm import Session
from config.email import get_settings
import emailmanage.models as models
import emailmanage.schemas as schemas

# Define the template directory
template_dir = 'emailmanage/templates'
# Template configuration
env = Environment(loader=FileSystemLoader(template_dir))

def sendSimpleMail(db:Session, attachment: UploadFile = File(default=None), subject: str = Form(), body: str = Form(), emails: str = Form()):

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = get_settings().MAIL_FROM
    msg['To'] = emails
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Add the attachment
        attachmen = attachment.file.read()
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachmen)
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment.filename}",
        )
        msg.attach(part)
    except Exception as e:
        print(e)

    # Create SMTP connection and send the email
    with smtplib.SMTP(get_settings().MAIL_SERVER, get_settings().MAIL_PORT) as server:
        server.starttls()
        server.login(get_settings().MAIL_USERNAME, get_settings().MAIL_PASSWORD)
        server.send_message(msg)

    return {"message": "Email sent successfully"}

def sendHtmlMail(db:Session, attachment: UploadFile = File(default=None), subject: str = Form(), body: str = Form(), emails: str = Form()):
    variables = {"body" : body}
    # Render the email template
    template = env.get_template(name = "verification.html")
    email_body = template.render(**variables)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = get_settings().MAIL_FROM
    msg['To'] = emails
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'html'))

    try:
        # Add the attachment
        attachmen = attachment.file.read()
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachmen)
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment.filename}",
        )
        msg.attach(part)
    except Exception as e:
        print(e)

    # Send the email
    with smtplib.SMTP(get_settings().MAIL_SERVER, get_settings().MAIL_PORT) as server:
        server.starttls()
        server.login(get_settings().MAIL_USERNAME, get_settings().MAIL_PASSWORD)
        server.send_message(msg)
    return {"message": "Email sent successfully"}
