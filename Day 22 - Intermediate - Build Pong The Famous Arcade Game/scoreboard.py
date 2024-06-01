from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,220)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100,220)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        
    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        if self.r_score > self.l_score and self.r_score != self.l_score:
            score_game = "Right Paddle Win."
        else:
            score_game = "Left Paddle Win."
        self.clear()
        self.goto(0,0)
        self.write(f"{score_game} Game Over", align="center", font=("Courier", 30, "normal"))
        