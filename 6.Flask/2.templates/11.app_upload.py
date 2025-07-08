from flask import Flask, request, render_template
import os 

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = ['png', 'jpg', 'jepg', 'gif']

os.makedirs(UPLOAD_FOLDER, exist_ok= True ) # 폴더 없으면 폴더 만들어주기
@app.route('/')
def index():
    return render_template('upload.html')

def allowed_file(filename):
    #파일명에 .있는지 확인
    if '.' not in filename:
        return False
    #확장자 파트를 오른쪽 부터 읽어서 확인
    ext =filename.rsplit('.' , 1)[1].lower()
    #확장자가 우리의 허용목록에 있는지 확인
    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        return False
    
def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

# allowed_file == allowed_file_pythonic
@app.route('/upload', methods=['post'])
def upload_file():
    # print(request.form) E이전에 받아온 건 파일 명 만을 받아옴
    print(request.files) # 실제로 파일 내용까지 FileStorage라는 객체형태로 파일 내용까지 받아옴.
    file = request.files['file']
    if file.filename == '':
        return '파일 이름이 올바르지 않습니다.'
    
    if allowed_file_pythonic(file.filename):
            # file store
        filepath = os.path.join('./', UPLOAD_FOLDER , file.filename)
        file.save(filepath)
        return '파일 업로드에 성공'
    else:
        '허용되지 않는 파일이다.'
        
    if 'file' not in request.files:
        return '파일이 올바르게 전송되지 않습니다.'
    print('################ file :', file)
    return '파일을 받았습니다💩'

   

if __name__ == '__main__':
    app.run(debug=True, port=5050)