from turtle import Turtle, Screen

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("orange", "cyan1")
my_turtle.width(3)


def segitiga_r():
    my_turtle.down()
    my_turtle.forward(100)
    my_turtle.left(120)
    my_turtle.forward(100)
    my_turtle.left(120)
    my_turtle.forward(100)
    my_turtle.right(240)
    my_turtle.up()
    my_turtle.home()


def segitiga_l():
    my_turtle.down()
    my_turtle.backward(100)
    my_turtle.right(120)
    my_turtle.backward(100)
    my_turtle.right(120)
    my_turtle.backward(100)
    my_turtle.left(240)
    my_turtle.up()
    my_turtle.home()


# segitiga_l()
# segitiga_r()
while True:
    my_turtle.forward(200)
    my_turtle.left(170)
    if abs(my_turtle.pos()) < 1:
        break

for steps in range(100):
    for c in ("blue", "red", "green"):
        my_turtle.color(c)
        my_turtle.forward(steps)
        my_turtle.right(30)

my_screen = Screen()
my_screen.exitonclick()
