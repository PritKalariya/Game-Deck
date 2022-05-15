# this is the main file.
# To start the project, execute this file

from tkinter import *
import os


def login():
    main.destroy()
    os.system('python login.py')


# main window gui
main = Tk()
main.title("Welome Game Deck!!")
main.geometry("1377x768")
main.resizable(0, 0)
main.configure(background='white')


# bg for tkinter window
main_bg = Label(main)
main_bg.place(relx=0, rely=0, width=1377, height=768)
main_img = PhotoImage(file="./images/pages/welcome_to_game_deck.png")
main_bg.configure(image=main_img)


# Display continue btn, linking to login page after the animation is complete.
# Delay the btn for 5 second
def continue_btn():
    # cont_bg = Label(main)
    cont_img = PhotoImage(file="./images/buttons/continue_btn.png")
    cont_btn = Button(main)
    cont_btn.configure(
        text="login",
        # image=cont_img,
        bg="black",
        fg="white",
        borderwidth="0",
        cursor="hand2",
        font=("Arial", 20),
        command=login
    )
    cont_btn.place(x=200, y=550)
continue_btn()
# main.after(5000, lambda: continue_btn())


main.mainloop()