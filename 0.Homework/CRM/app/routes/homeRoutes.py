from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__, url_prefix="/")
# register
@home_bp.route("/")
def render_home():
    return render_template("home.html")

@home_bp.route('/register')
def render_register():
    return render_template('register.html')

@home_bp.route('/login/google')
def login_google():
    return 