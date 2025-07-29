from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

# create_app()은 함수 안에서 flask앱을 만들고 설정 config, blueprint 등록 db연결등을처리한다.
def create_app():
    app = Flask(__name__)
    app.config.from_object("config") 
    
    db.init_app(app)
   
    from app.routes.userRoutes import user_bp
    app.register_blueprint(user_bp)
    
    from app.routes.storeRoutes import store_bp
    app.register_blueprint(store_bp)
    
    from app.routes.orderItemRoutes import orderItem_bp
    app.register_blueprint(orderItem_bp)
    
    from app.routes.itemRoutes import item_bp
    app.register_blueprint(item_bp)
    
    from app.routes.orderRoutes import order_bp
    app.register_blueprint(order_bp)
    
    from app.routes.homeRoutes import home_bp
    app.register_blueprint(home_bp)
    
    
    return app