from app.models.users import User
from app.models.orders import Order
from app.models.orderitems import OrderItems
from app.models.stores import Store
from app.models.items import Item
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

def search_user(session, name=None, gender=None, page=1, per_page=10) -> list[User]:
    filters = []
    
    if name:
        filters.append(func.lower(User.name).like(f"%{name.lower()}%"))
    if gender: 
        filters.append(func.lower(User.gender) == gender.lower())
    if not filters:  
        return []

    query = session.query(User).filter(*filters)
    total = query.count()  # 전체 개수
    users = query.offset((page - 1) * per_page).limit(per_page).all()

    return {
        "total": total,
        "page": page,
        "per_page": per_page,
        "users": users
    }



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
  
  
def get_regular_store(session, user_id):
    result = (
        session.query(
            Store.name,
            func.count(Store.id).label('frequency')
        )
        .join(Order, Order.store_id == Store.id)
        .filter(Order.user_id == user_id)
        .group_by(Store.name)   
    )

    return [
        {'store_name': name, 'frequency': frequency}
        for name, frequency in result
    ]

def get_regular_goods(session, user_id):
    result = (session.query(Item.name.label('items_name') , func.count(Item.id).label('frequency'))
                .join(Order, Order.id == OrderItems.order_id)
                .join(OrderItems, OrderItems.item_id == Item.id)
                .filter(Order.user_id == user_id)
                .group_by(Item.name)
              )
    return [
        {'item_name' : name,
         'frequency' : frequency
         } for name, frequency in result
    ]


