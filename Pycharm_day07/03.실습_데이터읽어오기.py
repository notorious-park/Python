fp = open("./data/test.txt", "r", encoding="UTF-8")
# . : 하나만 있을경우 이 파일이 있는 경로에 data 폴더가 없음
# 해결 : 1) ..으로 할 경우 상위 디렉토리로 올라가 찾음!!!
# 해결 : 2) 해당 data 폴더를 현재 파일이 있는 라이브러리에 지정!!!

# fp2 = open("./data/test.txt", "r",encoding='UTF-8')   # 한글 사용 시

#with open ("./data/test.txt", encoding='UTF-8') as fp3
#    data = fp3.read()   # Close 안써도 됨

print(fp.read())

fp.close()   # 사용 후 반드시 종료할 것!