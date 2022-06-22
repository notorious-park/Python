#for문 예제
scope = [1,2,3,4,5]
for x in scope:
    print(x)

scope2 = list('qwerasdf')
print(scope2)
for x in scope2:
    print(x)

#range 함수예제
result = list(range(10))
print('range(10) : ',result)

result = list(range(5,10))
print('range(5,10) : ',result)

result = list(range(1,10,2)) #홀수
print('range(1,10,2) : ',result)

result = list(range(0,10,2)) #짝수
print('range(0,10,2) : ',result)