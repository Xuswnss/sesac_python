# from db_crud_sqlite import (
#     create_table, 
#     insert_user, 
#     get_users, 
#     update_user_age, 
#     get_user_by_name, 
#     delete_user_by_name, 
#     delete_user_by_age
# )

import db_crud_sqlite as db
# import db_crud_mysql as db
# import db_crud_postgresql as db

# 메인 함수
def main():
    # 테이블 생성
    db.create_table()
    
    # 데이터 삽입
    db.insert_user('Alice', 30)
    db.insert_user('Bob', 25)
    db.insert_user('Charlie', 35)

    # 데이터 조회
    print("데이터 목록:")
    users = db.get_users()
    for user in users:
        print(user)
        
    # 데이터 업데이트
    db.update_user_age('Alice', 32)
    
    # 업데이트 후 데이터 조회
    print("사용자 수정후:")
    user = db.get_user_by_name('Alice')
    print(user)
    
    # 데이터 삭제
    db.delete_user_by_name('Bob')
    print("사용자 삭제후:")
    user = db.get_user_by_name('Bob')
    print(user)
    
    print("데이터 목록:")
    users = db.get_users()
    for user in users:
        print(user)
        
    # 데이터 삭제
    db.delete_user_by_name('Alice')
    print("데이터 삭제후 목록:")
    user = db.get_user_by_name('Alice')
    print(user)
    
    db.delete_user_by_age(30)
    print("데이터 삭제후 목록:")
    users = db.get_users()
    for user in users:
        print(user)
        
    db.delete_user_by_age(35)
    print("데이터 삭제후 목록:")
    users = db.get_users()
    for user in users:
        print(user)
    

if __name__ == '__main__':
    main()