from flask import Flask, render_template, request, redirect
import database as db

app =Flask(__name__)

@app.route('/')
def index():
    page_box = db.get_users()
    page = request.args.get('page',default=1,type=int )
    print('##### page : ', page)
    items_per_page = 10
    print('#### page box :', int(len(page_box)/ items_per_page) + 1)
    last_page = int(len(page_box) / items_per_page ) 
    users = db.get_users_per_page(page, items_per_page)
    return render_template('index.html', users = users, last_page = last_page)

if __name__ == '__main__':
    app.run(debug=True, port=5050)