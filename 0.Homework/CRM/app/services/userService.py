from app.models.users import User
from app.models.orders import Order
from sqlalchemy import func


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


# user paginated
def user_paginated(session, page=1, per_page=10):
    pagination = session.query(User).paginate(page=page, per_page=per_page, error_out=False)
    return pagination  

# user-detail
def get_user_by_id(session,user_id):
    user = session.get(User, user_id)
    print('#### user : ', user)
    session.commit()
    return user

def get_orderList_by_userId(session, user_id):
    orders = session.query(Order).filter(Order.user_id == user_id).all()
    print('### orders : ', orders)
    session.commit()
    return orders
    


