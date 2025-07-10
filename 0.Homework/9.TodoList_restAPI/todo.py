from flask import Flask,request

app = Flask(__name__)

todo = []

@app.route('/')
def index():
    pass
#정보 가져와서 등록하기
@app.route('/upload')
def upload():
    list = request.args.get('userInput')
    print(list)
#삭제하기
@app.route('/delete')
def delete():
    pass


if __name__ == '__main__':
    app.run(debug=True, port= 5050)