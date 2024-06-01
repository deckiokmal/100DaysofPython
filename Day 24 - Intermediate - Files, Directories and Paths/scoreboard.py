from turtle import Turtle


ALIGMENT = "center"
FONT = ("courier", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.reset()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt","r") as file:
            score = file.read()
            self.high_score = int(score)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt","w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
