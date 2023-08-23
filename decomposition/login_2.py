"""Import moduels
This page is desgin for user to login from.
The data will be get from the database
and will be scan for the username and password"""
import tkinter as tk
import sqlite3
from tkinter import font, Canvas, PhotoImage, StringVar, CENTER, Button, Label
import sys
import subprocess
import customtkinter
from PIL import ImageTk, Image


class LoginApp:
    """All the functions and the GUI will be storing into this class"""

    def __init__(self, root):
        # Can't have only 1 positional arugment, it needs 2 arguemnts
        # Create the main application window
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Create Canvas
        self.canvas = Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=True)

        # create font
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        small_custom_font = font.Font(
            family="Helvetica", size=12, weight="bold")
        
        # Define an image and create background
        self.background = PhotoImage(file="assets/gym_background_2.png")
        self.canvas.create_image(0, 0, image=self.background, anchor="nw")

        # Define the image for the button
        self.image_button = PhotoImage(file='assets/button_image.png')

        # Create a database connection
        self.connection = sqlite3.connect("db/registration.db")
        self.cursor = self.connection.cursor()

        # Define a string varable
        self.username_verify = StringVar()
        self.password_verify = StringVar()

        # Create logo image
        self.logo = ImageTk.PhotoImage(Image.open(
            "assets/Logo.png").resize((200, 150), Image.ANTIALIAS))
        self.logo_image = customtkinter.CTkButton(
            master=self.root,
            image=self.logo,
            text="",
            compound="left",
            hover=False,
            bg_color="#020202")
        self.canvas.create_window(250, 230, window=self.logo_image)

        # Create a background_rectangle
        self.background_rectangle = self.canvas.create_rectangle(
            100, 100, 400, 650, fill="#4B9CD3")

        # Create a Intruction text
        self.canvas.create_text(
            250,
            130,
            text="Login",
            fill="black",
            font=custom_font)

        # Create a Username text
        self.canvas.create_text(
            250,
            325,
            text="Username",
            fill="black",
            font=custom_font)

        # Create a login wdiget for the user
        self.username_login_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.username_verify,
            placeholder_text="Username",
            height=35,
            width=250,
            bg_color="#4B9CD3")
        self.username_login_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Create a Password text
        self.canvas.create_text(
            250,
            400,
            text="Password",
            fill="black",
            font=custom_font)

        # Create a entry widget for the user
        self.password_login_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.password_verify,
            placeholder_text="Password",
            height=35,
            width=250,
            show="*",
            bg_color="#4B9CD3")
        self.password_login_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Create a login button
        self.login_button = Button(
            self.root,
            image=self.image_button,
            text="Login",
            font=custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=100,
            compound=CENTER,
            command=self.valid_credentials)
        self.login_button_window = self.canvas.create_window(
            250, 490, anchor="center", window=self.login_button)

        # create a label for the error messsage
        self.error_label = Label(self.root, text="", fg="red", bg="#4B9CD3")
        self.error_label.place(relx=0.5, rely=0.65, anchor=CENTER)
        
        # Create text for intruction
        self.canvas.create_text(
            250,
            550,
            text="Please enter your username \nand password to login",
            fill="black",
            font=small_custom_font)

        # Already have an account message and login link message
        self.canvas.create_text(
            250,
            600,
            text="Don't have an account click here \n ->",
            fill="black",
            font=small_custom_font)

        # Create a back button
        self.back_button = Button(
            self.root,
            image=self.image_button,
            text="Back",
            font=custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=100,
            compound=CENTER,
            command=self.register)
        self.back_button_window = self.canvas.create_window(
            250, 620, anchor="center", window=self.back_button)

    # Function for the register button
    def register(self):
        """Destory login page and then import register page"""
        self.root.destroy()
        # Open register.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "register.py"])


# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


# Check if is the script running the main progarm
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
