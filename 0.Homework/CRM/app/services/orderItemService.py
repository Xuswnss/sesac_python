from app.models.orderitems import OrderItems
from app.models.orders import Order

def get_orderItems(session,page =1, per_page=10):
    pagination = session.query(OrderItems).paginate(page = page, per_page=per_page, error_out =False)
    return pagination
    


def get_orderItems_by_orderId(session,order_id):
    orders = session.query(OrderItems).filter(OrderItems.order_id == order_id).all()
    session.commit()
    return orders

   