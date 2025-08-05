from dotenv import load_dotenv
import os
import requests

# .env 파일에서 OPEN_API_KEY 로드
load_dotenv()
OPEN_API_KEY = os.getenv('OPEN_API_KEY')

response = requests.post(
    'https://api.openai.com/v1/chat/completions',  # ✅ 정확한 endpoint
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPEN_API_KEY}'
    },
    json={
        'model': 'gpt-4o',  # 또는 gpt-3.5-turbo
        'messages': [
            {'role': 'user', 'content': '한식 먹을려고'}
        ],
        'temperature': 0.7
    }
)

# 응답 파싱
data = response.json()
print(data)
print(data['choices'][0]['message']['content'])  # ✅ 생성된 문장 출력
