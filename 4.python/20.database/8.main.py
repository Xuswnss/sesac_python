import db_crud_sqlite as db  
def main():
    db.create_table()
   
    # db.insert_user('user1', 20)
    # db.insert_user('user2', 22)
    # db.insert_user('user3', 23)
    # db.insert_user('user4', 27)
    
    
    print('########### data lists')
    users = db.get_user()
    for user in users:
        print(user)

    print('############ update data')
    db.update_user_age('user1',100)

    print('########## select user')
    user = db.get_user_by_name('user2')
    print(user)

    print('########### delete user')
    db.delete_user_by_name('user3')
    users = db.get_user()
    for user in users:
        print(user)

    
if __name__ == '__main__':
        main()

    
