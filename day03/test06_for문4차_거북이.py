#터틀1차 - 원 그리기
# import turtle as t
#
# num_circle = 100
# radius = 100
#
# t.bgcolor('black')
# t.color('red')
# t.speed(0)
# input('')
#
# for _ in range(num_circle): # _ : 아무 의미 없는 변수로 공란처리하면 오류떠서 임의로 해놓는 것
#     # t.left(270)
#     t.circle(radius)
#     t.left(180/num_circle)
#
# t.done()


#터틀2차 - 점섬 그리기
# import  turtle as t
#
# t.pensize(8)
# t.color('green')
# t.speed(5)
#
# for x in range(10):
#     t.forward(30)
#     t.penup()
#     t.forward(30)
#     t.pendown()
    # t.forward(30)
    # t.penup()
    # t.left(90)
    # t.forward(30)
    # t.penup()
    # t.forward(30)
    # t.pendown()
    # t.left(90)
    # t.forward(30)
    # t.penup()
    # t.forward(30)
    # t.pendown()
    # t.left(90)
    # t.forward(30)
    # t.penup()
    # t.forward(30)
    # t.pendown()

# t.done()

#터틀3차 - 바둑판 그리기
import turtle
t = turtle.Turtle()
t.shape('turtle')

dot_distance = 25
width = 10
height = 10

t.color('red')
t.pensize(3)
t.penup()
for y in range(height):
    for i in range(width):
        t.dot()
        t.forward(dot_distance)

    t.backward(dot_distance * width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)
turtle.done()

