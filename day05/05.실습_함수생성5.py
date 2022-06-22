#keyword arguments
def introduceMyCar(brand,seats = 4,type = '세단'):
    print('나의 차는 {} {}인승 {}입니다.'.format(brand,seats,type))

#Summary : 위치가 동일하다면 굳이 인자값(변수명) 안줘도 됨
#          만약 위치가 다르다면 반드시 인자값(변수명) 꼭 사용할 것!!!
#          default값이 있다면 그대로 불러옴

#위치 인자값 1개
introduceMyCar('K5')

#키워드 인자값 1개
introduceMyCar('볼보')

#위치 인자값 1개, 키워드 인자값 1개 혼용 사용
introduceMyCar('BMW',seats = 8)

#키워드 인자값 2개
introduceMyCar(brand = '포르쉐',type = '스포츠카')

#순서 바뀐 키워드 인자값 2개, 순서가 바뀐 경우는 반드시 인자값 사용
introduceMyCar(type = 'SUV', brand='아우디')

#순서를 지킨 위치 인자값 3개, 순서 같다면 상관 없음
introduceMyCar('그랜져',5,'SUV')

#순서 바꾼 인자값 3개, 순서 다를 경우 반드시 키워드 인자값 사용할 것!!!
introduceMyCar(type = '머슬카',brand = '르노삼성', seats = 2)