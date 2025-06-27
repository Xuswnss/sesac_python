from PIL import Image, ImageFilter


# 이미지 열기 (경로 수정)
image = Image.open('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/4.python/image/cat.jpg')

# 이미지 크기를 줄이고 싶음
resized_image = image.resize((400, 300))
resized_image.save('../image/small_cat.jpg')

# blur cat
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('../image/blurCat.jpg')
