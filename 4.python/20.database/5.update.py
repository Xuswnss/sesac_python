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


# ------------------
cur.execute('UPDATE users SET name="user1"')
cur.execute('UPDATE users SET name="?" WHERE id = ?', (50,1))
#-------------------

conn.commit()

conn.close()

