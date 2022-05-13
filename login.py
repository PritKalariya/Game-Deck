from tkinter import *
import os
import sqlite3
from tkinter import *
from tkinter import messagebox

from matplotlib import image


def login():
    main.destroy()
    os.system('python main.py')


def verify_login():
    if username_entry.get() != "" and password_entry.get() != "":
        username = username_entry.get()
        password = password_entry.get()

        with sqlite3.connect("./database/users.db") as db:
            cur = db.cursor()
        find_user = cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = {password}")
        result = find_user.fetchall()
        # print(result)

        if result:
            username_entry.delete(0, END)
            password_entry.delete(0, END)

            dummy = Tk()
            dummy.withdraw()
            messagebox.showinfo("Login Successful", "Welcome to Game Deck!!")
            login()
        else:
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo("Login Failed", "Invalid username or password")
    else:
        messagebox.showinfo("Empty Fields", "Please enter valid username and password.")


# design a login page
main = Tk()
main.title("Login Page")
main.geometry("450x700")
main.resizable(0, 0)
main.configure(background="white")


window_bg = Label(main)
window_bg.place(relx=0, rely=0, width=450, height=700)
img = PhotoImage(file="./images/pages/login.png")
window_bg.configure(image=img)


username_entry = Entry(main)
username_entry.place(relx=-0.100, rely=-0.034, width=370, height=24)
username_entry.configure(
    background="white",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0
)
username_entry.place(x=100, y=200)

password_entry = Entry(main)
password_entry.place(relx=-0.100, rely=-0.055, width=370, height=24)
password_entry.configure(
    background="white",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0,
    show="*"
)
password_entry.place(x=100, y=300)


login_bg = Label(main)
login_img = PhotoImage(file="./images/buttons/login_btn.png")
login_btn = Button(main)
login_btn.configure(
    text="login",
    image=login_img,
    bg="white",
    fg="red",
    borderwidth="0",
    font=("Arial", 20),
    command=login
)
login_btn.place(x=145, y=480)


main.mainloop()