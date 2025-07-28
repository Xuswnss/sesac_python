from app.models.items import Item
from app.models.orderitems import OrderItems
from app.models.orders import Order
from collections import defaultdict
from datetime import datetime


def get_items(session,page =1, per_page=10):
    pagination = session.query(Item).paginate(page = page, per_page=per_page, error_out =False)
    return pagination

def get_item_by_id(session ,item_id):
    result = session.query(Item).filter(Item.id == item_id)
    session.commit()
    return result

def get_monthly_sales(session, item_id):
    # 주문 일자와 단가를 가져옴
    results = (
        session.query(Order.order_at, Item.unit_price)
        .select_from(OrderItems)
        .join(Order, OrderItems.order_id == Order.id)
        .join(Item, OrderItems.item_id == Item.id)
        .filter(Item.id == item_id)
        .all()
    )

    monthly_data = {}

    for order_date_str, unit_price in results:
        # 날짜 문자열에서 연-월만 추출
        try:
            year_month = order_date_str[:7]  # 'YYYY-MM'
        except Exception:
            continue  # 예외 발생 시 건너뜀

        # 초기화
        if year_month not in monthly_data:
            monthly_data[year_month] = {'count': 0, 'total_revenue': 0}

        # 누적 합산
        monthly_data[year_month]['count'] += 1
        monthly_data[year_month]['total_revenue'] += int(unit_price)

    # 결과 리스트 구성
    monthly_sales = []
    for year_month in sorted(monthly_data.keys()):
        monthly_sales.append({
            'date': year_month,
            'total_revenue': monthly_data[year_month]['total_revenue'],
            'count': monthly_data[year_month]['count']
        })

    return monthly_sales

    
    # for row in results:
    #     date = row[0]
    #     item = row[1]
    #     print("row type:", item.type)
    #     print("order_At:", date, type(date))
    #     print("Item name:", item.name)
    #     print("Item unit_price:", item.unit_price)
    #     print("------")
    




    
    