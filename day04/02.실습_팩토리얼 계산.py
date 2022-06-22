#팩토리얼 표 : 0부터 100까지의 Factorial table 생성

idx, gop, sum = 0,0,0
factorial = []
total_sum = []

num_chk_list = list('0123456789')
print(num_chk_list)

while True:
    key_in = input('숫자를 입력하세요[1~100]')
    chk_num = True
    for char in key_in:
        is_num = char in num_chk_list
        chk_num *= is_num
        if not is_num:
            break
    if chk_num:
        last_sum = int(key_in)
        print('입력한 숫자 : ', last_sum)
        break
    else:
        print('입력한 값이 숫자가 아닙니다.')
#
title = str(last_sum) + '까지의 팩토리얼 테이블 구하기!'
print('-'*100)
print(title)
print('-'*100)

numbers = list(range(last_sum+1))

while idx < len(numbers):
    num = numbers[idx]
    gop *= num
    if gop < 1:
        gop = 1
    else: gop
    # gop = 1 if gop < 1 else gop

    factorial.append(gop)
    idx += 1

for fact_num in range(len(factorial)):
    print(str(fact_num)+'! = ',factorial[fact_num])