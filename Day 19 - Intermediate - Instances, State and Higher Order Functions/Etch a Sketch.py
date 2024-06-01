# Etch a Sketch App
# W = Forward
# S = Backward
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

import turtle as t

T = t.Turtle()
S = t.Screen()

tim = T


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def left():
    tim.left(45)
    tim.heading()


def right():
    tim.right(45)
    tim.heading()


def clear():
    tim.clear()  # Clear out the drawing (if any)
    tim.reset()  # Reset the turtle to original position


S.listen()
t.onkey(forward, "w")
t.onkey(backward, "s")
t.onkey(left, "a")
t.onkey(right, "d")
t.onkey(clear, "c")


S.exitonclick()
