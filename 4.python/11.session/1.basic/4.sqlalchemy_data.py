from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import json

app = Flask(__name__)

app.secret_key = 'xuswns' #세션 암호하를 위한 키 (내가 관리하고 내가 암호화하고)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'
db = SQLAlchemy(app)
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_PERMANENT'] =False #브라우저가 닫히면 삭제
app.config['SESSION_SQLALCHEMY'] = db
Session(app) #우리의 앱의 세션기능을 더해줌
    
    

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    session['count'] = 42
    session['my_list'] =['apple','banana','watermelon']
    # 저장을 하고 사용자에게는 기본 id만 준다.
    session_store(session.sid, dict(session))
    return '세션이 저장되었습니다.'

def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id=sid)
    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()
    
def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data and session_data.data:
        return json.loads(session_data.data)
    return {}

@app.route('/get-session')
def get_session():
    stored_session_data = get_session_data(session.sid)
    stored_session_str = json.dumps(stored_session_data, indent= 4)
    return f'stored data : {stored_session_str}'
    # if 'username' in session:
    #     return f'session info {session["username"]}'
    # else:
    #     return f'not found'

@app.route('/clear-session')
def del_session():
    session.pop('username', None) #세션에서 값 삭제
    return f'세젼정보가 삭제되었습니다.'


class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key = True)
    data = db.Column(db.Text)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)

