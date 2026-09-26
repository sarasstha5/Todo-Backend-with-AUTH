from typing import List

from fastapi import FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType


conf = ConnectionConfig(
    MAIL_USERNAME="sarasstha04@gmail.com",
    MAIL_PASSWORD="vuil xnuk ahjl tazg",
    MAIL_FROM="sarasstha04@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

app = FastAPI()



async def send_email(email: str):
    message = MessageSchema(
        subject="Registration Confirmation!",
        recipients=[email],
        body="<p>Account has been sucessfully created. For any support contact to our team!</p>",
        subtype=MessageType.html,
    )
    await FastMail(conf).send_message(message)
    return {"email sent sucessfully"}