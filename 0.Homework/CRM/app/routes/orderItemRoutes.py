from flask import Flask, render_template, Blueprint, jsonify, request
from app import db
import app.services.orderItemService as orderItemService
import app.services.orderService as orderService


orderItem_bp = Blueprint('orderitems', __name__ , url_prefix= '/orderitems')

@orderItem_bp.route('/')
def render_orderItem():
    return render_template('orderitem.html')


@orderItem_bp.route('/api/get-orderitems')
def api_get_orderitems():
    print('#### orderItems_list_api() 호출')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page',10))
    pagination = orderItemService.get_orderItems(db.session,page, per_page)
    stores = pagination.items
    
    result = {
        'orderitems' : [s.to_dict() for s in stores],
        'total' : pagination.total,
        'page' : pagination.page,
        'per_page' : pagination.per_page,
        'pages' : pagination.pages
    }
    
    return jsonify(result)

@orderItem_bp.route('/orderItem-detail/<string:order_id>')
def render_order_detail(order_id):
    print('### input OrderId : ', order_id)
    return render_template('orderItem-detail.html', order_id = order_id)

@orderItem_bp.route('/api/get-order-item/<string:order_id>')
def get_order_detail(order_id):
    result = orderItemService.get_orderItems_detail_by_orderId(db.session, order_id)
    
    response = [
        {
        **row[0].to_dict(),
        'item_name': row[1]
        }
    for row in result
]

    return jsonify(response)


    
    