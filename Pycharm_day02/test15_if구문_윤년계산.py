# Tip) 블럭문 이동 시 Tab 키! / 거꾸로는 Shift + Tab 키
year = int(input('확인하고자 하는 연도를 입력해주세요.'))

#Case1)
# is_leap = False
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             is_leap = True
#         else: is_leap = False
#     else: is_leap = True
# else: is_leap = False
#윤년 여부 (if)
# if is_leap:
#     print('윤년입니다!')
# else: print('윤년이 아닙니다!')



#Case2) elif 사용
# result = ''
# if year % 400 == 0:
#     result = 'y'
# elif year % 100 == 0:
#     result = 'n'
# elif year % 4 == 0:
#     result = 'y'
# else: result = 'n'
#
# if result == 'y':
#     print('윤년입니다!')
# else: print('윤년이 아닙니다!')



#Case3) 가장 빠른 방법
is_leap = False
is_leap = (year % 400 == 0) or ((year % 100 != 0)and(year % 4 == 0))

if is_leap:
    print('윤년입니다!')
else: print('윤년이 아닙니다!')