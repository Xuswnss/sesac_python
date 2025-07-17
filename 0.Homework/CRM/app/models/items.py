from sqlalchemy import Column,String
from app import db

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(String, primary_key=True)
    name = db.Column(String)
    type = db.Column(String)
    unit_price = db.Column(String)
    
# create table if not exists items(
#     id text primary key,
#     name text,
#     type text,
#     unit_price text
# );
# .import item_data.csv items
    