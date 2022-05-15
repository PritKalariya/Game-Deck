from tkinter import *

from matplotlib import image


main = Tk()
main.title("Instructions")
main.geometry("1377x768")
main.resizable(0, 0)
main.configure(bg="black")

# bg for tkinter window
window_bg = Label(main)
window_bg.place(x=0, y=0, width=1377, height=768)
bg = PhotoImage(file="./images/pages/instructions.png")
window_bg.configure(image=bg)


main.mainloop()