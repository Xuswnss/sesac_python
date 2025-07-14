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

#데이터 조회
cur.execute('select * from users')

#결과 가져오기 -> 모든 행을 다 가져오기 fetchall()
rows = cur.fetchall()
for row in rows:
    print(f'행 출력 : {row}')
    
print('- ' * 10)
  
rows = cur.fetchone()
print(rows)

print('- ' * 10)
cur.execute('select  count(*) from users')
rows = cur.fetchall() #결과 리스트
print(rows)
cur.execute('select  count(*) from users')
rows = cur.fetchone()
print(rows) # 결과 튜플

cur.execute('select  count(*) from users')
rows = cur.fetchone()[0]
print(rows) #결과 value

#-------------------

conn.commit()

conn.close()
print(f"DB 완료 됨: {db_path}")
