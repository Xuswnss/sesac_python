#pip install Flask
# flask는 기본적으로 5000번 포트를 제공한다.
from flask import Flask # 대문자 -> 객체

app = Flask(__name__) 
print(app)

@app.route('/') #사용자가 / 에 접속하면, 이 아래 함수로 접속해줘
def home():
    return "<h1> Hello, Flask! </h1>"

@app.route('/xuswns') #사용자가 / 에 접속하면, 이 아래 함수로 접속해줘
def xuswns():
    return "<h1> Hello, xuswns! </h1>"

@app.route('/user') #사용자가 / 에 접속하면, 이 아래 함수로 접속해줘
def user():
    return "<h1> Hello, user! </h1>"

@app.route('/user/<username>') #사용자가 / 에 접속하면, 이 아래 함수로 접속해줘
# 따로 지정하지 않으면 문자열로 처리 , 타입 지정 따로 ㄱㄴ
#플라스크 데코레이션 <...>을 함수인자로 전달한다
def user_name(username):
    print('username')
    return f"<h1> Hello, {username}! </h1>"


@app.route('/<int:age>')
def user_age(age):
    result = f'<h1>your age ? : {age}</h1>'
    return result


@app.route('/user/<float:weight>')
def user_weight(weight):
    result = f'<h1>your weight ? : {weight}</h1>'
    return result

@app.route('/user/<name>/<int:age>/<float:weight>')
def user_all(name,age,weight):
    return f'<h1>hello, {user}</h1> <h2>사용자 정보</h2> <ul><li>name : {name}</li><li>age : {age} </li><li>weight : {weight}</li></ul>'

if __name__ == '__main__':
#5000은 이미사용중인 port이므로 다른 포트로 변경해야함 ^.^!
#cmd + option + u => 코드보기
    app.run(port=5001, debug=True) #Debug모드가 켜져있으면 저장할 떄마다 재시작이 된다 ^.< !
    #오류메세지를 클라이언트에서 보여준다 but 절대 켜진상태로 배포를 하시면 안된다!!!! &.&
