from flask import Blueprint, render_template

product_blueprint = Blueprint('product', __name__, template_folder='../templates/product')

@product_blueprint.route('/')
def product_page():
    return render_template('product.html')