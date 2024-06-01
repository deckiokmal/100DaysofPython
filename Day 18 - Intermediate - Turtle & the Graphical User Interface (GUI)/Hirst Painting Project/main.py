import turtle
import random
from colorgram import color_list


T = turtle.Turtle()
S = turtle.Screen()

turtle.colormode(255)
t = T
t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(250)
t.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    t.penup()
    t.dot(20, random.choice(color_list))
    t.forward(50)
    t.pendown()

    if dot_count % 10 == 0:
        t.penup()
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = S
screen.exitonclick()
