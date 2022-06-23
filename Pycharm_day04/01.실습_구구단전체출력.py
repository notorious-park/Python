#구구단 전체 출력
cols = 4
rows = int(8/cols)+1
w_space = '\t\t'

for row in range(rows):
    dans = list()
    for col in range(cols):
        dan = (row * cols) + col + 2
        dans.append(dan)

    for num in range(10):
        for dan in dans:
            if dan > 9:
                continue

            if num < 1:
                print('{} 단 \t'.format(dan), end=w_space)
            else:
                gugutext = '{} X {} = {}'.format(dan,num,dan*num)
                print(gugutext, end=w_space)
        print()
print()

#반복되는 변수 정의 - 1) %s or %d   /   %()
#                  2) {}         /   .format{변수}
for x in range(10):
    if x > 5:
        print('{}는 5보다 큰수입니다.'.format(x))
    else:
        print('{}는 5보다 작은수입니다.'.format(x))
