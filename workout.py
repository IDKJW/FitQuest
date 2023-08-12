'''Import moduel
This page is all about the workout excerise for the user to interact with'''
import tkinter as tk
from tkinter import ttk, CENTER, PhotoImage, font
import subprocess
import sys
from PIL import ImageTk, Image


class WorkoutApp:
    '''This the a class that warps around all the functions and output'''

    def __init__(self):
        '''This create a canvas and by using canvas to hold all the image button
        which is the excerise wheere the user click on it.
        It takes them to the excerise that they click on'''
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("Workout")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Executing another python script with the same interpreter
        self.python_executable = sys.executable

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root, bg="#4B9CD3")
        button_frame.pack(fill="both", expand=True)

        # Create a font
        self.custom_font = font.Font(
            family="Helvetica", size=20, weight="bold")

        # Define image
        self.image_button = PhotoImage(file='assets/button_image.png')

        # Create a canvas widget with a scroll bar
        canvas = tk.Canvas(button_frame, bg="#4B9CD3")
        scrollbar = ttk.Scrollbar(
            button_frame,
            orient="vertical",
            command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas for the buttons
        button_canvas = tk.Frame(canvas, bg="#4B9CD3")
        canvas.create_window((0, 0), window=button_canvas, anchor="nw")

        # Back_button
        self.back_button = tk.Button(
            self.root,
            image=self.image_button,
            text="Back",
            font=self.custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=100,
            compound=CENTER,
            command=self.home)
        self.back_button_window = canvas.create_window(
            50, 50, anchor="center", window=self.back_button)

        # Create a text for Wokrout
        top_text = tk.Label(
            button_canvas, text="Workout", font=(
                "Helvetica", 60), bg="#4B9CD3")
        top_text.pack()

        # Create a text for instructions
        top_text = tk.Label(
            button_canvas,
            text="Click on any button to start your excerise",
            font=(
                "Helvetica",
                20), bg="#4B9CD3")
        top_text.pack()

        # Create workout buttons and outputing the text and the images on the
        # Create text and image button
        self.workout_button(
            button_canvas,
            "Back Exercises",
            "assets/back_traning.png",
            self.back)
        self.workout_button(
            button_canvas,
            "Bicep Exercises",
            "assets/bicep_traning.png",
            self.bicep)
        self.workout_button(
            button_canvas,
            "Chest Exercises",
            "assets/chest traning.png",
            self.chest)
        self.workout_button(
            button_canvas,
            "Triceps Exercises",
            "assets/Triceps_traning.png",
            self.triceps)
        self.workout_button(
            button_canvas,
            "Shoulder Exercises",
            "assets/shoulder_traning.png",
            self.shoulder)
        self.workout_button(
            button_canvas,
            "Cardio Exercises",
            "assets/cardio traning.png",
            self.cardio)
        self.workout_button(
            button_canvas,
            "Leg Exercises",
            "assets/leg traning.png",
            self.leg)
        self.workout_button(button_canvas,
                            "Abs Exercises",
                            "assets/abs traning.png",
                            self.abs)

        # Update the scroll region of the canvas
        button_canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Enable scrolling with the middle mouse button
        canvas.bind_all("<MouseWheel>",
                        lambda event: canvas.yview_scroll(-1 * int(event.delta / 120),
                                                          "units"))
    # Function for the buttons

    def workout_button(self, parent, text, image_path, command):
        """This functions is where all the button functions are define such as
        defining the image and defing a font and pack the workout text"""
        workout_text = tk.Label(parent, text=text, font=("Helvetica", 30))
        workout_text.pack()

        workout_image = ImageTk.PhotoImage(
            Image.open(image_path).resize(
                (485, 250), Image.ANTIALIAS))
        workout_button = tk.Button(
            parent,  # Act  as a container for the button widget
            image=workout_image,
            text=text,
            command=command)
        workout_button.image = workout_image
        workout_button.pack()

    # Function for the back button
    def back(self):
        """Destory workout GUI and then import back GUI"""
        self.root.destroy()
        # Open back.py using the Python interpreter
        subprocess.Popen([self.python_executable, "back.py"])

    # Function for the home button
    def home(self):
        """Destory workout GUI and then import back GUI"""
        self.root.destroy()
        # Open home.py using the Python interpreter
        subprocess.Popen([self.python_executable, "home.py"])

    # Function for the bicep button
    def bicep(self):
        """Destory workout GUI and then import bicep GUI"""
        self.root.destroy()
        # Open bicep.py using the Python interpreter
        subprocess.Popen([self.python_executable, "bicep.py"])

    # Function for the abs button
    def abs(self):
        """Destory workout GUI and then import abs GUI"""
        self.root.destroy()
        # Open abs.py using the Python interpreter
        subprocess.Popen([self.python_executable, "abs.py"])

    # Function for the chest button
    def chest(self):
        """Destory workout GUI and then import chest GUI"""
        self.root.destroy()
        # Open chest.py using the Python interpreter
        subprocess.Popen([self.python_executable, "chest.py"])

    # Function for the leg button
    def leg(self):
        """Destory workout GUI and then import leg GUI"""
        self.root.destroy()
        # Open leg.py using the Python interpreter
        subprocess.Popen([self.python_executable, "leg.py"])

    # Function for the shoulder button
    def shoulder(self):
        """Destory workout GUI and then import shoulder GUI"""
        self.root.destroy()
        # Open shoulder.py using the Python interpreter
        subprocess.Popen([self.python_executable, "shoulder.py"])

    # Function for the triceps button
    def triceps(self):
        """Destory workout GUI and then import triceps GUI"""
        self.root.destroy()
        # Open triceps.py using the Python interpreter
        subprocess.Popen([self.python_executable, "triceps.py"])

    # Function for the cardio button
    def cardio(self):
        """Destory workout GUI and then import cardio GUI"""
        self.root.destroy()
        # Open cardio.py using the Python interpreter
        subprocess.Popen([self.python_executable, "cardio.py"])

    # Start the loop

    def run(self):
        """Start the mainloop """
        self.root.mainloop()


# Check if is the script running the main progarm
if __name__ == "__main__":
    app = WorkoutApp()
    app.run()
