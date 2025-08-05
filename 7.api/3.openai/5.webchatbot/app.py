from flask import Flask, request, send_from_directory, jsonify

from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)

client = OpenAI()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(data)
    # time.sleep(3)
    userInput = data['userInput']
    chatbot_response = ask_chatgpt(userInput)
    return jsonify({"response": f"{chatbot_response}"})

history = [] # 이전 대화 내용을 저장할 공간 - 지금은 데모용.. 실제로는 사용자별로 분리해야 대화 내용이 꼬이지 않음.

def ask_chatgpt(user_input):
    # history 에 저장한다
    history.append({'role':'user', 'content': user_input})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # gpt-4o-mini
        messages = history,
        temperature=1.0   # 0에 가까울수록 창의성을 떨어짐
    )
    
    chatgpt_response = response.choices[0].message.content
    
    # history 에 저장한다
    history.append({'role':'assistant', 'content': chatgpt_response})
    
    if len(history) > 10:
        history.pop(0)  # 가장 오래된거 하나 삭제
        history.pop(0)  # 가장 오래된거 하나더 삭제
        
    print(history)
    print('대화내용길이: ', len(history))
    
    return chatgpt_response

if __name__ == "__main__":
    app.run(debug=True)