from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # CORS 설정으로 프론트엔드에서 API 호출 가능

# 전역 변수로 대화 히스토리 관리 (실제 프로덕션에서는 세션/DB 사용 권장)
chat_histories = {}

# OpenAI API 키 설정
openai_api_key = os.getenv('OPEN_API_KEY')
if not openai_api_key:
    print("Warning: OPENAI_API_KEY not found in environment variables")

client = openai.OpenAI(api_key=openai_api_key) if openai_api_key else None

def ask_chatgpt(user_input, session_id='default'):
    """원본 코드 기반의 ChatGPT 호출 함수"""
    if not client:
        return "OpenAI API 키가 설정되지 않았습니다."
    
    # 세션별 히스토리 관리
    if session_id not in chat_histories:
        chat_histories[session_id] = []
    
    history = chat_histories[session_id]
    
    # 사용자 메시지 히스토리에 추가
    gpt_question = {'role': 'user', 'content': user_input}
    history.append(gpt_question)
    
    print(f'########  실제로 우리가 gpt에게 던지는 메세지 (Session: {session_id})')
    print('-------- 질문 시작 ---------')
    for msg in history:
        print(f"{msg['role']}: {msg['content']}")
    print('---------여기 까지 -----------')
    
    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=history,
            max_tokens=500,
            temperature=0.7
        )
        
        gpt_response = {
            'role': 'assistant', 
            'content': response.choices[0].message.content
        }
        history.append(gpt_response)
        
        return gpt_response['content']
    
    except Exception as e:
        print(f"OpenAI API 오류: {str(e)}")
        return f"죄송합니다. 오류가 발생했습니다: {str(e)}"

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """채팅 API 엔드포인트"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': '메시지가 필요합니다.'}), 400
        
        user_message = data['message'].strip()
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({'error': '빈 메시지는 보낼 수 없습니다.'}), 400
        
        # ChatGPT 응답 생성
        bot_response = ask_chatgpt(user_message, session_id)
        
        return jsonify({
            'success': True,
            'response': bot_response,
            'session_id': session_id
        })
    
    except Exception as e:
        print(f"채팅 처리 오류: {str(e)}")
        return jsonify({'error': f'서버 오류가 발생했습니다: {str(e)}'}), 500

@app.route('/api/clear_history', methods=['POST'])
def clear_history():
    """대화 히스토리 초기화"""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default') if data else 'default'
        
        if session_id in chat_histories:
            chat_histories[session_id] = []
        
        return jsonify({
            'success': True,
            'message': '대화 히스토리가 초기화되었습니다.'
        })
    
    except Exception as e:
        return jsonify({'error': f'히스토리 초기화 오류: {str(e)}'}), 500

@app.route('/api/status', methods=['GET'])
def status():
    """서버 상태 확인"""
    return jsonify({
        'status': 'running',
        'openai_configured': client is not None,
        'active_sessions': len(chat_histories)
    })

if __name__ == '__main__':
    print("Flask 챗봇 서버 시작...")
    print(f"OpenAI API 설정 상태: {'✓' if client else '✗'}")
    app.run(debug=True, host='0.0.0.0', port=5000)