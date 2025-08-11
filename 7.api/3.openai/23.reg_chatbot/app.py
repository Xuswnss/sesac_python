from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from vectoreStore import initialize_vector_db, create_vector_db

load_dotenv()
DATA_DIR = 'DATA'
app = Flask(__name__, static_url_path='')
data_path = os.path.abspath("3.openai/23.reg_chatbot")
path  = os.path.join(data_path)
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods = ['POST'])
def upload_file():
    global path
    if 'file' not in request.files:
        
        return jsonify({'message' : '파일이 없습니다'})
    
    file = request.files['file']
    print('###### file' , file.filename)
    if file:
        file_path = os.path.join(data_path ,DATA_DIR, file.filename)
        create = create_vector_db(path)
        print(f'\n\n\n create file {create}')
        file.save(file_path)
        return jsonify({'message' : 'upload성공'})
    
        
@app.route('/ask', methods = ['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question', '')
    # gpt_answer = answer_question(question)
    # print(f' \n\n\n\########## gpt_answer : {gpt_answer}')
    return jsonify({'message' : f'질문을 받았습니다. ({question})'})
    
    

if __name__ == '__main__':
    initialize_vector_db()
    app.run(debug=True)