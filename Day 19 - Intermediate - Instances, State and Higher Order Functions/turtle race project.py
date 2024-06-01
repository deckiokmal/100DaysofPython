from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
print(f"turtle you've choice is {user_bet} color.")

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.shape("turtle")
# tim.color("green")
# tim.setposition(-240, 0)

# timi = Turtle(shape="turtle")
# timi.penup()
# timi.color("red")
# timi.setposition(-240, 25)

colors = ("red", "orange", "green", "blue", "purple", "black")
num_turtle = 6
x_position = -240
y_position = -90
all_turtles = []

for turtle_index in range(0, num_turtle):
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.penup()
    turtle_obj.color(colors[turtle_index])
    turtle_obj.setposition(x_position, y_position)
    y_position += 30
    all_turtles.append(turtle_obj)


is_race_on = False

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! the {winning_color} turtle is the winner!")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
