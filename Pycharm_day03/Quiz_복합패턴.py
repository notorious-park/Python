import turtle as t

color = ['blue','yellow','purple','cyan','magenta','violet','red','green']
angle = 45
distance = 10
thick = 1
t.left(90)

for i in range(45):
    thick += 1
    distance += 5
    t.color(color[i%8])
    t.pensize(thick)
    t.forward(distance)
    t.left(angle)

t.done()