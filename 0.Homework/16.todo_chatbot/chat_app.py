import os
from flask import Flask, request, jsonify, Blueprint
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

# OpenAI API 키 환경변수에서 자동 로드됨
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 도움이 되는 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# 간단한 람다 체인 구성
conversation = (
    RunnableLambda(lambda x: {
        "input": x["input"], 
        "chat_history": memory.chat_memory.messages
    }) |
    prompt |
    llm |
    RunnableLambda(lambda response: (
        memory.save_context({"input": response.additional_kwargs.get("input", "")}, {"output": response.content}),
        response.content
    )[1])  # 튜플의 두 번째 요소(response.content) 반환
)

chat_bp = Blueprint(
    'chat',
    __name__,
    url_prefix='/api/chat'
)

@chat_bp.route('/', methods=['POST'])
def chatbot():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': '유효하지 않은 JSON 데이터입니다.'}), 400
    
    user_input = data.get('userInput', '').strip()
    print('# userinput :',user_input)

    if not user_input:
        return jsonify({'error': '입력값이 없습니다.'}), 400

    try:
        
        response = conversation.invoke({"input": user_input})
        print('## response :',response)
        print(type(response), response)
        if isinstance(response, set):
            response = list(response)
        
        return jsonify({'chatbot': response})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': f'챗봇 응답 중 오류가 발생했습니다.{e}'}), 500