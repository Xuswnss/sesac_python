from flask import Flask, request, jsonify
from routes.chat_routes import chatbot_bp
from routes.todo_routes import todo_bp


app = Flask(__name__, static_folder='public', static_url_path='')
app.register_blueprint(chatbot_bp)
app.register_blueprint(todo_bp)

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)