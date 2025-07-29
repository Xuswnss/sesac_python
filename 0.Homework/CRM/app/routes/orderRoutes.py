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
    result = orderService.get_orders(db.session,page, per_page)
    orders = result.items
    
    result = {
        'orders' : [i.to_dict() for i in orders],
        'total' : result.total,
        'page' : result.page,
        'per_page' : result.per_page,
        'pages' : result.pages
    }
    
    return jsonify(result)


@order_bp.route('/order-detail/<string:order_id>')
def render_order_detail(order_id):
    return render_template('order-detail.html', order_id = order_id)

@order_bp.route('/api/get-order-detail/<string:order_id>')
def api_get_order_detail(order_id):
    result = orderService.get_order_by_orderId(db.session, order_id)
    result = [r.to_dict() for r in result]
    return jsonify(result)
    


