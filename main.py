from idlelib.colorizer import color_config
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()

screen.colormode(255)
def make_dashes(distance):
    for i in range(distance):
        if int(i % 3) == 0:
            timmy.forward(3)
        else:
            timmy.penup()
            timmy.forward(3)
        timmy.pendown()

def make_shapes(sides):
    angle = 360 / sides
    r = random.randint(1, 256)
    g = random.randint(1, 256)
    b = random.randint(1, 256)
    timmy.pencolor(r, g, b)

    for turns in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for i in range(10):
    if i >= 3:
        make_shapes(i)








screen.exitonclick()