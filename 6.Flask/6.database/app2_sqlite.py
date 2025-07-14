from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)

# 미션은?? 이 db를 사용해서, 아래 users.append 가 아니고.. db.insert_user 등등으로 바꾸기..
db.create_table()

@app.route('/', methods=['GET', 'POST'])
def index():    
    if request.method == 'POST':
        # POST 요청 처리하기
        name = request.form['name']
        age = int(request.form['age'])
        
        # 사용자 추가
        db.insert_user(name, age)
        return redirect('/') # 추가 끝났으면 그 페이지 다시 불러오기
    
    # GET 요청 처리하기
    users = db.get_users() # dict 로 변환 가능한 row 포멧으로 나와서.. 그냥 쓸수 있음.
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # 수업용으로 좋고, 실용적이지 않음. 왜? 하나 지울려고 모든 리스트를 새로 만들어야 함. 속도가 느림
    db.delete_user_by_id(user_id)
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = db.get_user_by_id(user_id)
    if not user:
        return "사용자를 찾을 수 없습니다.", 404
    
    if request.method == 'POST':
        # 미션3. POST = 실제 수정하는 코드
        name = request.form['name']
        age = int(request.form['age'])
        
        db.update_user_by_id(user_id, name, age)
        return redirect('/')
        
    # users라는 저 변수를 뒤져서, user_id를 찾아서, 수정한다...
    return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True, port=5050)