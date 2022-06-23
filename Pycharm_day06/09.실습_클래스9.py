# 이름장식 Name Mangling : __가 있는것에 한하여 이름을 변경해버리는 이름 장식 기법
# 변형된 규칙 : _[클래스명]__변수명

# dir() : 클래스 내부에 들어있는 객체들을 확인하는 명령문
class MyCountry:
    country : 'Korea'
    # __country: 'Korea'
    # city = 'Seoul'

result = dir(MyCountry)
print(result)

# 클래스 내부 변형변수는 정의시 사용했던 변수명으로는 접근이 불가능

num = 0
for internal_element in result:
    num += 1
    print(num,internal_element)