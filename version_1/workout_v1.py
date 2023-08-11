import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import sys


class WorkoutApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Workout")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Executing another python script with the same interpreter
        self.PYTHON_EXECUTABLE = sys.executable

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="both", expand=True)

        # Create a canvas widget
        canvas = tk.Canvas(button_frame)
        canvas.pack(fill="both", expand=True)

        top_text = tk.Label(canvas, text="Workout", font=("Helvetica", 60))
        top_text.pack()

        self.add_workout_button(canvas, "Back Exercises", "assets/back_traning.png", self.back)
        self.add_workout_button(canvas, "Bicep Exercises", "assets/bicep_traning.png", self.bicep)
        self.add_workout_button(canvas, "Chest Exercises", "assets/chest traning.png", self.chest)
        self.add_workout_button(canvas, "Triceps Exercises", "assets/Triceps_traning.png", self.triceps)
        self.add_workout_button(canvas, "Shoulder Exercises", "assets/shoulder_traning.png", self.shoulder)
        self.add_workout_button(canvas, "Cardio Exercises", "assets/cardio traning.png", self.cardio)
        self.add_workout_button(canvas, "Leg Exercises", "assets/leg traning.png", self.leg)
        self.add_workout_button(canvas, "Abs Exercises", "assets/abs traning.png", self.abs)

    def add_workout_button(self, parent, text, image_path, command):
        workout_text = tk.Label(parent, text=text, font=("Helvetica", 30))
        workout_text.pack()

        workout_image = ImageTk.PhotoImage(Image.open(image_path).resize((485, 250), Image.ANTIALIAS))
        workout_button = tk.Button(parent, image=workout_image, text=text, command=command)
        workout_button.image = workout_image
        workout_button.pack()

    def back(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/abs_v1.py"])

    def bicep(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/bicep_v1.py"])

    def abs(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/abs_v1.py"])

    def chest(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/chest_v1.py"])

    def leg(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/leg_v1.py"])

    def shoulder(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/shoulder_v1.py"])

    def triceps(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/triceps_v1.py"])

    def cardio(self):
        self.root.destroy()
        subprocess.Popen([self.PYTHON_EXECUTABLE, "design/version_1/cardio_v1.py"])

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = WorkoutApp()
    app.run()
