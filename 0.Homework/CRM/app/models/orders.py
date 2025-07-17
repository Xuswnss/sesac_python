from sqlalchemy import Column,String
from app import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(String, primary_key=True)
    order_at = db.Column(String)
    store_id= db.Column(String)
    user_id = db.Column(String)
    
    # create table if not exists orders(
    #     id text primary key,
    #     order_at text,
    #     store_id text,
    #     user_id text
    # );
    