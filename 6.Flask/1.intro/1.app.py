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



if __name__ == '__main__':
#5000은 이미사용중인 port이므로 다른 포트로 변경해야함 ^.^!
    app.run(port=5001)
