from flask import Flask, render_template, Blueprint, jsonify, request
import app.services.storeService as storeService
from app import db

# command + j  -> 터미널

store_bp = Blueprint('stores', __name__ , url_prefix= '/stores')

@store_bp.route('/', methods = ['GET'])
def store_page():
    return render_template('store.html')

@store_bp.route('/api', methods = ['GET'])
def store_list_api():
    print('#### store_list_api() 호출')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page',10))
    pagination = storeService.store_paginated(db.session,page, per_page)
    stores = pagination.items
    
    result = {
        'stores' : [s.to_dict() for s in stores],
        'total' : pagination.total,
        'page' : pagination.page,
        'per_page' : pagination.per_page,
        'pages' : pagination.pages
    }
    
    return jsonify(result)

