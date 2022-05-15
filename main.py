from tkinter import *
from tkinter import messagebox
import os


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

def profile():
    main.withdraw()
    os.system('python profile.py')
    main.deiconify()

def instructions():
    main.withdraw()
    os.system('python instructions.py')
    main.deiconify()

def exit():
    dummy = Tk()
    dummy.destroy()
    messagebox.showinfo("Exit", "Thank you for playing Game Deck!! \nSee you soon.")
    main.destroy()


# Main window GUI
main = Tk()
main.title("Game Deck")
main.geometry("1377x768")
main.resizable(0, 0)
main.configure(bg="white")


# bg for tkinter window
main_bg = Label(main)
main_bg.place(relx=0, rely=0, width=1377, height=768)
image = PhotoImage(file="./images/pages/main.png")
main_bg.configure(image=image)


# Game buttons
# row 1
snake_game_btn = Button(main, text ="PLAY",bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=snake)
snake_game_btn.place(x=320, y=352.5)

quiz_game_btn = Button(main, text ="PLAY", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=quiz_game)
quiz_game_btn.place(x=636, y=352.5)

pong_game_btn = Button(main, text ="PLAY", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=pong)
pong_game_btn.place(x=948, y=354)

# row 2
turtle_crossing_btn = Button(main, text ="PLAY",bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=turtle_crossing)
turtle_crossing_btn.place(x=320, y=678)

hangman_btn = Button(main, text ="PLAY", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=hangman)
hangman_btn.place(x=638, y=680)

profile_btn = Button(main, text ="USER", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=profile)
profile_btn.place(x=953, y=678)


# instruction btn
instruction_btn = Button(main, bg="#0074e4", relief="flat", width=3, height=2, cursor="hand2", command=instructions)
instruction_btn.place(x=30, y=26)

# exit btn
exit_btn = Button(main, bg="#0074e4", relief="flat", width=4, height=2, cursor="hand2", command=exit)
exit_btn.place(x=1312, y=26)


main.mainloop()