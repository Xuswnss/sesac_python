import os

os.getcwd() # getCurrentWorkingDirectory
print('get - current working directory')
print('현재 작업 디렉토리:',os.getcwd())


#파일 만들기
new_dir = 'sesac1234'
os.mkdir(new_dir)
print('생성완')

#디렉토리 이동
os.chdir(new_dir)
print('move ')

os.chdir('..')
print('move')

#파일 지우기
os.rmdir(new_dir)
print('삭제완')
