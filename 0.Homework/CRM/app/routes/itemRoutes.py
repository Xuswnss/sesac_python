from flask import Flask, render_template, Blueprint, jsonify, request
from app import db
import app.services.itemService as itemService


item_bp = Blueprint('items', __name__ , url_prefix= '/items')

@item_bp.route('/')
def render_item():
    return render_template('item.html')


@item_bp.route('/api/get-item')
def api_get_items():
    print('#### orderItems_list_api() 호출')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page',10))
    pagination = itemService.get_items(db.session,page, per_page)
    items = pagination.items
    
    result = {
        'items' : [i.to_dict() for i in items],
        'total' : pagination.total,
        'page' : pagination.page,
        'per_page' : pagination.per_page,
        'pages' : pagination.pages
    }
    
    return jsonify(result)

@item_bp.route('/item-detail/<string:item_id>')
def render_item_detail(item_id):
    return render_template('item-detail.html',item_id = item_id)

@item_bp.route('/api/get-item-detail/<string:item_id>')
def api_get_item_detail(item_id):
    result = itemService.get_item_by_id(db.session, item_id)
    result = [r.to_dict() for r in result]
    return jsonify(result)

@item_bp.route('/api/get-months-sales-data/<string:item_id>')
def api_get_months_sales_data(item_id):
    result =  itemService.get_monthly_sales(db.session,item_id)
    return jsonify(result)
    
    