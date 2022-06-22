# 구하고자 하는 함수 : a+b

# 1. 가장 기초적
def add(a,b):
    result = a + b
    return result

# 숫자를 하나 추가하고자 할때의 경우, 번거롭게 변수 한개씩 추가해야하는 문제 발생
# 2. 조금 개선
def add2(a,b,c=0):
    result = a + b + c
    return result

# 숫자가 지속해서 많아진다면 마찬가지로 번거롭게 추가해야하는 문제 발생
# 3. 앞에서 배웠던 걸로 수정 - 지속 반복되므로 for문 사용
def add3(nums):
    result = 0
    for num in nums:
        result += num
    return result

# 조금 더 개선
# 4. Arbitrary - 가변인자 사용해서 수정
def add4(*nums):
    result = 0
    for num in nums:
        result += num
    return result

result = add(1,2)
print(result)

result = add2(1,2,3)
print(result)

result = add3([1,2,3,4,5])
print(result)

result = add4(1,2,3,4,5)
print(result)
