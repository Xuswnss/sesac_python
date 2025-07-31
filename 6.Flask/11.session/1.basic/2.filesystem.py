from flask import Flask,session
from flask_session import Session
import os

app = Flask(__name__) 

app.secret_key = 'xuswns' #아무거나 무방

app.config['SESSION_TYPE'] = 'filesystem' #기본값 null 
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'my_session')
app.config['SESSION_PERMANENT'] =False #브라우저가 닫히면 삭제
app.config['SESSION_USE_SIGNER'] = True # 세션 쿠키에 서명사용 여부

Session(app) #우리의 앱의 세션기능을 더해줌\

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션이 저장되었습니다.'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f'session info {session["username"]}'
    else:
        return f'not found'

@app.route('/clear-session')
def del_session():
    session.pop('username', None) #세션에서 값 삭제
    return f'세젼정보가 삭제되었습니다.'

if __name__ == "__main__":
    app.run(debug=True)
