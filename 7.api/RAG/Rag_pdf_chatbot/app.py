from flask import Flask, request, jsonify
import os
from vectorsotre import initialize_vector_db, create_vector_db, delete_file_from_vstore
from chatbot import answer_question, initialize_llm

app = Flask(__name__, static_url_path="")
path = os.path.abspath("RAG/Rag_pdf_chatbot")
DATA_DIR = "/DATA"
PATH = os.path.join(path, 'DATA')

# Create DATA directory if it doesn't exist
if not os.path.exists(PATH):
    os.makedirs(PATH)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "파일이 없습니다."})
    
    file = request.files['file']
    if file:
        file_path = os.path.join(PATH, file.filename)
        file.save(file_path)
    
    # Add document to vector DB
    result = create_vector_db(file_path)
    if result:
        return jsonify({"message": "파일이 성공적으로 업로드 되었습니다."})        
    else:
         return jsonify({"message": "파일은 업로드 되었으나, DB가 정상적으로 생성되지 못했습니다."})    

@app.route('/ask', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question', '')
    
    answer = answer_question(question)
    
    return jsonify({"message": answer})

@app.route('/files')
def get_filelist():
    files = [f for f in os.listdir(PATH)
             if os.path.isfile(os.path.join(PATH, f))]
    return jsonify({"files": files})

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    # Delete from vector DB
    delete_file_from_vstore(filename)
    
    # Physically delete file
    path = os.path.join(PATH, filename)
    if os.path.exists(path):
        os.remove(path)
        
    return jsonify({"message": f"'{filename}' 을 삭제하였습니다."})

if __name__ == "__main__":
    initialize_vector_db()
    initialize_llm()
    app.run(debug=True)