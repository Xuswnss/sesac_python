from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join(app.root_path,'static', 'img')  # 'join' -> 'img'로 수정
UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif']


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
    query = request.args.get('q', '').lower().strip()
    print('####### input text :', query)
    results = []
    
    for item in images:
        if any(query in keyword for keyword in item['keywords']):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            filename = item['filename']
            results.append({
                'url': image_url,
                'filename': filename
            })
    
    return render_template('result.html', query=query, results=results)

@app.route('/admin', methods=['GET', 'POST'])  # POST 메서드 추가
def admin():
    keywords = request.form.get('key') if request.method == 'POST' else None
    return render_template('admin.html', images=images, keywords=keywords)

def get_file_size(file):
    pos = file.stream.tell()  # 이전 작업을 고려하여 현재 fd위치를 저장
    file.stream.seek(0, os.SEEK_END)  # 끝으로 가라
    size = file.stream.tell()  # file.tell() -> file.stream.tell()로 수정
    file.stream.seek(pos)  # 원래 위치로 돌아가라
    file.seek(0)  # 다시 처음위치로 이동시켜줌
    
    return size

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/uploads', methods=['POST'])
def uploads():
    # 파일 존재 확인을 먼저 수행
    
    if 'file' not in request.files:
        return '파일이 올바르게 전송되지 않습니다.'
    
    file = request.files['file']
    keywords = request.form.get('keywords', '').lower().split(',')
    error = ''
    
    print('######## upload', request.files)
    
    if file.filename == '':
        error = '파일 이름이 올바르지 않습니다'
        return error
    
    if not allowed_file_pythonic(file.filename):
        error = '허용되지 않는 파일 형식입니다'
        return error
    
    file_size = get_file_size(file)
    max_size = 1 * 1024 * 1024  # 1MB
    if file_size > max_size:
        error = '파일 사이즈가 너무 큽니다'
        return error
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # 폴더 없으면 폴더 만들어주기
    filepath = os.path.join('/', IMG_FOLDER, file.filename)
    print('filepath : ', filepath)
    file.save(filepath)
    
    print('################ file :', file)
    
    images.append({
        'filename': file.filename,
        'keywords': [kw.strip() for kw in keywords if kw.strip()]  # 빈 값 제거
    })
    
    print('users : ', images)
    return '파일을 받았습니다💩'

@app.route('/delete', methods=['POST', 'GET'])  
def delete():
  
    return '삭제 완료되었습니다..'

if __name__ == '__main__':
    app.run(debug=True, port=5051)