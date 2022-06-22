import turtle

in_color = input('원의 색깔을 입력하세요(R/G/B/Etc)')
is_filled = input('원의 색깔을 채우시겠습니까?')

if in_color == 'R' or in_color == 'r':
    color = 'red'
elif in_color == 'B' or in_color == 'b':
    color = 'blue'
elif in_color == 'G' or in_color == 'g':
    color = 'green'
else: color = 'black'

turtle.begin_fill()

turtle.color(color)
turtle.pensize(20)
turtle.circle(200)

if is_filled == 'Y' or is_filled == 'y':
    turtle.end_fill()
else: pass

turtle.done()