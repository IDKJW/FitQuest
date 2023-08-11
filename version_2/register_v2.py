import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox  # Import messagebox for error messages
import re  # Import re module for regular expressions
import customtkinter
from PIL import ImageTk, Image


# Destroy this window and open the login screen
def login():
    register_screen.destroy()
    import login  # Assuming there is a login.py file to open the login screen


def register_user():
    # Get username and password
    username_value = username.get()
    password_value = password.get()
    
    # Check password requirements
    # Check if there is at least one capital letter in the password section
    if not re.search(r"[A-Z]", password_value):
        error_label.config(text="Password must contain at least one capital letter", fg="red")
        return
    # Check if there is at least one number in the password section
    if not re.search(r"\d", password_value):
        error_label.config(text="Password must contain at least one number", fg="red")
        return
    # Check if there is at least one symbol in the password section
    if not re.search(r"\W", password_value):
        error_label.config(text="Password must contain at least one symbol", fg="red")
        return
    
    # Insert the user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username_value, password_value))
    connection.commit()
    
    login()


# Designing for registration
register_screen = tk.Tk()
register_screen.title("Register")
register_screen.geometry("500x800")
register_screen.resizable(width=False, height=False)

# Create a database connection
connection = sqlite3.connect("db/registration.db")
cursor = connection.cursor()

# Create a table for registration
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

# Background image
background_image_login = PhotoImage(file="assets/background2.png")
background_label_login = Label(register_screen, image=background_image_login)
background_label_login.place(x=0, y=0, relwidth=1, relheight=1)

# Creating an empty tuple for username and password
username = StringVar()
password = StringVar()

# Create an empty label for the image
logo = ImageTk.PhotoImage(Image.open("assets/Logo.png").resize((180, 130), Image.ANTIALIAS))
logo1 = customtkinter.CTkButton(master=register_screen, image=logo, text="", compound="left", hover=False, bg_color="#020202")
logo1.place(relx=0.48, rely=0.2, anchor=CENTER)

# Create an empty label for the text
username_label = Label(register_screen, text="Username")
username_label.place(relx=0.5, rely=0.3, anchor=CENTER)

# Create a customentry widget for username
username_entry = customtkinter.CTkEntry(master=register_screen, textvariable=username, placeholder_text="Username", height=35, width=250)
username_entry.place(relx=0.5, rely=0.35, anchor=CENTER)

# Create an empty label for the text
password_label = Label(register_screen, text="Password")
password_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# Create a customentry widget for password
password_entry = customtkinter.CTkEntry(master=register_screen, textvariable=password, placeholder_text="Password", height=35, width=250, show="*")
password_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

# Create a button
register_button = customtkinter.CTkButton(master=register_screen, text="Register", command=register_user, height=35, width=250)
register_button.place(relx=0.5, rely=0.55, anchor=CENTER)

# Create an empty label for the error message
error_label = Label(register_screen, text="", fg="red")
error_label.place(relx=0.5, rely=0.62, anchor=CENTER)

# Already have an account message and login link
message_label = Label(register_screen, text="Already have an account? Click here->")
message_label.place(relx=0.5, rely=0.68, anchor=CENTER)
login_link = Label(register_screen, text="Login", fg="white", cursor="hand2")
login_link.place(relx=0.77, rely=0.68, anchor=CENTER)
login_link.bind("<Button-1>", lambda event: login())



register_screen.mainloop()

# Close the database connection
connection.close()
