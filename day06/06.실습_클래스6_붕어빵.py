class 빵틀:
    모양 = str()
    반죽 = str()
    앙꼬 = str()
    단가 = int()

    def __init__(self,모양,반죽,앙꼬,단가):
        self.모양 = 모양
        self.반죽 = 반죽
        self.앙꼬 = 앙꼬
        self.단가 = 단가

    def 굽기(self,주문갯수):
        # 한번에 최대 10개씩 굽는다
        # 한판 굽는데 걸리는 시간은 5분
        굽는횟수 = (주문갯수-1) / 10 + 1
        완성시간 = int(굽는횟수) * 5
        return 완성시간

    def 가격(self,주문갯수):
        금액 = 주문갯수 * self.단가
        return 금액

    def 주문(self,주문갯수,지불금액):
        print('break point---1')   # 오류 발생 시, 위치 파악을 위한 중간 검증
        대기시간 = self.굽기(주문갯수)
        print('break point---2')   # 오류 발생 시, 위치 파악을 위한 중간 검증
        주문금액 = self.가격(주문갯수)
        print('break point---3')   # 오류 발생 시, 위치 파악을 위한 중간 검증
        거스름돈 = 지불금액 - 주문금액
        print('break point---4')   # 오류 발생 시, 위치 파악을 위한 중간 검증
        return 대기시간, 거스름돈

# 타꼬야끼 주문
print('#타꼬야끼 주문 (1개 500원)')

타꼬야끼 = 빵틀('타꼬야끼','밀가루','낙지',500)

order = 20
payment = 5000

wait_time, change = 타꼬야끼.주문(order,payment)
shape = 타꼬야끼.모양
print('{}빵 {}개를 주문하셨고, {}원을 지불하셨습니다'.format(shape,order,payment))

if change == 0:
    message = '손님, {wt}분만 기다려주세요.'.format(wt=wait_time)
elif change > 0:
    message = '잔돈은 {ch}원입니다. {wt}분만 기다려주세요'.format(ch=change,wt=wait_time)
elif change < 0:
    message = '손님, 금액이 {ch}원 부족합니다.'.format(ch=-change)
else:
    message = 'Error'

print('==>',end = '')
print(message)
print('-'*50)