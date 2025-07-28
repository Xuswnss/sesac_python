from app.models.stores import Store
from app.models.orders import Order
from app.models.items import Item
from app.models.orderitems import OrderItems
from sqlalchemy.orm import joinedload
from sqlalchemy import func

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
            # ✅ month가 있는 경우: 해당 월에 해당하는 날짜만 필터링             
            if not date_key.startswith(month):                 
                continue          

        if date_key not in sales_data:             
            sales_data[date_key] = {'count': 0, 'total_revenue': 0}          

        sales_data[date_key]['count'] += 1         
        sales_data[date_key]['total_revenue'] += price      

    # 📌 정렬된 결과 리스트     
    sales_list = [         
        {             
            'date': key,             
            'total_revenue': sales_data[key]['total_revenue'],             
            'count': sales_data[key]['count']         
        }         
        for key in sorted(sales_data.keys())     
    ]      

    return sales_list