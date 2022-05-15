from tkinter import *
from main import Main_page


class Instructions_page():
    def  __init__(self):
        pass

    def gui(self):
        self.main = Toplevel()
        self.main.title("Instructions")
        self.main.geometry("1377x768")
        self.main.resizable(0, 0)
        self.main.configure(bg="black")


        # bg for tkinter window
        self.window_bg = Label(self.main)
        self.window_bg.place(x=0, y=0, width=1377, height=768)
        self.bg = PhotoImage(file="./images/pages/instructions.png")
        self.window_bg.configure(image=self.bg)


        self.main.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.main.mainloop()


    def on_closing(self):
        self.main.destroy()
        Main_page().gui()


# demo = Instructions_page()
# demo.gui()