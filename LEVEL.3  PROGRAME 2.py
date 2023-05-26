import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size+20)
    turtle.right(angle+20)
    turtle.forward(shift+10)
    draw_circle(size+20, angle+20,shift+10)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)


