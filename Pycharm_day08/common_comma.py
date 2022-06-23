# 02.실습_팩토리얼2 결과값에 콤마 붙여주기 위한 함수

def cs_num(num):
    '''
        숫자값에 콤마를 붙혀서 리턴해주는 함수
        param  : num(숫자형)
        return : ret_num(문자형)
    '''
    ret_num = str()
    str_num = str(num)
    rev_num = str_num[::-1]

    # comma = rev_num[3::3]
    ret = rev_num
    tmp = str()

    for i in range(len(ret)):
        if i % 3 == 0:   # 혹은 i > 0 조건 추가해서 밑에 [1:]조건 뺄 수 있음
            tmp += ','
        tmp += rev_num[i]
        # print(i,tmp)

    tmp_num = tmp[1:]

    ret_num = tmp_num[::-1]
    return ret_num

num = 1588134567
ret_num = cs_num(num)

print('입력값1 : {}'.format(num))
print('결과값1 : {}'.format(ret_num))



# 다른 방법!!!!!
cs_num2 = '{:,}'.format(int(num))
print('결과값2 :',cs_num2)