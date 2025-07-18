from sqlalchemy import Column,String
from app import db

class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(String, primary_key=True)
    name = db.Column(String)
    type = db.Column(String)
    address = db.Column(String)
    
    def to_dic(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'type': self.type,
            'address' : self.address
        }
    
