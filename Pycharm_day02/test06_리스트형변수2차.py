kia = ['양현종','로니','한승혁','임기영']
print('kia투수 : ', kia)
#모든 변수 시작은 0번이다!!!

#리스트형 추가
kia.append('정해영')
print('kia투수 추가 : ', kia)

#리스트형 추가2
kia.insert(4,'장현식')
print('kia투수 2차추가: ', kia)

#리스트형 삭제
kia.remove('로니')
print('kia투수 삭제 : ', kia)

#리스트형 삭제2
kia.pop(2)
print('kia투수 2차삭제 : ', kia)

# kia[3] = '윤석민
# print('kia마무리 투수 변경 : ',kia)

#특정 텍스트 추가 : append / add
#특정 텍스트 삭제 : remove / discard
        # -> 차이점 : 없는 값 삭제 시, remove의 경우 오류 / discard는 없는대로 그냥 실행됨

#텍스트 특정 부분 추가 : insert
#텍스트 특정 부분 삭제 : pop
#특정 텍스트 변경 : 변수이름[바꾸고자 하는 순서] = 바꿀이름
#Sapmle
# planet = '화성'
# pos = solarsys.index(planet)
# print(pos)
# solarsys[pos] = 'Mars'
# print('태양계 : ',solarsys)


