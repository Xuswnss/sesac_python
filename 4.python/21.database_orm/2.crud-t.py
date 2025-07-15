from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# 현재 파일 기준 디렉토리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 해당 디렉토리 하단의 users.db
db_path = os.path.join(BASE_DIR, 'users.db')
# 절대경로로 DB 연결
engine = create_engine(f"sqlite:///{db_path}")

Base = declarative_base()

#테이블 설계
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
Base.metadata.create_all(engine)

Session =sessionmaker(bind=engine)

sess = Session()
# ----------- CRUD 함수 만들기 ----------------
#1. user 생성
def create_user(session, name: str , age : int) -> User:
    new_user = User(name = name, age = age)
    session.add(new_user)
    session.commit()
    return User
# 2. 전체 User 조회
def get_users(session) -> list[User]:
    user_list = session.query(User).all() # 반환 값 리스트임
    #아무 인자도 안받고 사용자 리스트 반납
    return user_list

# 3. id로 user 값 조회
def get_user_by_id(session, user_id : int) -> User | None:
    # user = session.get(User, user_id)
    user = session.query(User).filter_by(id = user_id).first()
    return user

# 4. 업데이트 유저 나이   
def update_user_age(session, user_id: int, new_age: int) -> bool:
    user = session.get(User, user_id) 
    if not user:
        return False
    user.age = new_age
    session.commit()
    return True

  
#5. 삭제 회원
def delete_user(session, user_id : int ) -> bool:
    #사용자를 삭제하고 성공시 true
    users = session.query(User).all()
    for  i ,user in enumerate(users):
        if user.id == user_id:
            del user[i]
            session.commit()
            return True
    return False

# ----------- CRUD 함수 만들기 ----------------

if __name__ == '__main__':
    Session = sessionmaker(bind=engine , expire_on_commit= False)
    with Session() as sess : 
        # 1) 사용자 만들기
        user1 = create_user(sess, 'user1', 20)
        user2 = create_user(sess, 'user2', 22)
        print(f'추가된 사용자 Id : {user1.id}, {user2.id}')
        
        #2 사용자 조회
        get_user1 = get_user_by_id(sess, user1.id)
        print(f'조회한 사용자 정보 : {get_user1.name}')

        get_user2 = get_user_by_id(sess, user2.id)
        print(f'조회한 사용자 정보 : {get_user2.name}')
        
        #사용자 정보 수정
        update_user1 = update_user_age(sess, user1.id , 100)
        print(f'업데이트 요청 성공 여부 : {update_user1}')

        # 4) 사용자 모두 조회
        users = get_users(sess)
        for u in users:
            print(f'Id : {u.id}\n 이름 : {u.name}\n 나이 : {u.age}\n')

        # 사용자 삭제
        
        delete_user1 = delete_user(sess, user1.id)
        print(f'삭제 되었나요 ? : {delete_user1}')




