# 요약 정리
# 리스트형 : 변경 가능 / 중복 허용     []
# 튜플형   : 변경 불가 / 중복 허용    ()
# 세트형   : 변경 가능 / 중복 불가    {}
# 사전형   : 변경 가능 / 중복 불가    {} -> 000 : 000으로 묶음으로 구성

bans = {'잎새반':'찬영이',
        '열매반':'예영이',
        '햇살반':'준영이',
        '열매반':'채영이',}
print(type(bans))
print('반의수 : ',len(bans))

#읽기 - 변수명[첫번째 변수이름]
print('잎새반 : ',bans['잎새반'])
print('햇살반 : ',bans['햇살반'])
print('열매반 : ',bans['열매반']) #중복될 경우 나중의 값으로 엎어치기 됨

#추가 - 그냥 입력하면 됨
bans['꽃잎반'] = '희영이'
print('반 추가 : ',bans)
bans['새싹반'] = '현종이'
print('반 추가 : ',bans)

#변경
bans['햇살반'] = '아무개'
print('반 변경 : ',bans) #변경 시, 별도 함수가 아니라 그냥 해당값 변경으로 진행함

#삭제
del bans['잎새반'] #변수 삭제 시, del 사용
print('반 삭제 : ',bans)


#사전형 함수
customer = {
        'name'      : '박요온',
        'gender'    : '남자',
        'email'     : 'lucky2734@jbbank.co.kr',
        'company'   : '전북은행',
        'address'   : '전주시 백제대로 566'
           }

print(customer)
print('customer.keys() \t : ', customer.keys())
print('customer.values() \t : ', customer.values())
print('cusomter.items() \t : ', customer.items())

for key, value in customer.items():
        print('%s \t : %s' %(key,value))