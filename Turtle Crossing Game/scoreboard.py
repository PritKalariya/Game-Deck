from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        with open("data.txt", mode="r") as data:
            self.highestlevel = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} \tHighest Level: {self.highestlevel}", align="left", font=FONT)


    def level_up(self):
        self.level += 1
        if self.level > self.highestlevel:
            self.highestlevel = self.level
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highestlevel}")
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game OVER!", align="center", font=FONT)