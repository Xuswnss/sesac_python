from flask import Flask, render_template
from user.user_routes import user_blueprint
from admin.admin_routes import admin_blueprint
from product.product_routes import product_blueprint

app = Flask(__name__,)

app.register_blueprint(user_blueprint, url_prefix = "/user")
app.register_blueprint(admin_blueprint, url_prefix = "/admin")
app.register_blueprint(product_blueprint, url_prefix = "/product")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)