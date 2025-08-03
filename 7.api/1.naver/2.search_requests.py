import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv() #.env파일을 읽어서, 안에 있는 내용을 메모리에 둔다.

text = 'Python 개발'
client_id =  os.getenv('NAVER_CLIENT_ID')
secrete_key = os.getenv('NAVER_CLIENT_SECRETE') # 발급받은 secreteKey
encText = requests.utils.quote(text)
url = 'https://openapi.naver.com/v1/search/blog?query='+encText
print('##### url :', url)
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret' : secrete_key
}


response = requests.get(url, headers = headers)
print('####### response : ', response.status_code)
if response.status_code == 200:
    response_body = response.text
    print(response_body)
    print('#### end')
    data = json.loads(response_body)
    selected_columns = [['title', 'link'] ]
    
    for item in data['items']:
        # print(item['title'] , item['link'])
        selected_columns.append([item['title'], item['link']])

