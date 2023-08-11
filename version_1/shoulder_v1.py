import tkinter as tk
import sqlite3
from tkinter import *
import os
import tkinter
import customtkinter
from PIL import ImageTk, Image
import io
import random
import sys
import subprocess

#Executing another python script with the same interpreter
python_executable = sys.executable

# A function where it generate random exercise
def generate_random_exercise():
    global exercises_shown

    # Check if all exercises have been shown
    if len(exercises_shown) == len(exercises):
        exercise_label.config(text="All exercises have been shown.")
        reps_label.config(text="")
        image_label.config(image="")
        return

    # Get a random exercise that hasn't been shown yet
    exercise = random.choice(exercises)
    while exercise in exercises_shown:
        exercise = random.choice(exercises)
    # read the excerise, reps and image in the database 
    exercise_name = exercise[0]
    reps = exercise[1]
    image_data = exercise[2]

    # Display the exercise and reps
    exercise_label.config(text="Exercise: " + exercise_name)
    reps_label.config(text="Reps: " + str(reps))

    # Load and display the image
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((400, 300))  # Adjust the size
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    # Add the exercise to the list of shown exercises
    exercises_shown.append(exercise)

def home(event):
    shoulder.destroy()
    subprocess.Popen([python_executable,"design/version_1/home_v1.py"])
    return

# Create a database connection
connection = sqlite3.connect("db/workout.db")
cursor = connection.cursor()

# Get all exercises from the database
cursor.execute("SELECT exercise, reps, image FROM Shoulder")
exercises = cursor.fetchall()

# Close the database connection
connection.close()

# Create the main application window
shoulder = tk.Tk()
shoulder.title("shoulder Exercise")
shoulder.geometry("500x800")
shoulder.resizable(width=False, height=False)

# Create background image
background_image = PhotoImage(file="assets/Aim high.png")
background_label = Label(shoulder, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create an empty list to track the shown exercises
exercises_shown = []

# Create labels for exercise and reps
exercise_label = tk.Label(shoulder, text="Exercise:", background="black", fg="white")
exercise_label.pack()

reps_label = tk.Label(shoulder, text="Reps:", background="black", fg="white")
reps_label.pack()

# Create an empty label for the image
image_label = tk.Label(shoulder, background="black")
image_label.pack()

# Create a button to generate random exercise
generate_button = tk.Button(shoulder, text="Generate Exercise", command=generate_random_exercise, background="black", fg="black")
generate_button.pack()

# Create a label with clickable text
shoulder_text_button = tk.Label(shoulder, text="<-Back", fg="blue", cursor="hand2", background="black")
shoulder_text_button.pack()

# Bind the click event to the label
shoulder_text_button.bind("<Button-1>", home)

shoulder.mainloop()
