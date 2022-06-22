#함수 생성1
def add_txt(arg1,arg2):
    print(arg1,arg2)

para1 = '대~한민국'
para2 = '짝짝~짝~짝.짝!'
add_txt(para1,para2)

#함수 생성2
def add_num(num1,num2):
    result = num1 + num2
    return result

para1 = 40
para2 = 50
sum = add_num(para1,para2)

#결과는 같음 - 첫번째는 변수 타입 지정해서 / 두번째는 지정 안하고
print('%d와 %d의 합은 %d입니다.'%(para1,para2,sum))
print('{}와 {}의 합은 {}입니다.'.format(para1,para2,sum))