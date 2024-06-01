from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


# Create and move a padlle
l_paddle = Paddle(380, "blue")
r_paddle = Paddle(-380, "red")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    
    scoreboard.update_scoreboard()
    ball.move()
    
    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    # Detect collision with r_paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        
    # Detect l_paddle miss the ball
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.update_l_score()
    
    # Detect r_paddle miss the ball
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.update_r_score()

# End of line
screen.exitonclick()