import os

DEBUG = True
PORT = 5050

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


db_path = os.path.join(BASE_DIR,  'data', 'crm.db')
db_path = os.path.abspath(db_path)  # 절대경로로 변환

print('####db 파일 절대 경로',db_path)  # 경로 확인
print('#### db 파일이 존재합니까 ? ',os.path.exists(os.path.dirname(db_path)))  
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
