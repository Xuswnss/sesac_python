from flask import Blueprint, request, jsonify
from services import chat_service as chatbot

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/api/chat', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    question = data.get('userInput')
    
    result = chatbot.handle_chat(question)
    
    return jsonify({'chatbot': f'[BOT] {result}'})