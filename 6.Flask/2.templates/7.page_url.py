from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'id': i, 'name': f'User{i}', 'age' :20 + i, 'phone' : f'010-0000-{str(i).zfill(4)}' } for i in range(1,100)
]
# http://localhost:5050/?pages=1
@app.route('/')
def users():
    page = None
    return render_template('user.html' , users= users , page = page)

if __name__ == '__main__':
    app.run(debug=True, port=5050)