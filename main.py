from tkinter import *
import os
from manage_profiles import UserProfile


# Game open functions
def pong():
    main.withdraw()
    if  os.getcwd().split('\\')[-1] == 'Pong Game':
        os.system("python pong.py")
    else:
        os.chdir("Pong Game")
        os.system("python pong.py")
        os.chdir("..")
    main.deiconify()

def snake():
    main.withdraw()
    if  os.getcwd().split('\\')[-1] == 'Snake Game':
        os.system("python main.py")
    else:
        os.chdir("Snake Game")
        os.system("python main.py")
        os.chdir("..")
    main.deiconify()

def quiz_game():
    main.withdraw()
    if  os.getcwd().split('\\')[-1] == 'Quiz Game (GUI)':
        os.system("python main.py")
    else:
        os.chdir("Quiz Game (GUI)")
        os.system("python main.py")
        os.chdir("..")
    main.deiconify()

def turtle_crossing():
    main.withdraw()
    if  os.getcwd().split('\\')[-1] == 'Turtle Crossing Game':
        os.system("python main.py")
    else:
        os.chdir("Turtle Crossing Game")
        os.system("python main.py")
        os.chdir("..")
    main.deiconify()

def hangman():
    main.withdraw()
    if  os.getcwd().split('\\')[-1] == 'Hangman Game':
        os.system("python hangman.py")
    else:
        os.chdir("Hangman Game")
        os.system("python hangman.py")
        os.chdir("..")
    main.deiconify()

def logout():
    main.destroy()
    os.system('python login.py')


# Database
userprofile = UserProfile()
# userprofile.display_db()


# Main window GUI
main = Tk()
main.title("Game Deck")
main.geometry("1377x768")
main.resizable(0, 0)
main.configure(bg="white")


btn1 = Button(main, text="Pong Game", bg="black", fg="white", font=("Arial", 20), command=pong)
btn1.place(x=100, y=100)

btn2 = Button(main, text="Snake Game", bg="black", fg="white", font=("Arial", 20), command=snake)
btn2.place(x=400, y=100)

btn3 = Button(main, text="Quiz Game", bg="black", fg="white", font=("Arial", 20), command=quiz_game)
btn3.place(x=800, y=100)

btn4 = Button(main, text="Turtle Crossing Game", bg="black", fg="white", font=("Arial", 20), command=turtle_crossing)
btn4.place(x=200, y=400)

btn5 = Button(main, text="Hangman", bg="black", fg="white", font=("Arial", 20), command=hangman)
btn5.place(x=200, y=500)


# buttons
logout = Button(main, text="Logout", bg="black", fg="white", font=("Arial", 20), command=logout)
logout.place(x=100, y=600)


main.mainloop()