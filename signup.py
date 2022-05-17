from tkinter import *
from tkinter import messagebox
from manage_profiles import UserProfile


class Signup_page():
    def __init__(self):
        pass


    def gui(self):
        self.userprofile = UserProfile()

        # design a signup page
        # self.main = Tk()
        self.main = Toplevel()
        self.main.title("Login Page")
        self.main.geometry("1200x700")
        self.main.resizable(0, 0)
        self.main.configure(background="white")


        # bg image for the tkinter window
        self.label = Label(self.main)
        self.label.place(relx=0, rely=0, width=1200, height=700)
        self.img = PhotoImage(file="./images/pages/signup.png")
        self.label.configure(image=self.img)


        # input feilds
        self.name_entry = Entry(self.main)
        self.name_entry.place(relx=0, rely=0, width=370, height=24)
        self.name_entry.configure(
            background="#121212",
            font="Arial",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.name_entry.place(x=125, y=215)

        self.username_entry = Entry(self.main)
        self.username_entry.place(relx=0, rely=0, width=370, height=24)
        self.username_entry.configure(
            background="#121212",
            font="Arial",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.username_entry.place(x=125, y=340)

        self.password_entry = Entry(self.main)
        self.password_entry.place(relx=0, rely=0, width=370, height=24)
        self.password_entry.configure(
            background="#121212",
            font="Arial",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.password_entry.place(x=125, y=468)

        self.email_entry = Entry(self.main)
        self.email_entry.place(relx=0, rely=0, width=370, height=24)
        self.email_entry.configure(
            background="#121212",
            font="Arial",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.email_entry.place(x=704, y=212)

        self.age_entry = Entry(self.main)
        self.age_entry.place(relx=0, rely=0, width=370, height=24)
        self.age_entry.configure(
            background="#121212",
            font="Arial",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.age_entry.place(x=704, y=337)

        self.dob_entry = Entry(self.main)
        self.dob_entry.place(relx=0, rely=0, width=370, height=24)
        self.dob_entry.configure(
            background="#121212",
            font="Arial",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.dob_entry.place(x=704, y=465)


        # register buttons
        self.register_bg = Label(self.main)
        self.register_img = PhotoImage(file="./images/buttons/register_btn.png")
        self.register_btn = Button(self.main)
        self.register_btn.configure(
            text="register",
            image=self.register_img,
            bg="#121212",
            fg="#121212",
            relief="flat",
            borderwidth="0",
            cursor="hand2",
            font=("Arial", 20),
            command=self.register_user
        )
        self.register_btn.place(x=505, y=580)

        self.main.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.main.mainloop()


    # Helper methods
    def signup(self):
        self.main.destroy()
        from login import Login_page
        Login_page().gui()


    def register_user(self):
        if self.name_entry.get() != "" and self.username_entry != "" and self.password_entry.get() != "" and self.email_entry != "" and self.age_entry != "" and self.dob_entry != "":
            username = self.username_entry.get()
            name = self.name_entry.get()
            password = self.password_entry.get()
            email = self.email_entry.get()
            age = self.age_entry.get()
            dob = self.dob_entry.get()

            # add new user
            self.userprofile.register_new_user(name, username, email, password, age, dob)

            self.name_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.age_entry.delete(0, END)
            self.dob_entry.delete(0, END)

            self.dummy = Tk()
            self.dummy.destroy()
            messagebox.showinfo("User Registered", "New user registered. Enjoy Game deck!!")
            self.signup()
        else:
            messagebox.showerror("Empty Fields", "Please make sure all the feilds are filled.")


    def confirm_exit(self):
        self.dummy = Tk()
        self.dummy.destroy()
        yes_no = messagebox.askyesno("Confirm exit", "Are you sure you want to exit?")
        if yes_no:
            self.main.destroy()
            from login import Login_page
            Login_page().gui()


# demo = Signup_page()
# demo.gui()