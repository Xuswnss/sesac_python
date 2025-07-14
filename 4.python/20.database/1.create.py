import sqlite3
import os

# 현재 실행 중인 파일의 디렉토리 위치 가져오기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 그 디렉토리 하단에 'example.db' 생성
db_path = os.path.join(BASE_DIR, 'example.db')

# DB 연결
conn = sqlite3.connect(db_path)



print(f"DB 연결됨: {db_path}")

#커서 객체 생성
cur = conn.cursor()

#커서를 중심으로 DB에 입출력을 함
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL)')

conn.commit()

conn.close()

