basic = 'JB Financial Group Is Very Good!'

print('기존 문장대로 출력합니다\n',basic)
print('모두 대문자로 출력합니다\n',basic.upper())
print('모두 소문자로 출력합니다\n',basic.lower())

#대소문자 구분
change = str()

for x in basic:
    if x.islower(): #해당 문자가 소문자이면
        change += x.upper() #대문자로 변경
    else:           #해당 문자가 대문자이면
        change += x.lower() #소문자로 변경

print('대소문자를 바꾸어서 출력합니다.\n',change)

#대소문자 변경 함수 - swapcase() / 위와 같은 결과
print('대소문자를 바꾸어서 출렵합니다.\n',basic.swapcase())



