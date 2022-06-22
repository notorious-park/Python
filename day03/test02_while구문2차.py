#신호등 예제 _ 업그레이드

signal_color = ''

while signal_color != 'blue' and signal_color != 'yellow' and signal_color != 'red':
    signal_color = input('색을 영문으로 입력하세요! (blue / yellow / red)')

    if signal_color == 'blue':
        print('파란불입니다. 길을 건너주세요!')
    elif signal_color == 'yellow':
        print('노란불입니다. 서둘러주세요!')
    elif signal_color == 'red':
        print('빨간불입니다. 잠시 기다려주세요!')
    else:
        print('잘못된 색입니다. 다시 입력해주세요!')

print('신호등을 종료합니다.')