from random import randint

#로또번호 생성기 연습
print('#####로또번호 생성기#####')

ticket_no = 0

# Validation Check
while True:
    ticket_no = input("발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => ")
    ticket_no = ticket_no.strip()

    is_valid = bool()
    if len(ticket_no) == 1:
        if ticket_no in list('0123456789'):
            ticket_no = int(ticket_no)
            if 1 <= ticket_no <=5:
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


print('%s개의 로또번호 티켓을 주문하셨습니다.' % ticket_no)
print('-'*100)
final_ticket = dict()

for x in range(int(ticket_no)):
    tmp = list()
    for pick_number in range(6):
        pick_number = randint(1, 45)
        tmp.append(pick_number)
    key = '티켓%d' % (x+1)
    val = sorted(tmp)
    print(" * {} : {} ".format(key, val))
    final_ticket[key] = val

print('-' * 100)
print('생성한 로또번호는 최종적으로 dict형으로 저장')

print('final_ticket = ',final_ticket)