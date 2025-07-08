from flask import Flask, render_template

app = Flask(__name__)
users = [
    {'name' : 'Alice', 'age': 22, 'mobile' : '010-1234-1234'},
    {'name' : 'Bob', 'age': 23, 'mobile' : '010-4321-1234'},
    {'name' : 'Charlie', 'age': 24, 'mobile' : '010-1234-4321'},
    {'name' : 'Xuswns', 'age': 25, 'mobile' : '010-1111-1234'},
    
]


@app.route('/')
def home():
    return render_template('index3.html', users = users)

if __name__ == '__main__':
    app.run(debug=True, port=5050)