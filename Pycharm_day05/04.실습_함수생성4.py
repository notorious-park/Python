#default 함수
def ordermenu(menu):
    print('손님, {}를 주문하셨습니다.'.format(menu))

ordermenu('카푸치노')
ordermenu('아메리카노')



#default값 불러오기
def ordercoffee(menu = '카푸치노'):
    print('손님, {}를 주문하셨습니다.'.format(menu))

ordercoffee() #공란 시 위에서 지정했던 default값 불러옴 / 해당값 입력 시, 해당값으로 불러옴