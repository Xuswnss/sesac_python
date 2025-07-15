import sqlite3
import os


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# db_path = os.path.join(BASE_DIR, 'user-sample.db')

DATABASE = 'user-sample.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 가져온 내용을 dic
    conn.row_factory = sqlite3.Row
    
    return conn
# ------------------------ 상점
def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores')
    store = cursor.fetchall()
    # conn.commit()
    conn.close()
    return store

def search_stores(storename):
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores WHERE name LIKE ? ', (f'%{storename}%',))
    result = cursor.fetchall()
    conn.close()
    return result

# ------------------------ 상점
def get_user_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    users = cursor.fetchall()
    # conn.commit()
    conn.close()
    return users
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    # conn.commit()
    conn.close()
    return users
def get_users_per_page(page, count):
    offset_pos = (page - 1) * count
    
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
    

def search_users_by_name(name):
    pass

def search_user(name,gender,age):
    pass



    