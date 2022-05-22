import html
import sys
import git


sys.path.append(git.Repo('.', search_parent_directories=True).working_tree_dir)
from manage_profiles import UserProfile

user_profile = UserProfile()


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        with open("../active_user.txt", "r") as f:
            self.ACTIVE_USER = f.read()
        self.high_score = user_profile.get_score("quiz_game", self.ACTIVE_USER)
        self.question_list = q_list
        self.current_question = None


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            user_profile.update_score("quiz_game", self.score, self.ACTIVE_USER)
            return True
        else:
            return False