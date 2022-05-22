from turtle import Turtle
import sys
import git


# Append the root direcctory of git repository.
sys.path.append(git.Repo('.', search_parent_directories=True).working_tree_dir)
from manage_profiles import UserProfile


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.userprofile = UserProfile()
        self.level = 1
        with open("../active_user.txt", "r") as f:
            self.ACTIVE_USER = f.read()
        print(self.ACTIVE_USER)
        self.highestlevel = self.userprofile.get_score("turtle_crossing_game", self.ACTIVE_USER)
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
            self.userprofile.update_score("turtle_crossing_game", self.level, self.ACTIVE_USER)
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game OVER!", align="center", font=FONT)