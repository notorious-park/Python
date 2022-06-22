#튜플형 변수의 경우, 변수 변경 불가함
girl_group = ('블랙핑크','에이핑크','레드벨벳','걸스데이','우주소녀')
print(type(girl_group))
print('girl_group : ',girl_group)
print('girl_group[2] :',girl_group[2])


#객체 변경
# girl_group[2] = '트와이스'
# 위대로 하면 오류 발생

#방법 : 튜플형 변수를 리스트형변수로 변환 후 진행
girl_group = list(girl_group)
girl_group[2] = '트와이스'
girl_group = tuple(girl_group)
print('girl_group : ',girl_group)





width  = 20
height = 30
area = width * height
print('너비 :', width)
print('높이 :', height)
print('넓이 :', area)

data   = (15, 50)
width, height = data
area = width * height

print('너비 :', width);
print('높이 :', height);
print('넓이 :', area)
