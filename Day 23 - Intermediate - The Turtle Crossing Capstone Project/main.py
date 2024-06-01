import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    cars.create_car()
    cars.move_cars()

    level.update_scoreboard()

    # Detect Collision with top Wall and update score level
    if player.ycor() >= 280:
        player.finish_position()
        level.update_level()
        cars.level_up()

    # Detect Collision with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()