# Import modules
import tkinter
from tkinter import *
import os
import customtkinter
from PIL import ImageTk, Image
import subprocess
import sys


# Executing another python script with the same interpreter
python_executable = sys.executable

root = Tk()
# Designing the main screen


def main_screen():
    root.geometry("500x800")
    main_frame = Frame(root, bg='#020202')
    main_frame.pack(padx=20)
    main_frame.pack()
    background_image = PhotoImage(file="assets/Aim high.png")
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.title("Welcome to FitQuest")
    top_text = Label(
        root,
        text="Welcome to FitQuest",
        bg="#020202",
        font=(
            "Calibri",
            45))
    top_text.pack(pady=0, anchor=tkinter.CENTER)

    # Destory the home GUI and import register GUI

    def register():
        root.destroy()
        subprocess.Popen([python_executable, "design/version_1/register_vq.py"])
        return

    # Destory the home GUI and import login GUI

    def login():
        root.destroy()
        subprocess.Popen([python_executable, "design/version_1/login_v1.py"])
        return

    # Login button
    login_button = customtkinter.CTkButton(
        master=root,
        text="Login",
        command=login,
        height=35,
        width=250,
        bg_color="#020202")
    login_button.place(relx=0.48, rely=0.3, anchor=tkinter.CENTER)
    # register button
    register_button = customtkinter.CTkButton(
        master=root,
        text="Register",
        command=register,
        height=35,
        width=250,
        bg_color="#020202")
    register_button.place(relx=0.48, rely=0.4, anchor=tkinter.CENTER)
    # Logo act as a button
    logo = ImageTk.PhotoImage(Image.open("assets/Logo.png"), Image.ANTIALIAS)
    button1 = customtkinter.CTkButton(
        master=root,
        image=logo,
        text="",
        compound="left",
        hover=False,
        bg_color="#020202")
    button1.place(relx=0.48, rely=0.158, anchor=tkinter.CENTER)

    root.mainloop()


main_screen()
