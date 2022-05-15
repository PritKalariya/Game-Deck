# this is the main file.
# To start the project, execute this file

from tkinter import *
from login import Login_page


class Game_deck():
    def __init__(self):
        # main window gui
        self.main = Tk()
        self.main.title("Welome Game Deck!!")
        self.main.geometry("1377x768")
        self.main.resizable(0, 0)
        self.main.configure(background='white')


        # bg for tkinter window
        self.main_bg = Label(self.main)
        self.main_bg.place(relx=0, rely=0, width=1377, height=768)
        self.main_img = PhotoImage(file="./images/pages/welcome_to_game_deck.png")
        self.main_bg.configure(image=self.main_img)


        # Display continue btn, linking to login page after the animation is complete.
        # Delay the btn for 5 second
        def continue_btn():
            self.cont_bg = Label(self.main)
            self.cont_img = PhotoImage(file="./images/buttons/continue_btn.png")
            self.cont_btn = Button(self.main)
            self.cont_btn.configure(
                text="login",
                image=self.cont_img,
                bg="black",
                fg="white",
                borderwidth="0",
                cursor="hand2",
                font=("Arial", 20),
                relief="flat",
                command=self.login
            )
            self.cont_btn.place(x=200, y=550)
        # continue_btn()
        self.main.after(5000, lambda: continue_btn())


        self.main.mainloop()


    def login(self):
        self.main.withdraw()
        Login_page().gui()



game_deck = Game_deck()