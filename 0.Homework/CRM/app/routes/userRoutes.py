from flask import Flask, render_template, Blueprint, jsonify, request
import app.services.userService as userService
from app.models.users import User
from app import db

# command + j  -> 터미널

user_bp = Blueprint('users', __name__ , url_prefix= '/users')


@user_bp.route('/', methods=['GET'])
def user_page():
    return render_template('user.html')

@user_bp.route('/api', methods = ['GET'])
def user_list_api():
    print('#### userAPI 호출')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    print(f'### input page: {page}, per_page : {per_page}')
    pagination = userService.user_paginated(db.session, page, per_page)
    print(pagination.items)
    users = pagination.items
    # users를 순회한 객체 u를 to_dict()메서드 처리해서 리스트[]로 반환
    result = {
        "users": [u.to_dict() for u in users],
        "total": pagination.total,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "pages": pagination.pages
    }
    # print( result in range(1,10))
    return jsonify(result)



