#Import modules
import tkinter
from tkinter import *
import os
import customtkinter
from PIL import ImageTk, Image

login_screen = Tk()
login_screen.title("Login")
login_screen.geometry("500x800")
#background image
background_image_login = PhotoImage(file="assets/backgroun2.png")
background_label_login = Label(login_screen,image = background_image_login)
background_label_login.place(x=0, y=0, relwidth = 1 , relheight = 1)
#Logo act as a button 
logo = ImageTk.PhotoImage(Image.open("assets/Logo.png").resize((180,130),Image.ANTIALIAS))
logo1 =customtkinter.CTkButton(master=login_screen,image=logo,text="",compound="left" , hover=False, bg_color="#020202")
logo1.place(relx=0.48, rely=0.2, anchor=tkinter.CENTER)

top_text = Label(login_screen, text="Please enter details below to login").pack()
top_text=Label(login_screen, text="").pack()

def register():
    login_screen.destroy()
    import register
    
    def validCredentials(self):
        self.f = open('Gmail.txt', 'r')
        for line in self.f:
            f_email, f_pword = line.split()
            if f_email == self.uname.get() and f_pword == self.pword.get():
                self.f.close()
                return True
        self.f.close()
        return False
    
def home():
    login_screen.destroy()
    import home

global username_verify
global password_verify
 
username_verify = StringVar()
password_verify = StringVar()
 
global username_login_entry
global password_login_entry
 
login_text =Label(login_screen, text="Login")
login_text.place(relx= 0.5 , rely = 0.3,anchor=tkinter.CENTER)
username_login_entry = customtkinter.CTkEntry(master=login_screen,textvariable=username_verify, placeholder_text="Username",height = 35, width = 250,)
username_login_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

password_text =Label(login_screen, text="Password")
password_text.place(relx= 0.5 , rely = 0.4,anchor=tkinter.CENTER)
password_login_entry = customtkinter.CTkEntry(master=login_screen,textvariable=password_verify, placeholder_text="Password",height = 35, width = 250,)
password_login_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
    
login_button_1= customtkinter.CTkButton(master=login_screen, text="Login", command="home" , height = 35, width = 250 )
login_button_1.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

login_screen.mainloop()
