import sqlite3
import bcrypt


DB_FILENAME = 'users.db'

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

def hash_password(password):
    return bcrypt.sha256(password.encode()).hexdigest()

cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL
            )
            ''')

#테스트 사용자 추가

def create_user(username, password, name):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password, name) VALUES(?, ?,?)', (username, hashed_pw, name))
    conn.commit()
    print('#############database success')
    conn.close()
    
create_user('user1', 'password1', 'user1')
create_user('user2', 'password2', 'user2')

# hash_pw1= hash_password('password1')
# hash_pw2 = hash_password('password2')
# cur.execute('INSERT INTO users (username, password, name) VALUES(?, ?,?)', ('user1',hash_pw1,'user1'))
# cur.execute('INSERT INTO users (username, password, name) VALUES(?, ?,?)', ('user2', hash_pw2 ,'user2'))

