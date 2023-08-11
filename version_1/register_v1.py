
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox  # Import messagebox for error messages
import re  # Import re module for regular expressions
import customtkinter
from PIL import ImageTk, Image
import subprocess
import sys

# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class RegisterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Register")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Create a database connection
        self.connection = sqlite3.connect("db/registration.db")
        self.cursor = self.connection.cursor()

        # Create a table for registration
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

        # Background image
        self.background_image_login = PhotoImage(file="assets/background2.png")
        self.background_label_login = Label(
            self.root, image=self.background_image_login)
        self.background_label_login.place(x=0, y=0, relwidth=1, relheight=1)

        # Creating an empty tuple for username and password
        self.username = StringVar()
        self.password = StringVar()

        # Create an empty label for the image
        self.logo = ImageTk.PhotoImage(Image.open(
            "assets/Logo.png").resize((180, 130), Image.ANTIALIAS))
        self.logo1 = customtkinter.CTkButton(
            master=self.root,
            image=self.logo,
            text="",
            compound="left",
            hover=False,
            bg_color="#020202")
        self.logo1.place(relx=0.48, rely=0.2, anchor=CENTER)

        # Create an empty label for the text
        self.username_label = Label(self.root, text="Username")
        self.username_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Create a customentry widget for username
        self.username_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.username,
            placeholder_text="Username",
            height=35,
            width=250)
        self.username_entry.place(relx=0.5, rely=0.35, anchor=CENTER)

        # Create an empty label for the text
        self.password_label = Label(self.root, text="Password")
        self.password_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Create a customentry widget for password
        self.password_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.password,
            placeholder_text="Password",
            height=35,
            width=250,
            show="*")
        self.password_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Create a button
        self.register_button = customtkinter.CTkButton(
            master=self.root,
            text="Register",
            command=self.register_user,
            height=35,
            width=250)
        self.register_button.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Create an empty label for the error message
        self.error_label = Label(self.root, text="", fg="red")
        self.error_label.place(relx=0.5, rely=0.62, anchor=CENTER)

        self.arrow_image = ImageTk.PhotoImage(Image.open(
            "assets/back_button.png").resize((50, 50), Image.ANTIALIAS))
        self.arrow_button = customtkinter.CTkButton(
            master=self.root,
            image=self.arrow_image,
            text="",
            compound="left",
            fg_color='black',
            hover_color='black',
            command=self.welcome)
        self.arrow_button.place(relx=0.1, rely=0.1, anchor=CENTER)

        self.root.mainloop()

    def login(self):
        """Function destory home GUI and import login GUI"""
        self.root.destroy()
        subprocess.Popen([PYTHON_EXECUTABLE, "design/version_1/login_v1.py"])
        return

    def welcome(self):
        """Function destory home GUI and import welcome GUI"""
        self.root.destroy()
        subprocess.Popen([PYTHON_EXECUTABLE, "design/version_1/welcome_v1.py"])
        return

    def register_user(self):
        # Get username and password
        username_value = self.username.get()
        password_value = self.password.get()

        # Check password requirements
        # Check if there is at least one capital letter in the password section
        if not re.search(r"[A-Z]", password_value):
            self.error_label.config(
                text="Password must contain at least one capital letter", fg="red")
            return
        # Check if there is at least one number in the password section
        if not re.search(r"\d", password_value):
            self.error_label.config(
                text="Password must contain at least one number", fg="red")
            return
        # Check if there is at least one symbol in the password section
        if not re.search(r"\W", password_value):
            self.error_label.config(
                text="Password must contain at least one symbol", fg="red")
            return

        # Insert the user into the database
        self.cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username_value,
             password_value))
        self.connection.commit()

        self.login()


#
if __name__ == "__main__":
    RegisterApp()