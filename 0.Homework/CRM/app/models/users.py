from app import db
from sqlalchemy import String, Column


#db.Model?
# SQLAlchemy의 기본 ORM모델 클래스를 의미한다
# 내부에서 여러 메타정보를 관리 할 수 잇음
# User class를 DB테이블과 연결
# Base = declarative_base()를 직접 안해도 됨
class User(db.Model): 
    __tablename__ = 'users'
    id = db.Column(String, primary_key=True)
    name = db.Column(String)
    age = db.Column(String)
    gender = db.Column(String)
    birthday = db.Column(String)
    address = db.Column(String)
    
    
    # SQLAlchemy에는 자동으로 dict으로 변환해주는게 없어서 to_dict()메서드 반환
    def to_dict(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'age' : self.age,
            'gender' :  self.gender,
            'birthday' : self.birthday,
            'address' : self.address
        }