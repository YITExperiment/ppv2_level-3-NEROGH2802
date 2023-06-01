import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angle,shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 10,angle+10,shift+1)

t.bgcolor('black')
t.speed('fast')
t.pensize(40)

draw_circle(30,0,1)

ti.sleep(3)
t.hideturtle()
