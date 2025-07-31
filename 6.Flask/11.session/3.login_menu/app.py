from flask import Flask, render_template, redirect,request,url_for, session

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name' : 'user1' , 'id' : 'user1' , 'password' : 'password1'},
    {'name' : 'user2' , 'id' : 'user2' , 'password' : 'password2'},
    {'name' : 'user3' , 'id' : 'user3' , 'password' : 'password3'},
]

items = [
    {'id' : 'prod-001', 'name' : '사과' , 'price' : 1000},
    {'id' : 'prod-002', 'name' : '딸기' , 'price' : 2000},
    {'id' : 'prod-003', 'name' : '수박' , 'price' : 3000},
    {'id' : 'prod-004', 'name' : '레몬' , 'price' : 3000},
    
]

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        print(f'######### input ID :{id} , input pw {password}')
        user = next((u for u in users if u['id'] == id and u['password'] == password), None)
        if user:
            print('######## user 가 존재합니다')
            session['user'] = user
         
            return redirect(url_for('user'))
        else:
            error = '로그인 실패했습니다. 아이디 또는 비밀번호를 확인해주세요.'
            return render_template('login.html' , error = error)
        
    return render_template('login.html')
    
@app.route('/user')
def user():
    
    user = session.get('user')
    if user:
        return render_template('user.html', user = user)
    else:
        return redirect(url_for('login'))

@app.route('/product')
def product():
    user = session.get('user')
    if user == False or user == None :
        error = '로그인 해주세요'
        return render_template('product.html', error = error)
    return render_template('product.html', user = user, items=items)

@app.route('/logout')
def logout():
    session.pop('user', None) #user가 없ㅇ르 때 KeyError가 날 수 있으 그래서 없을 때 None을 반환한다.
    return redirect('login')

@app.route('/add-to-chart')
def add_to_chart(): 
    user = session.get('user')
    if not user:
        return render_template('product.html', error = '로그인 후 사용가능합니다.')
    item_id = request.args.get('item_id')
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart'] #빈 카트를 가져오거나, 이전에 담는 카트일 것이다. 
    
    if item_id in cart:
        cart[item_id] += 1
    else:
        cart[item_id] = 1
    session['cart'] = cart
    
    print('#### cart : ' , session.get('cart'))
    return redirect('/product')
    
@app.route('/cart')
def view_cart():
    user = session.get('user')
    if not user:
        return render_template("cart.html", user=None, items=items, error="로그인 후 사용할 수 있습니다.")
    
    cart = session.get("cart", {}) # 카트가 없으면 {} 빈 dict를 반환하겠다.
    
    cart_items = []
    for item_id, item_qty in cart.items():
        item = next((i for i in items if i['id'] == item_id), None)
        if item:
            a_item = item.copy()
            a_item["qty"] = item_qty
            cart_items.append(a_item)
    
    return render_template("cart.html", user=user, cart=cart_items)
    
   
    
if __name__ == '__main__':
    app.run(debug=True)