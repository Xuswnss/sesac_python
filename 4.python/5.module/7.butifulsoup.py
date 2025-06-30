# pip install bs4
import requests
import bs4
from bs4 import BeautifulSoup # 라이브러리 안에 있는 특정 객체만 가져오기

res = requests.get('http://makemyproject.net')
print(res)
print(res.text)
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
head = soup.find('head')
print('head : ', head)

body = soup.find('body')

bodytext = body.text.strip()
print('body.text :', bodytext)