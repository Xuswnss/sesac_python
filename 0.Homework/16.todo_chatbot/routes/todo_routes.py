from flask import Blueprint, request, jsonify
from services import todo_service as svc
# from services.todo_service import get_all, add_todo, modify_todo

todo_bp = Blueprint('todo', __name__)


# READ = todo 리스트 가져오기
@todo_bp.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify(svc.get_all())

# CREATE = todo 리스트 생성하기
@todo_bp.route('/api/todo', methods=['POST'])
def add_todo():
    # 1. 입력값 가져온다
    data = request.get_json()
    task = data.get('text')
    print('할일: ', task)
    # 2. 입력값 프로세싱 및 저장
    svc.add(task)
    # 3. 결과 반납
    return jsonify({'success': '성공적으로 추가됨'})

# UPDATE = todo 리스트 done/undone (toggle) 처리
@todo_bp.route('/api/todo/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    result = svc.toggle(todo_id)
    print('toggle todo : ', result)
    if result:
        return jsonify({'success': f'수정 완료 (ID: {todo_id}) '})
      
    return jsonify({'error': f'해당 항목이 없음 (ID: {todo_id}) '}), 404

# DELETE = todo 아이템 삭제하기
@todo_bp.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    result = svc.delete(todo_id)    
    print('delete result : ', result)    
    if result:
        return jsonify({'success': f'삭제 완료 (ID: {todo_id}) '})

    return jsonify({'error': f'해당 항목이 없음 (ID: {todo_id}) '}), 404