from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

app = Flask(__name__)

llm1 = OpenAI(temperature=1.3)
llm2 = ChatOpenAI(temperature=0.9)

@app.route('/api/name', methods=["POST"])
def generate_name():
    data = request.get_json()
    product = data.get("product", None)
    
    prompt = f"What is a good company name that makes {product}?"
    # 각자 프롬프트를 잘 만들어서, 언제나 한글 회사명으로 1개만 주어지게 한다.
    prompt = f"다음 상품을 만드는 창의 적인 회사 이름을 1개만 작성해줘. 상품명: {product}"
    
    result = llm1.invoke(prompt)
    names = result.strip()
    
    return jsonify({"product": product, "name": names})

@app.route('/api/name2', methods=["POST"])
def generate_name2():
    data = request.get_json()
    product = data.get("product", None)
    
    # 채팅 모델을 사용해서 동일한 질문을 한다.
    prompt = f"다음 상품을 만드는 창의 적인 회사 이름을 영어로 1개만 작성해줘. 상품명: {product}"

    messages = [
        SystemMessage(content="당신은 회사 이름을 창의적으로 잘 만드는 작명가 입니다."),
        HumanMessage(content=prompt)
    ]
    
    result = llm2.invoke(messages)
    name = result.content.strip('"')
    
    return jsonify({"product": product, "name": name})

if __name__ == "__main__":
    app.run(debug=True)