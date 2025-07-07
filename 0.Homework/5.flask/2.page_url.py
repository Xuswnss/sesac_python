from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'id': i, 'name': f'User{i}', 'age' :20 + i, 'phone' : f'010-0000-{str(i).zfill(4)}' } for i in range(1,100)
]
# http://localhost:5050/pages/1
@app.route('/')
@app.route('/page/<int:page>')
def users_list(page =1 ):
    page = int(request.args.get('page',1)) #default = 1
    per_page= 10
    start_page = (page - 1) * per_page
    end_page = start_page + per_page 
    user_page = users[start_page : end_page]
    total_page = (len(users) + per_page - 1) // per_page 
    return render_template('user_url.html' , users= user_page , page = page, total_pages =total_page)

if __name__ == '__main__':
    app.run(debug=True, port=5050)