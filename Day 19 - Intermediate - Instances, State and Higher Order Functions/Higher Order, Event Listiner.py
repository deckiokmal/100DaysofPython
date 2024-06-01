import turtle as t

T = t.Turtle()
S = t.Screen()

tim = T


def move_forwards():
    tim.forward(10)


S.listen()
S.onkey(key="space", fun=move_forwards)  # Function as an input


S.exitonclick()
