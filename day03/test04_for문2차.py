scope = list(range(1,100))
#pass : 아무 의미없음 / 단순히 칸 채우기용도인듯?
#continue : 뒤에 문장 생략하고 다시 앞으로 돌아감
for x in scope:
    if x <= 10:
        if x % 2 == 0:
            pass
            print('%s는 짝수입니다.' %x)
        else:
            pass
            print('%s는 홀수입니다.' %x)
    else:
        print('%s는 10보다 큰 수입니다.' %x)
        break
        print('after break')
print('프로그램을 종료합니다.')

#for문 예제2
bts_members = ['RM','슈가','진','제이홉','지민','뷔','정국']
num = 0
for member in bts_members:
    num += 1
    print('멤버%d ===> %s \t(이름길이 : %d)'   %(num,member,len(member)))