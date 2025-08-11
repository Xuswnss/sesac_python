# 내 메모 리스트 담을곳

# 아래 변수들은 내부변수임.. 남들이 가져다 쓰지 마시오.
_todos = []
_next_id = 1

def get_all():
    return _todos

def get_all_to_string():
    # return [{"ID": t["id"], "할일": t["task"], "완료": t["done"]} for t in _todos]
    return "\n".join([
        f"{t['id']}. {t['task']} [{'완료' if t['done'] else '미완료'}]" 
        for t in _todos])

def add(task):
    global _next_id
    
    new_todo = {'id': _next_id, 'task': task, 'done': False}
    _todos.append(new_todo)
    _next_id += 1
    return new_todo

def toggle(todo_id):
    for todo in _todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            return todo  # 뭘 반납할지는 내가 정하면 됨

    return None
      

def delete(todo_id):
    for todo in _todos:
        if todo['id'] == todo_id:
            _todos.remove(todo)
            return todo  # 지웠을때, 지운 아이템을 반환
    return None