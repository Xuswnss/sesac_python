import urllib.request
import json

text = 'Python 개발'
client_id = '' # 발급하는 아이디
secrete_key = '' # 발급받은 secreteKey
encText = urllib.parse.quote(text)

url = 'https://openapi.naver.com/v1/search/blog?query='+encText
print('######## url :', url)
request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header("X-Naver-Client-Secret", secrete_key)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))