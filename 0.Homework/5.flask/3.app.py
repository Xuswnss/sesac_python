from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Alice', 'age': 35, 'mobile': '050-5555-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
    {'name': 'David', 'age': 30, 'mobile': '050-4444-5678'},
]

# 미션1. 사용자 목록을 테이블로 그린다
# <table border="1"> <tr> <td>
# 미션2. 입력폼을 하나 만들고, 사용자 이름으로 원하는 사용자만 골라낸다


# http://localhost:5000/?name=aaa&age=22

@app.route('/')  # GET 파라미터 요청이 함께 온다는 것...
def home():
    name = request.args.get('name')
    age = request.args.get('age')
    phone = request.args.get('phone')
    
    result = users
    #여러조건을 확인하기 위해 전부 if문으로 코드를 짬!
    if name:
        result =  [ u for u in result if u['name'].upper() == name.upper()]
    if age:
        age = int(age)
        result = [u for u in result if u['age'] == age]
    if phone:
        result = [ u for u in result if u['mobile'] == phone]
        
    return render_template('app.html' , users = result)
    



if __name__ == '__main__':
    app.run(debug=True, port=5050)