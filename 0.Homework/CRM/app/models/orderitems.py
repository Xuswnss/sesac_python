from sqlalchemy import Column,String
from app import db

class OrderItems(db.Model):
    __tablename__ = 'orderitems'
    id = db.Column(String, primary_key=True)
    order_id = db.Column(String)
    item_id= db.Column(String)
    
    def to_dict(self):
        return{
            'id' : self.id,
            'order_id' : self.order_id,
            'item_id' : self.item_id
        }

# create table if not exists orderitems(
#     id text primary key,
#     order_id text,
#     item_id text
# );
# .import orderItem_data.csv orderitems