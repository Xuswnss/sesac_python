from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'my-secret-key'

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션이 저장되었습니다.'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f'session info {session['username']}'
    else:
        return f'not found'

@app.route('/clear-session')
def del_session():
    session.pop('username', None) #세션에서 값 삭제
    return f'세젼정보가 삭제되었습니다.'

if __name__ == "__main__":
    app.run(debug=True)
