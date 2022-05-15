from tkinter import *
import sqlite3
from tkinter import *
from tkinter import messagebox


global ACTIVE_USER
ACTIVE_USER = ""


class Login_page():
    def __init__(self):
        pass


    def gui(self):
        # design a login page
        # self.main = Tk()
        self.main = Toplevel()
        self.main.title("Login Page")
        self.main.geometry("450x700")
        self.main.resizable(0, 0)
        self.main.configure(background="white")


        # bg image for tkinter window
        self.window_bg = Label(self.main)
        self.window_bg.place(relx=0, rely=0, width=450, height=700)
        self.img = PhotoImage(file="./images/pages/login.png")
        self.window_bg.configure(image=self.img)


        # user entry feilds
        self.username_entry = Entry(self.main)
        self.username_entry.place(relx=-0.100, rely=-0.034, width=370, height=24)
        self.username_entry.configure(
            background="white",
            font="Arial",
            foreground="black",
            justify="left",
            relief="flat",
            bd=0
        )
        self.username_entry.place(x=100, y=200)

        self.password_entry = Entry(self.main)
        self.password_entry.place(relx=-0.100, rely=-0.055, width=370, height=24)
        self.password_entry.configure(
            background="white",
            font="Arial",
            foreground="black",
            justify="left",
            relief="flat",
            bd=0,
            show="*"
        )
        self.password_entry.place(x=100, y=300)


        # login btn
        self.login_bg = Label(self.main)
        self.login_img = PhotoImage(file="./images/buttons/login_btn.png")
        self.login_btn = Button(self.main)
        self.login_btn.configure(
            text="login",
            image=self.login_img,
            bg="white",
            fg="red",
            borderwidth="0",
            cursor="hand2",
            font=("Arial", 20),
            command=self.verify_login
        )
        self.login_btn.place(x=160, y=480)


        # Register btn
        self.register = Label(self.main)
        self.register.configure(
            text="Not registered? Register here",
            font=("Arial", 12),
            fg="black",
            bg="white"
        )
        self.register.bind("<Button-1>", self.register_page)
        self.register.place(x=130, y=550)


        self.main.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.main.mainloop()


    # Helper functions
    def login(self):
        self.main.destroy()
        from main import Main_page
        Main_page().gui()


    def set_active_user(self, username):
        global ACTIVE_USER
        ACTIVE_USER = username
        # print(ACTIVE_USER)


    def register_page(self, event):
        self.main.destroy()
        # Importing signup page here to avoid circular import error.
        from signup import Signup_page
        Signup_page().gui()


    def verify_login(self):
        if self.username_entry.get() != "" and self.password_entry.get() != "":
            username = self.username_entry.get()
            password = self.password_entry.get()

            with sqlite3.connect("./database/users.db") as db:
                cur = db.cursor()
            find_user = cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = {password}")
            result = find_user.fetchall()
            # print(result)

            if result:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)

                dummy = Tk()
                dummy.destroy()
                messagebox.showinfo("Login Successful", "Welcome to Game Deck!!")
                self.login()
                self.set_active_user(username)
            else:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showerror("Login Failed", "Invalid username or password")
        else:
            messagebox.showerror("Empty Fields", "Please enter valid username and password.")


    def confirm_exit(self):
        self.dummy = Tk()
        self.dummy.destroy()
        yes_no = messagebox.askyesno("Confirm selection", "Are you sure you want to exit?")
        if yes_no:
            self.main.destroy()


# demo = Login_page()
# demo.gui()