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
llm = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature= 0.7
)

summary_prompt = PromptTemplate.from_template(
    """
    다음 목록을 기반으로 간결한 요약을 작성해주세요
    
    리뷰목록:
    {reviews_text}
    """
)

translate_prompt = PromptTemplate.from_template(
    """다음 한국어 문장을 기반으로 {target_lang_name}으로 번역하시오
    
    {summary_ko}
    """
)

#chain 구성
summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm

# 우리가 궁극적으로 원하는 체인은 summary하고 translate를 같이하는 체인인 것이다.
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
summary_then_translate_chain = (
    {
        'summary_ko' : summary_prompt | llm | RunnableLambda(lambda m: m.content),
        # 'target_lang_name' :  RunnablePassthrough()
        'target_lang_name' :  RunnableLambda(lambda x : x['target_lang_name'])
    }
    | translate_prompt
    | llm
    | RunnableLambda(lambda m : m.content)
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
    lang_name = request.args.get('lang','ko')
    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    
    print("리뷰내용 통합: ", reviews_text)
   
    response_summary = summary_chain.invoke({'review_text': reviews_text}).content
    print('요약 내용', response_summary)
    response_translate = translate_chain.invoke({'summary_ko' : response_summary, 'target_lang_name' : lang_name}).content
    return jsonify({'summary': result['translated'], 'averageRating': average_rating})


if __name__ == '__main__':
    app.run(port=5000, debug=True)