from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, x_cor=370, paddle_color="white"):
        super().__init__()
        self.shape("square")
        self.color(paddle_color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor,0)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        