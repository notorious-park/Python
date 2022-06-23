#문자열 순서 바꾸기

#Case1) 요온 방법
basic = 'Life is too short, so you need Python'

change = str()

for x in list(range(-1,-len(basic)-1,-1)):
    change += basic[x] #그냥 = 로 해버리면 계속 업데이트쳐져서 마지막꺼만 남음

print('기존문장 : ',basic)
print('요온방법 : ',change)



#Case2) 강의교안
s = 'Life is too short, so you need Python'

new_s = str()                       # 신규 문자열형 변수 선언

for x in range(len(s)-1, -1, -1):   # range()를 활용한 역순 인덱스 추출
    new_s += s[x]                   # 문자열을 끝에서부터 앞으로 신규 변수에 붙이기

print('강의교안 : ',new_s)                        # 위 결과 출력



#Case3) 간단한 방법
s = 'Life is too short, so you need Python'
r = ''
for c in s:
    r = c + r #Reverse - 그냥 r + c로 하면 원래 문장 나옴
print('간단방법 : ',r)



#Case4) 초간단방법
s = 'Life is too short, so you need Python'
print('초간단법 : ',s[::-1])                      # 인덱스 사용법으로 역순 출력