import tkinter as tk
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import io
import random
import sys
import subprocess

# Executing another python script with the same interpreter
python_executable = sys.executable


class AbsExerciseApp:
    def __init__(self):
        # Create a database connection
        self.connection = sqlite3.connect("db/workout.db")
        self.cursor = self.connection.cursor()

        # Get all exercises from the database
        self.cursor.execute("SELECT exercise, reps, image FROM Abs")
        self.exercises = self.cursor.fetchall()

        # Close the database connection
        self.connection.close()

        # Create the main application window
        self.abs = tk.Tk()
        self.abs.title("abs Exercise")
        self.abs.geometry("500x800")
        self.abs.resizable(width=False, height=False)

        # Create background image
        background_image = PhotoImage(file="assets/Aim high.png")
        self.background_label = Label(self.abs, image=background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create an empty list to track the shown exercises
        self.exercises_shown = []

        # Create labels for exercise and reps
        self.exercise_label = tk.Label(
            self.abs, text="Exercise:", background="black", fg="white")
        self.exercise_label.pack()

        self.reps_label = tk.Label(
            self.abs, text="Reps:", background="black", fg="white")
        self.reps_label.pack()

        # Create an empty label for the image
        self.image_label = tk.Label(self.abs, background="black")
        self.image_label.pack()

        # Create a button to generate random exercise
        self.generate_button = tk.Button(
            self.abs,
            text="Generate Exercise",
            command=self.generate_random_exercise,
            background="black",
            fg="black")
        self.generate_button.pack()

        # Create a label with clickable text
        self.back_text_button = tk.Label(
            self.abs,
            text="<- Back",
            fg="blue",
            cursor="hand2",
            background="black")
        self.back_text_button.pack()

        # Bind the click event to the label
        self.back_text_button.bind("<Button-1>", self.text_clicked)

        self.abs.mainloop()

    def generate_random_exercise(self):
        # Check if all exercises have been shown
        if len(self.exercises_shown) == len(self.exercises):
            self.exercise_label.config(text="All exercises have been shown.")
            self.reps_label.config(text="")
            self.image_label.config(image="")
            return

        # Get a random exercise that hasn't been shown yet
        exercise = random.choice(self.exercises)
        while exercise in self.exercises_shown:
            exercise = random.choice(self.exercises)

        exercise_name = exercise[0]
        reps = exercise[1]
        image_data = exercise[2]

        # Display the exercise and reps
        self.exercise_label.config(text="Exercise: " + exercise_name)
        self.reps_label.config(text="Reps: " + str(reps))

        # Load and display the image
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((400, 300))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Add the exercise to the list of shown exercises
        self.exercises_shown.append(exercise)

    def text_clicked(self, event):
        self.abs.destroy()
        subprocess.Popen([python_executable, "design/version_1/home_v1.py"])


if __name__ == "__main__":
    app = AbsExerciseApp()
