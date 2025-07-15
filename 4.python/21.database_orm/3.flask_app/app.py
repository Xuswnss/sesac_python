# pip install flask-sqlalchemy

from flask import Flask, render_template, request, redirect
from models import db, User
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 해당 디렉토리 하단의 example.db
db_path = os.path.join(BASE_DIR, 'users1.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_path
db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    # 필요한 에러체크를 더 넣는게 좋음 - 중복사용자/누락된 데이터 등등 (지금은 생략)
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')  # redirect(url_for('index')) 가 좀 더 나은 코드이기는 함.

@app.route('/delete/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print('사용자 없음: ', id)
        
    return redirect('/')

@app.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify_user(id):
    user = db.session.get(User, id)
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_age = request.form.get('age')

        print("입력받은 name:", new_name)
        print("입력받은 age:", new_age)

        if new_name and new_age:
            user.name = new_name
            user.age = new_age
            db.session.commit()
            return redirect('/')
        else:
            return "입력값을 확인해주세요."

    return render_template('modify.html', users=user)

        
    

if __name__ == '__main__':
    # app = create_app() 
    app.run(debug=True, port= 5050)