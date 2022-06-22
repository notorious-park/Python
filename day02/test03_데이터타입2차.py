# Case1) 문자 읽을 때 n : 칸 아래 변경 / t : tab키만큼 공백
text = '안녕하세요 \n전북은행 00지점 입니다. \t무엇을 도와드릴까요??'
print(text)

text2 = '''\
        안녕하세요 전북은행 00지점 입니다.
        무엇을 도와드릴까요?
        감사합니다.\
        '''
print(text2)

# Case2) 문자 대문자 / 소문자 변경
test = 'Welcome to the JB Financial Group!'
result = test.upper() #대문자 변경
print(result)
print(result.isupper())

result = test.lower() #소문자 변경
print(result)
print(result.islower())

result = '!'.join(test) #문자 사이에 특정 텍스트 삽입
print(result)

