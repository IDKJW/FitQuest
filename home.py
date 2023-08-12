"""Import moduesl
This is the page after the users has login. This GUI interact with users with button.
The users can click on the button to select what they want to do """
import tkinter as tk
from tkinter import PhotoImage, Label, DISABLED, Canvas, TRUE,font
import subprocess
import sys
import customtkinter
from PIL import ImageTk, Image

# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class HomeApp:
    """This is where all the functions and output of the GUI will be in"""

    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("Home")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)
        
        # Create a font
        self.small_custom_font = font.Font(
            family="Helvetica", size=13, weight="bold")

        # Create a Canvas
        self.canvas = Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=TRUE)

        # Define image for a background and output the background
        background_image = PhotoImage(file="assets/pixel_gym_background.png")
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Motavtional image on top
        top_image = ImageTk.PhotoImage(Image.open(
            "assets/Motivation_image.png").resize((300, 225), Image.ANTIALIAS))
        image_label = Label(
            image=top_image,
            borderwidth=0,
            highlightthickness=0)
        image_label.place(relx=0.5, rely=0.24, anchor=tk.CENTER)

        # Create a button for Workout
        equipment_image = ImageTk.PhotoImage(Image.open(
            "assets/dumbell.png").resize((100, 100), Image.ANTIALIAS))
        equipment_button = customtkinter.CTkButton(
            master=self.root,
            image=equipment_image,
            compound="top",
            text="Workout",
            command=self.workout,
            fg_color="white",
            hover_color="gray",
            hover=True,
            border_color="white",
            border_width=0,
            corner_radius=3,
            text_color="black"
        )
        equipment_button.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

        # Create a button for diet
        food_image = ImageTk.PhotoImage(Image.open(
            "assets/food.png").resize((100, 100), Image.ANTIALIAS))
        food_button = customtkinter.CTkButton(
            master=self.root,
            image=food_image,
            compound="top",
            text="Diet",
            command=self.deit,
            fg_color="white",
            hover_color="gray",
            hover=True,
            border_color="white",
            border_width=0,
            corner_radius=3,
            text_color="black"
        )
        food_button.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

        # Create a button for system
        system_image = ImageTk.PhotoImage(Image.open(
            "assets/system.png").resize((100, 100), Image.ANTIALIAS))
        system_button = customtkinter.CTkButton(
            master=self.root,
            image=system_image,
            compound="top",
            text="System",
            command=self.coming_soon,
            fg_color="white",
            hover_color="gray",
            hover=True,
            border_color="white",
            border_width=0,
            corner_radius=3,
            text_color="black"
        )
        system_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

        # Create a button to find the closest gym
        closest_gym_image = ImageTk.PhotoImage(Image.open(
            "assets/Closest gym.png").resize((100, 100), Image.ANTIALIAS))
        closest_gym_button = customtkinter.CTkButton(
            master=self.root,
            image=closest_gym_image,
            compound="top",
            text="Closest gym",
            command=self.coming_soon,
            fg_color="white",
            hover_color="gray",
            hover=True,
            border_color="white",
            border_width=0,
            corner_radius=3,
            text_color="black"
        )
        closest_gym_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)
        
       # Create a label for the intruction text
        text_label = tk.Label(
            self.root,
            text="•Please click on the workout button to go to the workout page"
            "\n•Please click on the diet button to go to the diet page"
            "\n•Please click on the system button to go to the system"
            "\n•Please click on the closet gym button to go to the closest gym page",
            bg="white",
            fg="black",
            wraplength=420,
            font=self.small_custom_font)
        text_label.place(x=50, y=640)

        # Icon________________________________#
        # Create a white menu at the bottom
        carolina_white_menu = customtkinter.CTkButton(
            master=self.root,
            text="",
            command="",
            height=100,
            width=500,
            hover=False,
            border_color="white",
            hover_color="white",
            fg_color="white",
            state=DISABLED,
            corner_radius=0
        )
        carolina_white_menu.place(relx=0.5, rely=0.98, anchor=tk.CENTER)

        # Create a clickable icon for home which is this page
        home_icon = ImageTk.PhotoImage(Image.open(
            "assets/home_icon.png").resize((40, 40), Image.ANTIALIAS))
        home_button = customtkinter.CTkButton(
            master=self.root,
            image=home_icon,
            text="",
            command="",
            fg_color="white",
            hover_color="white",
            hover=True,
            compound="top",
            border_color="white",
            text_color="black",
            width=5,
            corner_radius=0
        )
        home_button.place(relx=0.1, rely=0.965, anchor=tk.CENTER)

        # Create a clickable icon for gym
        gym_icon = ImageTk.PhotoImage(Image.open(
            "assets/dumbell.png").resize((50, 50), Image.ANTIALIAS))
        gym_button = customtkinter.CTkButton(
            master=self.root,
            image=gym_icon,
            text="",
            command=self.workout,
            fg_color="white",
            hover_color="white",
            hover=True,
            compound="top",
            border_color="white",
            text_color="black",
            width=5,
            corner_radius=0
        )
        gym_button.place(relx=0.3, rely=0.965, anchor=tk.CENTER)

        # create a clickable icon for diet
        diet_icon = ImageTk.PhotoImage(Image.open(
            "assets/food.png").resize((50, 50), Image.ANTIALIAS))
        diet_button = customtkinter.CTkButton(
            master=self.root,
            image=diet_icon,
            text="",
            command=self.deit,
            fg_color="white",
            hover_color="white",
            hover=True,
            compound="top",
            border_color="white",
            text_color="black",
            width=5,
            corner_radius=0
        )
        diet_button.place(relx=0.5, rely=0.965, anchor=tk.CENTER)

        # create a clickable icon for system
        system_icon = ImageTk.PhotoImage(Image.open(
            "assets/shopping_cart.png").resize((40, 40), Image.ANTIALIAS))
        system_button = customtkinter.CTkButton(
            master=self.root,
            image=system_icon,
            text="",
            command=self.coming_soon,
            fg_color="white",
            hover_color="white",
            hover=True,
            compound="top",
            border_color="white",
            text_color="black",
            width=5,
            corner_radius=0
        )
        system_button.place(relx=0.7, rely=0.965, anchor=tk.CENTER)

        # create a clickable icon for closest gym
        gym_icon = ImageTk.PhotoImage(Image.open(
            "assets/closest gym.png").resize((40, 40), Image.ANTIALIAS))
        gym_button = customtkinter.CTkButton(
            master=self.root,
            image=gym_icon,
            text="",
            command=self.coming_soon,
            fg_color="white",
            hover_color="white",
            hover=True,
            compound="top",
            border_color="white",
            text_color="black",
            width=0,
            corner_radius=0
        )
        gym_button.place(relx=0.9, rely=0.965, anchor=tk.CENTER)

        self.root.mainloop()

    # Function for the workout button
    def workout(self):
        """Function to destroy home GUI and import workout GUI"""
        self.root.destroy()
        # Open workout.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "workout.py"])

    # Function for the deit button
    def deit(self):
        """Function to destroy home GUI and import diet GUI"""
        self.root.destroy()
        # Open diet.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "diet.py"])

    # Function for the comming_soon button
    def coming_soon(self):
        """Function to destroy home GUI and import coming_soon screen"""
        self.root.destroy()
        # Open comming_soon.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "coming_soon.py"])


# Check if is the script running the main progarm
if __name__ == "__main__":
    app = HomeApp()
