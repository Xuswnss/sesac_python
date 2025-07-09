from flask import Flask , jsonify, url_for, render_template, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 전체 라우트에 CORS 허용


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
    return send_from_directory(app.static_folder, "index.html")

@app.route('/api/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    
    return jsonify({"url": results})  # 순수 BE개발자는 여기까지...

if __name__ == "__main__":
    app.run(debug=True, port=5050)
    