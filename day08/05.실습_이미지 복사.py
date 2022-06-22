# Image 파일 복사
origin_img = './images/전북은행_로고.jpg'       # 파일명 일치하게끔
copied_img = './images/전북은행_로고_copy.jpg'  # 파일명 일치하게끔

# 바이너리 파일 복사하기
bufsize = 2 ** 10    # 1KB, 1024
f = open(origin_img,'rb')
h = open(copied_img,'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

h.close()
f.close()
