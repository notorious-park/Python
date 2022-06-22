#T-map  : 박성실
#도로주행 : 박요온

#정육각형 회전이동_수정후
import turtle as t

t.color('red')
t.pensize(5)
num_h = 6             # 육각형
distance = 100        # 변의길이
turn_ang = 360/num_h  # 각도

for _ in range(num_h):
    for _ in range(num_h):
        t.forward(distance)
        t.left(turn_ang)
    t.penup()
    t.forward(distance)
    t.pendown()
    t.right(turn_ang)

t.done()