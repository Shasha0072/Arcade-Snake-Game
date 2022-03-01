from turtle import Turtle
ALINGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALINGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align="center", font=FONT)
