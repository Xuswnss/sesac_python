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
    gpt_systemprompt = {'role':'system', 'content': '당신은 사용자를 도와 입력받은 문장을 영어로 번역해주는 어시스턴스입니다.'}
    
    if len(history) == 0:
        history.append(gpt_systemprompt)
    print('####### history : ', history)

    gpt_question = {'role':'user', 'content': user_input}
    history.append(gpt_question)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history,
        temperature=1.0
    )

    chatgpt_response = response.choices[0].message.content
    history.append({'role': 'assistant', 'content': chatgpt_response})

    # history가 너무 길어지면 오래된 질문/응답 쌍 삭제 (system 메시지는 유지)
    while len(history) > 11:
        del history[1:3]  # system 다음부터 두 개씩 제거

    return chatgpt_response


if __name__ == "__main__":
    app.run(debug=True)