from app.models.orderitems import OrderItems
from app.models.orders import Order
from app.models.items import Item

#Flask-SQLAlchemy는 session을 자동으로 생성하고 db.session을 통해 접근할 수 있게 해 줍니다.
#따라서 session = Session() 과 같은 정의 없이도 사용할 수 있음.

def get_orderItems(session,page =1, per_page=10):
    pagination = session.query(OrderItems).paginate(page = page, per_page=per_page, error_out =False)
    return pagination

def get_orderItems_detail_by_orderId(session, order_id):
    result = session.query(OrderItems,Item.name).join(Item, OrderItems.item_id == Item.id).filter(OrderItems.order_id == order_id).all()
    print('#### get_orderItems_detail_by_orderId :', result)

    session.commit()
    return result

    




   