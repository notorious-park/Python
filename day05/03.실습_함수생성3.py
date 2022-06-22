#인세를 계산하는 함수
def cal_royalty(price,sales,per):
    rate = per / 100
    royalty = price * sales * rate
    return royalty

i = input('책의 정가는 얼마입니까?')
price = int(i)

i = input('책의 발행 부수는?')
sales = int(i)

i = input('인세율은 얼마입니까?')
per = float(i)

#최종 결과
final = cal_royalty(price,sales,per)
print('인세는 {}원입니다'.format(final))
