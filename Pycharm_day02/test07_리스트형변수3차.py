rainbow = ['빨강','주황','노랑','초록','파랑','남색','보라']
print('\n무지개색깔 : ', rainbow)

result = rainbow[2:5] #앞에 숫자 : 변수 위치(0번부터 시작) / 뒤에 숫자 : 앞에서 몇번째까지 볼건지(1번부터 시작)
print('rainbow[2:5] :',result)

result = rainbow[3:]
print('rainbow[3:] :',result)

result = rainbow[:]
print('rainbow[:] :',result)


result = rainbow[1::2] #:: 뜻 -> 몇번째 시작되는 변수에서 뒤에 숫자만큼 띄어쓰기 추출
print('rainbow[1::2] : ',result)

result = rainbow[1::3]
print('rainbow[1::3] : ',result)

result = rainbow[2::2]
print('rainbow[2::2] :',result)

result = rainbow[-3:]
print('rainbow[-3:] :',result)

result = rainbow[:-3]
print('rainbow[:-3] :',result)