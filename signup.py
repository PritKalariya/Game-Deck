from tkinter import *
from tkinter import messagebox
import os
from manage_profiles import UserProfile
import sqlite3


userprofile = UserProfile()


def signup():
    main.destroy()
    os.system('python login.py')


def register_user():
    if name_entry.get() != "" and username_entry != "" and password_entry.get() != "" and email_entry != "" and age_entry != "" and dob_entry != "":

        username = username_entry.get()
        name = name_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        age = age_entry.get()
        dob = dob_entry.get()

        # check for duplicate username and email id. if not duplicate, then register the user.
        # if username in userprofile.get_col_entires(username):
        #     dummy = Tk()
        #     dummy.withdraw()
        #     messagebox.showinfo("Registration Failed", "Username already exists.")
        # elif email in userprofile.get_col_entires(email):
        #     dummy = Tk()
        #     dummy.withdraw()
        #     messagebox.showinfo("Registration Failed", "Email already registered.")
        # else:
            # add new user
        userprofile.register_new_user(name, username, email, password, age, dob)

        name_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)
        age_entry.delete(0, END)
        dob_entry.delete(0, END)

        dummy = Tk()
        dummy.withdraw()
        messagebox.showinfo("User Registered", "New user registered. Enjoy Game deck!!")
        signup()
    else:
        messagebox.showinfo("Empty Fields", "Please make sure all the feilds are filled.")


# design a signup page
main = Tk()
main.title("Login Page")
main.geometry("1200x700")
main.resizable(0, 0)
main.configure(background="white")


# bg image for the tkinter window
label = Label(main)
label.place(relx=0, rely=0, width=1200, height=700)
img = PhotoImage(file="./images/pages/signup.png")
label.configure(image=img)


# input feilds
name_entry = Entry(main)
name_entry.place(relx=0, rely=0, width=370, height=24)
name_entry.configure(
    background="white",
    font="Arial",
    fg="black",
    relief="flat"
)
name_entry.place(x=125, y=215)

username_entry = Entry(main)
username_entry.place(relx=0, rely=0, width=370, height=24)
username_entry.configure(
    background="white",
    font="Arial",
    fg="black",
    relief="flat"
)
username_entry.place(x=125, y=340)

password_entry = Entry(main)
password_entry.place(relx=0, rely=0, width=370, height=24)
password_entry.configure(
    background="white",
    font="Arial",
    fg="black",
    relief="flat"
)
password_entry.place(x=125, y=468)

email_entry = Entry(main)
email_entry.place(relx=0, rely=0, width=370, height=24)
email_entry.configure(
    background="white",
    font="Arial",
    fg="black",
    relief="flat"
)
email_entry.place(x=704, y=212)

age_entry = Entry(main)
age_entry.place(relx=0, rely=0, width=370, height=24)
age_entry.configure(
    background="white",
    font="Arial",
    fg="black",
    relief="flat"
)
age_entry.place(x=704, y=337)

dob_entry = Entry(main)
dob_entry.place(relx=0, rely=0, width=370, height=24)
dob_entry.configure(
    background="white",
    font="Arial",
    fg="black",
    relief="flat"
)
dob_entry.place(x=704, y=465)


# register buttons
register_bg = Label(main)
register_img = PhotoImage(file="./images/buttons/register_btn.png")
register_btn = Button(main)
register_btn.configure(
    text="register",
    image=register_img,
    bg="white",
    fg="white",
    borderwidth="0",
    cursor="hand2",
    font=("Arial", 20),
    command=register_user
)
register_btn.place(x=505, y=580)


main.mainloop()