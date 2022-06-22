#Case1_인삿말
# name = input('당신의 이름은 무엇입니까')
# print(name + '님 반갑습니다')

#바로 윗줄 복사하는 단축키 : Ctrl + D


#Case2_주문
# order = input('00카페입니다. \n무엇을 주문하시겠습니까?')
# count = input('음료는 몇잔 준비해드릴까요?')
# print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요' %(order,count))

#Case3_정산_오류
# price = 5000
# cost = count * price
# print('%s %s잔을 주문하셨습니다. \n결제 하실 금액은 %s원입니다.' %(order,count,cost))

#Case4_정산_정답
# price = 5000
# cost = price * int(count)
# print('%s %s잔을 주문하셨습니다. \n결제 하실 금액은 %d원입니다.' %(order,count,cost))



#요온 연습
name = input('반갑습니다 고객님 전북은행입니다. 고객님 성함을 알려주세요')
print(name + '님 반갑습니다.')

product = input('찾으시는 대출 상품이 무엇이실까요?')
print(product + '대출상품 신청 도와드리겠습니다.')

amount = input('필요하신 자금은 얼마이신가요?')
print('네 감사드립니다 ' + amount + '원 신청 도와드리겠습니다.')

product_2 = input('다른 대출 상품도 찾으시는게 있으실까요?')
print(product_2 + '대출상품도 추가 신청 도와드리겠습니다.')

amount_2 = input('필요하신 자금은 얼마이신가요?')
print('네 감사드립니다 ' + amount_2 + '원 추가 신청 도와드리겠습니다.')

print('%s대출 %s원과 %s대출 %s원 대출 신청 접수하였습니다' % (product,amount,product_2,amount_2))

sum_amount = int(amount) + int(amount_2)
print('오래 기다려 주셔서 감사합니다. 신청해주신 두 상품 모두 승인되었고 총 대출금액은 %d원 입니다.' % sum_amount)





