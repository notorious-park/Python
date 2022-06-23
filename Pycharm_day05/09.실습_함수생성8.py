#지역변수와 전역변수
param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print('func1.strdata = {}, id = {}'.format(strdata,id(strdata)))

def func2():
    param = 20
    print('func2.strdata = {}, id = {}'.format(param,id(param)))

def func3():
    global param # ------------ global 사용 시, 전체에 해당값 적용 / id값도 동일------------
    param = 30
    print('func3.strdata = {}, id = {}'.format(param,id(param)))


func1()
print('main1.strdata = {}, id = {}'.format(strdata,id(strdata)))
func2()
print('main2.strdata = {}, id = {}'.format(param,id(param)))
func3()
print('main3.strdata = {}, id = {}'.format(param,id(param)))