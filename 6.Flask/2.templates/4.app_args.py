from flask import Flask, render_template, request

app = Flask(__name__)
users = [
    {'name' : 'Alice', 'age': 22, 'mobile' : '010-1234-1234'},
    {'name' : 'Bob', 'age': 23, 'mobile' : '010-4321-1234'},
    {'name' : 'Charlie', 'age': 24, 'mobile' : '010-1234-4321'},
    {'name' : 'Xuswns', 'age': 25, 'mobile' : '010-1111-1234'},
    
]
#사용자 목록을 테이블로 그린다.
#입력폼을 하나 만들고 상ㅅㅇ자 이름으로 원하는 사용자 골라내긴
@app.route('/') #get 파라미터 요청이 함께옴
def home():
 name= request.args.get('name')
 print('name', name)
 filtered_user = users
#  for u in users:
#      if u['name'].lower() == name.lower():
#          filtered_user =[u]
#          break
     
 if name : 
      filtered_user = [ u for u in users if u['name'].lower() == name.lower()]
      
 print(filtered_user)

 return render_template('index4.html', user = filtered_user)
      
if __name__ == '__main__':
    app.run(debug=True, port=5050)