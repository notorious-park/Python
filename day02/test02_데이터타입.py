x = 50
y = 4

#Case1) 데이터 타입
x = 10
y = 20

print('x == y = ', x==y)
print('x != y = ', x!=y)
print('x > y = ', x>y)
print('x < y = ', x<y)

print('2x == y =', x*2 == y)
print('x**2 > y**2 =', x**2 > y**2)
print('x**4 > y**3 =', x**4 > y**3)



# Case2) 문자 추출 및 변환
# Tip) Shift + Enter 누를 경우 뒤에 text 있더라도 커서가 바로 아래쪽으로 이동!!!
test = '파이썬 프로그래밍 재미있다!'

result = test.startswith('파이썬') # 문자열이 '파이썬으로 시작하는지 확인
print(result)
result = test.endswith('!') # 문자열이 '!'로 끝나는지 확인
print(result)
result = test.endswith('어렵다') # 문자열이 '어려워요!'로 끝나는지 확인
print(result)
result = test.replace('파이썬','Python') # 문자열중 '파이썬'을 'Python'으로 변경
print(result)
result = test.replace('재미있다','어렵다')
print(result)