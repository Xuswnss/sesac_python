from sqlalchemy import Column,String
from app import db

class OrderItems(db.Model):
    __tablename__ = 'orderitems'
    id = db.Column(String, primary_key=True)
    order_id = db.Column(String)
    item_id= db.Column(String)

# create table if not exists orderitems(
#     id text primary key,
#     order_id text,
#     item_id text
# );
# .import orderItem_data.csv orderitems