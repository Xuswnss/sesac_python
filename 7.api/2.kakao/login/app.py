from dotenv import load_dotenv
from flask import Flask, render_template, json, url_for, request,session, redirect
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
    pass

@app.route('/auth/kakao/callback')
def callback_kakao():
    pass

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    pass

if __name__ == '__main__':
    app.run(debug=True)
    