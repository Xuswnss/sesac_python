#pip install requests
# 파이썬 가상환경 디렉토리에 설치가 됨
# delete : pip uninstall ...

import requests

response = requests.get('http://makemyproject.net')

print(response)
print(response.status_code)
print(response.text) #html contents
