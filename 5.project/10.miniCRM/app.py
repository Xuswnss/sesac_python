from flask import Flask, render_template,request
import database as db

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    search_value = request.form.get('name','').strip()
    if search_value:
        stores = db.search_stores(search_value)
    else:
        stores = db.get_stores()
    # print('##### stores', stores.name)
    
    return render_template('index.html', stores = stores , search = search_value)



if __name__ == '__main__':
    app.run(debug=True, port=5050)