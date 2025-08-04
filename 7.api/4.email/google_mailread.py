import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os

load_dotenv()
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL')
GOOGLE_PASSWORD = os.getenv('GOOGLE_APP_PASSWORD')
RECIPIENT_MAIL = GOOGLE_EMAIL

mail = imaplib.IMAP4_SSL(IMAP_SERVER,IMAP_PORT)
mail.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)

mail.select('INBOX')
status, message = mail.search(None, 'ALL')

mail_ids = message[0].split()
latest_mail_id = mail_ids[-1]

#최신 메일 가져오기

status, msg_data = mail.fetch(latest_mail_id, '(RFC822)')
print(status, msg_data)


# 본문 데이터 파싱하기
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        #mail title decoding
        subject, encoding = decode_header(msg['subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if  encoding else 'utf-8')
        print(f'###### title : {subject}')

        #발신자 정보
        from_ = msg.get('From')
        print(f'###### 발신자 : {from_}')

        #메일 본문 추출
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                body = part.get_payload(decode=True).decode('utf-8')
                print(f'###### 본문 : {body}')
        else: 
            body = msg.get_payload(decode=True).decode('utf-8')
            print(f'###### 본문 : {body}')
            break
        mail.logout()



