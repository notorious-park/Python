#------------------------ 함수를 사용한 제곱 계산 ------------------------
def getSquare(num):
    return num**2

num = 2
result = getSquare(num)
print(result)



#------------------------ 람다 함수를 사용한 제곱 계산 ------------------------
print( (lambda x : x**2)(3) )

res = 5 + (lambda x : x**2)(3)
print(res)



#------------------------ 람다 함수를 다시 하나의 함수로 ------------------------
func1 = (lambda x : x**2)
print(type(func1))
print(func1(5))