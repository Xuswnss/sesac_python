import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL')
GOOGLE_PASSWORD = os.getenv('GOOGLE_APP_PASSWORD')
RECIPIENT_MAIL = GOOGLE_EMAIL

#mail 내용
subject = '구글 이메일 테스트입니다'
body= '이 메일은 파이썬을 통해서 생성되었습니다'

message = MIMEText(body)
message['subject'] = subject
message['from'] = GOOGLE_EMAIL
message['to'] = RECIPIENT_MAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()
    smtp.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)
    smtp.sendmail(GOOGLE_EMAIL, RECIPIENT_MAIL, message.as_string())
    print('####### 메일이 성공적으로 보내졌습니다')
except Exception as e:
    print(f'메일 전송 중 오류발생 : {e}')

    
