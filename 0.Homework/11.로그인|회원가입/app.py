from flask import Flask, render_template, request, redirect, url_for, session, flash
import bcrypt

from database import users, add_user
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
from config import MAIL_SETTINGS
import bcrypt
import os
import random
import string
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = 'app_secret_key'
app.config.update(MAIL_SETTINGS)
mail = Mail(app)

# 로그인
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        print(f'id: {id}, password : {password}')
        
        user = next((u for u in users if u['id'] == id and bcrypt.checkpw(password.encode('utf-8'), u['password'].encode('utf-8'))), None)
        if user:
            session['user'] = {'id': user['id'], 'name': user['name']}
            flash(f"{user['name']}님 환영합니다!", 'success')
            return redirect(url_for('login_success'))
        else:
            flash("로그인에 실패하셨습니다. 아이디와 비밀번호를 확인해주세요.", 'danger')
            print('로그인 실패')
            return redirect(url_for('index'))
    return render_template('index.html')

# 로그인 성공
@app.route('/success')
def login_success():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        flash("로그인 후 이용해주세요.", 'warning')
        return redirect(url_for('index'))



# 인증 코드 생성
def generate_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

# 회원가입 페이지
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        user_id = request.form.get('id')
        password = request.form.get('password')
        email = request.form.get('email')

        session['temp_user'] = {
            'name': name,
            'id': user_id,
            'password': password,
            'email': email
        }

        # 인증 코드 생성 및 메일 발송
        code = generate_code()
        session['email_code'] = code

        try:
            msg = Message('[회원가입 인증코드]', sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[email])
            msg.body = f'인증코드는 [{code}] 입니다.'
            mail.send(msg)
            flash('입력한 이메일로 인증코드를 보냈습니다.', 'info')
            return redirect(url_for('verify_email'))
        except Exception as e:
            flash(f"이메일 전송 실패: {e}", 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')

# 인증 코드 입력
@app.route('/verify', methods=['GET', 'POST'])
def verify_email():
    if request.method == 'POST':
        input_code = request.form.get('code')
        if input_code == session.get('email_code'):
            user = session.pop('temp_user')
            success = add_user(user['name'], user['id'], user['password'], user['email'])
            if success:
                flash("회원가입이 완료되었습니다! 로그인 해주세요.", 'success')
                return redirect(url_for('index'))
            else:
                flash("이미 존재하는 아이디입니다.", 'danger')
                return redirect(url_for('register'))
        else:
            flash("인증 코드가 일치하지 않습니다.", 'danger')
    return render_template('verify.html')

# 이메일 인증코드 전송 API
@app.route('/api/send-email-code', methods=['POST'])
def send_email_code():
    data = request.get_json()
    email = data.get('email')
    print('##### input email : ' , email)
    code = generate_code()

    session['email_code'] = code
    session['temp_user'] = data  # name, id, password, email 포함된 dict

    try:
        msg = Message('[회원가입 인증코드]', 
              sender=app.config.get('MAIL_DEFAULT_SENDER'),  
              recipients=[email])
        msg.body = f'인증코드는 [{code}] 입니다.'
        mail.send(msg)
        return {'success': True, 'message': '이메일로 인증코드를 전송했습니다.'}, 200
    except Exception as e:
        return {'success': False, 'message': f'이메일 전송 실패: {str(e)}'}, 500

# 인증코드 검증 API
@app.route('/api/verify-email-code', methods=['POST'])
def verify_email_code():
    data = request.get_json()
    input_code = data.get('code')
    expected_code = session.get('email_code')

    if input_code == expected_code:
        user = session.pop('temp_user')
        success = add_user(user['name'], user['id'], user['password'], user['email'])
        if success:
            session.pop('email_code', None)
            return {'success': True, 'message': '회원가입 완료'}, 200
        else:
            return {'success': False, 'message': '이미 존재하는 아이디입니다.'}, 409
    else:
        return {'success': False, 'message': '인증 코드가 일치하지 않습니다.'}, 400



# OAuth2 (구현 예정)
@app.route('/login/google')
def login_google():
    return

@app.route('/login/kakao')
def login_kakao():
    return

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("로그아웃 되었습니다.", 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
