from flask import Flask,render_template, request, redirect, url_for
from flask import session 

app = Flask(__name__)
app.secret_key = 'app_secret_key'
users = [
    {'name' : 'user1' , 'id' : 'user1' , 'password' : 'password1'},
    {'name' : 'user2' , 'id' : 'user2' , 'password' : 'password2'},
    {'name' : 'user3' , 'id' : 'user3' , 'password' : 'password3'},
]
@app.route('/' , methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        id =request.form.get('id')
        password = request.form.get('password')
        print(f'id: {id}, password : {password}')
      
        
        user = next((u for u in users if u['id'] == id and u['password'] == password), None)
        if user : 
            session['user'] = user #로그인한 사용자 정보를 세션에 저장하겠다는 뜻
            if session.get('user') == user:
                return redirect(url_for('login_success'))
        else:
            errors = {
                'error': '로그인에 실패하셨습니다'
            }
        print('로그인 실패')
        return render_template('index.html', txt=errors) 
    return render_template('index.html' )

# @app.route('/profile')
# def profile():
#     user = session.get('user') #위에서 우리거 저장한 정보
#     if user:
#         return f'당신은 아까 왔던 사용자군요. ⊂(ᴑ╹.╹ᴑ)੭  <h5>{user['name']}</h5>  '
#     else:
#         return f'로그인이 안된 사용자입니다 ૮Ꮚ⑅˵ᴗ͈ . ᴗ͈꒱ა'

@app.route('/success')
def login_success():
    user = session.get('user')
    if(user):
        return render_template('dashboard.html', user = user)
  
        

@app.route('/logout')
def logout():
    session.pop('user', None) #세션에서 값 삭제
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)