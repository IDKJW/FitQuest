"""Import moduels,
This is the comming soon page where the developer don't have time to get the pages done"""
import tkinter as tk
from tkinter import PhotoImage, TRUE, Canvas, font, CENTER
from datetime import datetime
import sys
import subprocess

# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class ComingSoonApp:
    """This is where all the functions and output of the GUI"""

    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("Coming soon")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Define an image
        background = PhotoImage(file="assets/gym_background_2.png")

        # Make a canvas
        self.canvas = Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=TRUE)

        # Create a image background
        self.canvas.create_image(0, 0, image=background, anchor="nw")

        # Create background_rectangle
        self.background_rectangle = self.canvas.create_rectangle(
            100, 100, 400, 650, fill="#4B9CD3")

        # Define a font
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")

        # Create a label with the text "Coming soon" and pack it
        self.canvas.create_text(
            250,
            200,
            text="Coming soon.........",
            fill="black",
            font=custom_font)

        # Create a label to display the countdown with a specified font
        self.countdown_label = tk.Label(
            self.canvas, font=custom_font, bg="black")
        self.countdown_label.pack(pady=230)

        # Create a label with the text "Coming soon" and pack it
        self.canvas.create_text(
            250,
            350,
            text="The person who made this \ndoesn't have time"
            "\nto do the rest of the code \nplease click here to go back \n     ->",
            fill="black",
            font=custom_font)

        # Create a button to generate random exercise
        image_button_image = PhotoImage(file='assets/button_image.png')
        # Create a image back button
        self.image_button = tk.Button(self.root, image=image_button_image,
                                      text="Back",
                                      font=custom_font,
                                      bg="white",
                                      fg="black",
                                      borderwidth=0,
                                      highlightthickness=0,
                                      height=30,
                                      width=150,
                                      compound=CENTER,
                                      command=self.home)
        self.chest_button_window = self.canvas.create_window(
            250, 400, anchor="center", window=self.image_button)

        # Call the 'update_countdown()' function to start updating the
        # countdown
        self.update_countdown()

        self.root.mainloop()


    # Function for the timer
    def update_countdown(self):
        """This is the countdown timeer that updates constanly
        when the user is at the current GUI"""
        current_time = datetime.now()  # Get the current date and time
        next_year = current_time.replace(
            year=current_time.year + 1,
            month=1,
            day=1,
            hour=0,
            minute=0,
            second=0)
        # Calculate the time left until the next New Year's Day (January 1st of
        # the following year)
        time_left = next_year - current_time
        # Update the label to display the time left
        self.countdown_label.config(text=str(time_left))
        # Schedule the function to run again after 1000 milliseconds (1 second)
        self.countdown_label.after(1000, self.update_countdown)


# Check if is the script running the main progarm
if __name__ == "__main__":
    ComingSoonApp()
