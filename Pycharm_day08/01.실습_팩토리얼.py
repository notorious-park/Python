factorial = [ ]
total_sum = [ ]

# 함수 1) 숫자 검증
num = list('0123456789')
def is_num():
    while True:
        x = input('숫자를 입력해 주세요.[1~100]')
        check = True
        for char in x:
            is_num = char in num
            check *= is_num
            if is_num == False:
                break

        if check:
            last_num = int(x)
            print('입력한 숫자 :', last_num)
            return last_num   # return 해줘야 함수값 표현 가능
            break
        else:
            print('입력한 값이 숫자가 아닙니다.')

title =  str(is_num()) + ' 까지의 합계 및 팩토리얼 테이블 구하기!!'
print('-'*50)
print(title)
print('-'*50)


# numbers = list(range(is_num()+1))
idx = 0
# numbers = list(range(is_num()))

# 함수 2) 팩토리얼 계산
# def factorial():
#     while idx < len(numbers):
#         num = numbers[idx]
#         sum += num
#         gop *= num
#
#         gop = 1 if gop < 1 else gop
#
#         total_sum.append(sum)
#         factorial.append(gop)
#         idx += 1


# 함수 3) 자릿수 계산
# def cs_num(num):




# test = is_num()

# print('-' * 100)
# print('{} 팩토리얼 테이블'.format(is_num()))
# print('-' * 100)