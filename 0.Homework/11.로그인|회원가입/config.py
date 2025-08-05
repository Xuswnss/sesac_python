# config.py
import os

MAIL_SETTINGS = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": os.getenv("EMAIL_USER"),  # .env에 설정
    "MAIL_PASSWORD": os.getenv("EMAIL_PASS"),
    "MAIL_DEFAULT_SENDER" : os.getenv("EMAIL_USER")  #
}
