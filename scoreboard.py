from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250 )
        self.update_scoreboard() #so that after the new level font is same

    def update_scoreboard(self):
        self.clear()#so that it not over writes on the previous one
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def increase_level(self):
        self.level+=1
        self.update_scoreboard()#so that after the new level font remain the same

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)