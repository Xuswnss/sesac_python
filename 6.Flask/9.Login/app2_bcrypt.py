from flask import Flask, render_template,request, redirect, url_for, flash
from flask import session
import sqlite3
from datetime import timedelta
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10) #1분이 지나면 자동으로 세션이 삭제된다.

DB_FILENAME = 'users.db'


def get_user_by_username(user_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username = ? ' , (user_id,))
    user = cur.fetchone()
    print('이미 존재하는 아이디입니다.', user)
    conn.commit()
    conn.close()
    return user
    
def create_user(user_id, user_pw, user_name):
    hash_pw = bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password, name) VALUES (?,?,?)' , (user_id, hash_pw, user_name))
    user = cur.fetchone()
    print('회원이 추가되었습니다.', user)
    conn.commit()
    conn.close()
    return user
    
    
def get_user(username, password):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username= ? ', (username,))
    user = cur.fetchone()
    conn.close()
    #한번에 username과 password로 비교할 수 없다. username -> password식으로 두 단계를 거쳐야 한다
    if user and bcrypt.checkpw(password.encode(), user['password']):
        return user
    return None
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('id')
        user_password = request.form.get('password')

        user = get_user(user_id, user_password)
        
        if user:
            session['user'] = {'id' : user['id'], 'name' : user['name']}
            flash('로그인에 성공했습니다' , 'success')
            return redirect(url_for('user'))
        flash('id와 password가 일치하지 않습니다', 'danger')
        return redirect(url_for('index'))
    
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        # user = session.get('user')
        # user = session.get('user', None)
        return render_template('user.html', name=user['name'])
    
    flash('비정상 접근입니다. 로그인 하세요' , 'warning')
    return redirect(url_for('login'))

@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('id')
        user_pw = request.form.get('password')
        user_pw2 = request.form.get('password2')
        user_name = request.form.get('name')
            
        if not user_id or not user_pw or not user_pw2 or not user_name:
            flash('모든 필드를 입력해주세요' , 'info')
            return redirect(url_for('register'))
        if user_pw != user_pw2:
            flash('비밀번호가 일치하지 않습니다' , 'danger')
            return redirect(url_for('register'))
        if get_user_by_username(user_id):
            flash('이미 존재하는 사용자 아이디 입니다', 'danger')
            return redirect(url_for('register'))
            
        create_user(user_id, user_pw, user_name)
        flash('회원가입이 완료되었습니다. 로그인 해주세요 ', 'success')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
        flash('정상적으로 로그아웃 됐습니다' , 'success')
        return redirect(url_for('index'))
    else: 
        flash('이미 로그아웃 됐습니다 ', 'warning')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)