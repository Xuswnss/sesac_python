from flask import Flask, render_template, request, redirect


users = []
next_id = 1 # id자동증가를 위한 초깃값 설정
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    global next_id
    if request.method == "POST":
        #post 요청 처리 
        # name =request.form.get('name')
        name = request.form['name']
        age = int(request.form.get('age'))
        users.append({
            'id': next_id,
            'name': name,
            'age': age
        })
        next_id += 1
        return redirect('/')
    #get 요청 처리
    return render_template('index.html', users = users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    global users
    print('###### input ID : ', user_id)
    # users에서 user-id를 찾아서 지운다.
    for user in users:
        if user_id == user['id']:
            users.remove(user)
        print('현재 유저 : ' , users)
        
        return redirect('/')
    
# for i, user in enumerate(users):
#     ...enumerate() -> index값도 같이 가져옴
#     del users[i]
# users = [u for u in users if u['id'] != user_id ]
            

@app.route('/update/<int:user_id>', methods = ['GET', 'POST'])
def update_user(user_id):
    # new_username = request.form.get('name')
    # new_user_age = request.form.get('age')
    # if request.method == 'POST':
    #     for user in users:
    #         if user_id == user['id']:
    #             user['name'] = new_username
    #             user['age'] = new_user_age   
    #             break
    user = next(( u for u in users if u['id'] == user_id), None)
    if request.method == 'POST':
        if not user:
            return '사용자를 찾을 수 없습니다', 404
        user['name'] = request.form['name']
        user['age'] = request.form['age']
        return redirect('/')
    return render_template('update_user.html', user = user)


if __name__ == '__main__':
    app.run(debug=True, port=5050)