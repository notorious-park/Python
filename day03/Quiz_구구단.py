#제출용도
# range = [1,2,3,4,5,6,7,8,9]
#
# x = input('출력할 단을 입력해주세요.[2~9]')
#
# print('%s단 출력\n----------------'%(x))
# for y in range:
#     print('%s * %s = ' %(x,y),end='')
#     print(int(x) * int(y))
# else: pass



#수정 - 강사님 보완사항
# x = input('출력할 단을 입력해주세요.[2~9]')
# print('%s단 출력\n----------------'%(x))
# for y in range(1,10):
#     print('%s * %s = ' %(x,y),end='')
#     print(int(x) * y)


#강사님 방법
dan = input('출력할 단을 입력해주세요.[2~9]')
print('{} 단 출 력'.format(dan))
print('-'*20)

for i in range(1,10):
    gop = int(dan) * i
    print('{} x {} = {}'.format(dan, i , gop))