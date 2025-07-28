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
 
def get_store_month_sales(session, store_id):
    results = (
        session.query(Order.order_at, Item.unit_price)
        .join(OrderItems, Order.id == OrderItems.order_id)
        .join(Item, OrderItems.item_id == Item.id)
        .filter(Order.store_id == store_id)
        .all()
    )
    print('################ result : ',results)

    monthly_data = {}

    for order_date_str, unit_price in results:
        # 날짜 문자열에서 연-월만 추출
        try:
            year_month = order_date_str[:7]  # 'YYYY-MM'
        except Exception:
            continue  # 예외 발생 시 건너뜀
        
          # 숫자로 변환 시도
        try:
            price = float(unit_price)
        except (ValueError, TypeError):
        # 숫자가 아니면 무시
            continue
        #db.header를 지우지 않아서 unitprice;라고 적혀있는 칼럼존재
        if year_month not in monthly_data:
            monthly_data[year_month] = {'count': 0, 'total_revenue': 0}

        monthly_data[year_month]['count'] += 1
        monthly_data[year_month]['total_revenue'] += float(price)

    monthly_sales = [
        {
            'date': year_month,
            'total_revenue': monthly_data[year_month]['total_revenue'],
            'count': monthly_data[year_month]['count']
        }
        for year_month in sorted(monthly_data.keys())
    ]
    print('############ monthly sales : ', monthly_sales)
    return monthly_sales
