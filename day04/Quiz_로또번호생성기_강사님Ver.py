from random import randint

proj_name = "##### 로또번호 생성기 #####"
print(proj_name)

# Validation Check
while True:
    ticket_cnt = input("발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => ")
    ticket_cnt = ticket_cnt.strip()

    is_valid = bool()
    if len(ticket_cnt) == 1:
        if ticket_cnt in list('0123456789'):
            ticket_cnt = int(ticket_cnt)
            if 1 <= ticket_cnt <=5:
                is_valid = True
            else:
                is_valid = False
        else:
            is_valid = False
    else:
        is_valid = False

    if is_valid:
        break
    else:
        warn_msg = "한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개 입니다. "
        warn_msg+= "다시 입력해주세요."
        print(warn_msg)

order_msg = "%d개의 로또번호 티켓을 주문하셨습니다." % ticket_cnt
print(order_msg)
print("-"*50)

final_ticket = dict()
for idx in range(ticket_cnt):

    lotto_num = set()
    while True:
        pick_num = randint(1, 46)
        lotto_num.add(pick_num)

        if len(lotto_num) == 6:
            break

    key = "티켓%d" % (idx + 1)
    val = sorted(list(lotto_num))
    print(" * {} : {} ".format(key, val))

    final_ticket[key] = val

print("-"*50)
print("생성한 로또번호는 최종적으로 dict형으로 저장")
print("final_ticket =", final_ticket)

