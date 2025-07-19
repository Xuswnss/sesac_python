from flask import Flask, render_template, Blueprint, jsonify, request
from app import db
import app.services.orderItemService as orderItemService


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
    
    