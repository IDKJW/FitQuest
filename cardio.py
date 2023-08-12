'''Import Modules
This is the cardio excerise page for the user to train their stamina and lose weight'''
import tkinter as tk
import sqlite3
from tkinter import PhotoImage, CENTER, TRUE, DoubleVar, font, ttk
import subprocess
import io
import random
import sys
from PIL import ImageTk, Image


# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class CardioExerciseApp:
    '''Class represent CardioExerciseaApp'''

    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("cardio Exercise")
        self.root.resizable(False, False)

        # Define a font
        self.custom_font = font.Font(
            family="Helvetica", size=20, weight="bold")
        self.small_custom_font = font.Font(
            family="Helvetica", size=15, weight="bold")

        # Create a Canvas
        self.canvas = tk.Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=TRUE)

        # Define an image and output it
        self.background_image = PhotoImage(
            file="assets/pixel_gym_background.png")
        self.canvas.create_image(-300, -100,
                                 image=self.background_image, anchor="nw")

        # Create a database connection
        connection = sqlite3.connect("db/workout.db")
        cursor = connection.cursor()

        # Get all exercises from the database
        cursor.execute("SELECT exercise, reps, image FROM Cardio")
        self.exercises = cursor.fetchall()

        # Close the database connection
        connection.close()

        # Create an empty list to track the shown exercises
        self.exercises_shown = []

        # Create labels for exercise and reps
        # create a colored rectangle to act as the background
        self.background_rectangle = self.canvas.create_rectangle(
            140, 80, 360, 130, fill="#4B9CD3")
        self.exercise_label = self.canvas.create_text(
            250, 100, text="Exercise:", fill="black", font="Helvetica 14 bold")
        self.reps_label = self.canvas.create_text(
            250, 120, text="Reps:", fill="black", font="Helvetica 14 bold")

        # Create an empty label for the image
        self.image_label = self.canvas.create_image(250, 300, anchor="center")

        # Create a button to generate random exercise
        image_button = PhotoImage(file='assets/button_image.png')
        self.generate_button = tk.Button(
            self.root,
            image=image_button,
            text="Generate Exercise",
            font=self.custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=180,
            compound=CENTER,
            command=self.generate_random_exercise)
        self.generate_button_window = self.canvas.create_window(
            250, 500, anchor="center", window=self.generate_button)

        # Create a image back button
        self.back_button = tk.Button(
            self.root,
            image=image_button,
            text="Back",
            font=self.custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=150,
            compound=CENTER,
            command=self.home)
        self.back_button_window = self.canvas.create_window(
            250, 550, anchor="center", window=self.back_button)

        # Create a progress bar
        self.progress_var = DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.canvas,
            variable=self.progress_var,
            length=400,
            mode='determinate')
        self.canvas.create_window(
            250, 650, anchor="center", window=self.progress_bar)
        
         # Create a label for the intruction text
        text_label = tk.Label(
            self.root,
            text="1.Click on the generate button to generate excerise"
            "\n2.Click on back button go back to the home page"
            "\n3.The progressbar is to show how many excerise have you done"
            "\n4.Find a right pace for yourself",
            bg="#4B9CD3",
            fg="black",
            wraplength=400,
            font=self.small_custom_font)
        text_label.place(x=50, y=620)

        self.root.mainloop()

    # Function for generating random exercise
    def generate_random_exercise(self):
        ''''Check if all exercises have been shown'''
        if len(self.exercises_shown) == len(self.exercises):
            self.canvas.itemconfig(
                self.exercise_label,
                text="All exercises have been shown.")
            self.canvas.itemconfig(self.reps_label, text="")
            self.canvas.itemconfig(self.image_label, image="")
            self.generate_button.config(
                text="Well Done")  # Change the button text
            return

        # Get a random exercise that hasn't been shown yet
        exercise = random.choice(self.exercises)
        while exercise in self.exercises_shown:
            exercise = random.choice(self.exercises)

        exercise_name = exercise[0]
        reps = exercise[1]
        image_data = exercise[2]

        # Display the exercise and reps
        self.canvas.itemconfig(
            self.exercise_label,
            text="Exercise: " +
            exercise_name)
        self.canvas.itemconfig(self.reps_label, text="Reps: " + str(reps))

        # Load and display the image
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((400, 300))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)
        self.canvas.itemconfig(self.image_label, image=photo)
        self.canvas.image = photo

        # Add the exercise to the list of shown exercises
        self.exercises_shown.append(exercise)

        # Update the progress bar
        self.progress_var.set(len(self.exercises_shown) /
                              len(self.exercises) * 100)

    # Function for the back button
    def home(self):
        '''Destory cardio GUI and then import home GUI'''
        self.root.destroy()
        # Open home.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "home.py"])


# Check if is the script running the main progarm
if __name__ == "__main__":
    app = CardioExerciseApp()
