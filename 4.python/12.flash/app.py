from flask import Flask,render_template,session,request, redirect, url_for, flash

app = Flask(__name__) 
app.secret_key = 'sesac'
users = [
    {'name' : 'user1', 'id' :'user1', 'password' : 'user1' }
]
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        user =request.form.get('id')
        password = request.form.get('password')
        user = next((u for u in users if u[id] == user and u['password'] == password),None)
        if user:
            session['user'] = user
            return redirect(url_for('user'))
        return redirect(url_for('home'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return redirect(url_for('home'))
    
@app.route('/user')
def user():
    user = session.get('user')
    render_template('user.html', user = user)    


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)