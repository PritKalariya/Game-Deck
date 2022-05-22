from turtle import Turtle
import sys
import git


# Append the root direcctory of git repository.
sys.path.append(git.Repo('.', search_parent_directories=True).working_tree_dir)
from manage_profiles import UserProfile


user_profile = UserProfile()
ALIGN = "center"
FONT = ("courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../active_user.txt", "r") as f:
            self.ACTIVE_USER = f.read()
        self.high_score = user_profile.get_score("snake_game", self.ACTIVE_USER)
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            user_profile.update_score("snake_game", self.high_score, self.ACTIVE_USER)
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"Game Over", align=ALIGN, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()