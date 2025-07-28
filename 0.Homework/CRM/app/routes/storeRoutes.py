from flask import Flask, render_template, Blueprint, jsonify, request
import app.services.storeService as storeService
from app import db

# command + j  -> 터미널

store_bp = Blueprint('stores', __name__ , url_prefix= '/stores')

@store_bp.route('/')
def render_store_page():
    return render_template('store.html')


@store_bp.route('/api')
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

@store_bp.route('/store-detail/<string:store_id>')
def render_store_detail_page(store_id):
    return render_template('store-detail.html', store_id = store_id)


@store_bp.route('/api/get-store-detail/<string:store_id>')
def api_get_store_detail(store_id):
    result = storeService.get_store_by_id(db.session, store_id)
    
    result = [r.to_dict() for r in result]
    return jsonify(result)

@store_bp.route('/api/get-store-month-sales/<string:store_id>')
def api_get_store_month_sales(store_id):
    month = request.args.get('month')
    print('######## input month : ', month)

    result = storeService.get_store_month_sales(db.session, store_id, month)
    return jsonify(result)

@store_bp.route('/api/get-customer-list/<string:store_id>')
def api_get_customer(store_id):
    month = request.args.get("month")  # 쿼리 파라미터에서 month 받기

    if month:
        print(f"🟡 month 있음: {month}")
        result = storeService.list_customer_by_month(db.session, store_id, month)
    else:
        print("⚪ month 없음 → 전체 리스트")
        result = storeService.list_all_customer(db.session, store_id)

    return jsonify(result)

 

