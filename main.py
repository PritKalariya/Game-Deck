from tkinter import *
from tkinter import messagebox
import os




class Main_page():
    def __init__(self):
        pass


    def gui(self):
        # Main window GUI
        # self.main = Tk()
        self.main = Toplevel()
        self.main.title("Game Deck")
        self.main.geometry("1377x768")
        self.main.resizable(0, 0)
        self.main.configure(bg="white")


        # bg for tkinter window
        self.main_bg = Label(self.main)
        self.main_bg.place(relx=0, rely=0, width=1377, height=768)
        self.image = PhotoImage(file="./images/pages/main.png")
        self.main_bg.configure(image=self.image)


        # Game buttons
        # row 1
        self.snake_game_btn = Button(self.main, text ="PLAY",bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=self.snake)
        self.snake_game_btn.place(x=320, y=352.5)

        self.quiz_game_btn = Button(self.main, text ="PLAY", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=self.quiz_game)
        self.quiz_game_btn.place(x=636, y=352.5)

        self.pong_game_btn = Button(self.main, text ="PLAY", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=self.pong)
        self.pong_game_btn.place(x=948, y=354)

        # row 2
        self.turtle_crossing_btn = Button(self.main, text ="PLAY",bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=self.turtle_crossing)
        self.turtle_crossing_btn.place(x=320, y=678)

        self.hangman_btn = Button(self.main, text ="PLAY", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=self.hangman)
        self.hangman_btn.place(x=638, y=680)

        self.profile_btn = Button(self.main, text ="USER", bg="#0074e4", relief="flat", width=10, height=1, cursor="hand2", command=self.profile)
        self.profile_btn.place(x=953, y=678)


        # instruction btn
        self.inst_btn = Label(self.main)
        self.ins_bg = PhotoImage(file="./images/buttons/instructions_btn.png")
        self.instruction_btn = Button(self.main, bg="#121212", relief="flat", image=self.ins_bg ,width=70, height=70, cursor="hand2", command=self.instructions)
        self.instruction_btn.place(x=5, y=7)

        # exit btn
        self.exit_btn = Label(self.main)
        self.exit_bg = PhotoImage(file="./images/buttons/exit_btn (2).png")
        self.exit_btn = Button(self.main, bg="#121212", relief="flat", image= self.exit_bg ,width=70, height=70, cursor="hand2", command=self.exit)
        self.exit_btn.place(x=1294, y=7)

        self.main.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.main.mainloop()



    # helper methods
    def run_file(self, name):
        if os.getcwd().split('\\')[-1] == name:
            os.system("python main.py")
        else:
            os.chdir(name)
            os.system("python main.py")
            os.chdir("..")


    def pong(self):
        self.main.withdraw()
        self.run_file("Pong Game")
        self.main.deiconify()

    def snake(self):
        self.main.withdraw()
        self.run_file("Snake Game")
        self.main.deiconify()

    def quiz_game(self):
        self.main.withdraw()
        self.run_file("Quiz Game (GUI)")
        self.main.deiconify()

    def turtle_crossing(self):
        self.main.withdraw()
        self.run_file("Turtle Crossing Game")
        self.main.deiconify()

    def hangman(self):
        self.main.withdraw()
        self.run_file("Hangman Game")
        self.main.deiconify()

    def profile(self):
        self.main.withdraw()
        from profile import Profile_page
        Profile_page().gui()

    def instructions(self):
        self.main.withdraw()
        from instructions import Instructions_page
        Instructions_page().gui()

    def exit(self):
        dummy = Tk()
        dummy.destroy()
        messagebox.showinfo("Exit", "Thank you for playing Game Deck!! \nSee you soon.")
        self.main.destroy()

    def confirm_exit(self):
        self.dummy = Tk()
        self.dummy.destroy()
        yes_no = messagebox.askyesno("Confirm selection", "Are you sure you want to exit?")
        if yes_no:
            self.exit()


# demo = Main_page()
# demo.gui()