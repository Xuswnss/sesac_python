from app.models.users import User
from sqlalchemy import func

# 유저 생성
def create_user(session, name, age) -> User:
    new_user = User(name = name, age = age)
    session.add(new_user)
    session.commit()
    return User

# 전체 회원 조회
def get_users(session) -> list[User]:
    user_list = session.query(User).all()
    # print('#### get_user() : ', user_list)
    session.commit()
    return user_list

# 회원 이름 조회
# 1. 이름과 나이값 받은 후 조회하는 코드 if문으로 쓰기
from sqlalchemy import func

def search_user(session, name=None, gender=None) -> User:
    filters = []
    
    if name:
 
        filters.append(func.lower(User.name).like(f"%{name.lower()}%"))

    if gender:
      
        filters.append(func.lower(User.gender) == gender.lower())

    if not filters:  
        return None

    # 사용자 검색
    user = session.query(User).filter(*filters).all()
    return user 

    
    
# update user
def update_user(session, name, age = None, gender = None) -> User:
    # 이름으로 유저 조회 (주의: 이름이 고유하지 않다면 문제가 생김)
    user = session.query(User).filter_by(name=name).first()

    if not user:
        print(f'{user}을 찾을 수 없습니다.')
    
    if name:
        user.name = name

    if age is not None:
        user.age = age
    if gender is not None:
        user.gender = gender

    session.commit()
    session.refresh(user)  
    return user


#delete user
def delete_user(session, user_id: int) -> bool:
    user = session.get(User, user_id)
    if user:
        session.delete(user)   
        session.commit()
        return True
    return False

# user paginated
def user_paginated(session, page=1, per_page=10):
    pagination = session.query(User).paginate(page=page, per_page=per_page, error_out=False)
    return pagination  




