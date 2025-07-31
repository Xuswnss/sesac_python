from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'app_secret_key'

users = [
    {'name': 'user1', 'id': 'user1', 'password': 'password1'},
    {'name': 'user2', 'id': 'user2', 'password': 'password2'},
    {'name': 'user3', 'id': 'user3', 'password': 'password3'},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        print(f'id: {id}, password : {password}')
        
        user = next((u for u in users if u['id'] == id and u['password'] == password), None)
        if user:
            session['user'] = user
            flash(f"{user['name']}님 환영합니다!", 'success')
            return redirect(url_for('login_success'))
        else:
            flash("로그인에 실패하셨습니다. 아이디와 비밀번호를 확인해주세요.", 'danger')
            print('로그인 실패')
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/success')
def login_success():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        flash("로그인 후 이용해주세요.", 'warning')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("로그아웃 되었습니다.", 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
