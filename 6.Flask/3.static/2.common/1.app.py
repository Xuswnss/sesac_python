from flask import Flask, render_template

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '/', 'static'))
print('BASE_DIR + STATIC_DIR : ', BASE_DIR + STATIC_DIR)

app = Flask(__name__, static_folder=STATIC_DIR)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port= 5050)
