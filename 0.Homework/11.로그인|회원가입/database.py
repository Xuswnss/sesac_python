import bcrypt
import json
import os

USER_FILE = 'users.json'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def save_users(users):
    with open(USER_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def load_users():
    if not os.path.exists(USER_FILE):
        return []

    with open(USER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_user(name, user_id, password, email):
    users = load_users()
    if any(u['id'] == user_id for u in users):
        return False
    new_user = {
        'name': name,
        'id': user_id,
        'password': hash_password(password),
        'email': email
    }
    users.append(new_user)
    save_users(users)
    return True

users = load_users()
