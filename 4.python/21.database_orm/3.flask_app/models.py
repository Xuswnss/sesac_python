from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 사용자 모델 정의
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    
    def __repr__(self):
        return f'[User {self.id} : {self.name} : {self.age}]'
    
    def __str__(self):
        return f'[User {self.id} : {self.name} : {self.age}]'