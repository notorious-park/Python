# 텍스트 파일 복사하기

f = open('./data/mydata.txt','r')       # 읽기
h = open('./data/mydata_copy.txt','w')  # 쓰기

data = f.read()
h.write(data)

h.close()
f.close()

with open('./data/mydata.txt','r') as fp:
    data = fp.read()

print(data)