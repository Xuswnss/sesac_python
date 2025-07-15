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
    print('##### 검색된 stores : ' , result)
    conn.close()
    
    # stores_dict = []
    # for s in result:
    #     stores_dict.append({
    #         'Id': s[0],
    #         'Name' : s[1],
    #         'Type' : s[2],
    #         'Address' : s[3]
    #     })
    return result

    