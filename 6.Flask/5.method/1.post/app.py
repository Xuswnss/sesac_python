from flask import Flask, render_template, request, redirect, url_for

selected_user = None
app = Flask(__name__)
# 사용자 목록 완성
# 로그인 사용자 id/pw 맞는지 체크
# 맞으면 로그인 성공 -> 성공페이지로 이동
users = [
    {'name': 'Alice', 'id': 'user1', 'password': 'user1'},
    {'name': 'Alice', 'id': 'user2', 'password': 'user2'},
    {'name': 'Bob', 'id': 'user3', 'password': 'user3'},
    {'name': 'Charlie', 'id': 'user4', 'password': 'user4'},
    {'name': 'David', 'id': 'user5', 'password': 'user5'},
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['get' , 'post'])
def login():
    print(request.method)
    if request.method == 'POST': # 대문자로 해야됨!
        user_id = request.form['id']
        user_password = request.form['password']
        print(f'입력된 아이디 {user_id}, input password = {user_password}')
        for user in users:
            if user['id'].lower() == user_id.lower().strip() and user['password'].lower() == user_password.lower().strip(): 
                user_name = user['name']
                print('user_name : ' , user_name)
                selected_user = user['name']
                print('user : ',selected_user)
                return render_template('login_success.html', user= selected_user )
            else:
                error = 'id/pw가 올바르지 않습니다.'
                return render_template('login_false.html', error = error)
            
            
        return redirect(url_for('user', user = user))
    else:
        return render_template('login.html')

@app.route('/user')   
@app.route('/user/<user>')
def user(user = None):
    return render_template('user.html', user=user)
    
@app.route('/product')
def product():
    return render_template('product.html')


if __name__ == '__main__':
    app.run(debug= True, port=5050)

#user = next((u for u in users if u['id'] == id and u['password'] == pw) , None )
## user = (u for u in users if u['id] == id and u ['pw'] == pw)