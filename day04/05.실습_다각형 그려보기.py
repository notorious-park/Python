import turtle as t

size_cnt = int(input('변의 갯수를 입력하세요.[3~8}'))
size_len = int(input('변의 길이를 입력하세요.[100~300}'))
c_mod = size_cnt % 3
color = 'red' if c_mod == 0 else 'green' if c_mod == 1 else 'blue'
# 나머지가 0이면 red / 나머지가 1이면 green / 나머지가 2이면 blue

t.color(color)
t.pensize(10)
t.speed(1)
turn_ang = 360/size_cnt

t.begin_fill() #채우기 시작

for _ in range(1):
    for i in range(size_cnt):
        t.forward(size_len)
        t.left(turn_ang)

t.end_fill() #채우기 끝
t.done()