from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))
        self.goto(-25,-25)
        self.write(f"Your final Level: {self.level}", align="center", font=("Courier", 20, "normal"))
