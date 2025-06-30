import os
import zipfile #압축

my_dir = 'sesac1234'

#디렉토리 안에 파일 읽어오기
for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    print('filePath',file_path)
    if(os.path.isfile(filename)):
        print(filename)
        zip_filename = f'{file_path}.zip'
        
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(file_path, arcname=filename)
        print()