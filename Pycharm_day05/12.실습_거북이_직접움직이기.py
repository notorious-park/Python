
import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def blank():
    t.clear()

t.shape('turtle')
t.speed(10)
t.bgcolor('black')
t.color('white')
t.pensize(5)

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank,"Escape")
t.onkeypress(pen_up,"Q")
t.onkeypress(pen_down,"W")
t.listen()
t.mainloop()


'''
# 마우스클릭으로 이어그리기
import turtle as t

t.speed(1)
t.pensize(5)
t.shape("turtle")

# t.hideturtle()
t.onscreenclick(t.goto)
t.mainloop()
'''