#함수 호출
def exchange(dollar):
    won = dollar * 1290
    return won

usd = 1000
krw = exchange(usd)

print('환전하신 금액은 %d원입니다.' %(krw))
print('환전하신 금액은 {}원입니다.'.format(krw))