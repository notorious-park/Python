#While 문

#Case1)
idx = 0
while idx < 3:
    print(idx)
    idx += 1
print('프로그램 종료!')


#Case2)
num = 1
sum = 0

while True:
    sum += num
    if sum > 55:
        break
    else: num += 1

print('num값이 %d일때 while문 탈출!!' % num)


#Case3)

numbers = [0,1,2,3,4,5,6,7,8,9]
idx, sum = 0,0

while idx < len(numbers):
    num = numbers[idx]
    sum += idx
    idx += 1

print('numbers의 합계는', sum, '입니다.')