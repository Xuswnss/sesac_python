from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

IMG_FOLDER = os.path.join(app.root_path,'static', 'img')  # 'join' -> 'img'로 수정
UPLOAD_FOLDER = 'uploads'


# 글로벌 변수
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

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        # pythonic하게 한줄로...
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append({
                'filename' : item['filename'],
                'url': image_url,
                'keywords': item['keywords']
            })
            print('######### result : ', results)
            
    return jsonify(results)

@app.route('/admin')
def admin():
    return render_template('admin.html', images=images)

@app.route('/images')
def get_images():
    return jsonify(images)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('inputFile')
    keywords = request.form.get('keywords')
    print(keywords)
    
    if file:
        filename = file.filename
        filepath = os.path.join(ROOT_PATH,'static', 'img', filename)
        print('filepate : ', filepath)
        file.save(filepath)
        images.append({'filename': filename, "keywords": keywords.lower().split(',')})
    
    return jsonify(images)



@app.route('/update/<filename>', methods=['POST'])
def update_keywords(filename):
    new_keywords = request.form.get('keywords')
    for i in images:
        if i["filename"] == filename:
            i["keywords"] = [word.strip() for word in new_keywords.lower().split(',') if len(word.strip())]
            break
        
    return jsonify(images)


@app.route('/delete/<filename>')
def delete_image(filename):
    print('삭제할파일: ', filename)
    global images   # 우리의 글로벌 변수를 읽어갈때는 문제가 없음. 단, 수정할꺼면 global로 설정해줘야지만, 해당 변수안의 내용을 수정할 수 있음.
    
    # 삭제할거 빼고 나머지를 다시 채움
    images = [
        img 
        for img in images 
        if img["filename"] != filename
    ]
    
    # 실제로 이미지를 지울거면??
    filepath = os.path.join('static', 'img', filename)
    if os.path.exists(filepath):
        # os.remove(filepath)
        print(f'{filepath} 지웠다고 치자...')
    
    return jsonify(images)


if __name__ == "__main__":
    app.run(debug=True, port=5051)
