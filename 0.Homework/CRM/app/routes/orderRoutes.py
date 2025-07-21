from flask import Flask, render_template, Blueprint, jsonify, request
from app import db
import app.services.orderService as orderService


order_bp = Blueprint('orders', __name__ , url_prefix= '/orders')

@order_bp.route('/')
def render_order():
    return render_template('order.html')



@order_bp.route('/api/get-order')
def api_get_orders():
    print('#### order_list_api() 호출')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page',10))
    pagination = orderService.get_orders(db.session,page, per_page)
    orders = pagination.items
    
    result = {
        'orders' : [i.to_dict() for i in orders],
        'total' : pagination.total,
        'page' : pagination.page,
        'per_page' : pagination.per_page,
        'pages' : pagination.pages
    }
    
    return jsonify(result)


