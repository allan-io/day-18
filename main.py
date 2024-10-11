from idlelib.colorizer import color_config
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()

screen.colormode(255)
# def make_dashes(distance):
#     for i in range(distance):
#         if int(i % 3) == 0:
#             timmy.forward(3)
#         else:
#             timmy.penup()
#             timmy.forward(3)
#         timmy.pendown()
#
# def make_shapes(sides):
#     angle = 360 / sides
#     r = random.randint(1, 256)
#     g = random.randint(1, 256)
#     b = random.randint(1, 256)
#     timmy.pencolor(r, g, b)
#
#     for turns in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for i in range(10):
#     if i >= 3:
#         make_shapes(i)

def random_walk(distance):
    timmy.speed(10)
    timmy.pensize(10)

    # for _ in range(distance):
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy.pencolor((r, g, b))
        angle = random.choice([90, 180, 270, 0])
        timmy.forward(20)
        timmy.right(angle)

random_walk(10000000)


screen.exitonclick()