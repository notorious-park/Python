from random import randint
result = ''

def games(computer, user):
    if computer == 0:
        computer = '가위'
    elif computer == 1:
        computer = '바위'
    else:
        computer = '보'

    if computer == user:
        result = '비겼다!'
        result2 = 'A'
        return result
        return result2
    elif (computer =='가위' and user =='보') or (computer =='바위' and user =='가위') or (computer =='보' and user == '바위'):
        result = '사용자 패배'
        result2 = 'B'
        return result
        return result2
    else :
        result = '사용자 승리'
        result2 = 'B'
        return result
        return result2
    print('컴퓨터 : ', computer)
    print('사용자 : ', user)
    print(result)

while True:
    user = input('가위 바위 보 ? ')
    computer = randint(0, 2)
    while True:
        if user != '가위' and user != '바위' and user != '보':
            pass
            print('가위 바위 보 중 하나를 입력해주세요!')
        else:
            break
    result = games(computer,user)
    if result != 'A':
        break
        print(result)
    else:
        pass