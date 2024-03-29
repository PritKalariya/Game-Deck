from tkinter import *
from tkinter import messagebox
from login import Login_page
from main import Main_page
from manage_profiles import UserProfile



class Profile_page():
    def __init__(self):
        # use db connection to load highscores for each game (based on username)
        with open("./active_user.txt", "r") as f:
            self.ACTIVE_USER = f.read()
        # print(self.ACTIVE_USER)
        self.userprofile = UserProfile()
        self.active_user_data = self.userprofile.get_user_data(self.ACTIVE_USER)
        # print(self.active_user_data)



    def gui(self):
        # design a profile page
        self.main = Toplevel()
        self.main.title("Profile")
        self.main.geometry("900x600")
        self.main.resizable(0, 0)
        self.main.configure(background="white")


        # bg image for tkinter window
        self.window_bg = Label(self.main)
        self.window_bg.place(relx=0, rely=0, width=900, height=600)
        self.img = PhotoImage(file="./images/pages/profile.png")
        self.window_bg.configure(image=self.img)


        # Highscores
        self.pong_game = Label(self.main)
        self.pong_game.place(relx=0, rely=0, width=50, height=50)
        self.pong_game.configure(
            text="/",
            background="#121212",
            font=("Arial", 20),
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.pong_game.place(x=426, y=140)

        self.snake_game = Label(self.main)
        self.snake_game.place(relx=0, rely=0, width=50, height=50)
        self.snake_game.configure(
            text=self.active_user_data[0][7],
            background="#121212",
            font=("Arial", 20),
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.snake_game.place(x=692.7, y=140)

        self.quiz_game = Label(self.main)
        self.quiz_game.place(relx=0, rely=0, width=50, height=50)
        self.quiz_game.configure(
            text=self.active_user_data[0][8],
            background="#121212",
            font=("Arial", 20),
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.quiz_game.place(x=426, y=300)

        self.hangman_game = Label(self.main)
        self.hangman_game.place(relx=0, rely=0, width=50, height=50)
        self.hangman_game.configure(
            text=self.active_user_data[0][10],
            background="#121212",
            font=("Arial", 20),
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.hangman_game.place(x=692.7, y=300)

        self.turtle_crossing_game = Label(self.main)
        self.turtle_crossing_game.place(relx=0, rely=0, width=50, height=50)
        self.turtle_crossing_game.configure(
            text=self.active_user_data[0][9],
            background="#121212",
            font=("Arial", 20),
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.turtle_crossing_game.place(x=558.7, y=465)


        # profile image
        self.profile_icon = Label(self.main)
        self.profile_icon.place(relx=0, rely=0, width=130, height=125)
        self.profile_img = PhotoImage(file="./images/profiles/profile_logo.png")
        self.profile_icon.configure(image=self.profile_img)
        self.profile_icon.place(x=112, y=100)


        # profile details
        self.name = Label(self.main)
        self.name.place(relx=0, rely=0, width=235, height=30)
        self.name.configure(
            text=self.active_user_data[0][0],
            background="#121212",
            font="Arial",
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.name.place(x=70, y=250)

        self.username = Label(self.main)
        self.username.place(relx=0, rely=0, width=235, height=30)
        self.username.configure(
            text=self.active_user_data[0][1],
            background="#121212",
            font="Arial",
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.username.place(x=70, y=290)

        self.email = Label(self.main)
        self.email.place(relx=0, rely=0, width=235, height=30)
        self.email.configure(
            text=self.active_user_data[0][3],
            background="#121212",
            font="Arial",
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.email.place(x=70, y=330)

        self.dob = Label(self.main)
        self.dob.place(relx=0, rely=0, width=235, height=30)
        self.dob.configure(
            text=self.active_user_data[0][5],
            background="#121212",
            font="Arial",
            foreground="white",
            justify="left",
            relief="flat",
            bd=0
        )
        self.dob.place(x=70, y=370)


        # btn for profile
        self.delete_btn = Button(self.main)
        self.delete_img = PhotoImage(file="./images/buttons/delete_btn.png")
        self.delete_btn.configure(
            text="Update",
            image=self.delete_img,
            bg="#121212",
            fg="red",
            borderwidth="0",
            cursor="hand2",
            font=("Arial", 20),
            command=self.delete_profile
        )
        self.delete_btn.place(x=119, y=420)

        self.logout_btn = Button(self.main)
        self.logout_img = PhotoImage(file="./images/buttons/logout_btn.png")
        self.logout_btn.configure(
            text="Logout",
            image=self.logout_img,
            bg="#121212",
            fg="red",
            borderwidth="0",
            cursor="hand2",
            font=("Arial", 20),
            command=self.logout
        )
        self.logout_btn.place(x=113, y=480)


        self.main.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        # self.main.mainloop()


    # Helper function
    def delete_profile(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete your profile? \nAll your data will be lost forever."):
            self.userprofile.delete_user(self.ACTIVE_USER)
            # print(self.ACTIVE_USER)
            self.main.destroy()
            messagebox.showinfo("Thank you", "Thank you for playing Game Deck.")
            Login_page().gui()


    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.main.destroy()
            Login_page().gui()


    def confirm_exit(self):
        self.main.destroy()
        Main_page().gui()


# demo = Profile_page()
# demo.gui()