import tkinter as tk
from tkinter import PhotoImage, CENTER, TRUE, DoubleVar,font, ttk, StringVar, Label
import sqlite3
import customtkinter
from PIL import ImageTk, Image
import sys
import subprocess

# Executing another python script with the same interpreter
python_executable = sys.executable


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Create a database connection
        self.connection = sqlite3.connect("db/registration.db")
        self.cursor = self.connection.cursor()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        # Create an empty tuple for username and password
        self.username = StringVar()
        self.password = StringVar()

        # Create a back button
        self.arrow_image = ImageTk.PhotoImage(Image.open("assets/back_button.png").resize((50, 50), Image.ANTIALIAS))
        self.arrow_button = customtkinter.CTkButton(
            master=self.root,
            image=self.arrow_image,
            text="",
            compound="left",
            fg_color='black',
            hover_color='black',
            command=self.root.destroy)
        self.arrow_button.place(relx=0.2, rely=0.2, anchor=CENTER)

        # Create a background image
        self.background_image_login = PhotoImage(file="assets/background2.png")
        self.background_label_login = Label(self.root, image=self.background_image_login)
        self.background_label_login.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a font
        bold_font = ("Helvetica", 30, "bold")
        small_bold_font = ("Helvetica", 15, "bold")

        # Intruction text
        intruction_text = Label(self.root, text="Login", font=bold_font)
        intruction_text.place(relx=0.5, rely=0.15, anchor=CENTER)

        # Create an empty label for the image
        self.logo = ImageTk.PhotoImage(Image.open("assets/Logo.png").resize((180, 130), Image.ANTIALIAS))
        self.logo1 = customtkinter.CTkButton(
            master=self.root,
            image=self.logo,
            text="",
            compound="left",
            hover=False,
            bg_color="#020202")
        self.logo1.place(relx=0.48, rely=0.3, anchor=CENTER)

        # Create a login text
        login_text = Label(self.root, text="Login", font=small_bold_font)
        login_text.place(relx=0.5, rely=0.42, anchor=CENTER)

        # Create an empty entry for username
        self.username_login_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.username_verify,
            placeholder_text="Username",
            height=35,
            width=250)
        self.username_login_entry.place(relx=0.5, rely=0.47, anchor=CENTER)

        # Create a password text
        password_text = Label(self.root, text="Password", font=small_bold_font)
        password_text.place(relx=0.5, rely=0.53, anchor=CENTER)

        # Create an empty entry for password
        self.password_login_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.password_verify,
            placeholder_text="Password",
            height=35,
            width=250,
            show="*")
        self.password_login_entry.place(relx=0.5, rely=0.58, anchor=CENTER)

        # Create a button
        login_button_1 = customtkinter.CTkButton(
            master=self.root,
            text="Login",
            command=self.valid_credentials,
            height=35,
            width=250)
        login_button_1.place(relx=0.5, rely=0.65, anchor=CENTER)

        # Create an empty label for error message
        self.error_label = Label(self.root, text="", fg="red")
        self.error_label.place(relx=0.5, rely=0.8, anchor=CENTER)

        # Already have an account message and login link
        message_label = Label(self.root, text="Don't have an account? Click here->")
        message_label.place(relx=0.5, rely=0.7, anchor=CENTER)
        login_link = Label(self.root, text="Register", fg="white", cursor="hand2")
        login_link.place(relx=0.76, rely=0.7, anchor=CENTER)
        login_link.bind("<Button-1>", self.register)

    def valid_credentials(self):
        # Get username and password
        username = self.username_verify.get()
        password = self.password_verify.get()

        # Check if the credentials exist in the database
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()

        if user is not None:
            # If the user exists, close the database connection and proceed to
            # the home screen
            self.connection.close()
            self.root.destroy()
            subprocess.Popen([python_executable, "design/version_1/home_v1.py"])
            return
        else:
            # If the user doesn't exist, show an error message
            self.error_label.config(text="Incorrect username or password")

    def register(self, event):
        self.root.destroy()
        subprocess.Popen([python_executable, "design/version_1/register_v1.py"])
        return


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
