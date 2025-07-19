from app.models.orders import Order
from app.models.orderitems import OrderItems


def get_orders(session,page =1, per_page=10):
    pagination = session.query(Order).paginate(page = page, per_page=per_page, error_out =False)
    return pagination   
  
