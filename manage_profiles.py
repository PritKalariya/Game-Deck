import sqlite3
from tkinter import Tk
from tkinter import messagebox


class UserProfile():
    def __init__(self, **kwargs):
        self.name = ""
        self.username = ""
        self.email = ""
        self.password = ""
        self.age = ""
        self.dob = ""
        self.pong_game = 0
        self.snake_game = 0
        self.quiz_game = 0
        self.turtle_crossing_game = 0
        self.hangman = 0


    def create_table(self):
        conn = sqlite3.connect('./database/users.db')
        c = conn.cursor()
        c.execute(
            "CREATE TABLE users (name TEXT, username TEXT PRIMARY KEY, email TEXT, password PASSWORD, age INTEGER, dob TEXT, pong_game INTEGER, snake_game INTEGER, quiz_game INTEGER, turtle_crossing_game INTEGER, hangman INTEGER)"
        )
        conn.commit()
        conn.close()


    def display_db(self):
        try:
            conn = sqlite3.connect('./database/users.db')
            c = conn.cursor()
            c.execute("SELECT * FROM users")
            print(c.fetchall())
            conn.commit()
            conn.close()
        except sqlite3.DatabaseError:
            dummy = Tk()
            dummy.withdraw()
            messagebox.showerror("Error", "Database not found")


    def register_new_user(self, name, username, email, password, age, dob):
        conn = sqlite3.connect('./database/users.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [name, username, email, password, age, dob, 0, 0, 0, 0, 0]
        )
        conn.commit()
        conn.close()


    def update_score(self, game_name, score, username):
        conn = sqlite3.connect('./database/users.db')
        c = conn.cursor()
        c.execute(
            f"UPDATE users SET {game_name} = {score} WHERE username = '{username}'"
        )
        conn.commit()
        conn.close()

    def delete_user(self, username):
        conn = sqlite3.connect('./database/users.db')
        c = conn.cursor()
        c.execute(
            f"DELETE FROM users WHERE username = '{username}'"
        )
        conn.commit()
        conn.close()