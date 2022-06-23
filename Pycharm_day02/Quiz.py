import turtle
import math


turtle.color('red')
turtle.pensize(5)

angle_1 = 90
angle_2 = 45
angle_3 = 135
width = 100
forward_diagonal = math.sqrt(width**2+width**2)

# 1.사각형 그리기
turtle.right(angle_1)
turtle.forward(width)

turtle.right(angle_1)
turtle.forward(width)

turtle.right(angle_1)
turtle.forward(width)

turtle.right(angle_1)
turtle.forward(width)

# 2.대각선 그리기
turtle.right(angle_3)
turtle.forward(forward_diagonal)

turtle.right(angle_3)
turtle.forward(width)

turtle.right(angle_3)
turtle.forward(forward_diagonal)

turtle.left(angle_3)
turtle.forward(width)

# 3. 지붕 그리기
turtle.left(angle_2)
turtle.forward(forward_diagonal/2)

turtle.left(angle_1)
turtle.forward(forward_diagonal/2)

turtle.done()

