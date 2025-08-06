from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI,ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static')
app = Flask(__name__, static_folder='public', static_url_path='')
# openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
openai = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature= 0.7
)



reviews = [] # 사용자 후기를 저장할 DB

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')
    
    reviews.append({'rating': rating, 'opinion': opinion})
    
    return jsonify({'message':'성공적으로 저장됨'})

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': reviews})

@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang','ko')
    print('언어 : ', target_lang)
    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    
    print("리뷰내용 통합: ", reviews_text)
    print('target Lang:', target_lang)
   
  
    # 1. PromptTemplate 정의
    prompt = PromptTemplate(
        input_variables=["target_lang", "reviews_text"],
        template="다음 리뷰 목록을 기반으로 {target_lang} 나라 말로 간결하게 한줄로 요약해 주세요:\n\n{reviews_text}"
    )
    llm = OpenAI(temperature=0.5)
    # 3. 체인 생성
    chain = prompt | llm | RunnableLambda(lambda x: {"translated": x.strip()})
    try:
        # 4. 입력을 딕셔너리로 전달
        result = chain.invoke({
            "target_lang": target_lang,
            "reviews_text": reviews_text
        })
        print("AI 요약 결과:", result)
    except Exception as e:
        print("AI 요약 중 에러 발생:", e)
        return jsonify({'summary': 'AI 요약 실패', 'averageRating': average_rating}), 500

    return jsonify({'summary': result['translated'], 'averageRating': average_rating})


if __name__ == '__main__':
    app.run(port=5000, debug=True)