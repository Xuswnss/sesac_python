from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello!'


@app.route('/search')
def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1)
    print('query :', query ,'page :', page)
    result = f'query : {query} , page : {page}'
    return result
    

if __name__ == '__main__':
    app.run(debug=True, port = 5050)