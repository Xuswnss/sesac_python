#pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# 현재 파일 기준 디렉토리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 해당 디렉토리 하단의 example.db
db_path = os.path.join(BASE_DIR, 'example.db')

# 절대경로로 DB 연결
engine = create_engine(f"sqlite:///{db_path}")

# 그 디렉토리 하단에 'example.db' 생성
# engine = create_engine('sqlite:///example.db') #상대경로
# engine = create_engine('sqlite:////tmp/example.db') # 절대경로
# engine = create_engine('sqlite:///./example.db') #절대경로

#베이스 클래스를 만들어서 객체랑 DB를 연결한다
Base = declarative_base()

class User(Base):
#optional : DB 테이블 명은 기본적으로 class name으로 되지만 따로 지정해주고 싶을 떄는 __tablename__ = 'users'이런식으로 지정해준다.
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# DB에게 테이블 생성하라고 시틴다.
Base.metadata.create_all(engine)

#세션을 통해서 실제 DB와 CRUD를 함.
Session = sessionmaker(bind=engine)
sess = Session()


#INSERT INTO users(name, age ) VALUES ('user1', 30)
new_user = User(name="user1", age=30)
sess.add(new_user)
sess.commit()

#SELECT * FROM users
users = sess.query(User).all()
print(users)
for user in users:
    print(user.id, user.name, user.age)