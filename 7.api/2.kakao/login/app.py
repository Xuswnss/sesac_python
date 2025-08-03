from dotenv import load_dotenv
from flask import Flask, render_template, json, url_for, request,session, redirect, jsonify
import requests
import os
import json

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET')
KAKAO_CLIENT_SECRET = os.getenv('KAKAO_CLIENT_SECRET')
KAKAO_REDIRECT_URI = os.getenv('KAKAO_REDIRECT_URI')
KAKAO_REST_API_KEY = os.getenv('KAKAO_REST_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login/kakao')
def login_kakao():
    auth_url = (
        'https://kauth.kakao.com/oauth/authorize?'
        f'response_type=code&client_id={KAKAO_REST_API_KEY}&'
        f'redirect_uri={KAKAO_REDIRECT_URI}&'
        f'scope=profile_nickname'
    )
    return redirect(auth_url)

@app.route('/auth/kakao/callback')
def callback_kakao():
    code = request.args.get('code')
    print(f"code: {code},")
    # Kakao OAuth 토큰 요청 URL
    url = "https://kauth.kakao.com/oauth/token"

    # 요청 데이터 설정
    data = {
        'grant_type': 'authorization_code',
        'client_id': KAKAO_REST_API_KEY,
        'redirect_uri': KAKAO_REDIRECT_URI,
        'client_secret': KAKAO_CLIENT_SECRET,
        'code': code
        }
    token_headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data,headers=token_headers).json()
    print('############ response : ', response)
    access_token = response.get('access_token')
    profile_scope = response.get('scope')
    print(f'######### scope : {profile_scope}')

    #사용자 정보 요청
    headers = {'Authorization' : f'Bearer {access_token}'}
    profile = requests.get('https://kapi.kakao.com/v2/user/me',headers=headers).json()
    print(f'profile : {profile}')
    kakao_id = profile.get('id')
    connected_at = profile.get('connected_at')
    nickname = profile.get('properties', {}).get('nickname')

    session['user'] = {
        'id': kakao_id,
        'connected_at': connected_at,
        'nickname': nickname
    }

    return redirect(url_for('profile'))

    # return jsonify(profile)
    


@app.route('/profile')
def profile():
    user = session.get('user')
    kakao_id = user.get('id')
    connected_at = user.get('connected_at')
    nickname = user.get('nickname')
    print('###### nickname : ' , nickname)
    print('###### user :', user)
    return render_template('profile.html',
                           kakao_id=kakao_id,
                           connected_at=connected_at,
                           nickname=nickname)
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    