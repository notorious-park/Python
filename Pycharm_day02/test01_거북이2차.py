# import turtle
#
# size = input('크기를 입력하세요. [100~300]')
# color = input('선의 색깔을 입력하세요. [red, green, blue]')
# thick = input('선의 굵기를 입력하세요. [1~30]')
#
# angle = 90
# thick = int(thick)
# size = int(size)
#
# turtle.color(color)
# turtle.pensize(thick)
#
# turtle.left(angle)
# turtle.forward(size)
#
# turtle.left(angle)
# turtle.forward(size)
#
# turtle.left(angle)
# turtle.forward(size)
#
# turtle.left(angle)
# turtle.forward(size)
#
# turtle.done()

import turtle

size = input('크기를 입력하세요. [100~300]')
color = input('선의 색깔을 입력하세요. [red, green, blue]')
thick = input('선의 굵기를 입력하세요. [1~30]')

angle = 120
thick = int(thick)
size = int(size)

turtle.color(color)
turtle.pensize(thick)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.done()