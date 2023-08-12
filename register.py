"""Import moduels
This page is for the user to register their frist account if they don't have one"""
import tkinter as tk
import sqlite3
from tkinter import font, TRUE, PhotoImage, StringVar
from tkinter import Checkbutton, DISABLED, CENTER, IntVar, Button, Label
import re
import subprocess
import sys
import customtkinter
from PIL import ImageTk, Image


# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class RegisterApp:
    """This is where all the functions and where the GUI will be created for register screen"""

    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("Register")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=TRUE)

        # Create font
        global small_custom_font
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        small_custom_font = font.Font(
            family="Helvetica", size=13, weight="bold")
        


        # Create a database connection
        self.connection = sqlite3.connect("db/registration.db")
        self.cursor = self.connection.cursor()

        # Create a table for registration
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
""")

        # Define backgrounf image and create background
        self.background = PhotoImage(file="assets/gym_background_2.png")
        self.canvas.create_image(0, 0, image=self.background, anchor="nw")

        # Define the image for button
        self.image_button = PhotoImage(file='assets/button_image.png')

        # Creating an empty tuple for username and password
        self.username = StringVar()
        self.password = StringVar()

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

        # Create background_rectangle
        self.background_rectangle = self.canvas.create_rectangle(
            100, 100, 400, 650, fill="#4B9CD3")

        # Create Intruction text
        self.canvas.create_text(
            250,
            130,
            text="Register",
            fill="black",
            font=custom_font)

        # Create Username text
        self.canvas.create_text(
            250,
            325,
            text="Username",
            fill="black",
            font=custom_font)

        # Create Password text
        self.canvas.create_text(
            250,
            400,
            text="Password",
            fill="black",
            font=custom_font)

        # Create a customentry widget for username
        self.username_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.username,
            placeholder_text="Username",
            height=35,
            width=250,
            bg_color="#4B9CD3")
        self.username_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Create a customentry widget for password
        self.password_entry = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.password,
            placeholder_text="Password",
            height=35,
            width=250,
            show="*",
            bg_color="#4B9CD3")
        self.password_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Create a checkbox variable to store the state
        self.password_valid = IntVar()
        self.password_valid.set(0)

        # Create a checkbox
        self.password_check = Checkbutton(
            self.root,
            text="Password meets requirements",
            font=small_custom_font,
            variable=self.password_valid,
            state=DISABLED,
            bg="#4B9CD3")
        self.password_check.place(relx=0.5, rely=0.68, anchor=CENTER)

        # Create a register button
        self.register_button = Button(
            self.root,
            image=self.image_button,
            text="Register",
            font=custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=100,
            compound=CENTER,
            command=self.register_user)
        self.register_button_window = self.canvas.create_window(
            250, 490, anchor="center", window=self.register_button)

        # Create an empty label for the error message
        self.error_label = Label(self.root, text="", fg="red", bg="#4B9CD3")
        self.error_label.place(relx=0.5, rely=0.65, anchor=CENTER)

        # Create text for intruction
        self.canvas.create_text(
            250,
            585,
            text="•Please enter your username \n and password to register"
            "\n•Click here go back to the Welcome page",
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
            command=self.welcome)
        self.back_button_window = self.canvas.create_window(
            250, 630, anchor="center", window=self.back_button)

        # Register the callback to check the password validity
        self.password.trace_add("write", self.check_password_validity)

        self.root.mainloop()

    # Function for the login button
    def login(self):
        """Function destroy home GUI and import login GUI"""
        self.root.destroy()
        # Open login.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "design/login.py"])

    # Function for the welcome button
    def welcome(self):
        """Function destroy home GUI and import welcome GUI"""
        self.root.destroy()
        # Open welcome.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "design/welcome.py"])

    # Function to check the the password
    def check_password_validity(self, *args):
        """This function is checking the password reuqiemnt"""
        # Can't deleted *args because it is used to pass the requiemnt
        # Get password value
        password_value = self.password.get()

        # Check password requirements
        # Check if there is at least one capital letter in the password section
        capital_letter = bool(re.search(r"[A-Z]", password_value))
        # Check if there is at least one number in the password section
        has_number = bool(re.search(r"\d", password_value))
        # Check if there is at least one symbol in the password section
        has_symbol = bool(re.search(r"\W", password_value))

        # Update checkbox state based on password validity
        if capital_letter and has_number and has_symbol:
            self.password_valid.set(1)
            self.error_label.config(text="", fg="red")
        else:
            self.password_valid.set(0)
            self.error_label.config(
                text="Password must contain at least one\ncapital letter one number,and one symbol",
                fg="red")
    # Function to get the passowrd and username

    def register_user(self):
        """Get username and password"""
        username_value = self.username.get()
        password_value = self.password.get()

        # Check if the password meets requirements
        if self.password_valid.get() == 0:
            self.error_label.config(
                text="Password does not meet the requirements", font=small_custom_font,fg="red")
            return

        # Insert the user into the database
        self.cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username_value,
             password_value))
        self.connection.commit()

        self.login()


# Check if is the script running the main progarm
if __name__ == "__main__":
    RegisterApp()
