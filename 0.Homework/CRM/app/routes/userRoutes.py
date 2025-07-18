from flask import Flask, render_template, Blueprint, jsonify, request
import app.services.userService as userService
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
    # print(f'### input page: {page}, per_page : {per_page}')
    pagination = userService.user_paginated(db.session, page, per_page)
    # print(pagination.items)
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


@user_bp.route('/api/search' , methods= ['GET'])
def user_search():
    print('### userSearch() 호출')
    #get은  args.get으로 가져오고
    # post는 form.get
    name = request.args.get('name',None) 
    gender = request.args.get('gender', None)

    if not name or not gender:
        return jsonify({
            'error' : '이름과 성별을 입력해세요',
            'status' : 400
        })
    name = name.lower()
    result = userService.search_user(db.session,name,gender)
    return  jsonify([u.to_dict() for u in result])

@user_bp.route('/user-detail/<string:user_id>', methods = ['GET'])
def get_user_detail(user_id):
    print('##### input User Id : ', user_id)
    return render_template('user-detail.html', user_id = user_id)


@user_bp.route('/user-detail/api/get-user/<string:user_id>')
def api_get_user(user_id):
    user = userService.get_user_by_id(db.session,user_id)
    print('#### get_user_by_id : ', user)
    return jsonify(user.to_dict())


@user_bp.route('/user-detail/api/order-list/<string:user_id>')
def api_get_user_orders(user_id):
    user = userService.get_orderList_by_userId(db.session,user_id)
    print(user)
    return jsonify([u.to_dict() for u in user])


