from flask import Flask, request, render_template, redirect, url_for
import os 
#url_for:함수가 가진 url 을 불러오는 함수
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif']

os.makedirs(UPLOAD_FOLDER, exist_ok= True ) # 폴더 없으면 폴더 만들어주기
@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('upload.html', file_list = file_list, files = files)

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
def get_file_size(file):
    pos = file.stream.tell() # 이전 작업을 고려하여 현재 fd위치를 저장
    file.stream.seek(0, os.SEEK_END) # 끝으로 가라
    size = file.tell() # 너의 현재 위치를 기반으로 크기를 알려줘야
    file.stream.seek(pos) # 원래 위치로 돌아가라
    file.seek(0) # 다시 처음위치로 이동시켜줌 
    return size
    
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
    
    file_size = get_file_size(file)
    max_size = 1 * 1024 * 1024
    if file_size > max_size:
        return '파일사이즈 너무 그다..'
    
    
    if allowed_file_pythonic(file.filename):
            # file store
        filepath = os.path.join('./', UPLOAD_FOLDER , file.filename)
        file.save(filepath)
        file_list.append(file.filename)
        print(file_list)
        return redirect(url_for('index'))
    else:
        '허용되지 않는 파일이다.'
           
        
    if 'file' not in request.files:
        return '파일이 올바르게 전송되지 않습니다.'
    print('################ file :', file)
    return '파일을 받았습니다💩'

@app.route('/delete/<filename>' , methods= ['get', 'post'])
def delete_list(filename):
    filepath =os.path.join('./','uploads', filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return redirect(url_for('index'))
    else: 
        return '해당 파일은 존재하지 않습니다.'


   

if __name__ == '__main__':
    app.run(debug=True, port=5050)
    
#미션1 파일목록을 보여준다(메인 라우트에서 uploads폴더 안의 파일명을 보여준다)
#미션2 각각의 파일 옆에 삭제 버튼 추가
# 삭제