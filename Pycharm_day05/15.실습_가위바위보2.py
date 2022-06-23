import random

com = random.randint(0,2)

while True:
    my = input('도전? [가위/바위/보/종료]')
    is_finish = False

    if my == "종료":
        is_finish = True

    is_valid = bool()
    if my == "가위" or my == "바위" or my == "보":
        is_valid = True
    else:
        is_valid = False

    if is_valid:
        break
    else:
        warn_msg = "가위. 바위, 보 중에서 입력하세요. "
        print(warn_msg)

    if is_finish:
        print("게임종료!!!")
        break

def make_num(name):
    rsp ={"가위" : 0, "바위" : 1, "보" : 2}
    result = rsp[name]
    return result

def make_str(name):
    rsp ={0 : "가위", 1 : "바위", 2 : "보"}
    result = rsp[name]
    return result


def cal(num1, num2):
    x = num2 - make_num(num1)
    y = make_str(num2)
    is_over = bool()
    if x == -1 or x == 2:
        is_over = True
        result = "당신이 {}를 내고, Com이 {}를 내서 이겼습니다.".format(num1, y)
    elif x == 0:
        is_over = False
        result = "당신이 {}를 내고, Com이 {}를 내서 비겼습니다.".format(num1, y)
    else:
        is_over = True
        result = "당신이 {}를 내고, Com이 {}를 내서 졌습니다.".format(num1, y)

    return is_over, result



while True:
    is_over, result = cal(my, com)

    print(result)
    if is_over:
        break