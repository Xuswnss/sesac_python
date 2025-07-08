from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/' , methods = ['get', 'post'])
def index():
    return render_template('form.html')

@app.route('/submit', methods = ['post'])
def submit():
    # name =request.args.get('name') #get parameter(arguments) 를 받는 방식임.
    name = request.form.get('name')
    age = request.form.get('age')
    print('입력된 글자 : ' , name, age)

    return f'<h1>POST에 응답 ; 입력된 글자 : {name} : {age}</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5050)