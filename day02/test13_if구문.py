# if / else 혹은 if / elif / else 구문의 형태
# 반드시 if구문 끝나고 콜론(:) 찍을 것
num_a = 1500
num_b = 1500

if num_a > num_b:
    print('A가 B보다 큰 숫자입니다. 값은', num_a, '입니다.')
elif num_a < num_b:
    print('B가 A보다 큰 숫자입니다. 값은', num_b, '입니다.')
else:
    print('A와 B는 같은 숫자입니다. 값은', num_a, '입니다.')