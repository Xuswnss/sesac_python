import sqlite3
import os

# 현재 실행 중인 파일의 디렉토리 위치 가져오기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 그 디렉토리 하단에 'example.db' 생성
db_path = os.path.join(BASE_DIR, 'example.db')

def connect_db():
    conn = sqlite3.connect(db_path)
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL)
                ''')
    
    conn.commit()
    conn.close()

def insert_user(name,age):
    conn = connect_db()
    cur = conn.cursor()
    users = cur.execute('INSERT INTO users (name, age ) VALUES (?,?)',(name, age))
    print('추가된 회원 : ' , users)
    conn.commit()
    conn.close()
    
    
def get_user():
    conn = connect_db()
    cur = conn.cursor()
    user = cur.execute('SELECT * FROM users')
    user = cur.fetchall() 
    print('선택된 회원 : ', user[0])
    conn.commit()
    conn.close()
    return user
    
def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    user = cur.execute('SELECT * FROM users WHERE name =?', (name,))
    user = cur.fetchone()  

    print('이름으로 고른 회원 : ', user[0])
    conn.commit()
    conn.close()
    return user
    
    
def update_user_age(name,new_age):
    conn = connect_db()
    cur = conn.cursor()
    update_user = cur.execute('UPDATE users SET age = ? WHERE name = ? ', (new_age, name))
    print('updated user : ', update_user)
    conn.commit()
    conn.close()
    
    
def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE name =?', (name,))
    conn.commit()
    conn.close()

def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE age = ?', (age,))
    conn.commit()
    conn.close()
    
def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    
def main():
    create_table()
   
    # insert_user('user1', 20)
    # insert_user('user2', 22)
    # insert_user('user3', 23)
    # insert_user('user4', 27)
    
    
    print('########### data lists')
    users = get_user()
    for user in users:
        print(user)

    print('############ update data')
    update_user_age('user1',100)

    print('########## select user')
    user = get_user_by_name('user2')
    print(user)

    print('########### delete user')
    delete_user_by_name('user3')
    users = get_user()
    for user in users:
        print(user)

    
if __name__ == '__main__':
        main()

    
