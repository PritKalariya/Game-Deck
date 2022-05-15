from tkinter import *
import os
# from manage_profiles import UserProfile
# import login



# check if user is logged in
# print(login.ACTIVE_USER)


# use db connection to load highscores for each game (based on username)
# userprofile = UserProfile()
# active_user_data = userprofile.get_user_data(login.)
# print(active_user_data)


# helper functions
def update_profile():
    pass

def logout():
    main.destroy()
    os.system("python login.py")


# design a profile page
main = Tk()
main.title("Profile")
main.geometry("900x600")
main.resizable(0, 0)
main.configure(background="white")


# bg image for tkinter window
window_bg = Label(main)
window_bg.place(relx=0, rely=0, width=900, height=600)
img = PhotoImage(file="./images/pages/profile.png")
window_bg.configure(image=img)


# Highscores
pong_game = Label(main)
pong_game.place(relx=0, rely=0, width=50, height=50)
pong_game.configure(
    # text=active_user_data[0][6],
    background="red",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0
)
pong_game.place(x=426, y=140)

snake_game = Label(main)
snake_game.place(relx=0, rely=0, width=50, height=50)
snake_game.configure(
    # text=active_user_data[0][7],
    background="red",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0
)
snake_game.place(x=692.7, y=140)

quiz_game = Label(main)
quiz_game.place(relx=0, rely=0, width=50, height=50)
quiz_game.configure(
    # text=active_user_data[0][8],
    background="red",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0
)
quiz_game.place(x=426, y=300)

hangman_game = Label(main)
hangman_game.place(relx=0, rely=0, width=50, height=50)
hangman_game.configure(
    # text=active_user_data[0][10],
    background="red",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0
)
hangman_game.place(x=692.7, y=300)

turtle_crossing_game = Label(main)
turtle_crossing_game.place(relx=0, rely=0, width=50, height=50)
turtle_crossing_game.configure(
    # text=active_user_data[0][9],
    background="red",
    font="Arial",
    foreground="black",
    justify="left",
    relief="flat",
    bd=0
)
turtle_crossing_game.place(x=558.7, y=465)


# profile image
profile_icon = Label(main)
profile_icon.place(relx=0, rely=0, width=130, height=125)
profile_img = PhotoImage(file="./images/profiles/profile_logo.png")
profile_icon.configure(image=profile_img)
profile_icon.place(x=112, y=100)


# profile details
name = Label(main)
name.place(relx=0, rely=0, width=150, height=30)
name.configure(
    text="demo name",
    background="#121212",
    font="Arial",
    foreground="white",
    justify="left",
    relief="flat",
    bd=0
)
name.place(x=110, y=250)

username = Label(main)
username.place(relx=0, rely=0, width=150, height=30)
username.configure(
    text="demo username",
    background="#121212",
    font="Arial",
    foreground="white",
    justify="left",
    relief="flat",
    bd=0
)
username.place(x=110, y=275)

bio = Label(main)
bio.place(relx=0, rely=0, width=235, height=80)
bio.configure(
    text="bio",
    background="red",
    font="Arial",
    foreground="white",
    justify="left",
    relief="flat",
    bd=0
)
bio.place(x=70, y=315)


# btn for profile
update_btn = Button(main)
update_img = PhotoImage(file="./images/buttons/update_btn.png")
update_btn.configure(
    text="Update",
    image=update_img,
    bg="#121212",
    fg="red",
    borderwidth="0",
    cursor="hand2",
    font=("Arial", 20),
    command=update_profile
)
update_btn.place(x=110, y=420)

logout_btn = Button(main)
logout_img = PhotoImage(file="./images/buttons/logout_btn.png")
logout_btn.configure(
    text="Logout",
    image=logout_img,
    bg="#121212",
    fg="red",
    borderwidth="0",
    cursor="hand2",
    font=("Arial", 20),
    command=logout
)
logout_btn.place(x=113, y=480)


main.mainloop()