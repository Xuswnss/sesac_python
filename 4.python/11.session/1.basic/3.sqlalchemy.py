from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.secret_key = 'xuswns' #세션 암호하를 위한 키 (내가 관리하고 내가 암호화하고)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db

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

