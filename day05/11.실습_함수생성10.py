# 계산기
def calculator(type,num1=0,num2=0):
    result = 0
    if type == '+':
        result = num1 + num2
    elif type == '-':
        result = num1 - num2
    elif type == '*':
        result = num1 * num2
    elif type == '/':
        result = num1 / num2
    elif type == '**':
        result = num1 ** num2
    elif type == '%':
        result = num1 % num2
    else:
        print('잘못된 기호입니다. 기호를 재확인해주세요!')
        result = 'Error!!!'
    return result


type = '%'
num1 = 5
num2 = 2
result = calculator(type,num1,num2)
print('{} {} {}의 계산값은 {}입니다.'.format(num1,type,num2,result))