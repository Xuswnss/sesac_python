from flask import Flask , jsonify, url_for
import random

app = Flask(__name__)

dog_images=[
    'dog1.jpg',
    'dog2.jpg',
    'dog3.jpg',
    'dog4.jpg',
]
@app.route('/')
@app.route('/random-dog')
def random_dog():
    random_url = random.choice(dog_images)
    image_url = url_for('static', filename= f'img/{random_url}', _external = True)
    return jsonify({'url':image_url})

if __name__ == '__main__':
    app.run(debug=True, port=5050)