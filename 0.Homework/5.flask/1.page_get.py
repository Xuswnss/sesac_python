from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'id': i, 'name': f'User{i}', 'age' :20 + i, 'phone' : f'010-0000-{str(i).zfill(4)}' } for i in range(1,100)
]
# http://localhost:5050/?pages=1
@app.route('/')
def users_list():
    page = int(request.args.get('page',1)) #default = 1
    per_page= 10
    # if page=3 
    # start_page = 2 * 10 = 20 -> users[20]부터 시작
    start_page = (page - 1) * per_page
    end_page = start_page + per_page # 시작 위치 + 보여줄 개수
    # if page = 1 -> users[0:10]
    
    user_page = users[start_page : end_page]
    
    total_page = (len(users) + per_page - 1) // per_page 
    return render_template('user.html' , users= user_page , page = page, total_pages =total_page)

if __name__ == '__main__':
    app.run(debug=True, port=5050)