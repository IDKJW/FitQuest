#Import modules
import tkinter
from tkinter import *
import os
import customtkinter
from PIL import ImageTk, Image

home = Tk()
home.title("Home")
home.geometry("500x800")

def workout():
    home.destroy()
    import workout

def deit():
    home.destroy()
    import deit

def coming_soon():
    home.destroy
    import coming_soon
    

background_image = PhotoImage(file="assets/Aim high.png")
background_label = Label(home,image = background_image)
background_label.place(x=0, y=0, relwidth = 1 , relheight = 1)

#Image on the top 
Top_iamge = ImageTk.PhotoImage(Image.open("assets/Motivation_image.png").resize((300,225),Image.ANTIALIAS))
image_label =Label(image = Top_iamge)
image_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

#Create a button for Workout 
equipment_image = ImageTk.PhotoImage(Image.open("assets/dumbell.png").resize((100,100),Image.ANTIALIAS))
equipment_button =customtkinter.CTkButton(master=home,image=equipment_image,compound="top",text="Workout", command="workout",fg_color="white", hover_color= "White" , hover= True,border_color="White" , border_width= 0 ,text_color="black")
equipment_button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

#Create a button for diet
food_image = ImageTk.PhotoImage(Image.open("assets/food.png").resize((100,100),Image.ANTIALIAS))
food_button = customtkinter.CTkButton(master = home,image=food_image, text="Diet",fg_color="white", hover_color= "White" , hover= True, compound="top" , border_width= 0, border_color= "White",text_color="black")
food_button.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

#Create a button for system
system_image = ImageTk.PhotoImage(Image.open("assets/system.png").resize((100,100),Image.ANTIALIAS))
system_button = customtkinter.CTkButton(master = home,image=system_image, text="Coming Soon",fg_color="white", hover_color= "White" , hover= True, compound="top" , border_width= 0, border_color= "White",text_color="black")
system_button.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

#Create a button to find the closest gym 
closest_gym_image = ImageTk.PhotoImage(Image.open("assets/Closest gym.png").resize((100,100),Image.ANTIALIAS))
closest_gym_button = customtkinter.CTkButton(master = home,image=closest_gym_image, text="Coming Soon",fg_color="white", hover_color= "White" , hover= True, compound="top" , border_width= 0, border_color= "White", text_color="black")
closest_gym_button.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)




#Icon_____________________________________________________________________________________________________________________________________________________________________________________________#
white_menu= customtkinter.CTkButton(master=home, text="", command="" , height = 40, width = 500, hover=False, border_color= "white", hover_color= "white",fg_color="white",state=DISABLED,corner_radius= 0)
white_menu.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

#Creat a clickable icon for home which is this page
home_icon = ImageTk.PhotoImage(Image.open("assets/home_icon.png").resize((30,30),Image.ANTIALIAS))
home_button = customtkinter.CTkButton(master = home,image=home_icon, text="",fg_color="white", hover_color= "white" , hover= True, compound="top" , border_color= "white", text_color="blakc" , width=5,corner_radius= 0)
home_button.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)



#Create a clickable icon for gym 
gym_icon = ImageTk.PhotoImage(Image.open("assets/dumbell.png").resize((30,30),Image.ANTIALIAS))
gym_button = customtkinter.CTkButton(master = home,image=gym_icon, text="",fg_color="white", hover_color= "white" , hover= True, compound="top" , border_color= "white", text_color="black",width=5,corner_radius= 0)
gym_button.place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)

#create a clickzble icon for diet 
diet_icon = ImageTk.PhotoImage(Image.open("assets/food.png").resize((30,30),Image.ANTIALIAS))
diet_button = customtkinter.CTkButton(master = home,image=diet_icon, text="",fg_color="white", hover_color= "white" , hover= True, compound="top" ,  border_color= "white", text_color="black",width=5,corner_radius= 0)
diet_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

#create a clickable icon for system 

system_icon = ImageTk.PhotoImage(Image.open("assets/shopping_cart.png").resize((30,30),Image.ANTIALIAS))
system_button = customtkinter.CTkButton(master = home,image=system_icon, text="",fg_color="white", hover_color= "white" , hover= True, compound="top" , border_color= "white", text_color="black",width=5,corner_radius= 0)
system_button.place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)

#create a clickable icon for cloest gym

gym_icon = ImageTk.PhotoImage(Image.open("assets/closest gym.png").resize((30,30),Image.ANTIALIAS))
gym_button = customtkinter.CTkButton(master = home,image=gym_icon, text="",fg_color="white", hover_color= "white" , hover= True, compound="top" , border_color= "white", text_color="black",width=0,corner_radius= 0)
gym_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)



home.mainloop()
