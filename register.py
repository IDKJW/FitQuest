#Import modules
import tkinter
from tkinter import *
import os
import customtkinter
from PIL import ImageTk, Image


# Designing for registration
register_screen = Tk()
register_screen.title("Register")
register_screen.geometry("500x800")

#background image
background_image_login = PhotoImage(file="assets/backgroun2.png")
background_label_login = Label(register_screen,image = background_image_login)
background_label_login.place(x=0, y=0, relwidth = 1 , relheight = 1)

global username
global password
global username_entry
global password_entry   

username = StringVar()
password = StringVar()

def login():
    register_screen.destroy()
    import login
 
 
def onClick():
    f = open('Gmail.txt','a')
    f.write(username.get()+' '+password.get()+'\n')
    f.close()
    login()
    

logo = ImageTk.PhotoImage(Image.open("assets/Logo.png").resize((180,130),Image.ANTIALIAS))
logo1 =customtkinter.CTkButton(master=register_screen,image=logo,text="",compound="left" , hover=False, bg_color="#020202")
logo1.place(relx=0.48, rely=0.2, anchor=tkinter.CENTER)

username_lable = Label(register_screen, text="Username")
username_lable.place(relx= 0.5 , rely = 0.3,anchor=tkinter.CENTER)
username_entry = customtkinter.CTkEntry(master=register_screen,textvariable=username, placeholder_text="Username",height = 35, width = 250,)
username_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

password_lable = Label(register_screen, text="Password")
password_lable.place(relx= 0.5 , rely = 0.4,anchor=tkinter.CENTER)
password_entry = customtkinter.CTkEntry(master=register_screen,textvariable=password, placeholder_text="Password",height = 35, width = 250,)
password_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)


register_button_1= customtkinter.CTkButton(master=register_screen, text="Register", command = onClick,height = 35, width = 250 )
register_button_1.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)




register_screen.mainloop()
