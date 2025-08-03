import sqlite3
import hashlib


DB_FILENAME = 'users.db'

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL
            )
            ''')

#테스트 사용자 추가

hash_pw1= hash_password('password1')
hash_pw2 = hash_password('password2')
cur.execute('INSERT INTO users (username, password, name) VALUES(?, ?,?)', ('user1',hash_pw1,'user1'))
cur.execute('INSERT INTO users (username, password, name) VALUES(?, ?,?)', ('user2', hash_pw2 ,'user2'))

conn.commit()
print('#############database success')
conn.close()