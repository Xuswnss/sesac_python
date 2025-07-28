from app.models.stores import Store
from app.models.orders import Order
from app.models.items import Item
from app.models.users import User
from sqlalchemy import func
from app.models.orderitems import OrderItems


def get_stores(session) -> list[Store]:
    store_list = session.query(Store).all()
    session.commit()
    return store_list

# store paginated
def store_paginated(session, page=1, per_page=10):
    pagination = session.query(Store).paginate(page=page, per_page=per_page, error_out=False)
    return pagination  


def get_store_by_id(session, store_id):
    # 해당 store의 정보, 주문, 주문 아이템, 아이템까지 모두 가져오기
    result = session.query(Store).filter(Store.id == store_id).all()
    session.commit()
    return result
 
def get_store_month_sales(session, store_id, month=None):     
    results = (         
        session.query(Order.order_at, Item.unit_price)         
        .join(OrderItems, Order.id == OrderItems.order_id)         
        .join(Item, OrderItems.item_id == Item.id)         
        .filter(Order.store_id == store_id)         
        .all()     
    )      

    sales_data = {}      

    for order_date, unit_price in results:         
        try:             
            if hasattr(order_date, 'strftime'):                 
                date_key = order_date.strftime('%Y-%m-%d') if month else order_date.strftime('%Y-%m')             
            else:                 
                date_key = str(order_date)[:10] if month else str(order_date)[:7]         
        except Exception:             
            continue          

        try:             
            price = float(unit_price)         
        except (ValueError, TypeError):             
            continue          

        if month:                      
            if not date_key.startswith(month):                 
                continue          

        if date_key not in sales_data:             
            sales_data[date_key] = {'count': 0, 'total_revenue': 0}          

        sales_data[date_key]['count'] += 1         
        sales_data[date_key]['total_revenue'] += price      
   
    sales_list = [         
        {             
            'date': key,             
            'total_revenue': sales_data[key]['total_revenue'],             
            'count': sales_data[key]['count']         
        }         
        for key in sorted(sales_data.keys())     
    ]      

    return sales_list




from sqlalchemy import func, extract

from sqlalchemy import func, extract
from app.models.orders import Order
from app.models.users import User

def list_all_customer(session, store_id):
    results = (
        session.query(Order.user_id, User.name, func.count(Order.id).label("frequency"))
        .join(User, Order.user_id == User.id)
        .filter(Order.store_id == store_id)
        .group_by(Order.user_id, User.name)
        .all()
    )

    return [
        {"user_id": user_id, "name": name, "frequency": frequency}
        for user_id, name, frequency in results
    ]


def list_customer_by_month(session, store_id, month):
    try:
        year, month_number = map(int, month.split('-'))
    except ValueError:
        return []

    results = (
        session.query(Order.user_id, User.name, func.count(Order.id).label("frequency"))
        .join(User, Order.user_id == User.id)
        .filter(Order.store_id == store_id)
        .filter(extract('year', Order.order_at) == year)
        .filter(extract('month', Order.order_at) == month_number)
        .group_by(Order.user_id, User.name)
        .all()
    )

    return [
        {"user_id": user_id, "name": name, "frequency": frequency}
        for user_id, name, frequency in results
    ]
