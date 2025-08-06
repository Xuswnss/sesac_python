from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static')
app = Flask(__name__, static_folder='public', static_url_path='')
# openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
openai = OpenAI()

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
    
    # 아래도 try catch 로 꼭 감싸야 함.. key가 없거나, 돈이 다 떨어졌거나, 서버가 죽었거나, 여러가지 이유로 요청에 실패할수 있음.
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': f'다음 리뷰 목록을 기반으로 간결하게 한줄로 요약해 주세요.\n\n{reviews_text}'
        }]
    )
    
    summary = response.choices[0].message.content.strip()
    print("요약리뷰내용: ", summary)
    return jsonify({'summary': summary, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(port=5000, debug=True)