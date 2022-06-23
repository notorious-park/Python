actor = {'유재석','노홍철','정준하','노홍철','정형돈','하하','유재석','박명수'}
#세트형 변수의 경우 중복제거되어 산출

print(actor)
print(type(actor))
print('유재석 유무 : ','유재석' in actor)
print('박명수 유무 : ','박명수' in actor)
print('강호동 유무 : ','강호동' in actor)

#세트형 집합 연산자
a = set('abracadabra')
b = set('alacazam')

print('a :\t',a)
print('b :\t',b)
print('합집합 :\t',a|b)
print('교집합 :\t',a&b)
print('차집합 :\t',a-b)


#중복 제거 및 정렬
beast = ['lion','tiger','wolf','tiger','lion','bear','lion'] #리스트형 변수
print('beast : ',beast)

unique_beast = list(set(beast)) #세트형으로 만들어 중복제거한 후 다시 리스트형 변수로 변환
print('unique_beast : ',unique_beast)

sorted_beast = sorted(unique_beast) #알파벳순 정렬
print('sorted_beast : ',sorted_beast)

#요온 연습
beast = set(['lion','tiger','wolf','tiger','lion','bear','lion']) #리스트형 변수
print(beast)
beast.add('fox') #변수 추가
print(beast)

#변수 삭제 : discard의 경우, 없는 값 삭제 시, 그냥 없는대로 진행
beast.discard('apple')
print(beast)
#오류 발생 : remove의 경우, 없는 값 삭제 시, 오류 발생함(key error)
# beast.remove('apple')
# print(beast)