#삼각형 그리기
for x in range(1,10,2):
    mark = '*' * x
    print(mark)


#정삼각형 그리기
for i in range(1,10,2):
    # mark = ' ' * int((10-i)/2) + '*' * i        #방법1) Basic
    mark = '{space}{star} i={idx}' .format(     #방법2) 강사님 - 어렵다...
            space = ' ' * int((10-i)/2),
            star  = '*' * i,
            idx   = i
    )
    print(mark)


#중첩 for문
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for x in range(3):
    for y in range(3):
        print('matrix[',x,'],[',y,'] :', matrix[x][y], end = ', \t')
        #, end = ', \t' : 안쓰면 기본 default 값이 \n이여서 밑으로 내려감
    print()