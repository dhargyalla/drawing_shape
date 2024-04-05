import turtle
from turtle import Turtle,Screen
import random
color = ["red","blue","yellow","orange","tan","mango","blue","yellow","orange","tan","mango"]
tim = Turtle()


def make_shape(sides):

    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for sides in range(3, 11):
    make_shape(sides)
    tim.color(random.choice(color))
turtle.done()

#different way to implement this problem
# side = 3
# shape = Turtle()
# while side < 10:
#     angle = round(360 / side,2)
#     for i in range(side):
#         shape.forward(100)
#         shape.right(angle)
#     i -= 2
#     shape.color(color[i])
#     side += 1
# screen = Screen()
# screen.exitonclick()


