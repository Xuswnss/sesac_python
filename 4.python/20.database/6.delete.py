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

cur.execute('DELETE FROM users WHERE id=1')
cur.execute('DELETE FROM users WHERE name= ?',('user1',)) #('user1')이런식으로 표현하면 이게 튜플인지 ()단일 인자인지를 구별 할 수 없다.ㄴ('user1',)
#-------------------

conn.commit()

conn.close()

