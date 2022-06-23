#T-map  : 박성실
#도로주행 : 박요온

#정육각형 회전이동_수정전
import turtle as t

t.color('red')
t.pensize(5)
num_h = 6

for _ in range(1,7):
    for _ in range(num_h):
        t.forward(50)
        t.left(360/num_h)
    t.penup()
    t.forward(50)
    t.pendown()
    t.right(60)
t.done()