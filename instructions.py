from tkinter import *

from matplotlib import image


class Instructions_page():
    def __init__(self):
        pass

    def gui(self):
        self.main = Tk()
        self.main.title("Instructions")
        self.main.geometry("1377x768")
        self.main.resizable(0, 0)
        self.main.configure(bg="black")


        # bg for tkinter window
        self.window_bg = Label(self.main)
        self.window_bg.place(x=0, y=0, width=1377, height=768)
        self.bg = PhotoImage(file="./images/pages/instructions.png")
        self.window_bg.configure(image=self.bg)


        self.main.mainloop()


demo = Instructions_page()
demo.gui()