from random import randint
result = 0
user = input('가위(0) 바위(1) 보(2) ? ')
com = randint(0, 2)

class GameMZP:

    def 재경기(self):
        if int(user) > 2 or int(user) < 0:
            print('가위바위보 중 다시 입력하세요!')
            return False
        return True

    def 가위바위보(self):
        if com == user:
            result = 0 # 비김
            return result
        elif (com == 0 and user == 2) or (com == 1 and user == 0) or (com == 2 and user == 1):
            result = 1  # 컴퓨터 승
            return result
        else:
            result = 2 # 사용자 승
            return result

print('사용자 입력값 : ', user)
print('컴퓨터 입력값 : ', com)

test = GameMZP()
test.가위바위보()
test.재경기()

