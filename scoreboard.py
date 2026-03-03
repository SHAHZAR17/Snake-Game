from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=-1
        # self.highscore=0
        with open("data.txt") as f:
            cont = f.read()
            self.highscore=int(cont)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,277)
        self.update()
        self.inc()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score = {self.highscore}", False, "center", ("Arial", 15, "normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open('data.txt','w') as f:
                f.write(f"{self.highscore}")
        self.score=0
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", False, "center", ("Arial", 15, "normal"))

    def inc(self):
        self.score+=1
        self.update()