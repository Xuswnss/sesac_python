from flask import Flask , jsonify, url_for, render_template, request
import random

app = Flask(__name__)

images = [
    {
        'filename': 'dog1.jpg',
        'keywords': ['dog', 'animal', 'cute'],
    },
    {
        'filename': 'dog2.jpg',
        'keywords': ['dog', 'pet', 'cool'],
    },
    {
        'filename': 'dog3.jpg',
        'keywords': ['dog', 'zoo', 'lovely'],
    },
    {
        'filename': 'dog4.jpg',
        'keywords': ['dog', 'pet', 'cute'],
    },
]

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/search' )
def search():
    query = request.args.get('q','').lower()
    results = []
    for item in images:
    #    found = False
    #    for keyword in item['keywords']:
    #        if query in keyword:
    #            found = True
    #    if found:
    #         image_url = url_for('static', filename=f'img/{item['filename']}')
    #         results.append(image_url)
            
        if any(query in keyword for keyword in item['keywords']):
            image_url = url_for('static', filename=f'img/{item['filename']}')
            results.append(image_url)
    # return jsonify({'url' : results})
    return render_template('result.html', query = query, results = results)
            
        



if __name__ == '__main__':
    app.run(debug=True, port=5050)