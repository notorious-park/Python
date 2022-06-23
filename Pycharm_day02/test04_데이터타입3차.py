#Immutable 예제
hello = '안녕하세요!'
print(hello)
print(id(hello))

hello = '반갑습니다!'
print(hello)
print(id(hello)) #서로 id 다름!

#--------------------------------------------------------------------------#
# Tip) 오류 발생 시, 컨트롤키 누르고 에러문구(파란색) 클릭할 경우 에러 발생한 지점 화면 나옴!!!

#mutable 예제 / 리스트형변수
hello_list = ['안녕하세요!']
print(hello_list)
print(id(hello_list))

hello_list[0] = '반갑습니다!' # 리스트 첫번째 항목 값 변경하기
print(hello_list)
print(id(hello_list)) #서로 id 동일함!