from flask import Flask, request, jsonify
from chat_app import chat_bp


app = Flask(__name__, static_folder='public', static_url_path='')
app.register_blueprint(chat_bp)

todo = []
todo_id_counter = 1  # 고유 ID 부여용

@app.route('/')
def home():
    return app.send_static_file('index.html')


# [READ] 전체 todo 목록 반환
@app.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify(todo)


# [CREATE] 새로운 todo 추가
@app.route('/api/todo', methods=['POST'])
def add_todo():
    global todo_id_counter

    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': '제목이 필요합니다.'}), 400

    new_todo = {
        'id': todo_id_counter,
        'title': data['title'],
        'done': False
    }
    todo.append(new_todo)
    todo_id_counter += 1

    return jsonify(new_todo), 201


# [UPDATE] 특정 todo의 상태 토글
@app.route('/api/todo/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    for item in todo:
        if item['id'] == todo_id:
            item['done'] = not item['done']
            return jsonify(item)
    return jsonify({'error': '해당 ID를 찾을 수 없습니다.'}), 404


# [DELETE] 특정 todo 삭제
@app.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo
    original_len = len(todo)
    todo = [item for item in todo if item['id'] != todo_id]

    if len(todo) == original_len:
        return jsonify({'error': '해당 ID를 찾을 수 없습니다.'}), 404
    return jsonify({'result': '삭제 완료'})


if __name__ == '__main__':
    app.run(debug=True)
