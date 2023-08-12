'''Import moduels
This diet page shwos the best diet food for the users
and it have a bmi calculater for the user to use to keep track of their progress'''
import tkinter as tk
from tkinter import font, PhotoImage, Canvas, TRUE, Button, CENTER
import sys
import subprocess


# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class DietApp:
    """Where all the functions and output of it"""

    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("Diet plan")
        self.root.geometry("500x800")
        self.root.resizable(width=False, height=False)

        # Create a Canvas
        self.canvas = Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=TRUE)

        # Define image and output it
        self.background = PhotoImage(file="assets/pixel_food_background.png")
        self.canvas.create_image(0, 0, image=self.background, anchor="nw")

        # Create a background color rectangle
        self.background_rectangle = self.canvas.create_rectangle(
            10, 10, 480, 760, fill="#4B9CD3")

        # Create a custom font for the text
        self.custom_font = font.Font(
            family="Helvetica", size=15, weight="bold")
        self.label_font = font.Font(weight="bold")
        self.small_custom_font = font.Font(family="Helvetica", size=13,)

        # Create text in canvas
        self.canvas.create_text(
            90,
            50,
            text="Lean Proteins:",
            fill="black",
            font=self.custom_font)

        # Create text in canvas
        self.canvas.create_text(
            235,
            70,
            text="Foods that have protein are the best for muscle growth",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            234,
            87,
            text="and repair. The food can be like chicken breast, turkey,",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            240,
            105,
            text="Turkey, tofu. lentils , greek yoghurt and eggs in your diet.",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            45,
            140,
            text="Tips:",
            fill="black",
            font=self.custom_font)

        # Create text in canvas
        self.canvas.create_text(
            240,
            165,
            text="Drinking water before each meal can help with weight loss",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            60,
            190,
            text="Snacks:",
            fill="black",
            font=self.custom_font)

        # Create text in canvas
        self.canvas.create_text(
            230,
            210,
            text="Best snacks that you eat are Greek yoghurt, nuts,rice   ",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            245,
            230,
            text="crackers, protein bars, protein smoothies, protein cake and",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            242,
            250,
            text="more. These have some good sources of protein and help",
            fill="black",
            font=self.small_custom_font)

       # Create text in canvas
        self.canvas.create_text(
            250,
            270,
            text="you to get some neutrons in. PLEASE CHECK THE LABEL ",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            243,
            300,
            text="BEFORE BUYING IT or you can use a cronometer app to \nscan before buying it ",
            fill="black",
            font=self.small_custom_font)

        # Create text in canvas
        self.canvas.create_text(
            125,
            340,
            text="Best choice for meal:",
            fill="black",
            font=self.custom_font)

        # Create text in canvas
        self.canvas.create_text(
            238,
            365,
            text="Chicken and rice. You could put some seasoning on the ",
            fill="black",
            font=self.small_custom_font)

       # Create text in canvas
        self.canvas.create_text(
            247,
            385,
            text="chicken so that the chicken is not dry and not boring at all. ",
            fill="black",
            font=self.small_custom_font)

        # Create text for intructions for back button
        self.canvas.create_text(
            247,
            450,
            text="Click here to go back to the home screen",
            fill="black",
            font=self.small_custom_font)

        # Create text for intructions for BMI caculator
        self.canvas.create_text(
            247,
            710,
            text="If you want to know your BMI,\n "
            "please enter your height and your body, \nafter that click on the caculate BMI button",
            fill="black",
            font=self.small_custom_font)

        # Define the image
        image_button = PhotoImage(file='assets/button_image.png')

        # Create a back button with a image
        back_button = Button(
            self.root,
            image=image_button,
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
        self.back_button_window = self.canvas.create_window(
            250, 500, anchor="center", window=back_button)

        # An entry widget for height
        height_label = tk.Label(
            self.canvas,
            text="Height (cm):",
            font=self.label_font,
            bg="#4B9CD3",
            fg="black")
        height_label.place(x=40, y=550)
        self.height_entry = tk.Entry(self.canvas)
        self.height_entry.place(x=130, y=550)

        # An entry widget for weight
        weight_label = tk.Label(
            self.canvas,
            text="Weight (kg):",
            font=self.label_font,
            bg="#4B9CD3",
            fg="black")
        weight_label.place(x=40, y=600)
        self.weight_entry = tk.Entry(self.canvas)
        self.weight_entry.place(x=130, y=600)

        # Result label for displaying the BMI
        self.result_label = tk.Label(
            self.canvas,
            font=(
                "Helvetica",
                18,
                "bold"),
            bg="#4B9CD3",
            fg="black")
        self.result_label.place(x=390, y=600, anchor="center")

        # Calculate button
        self.calculate_button = Button(
            self.root,
            image=image_button,
            text="Calculate BMI",
            font=self.custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=200,
            compound=CENTER,
            command=self.calculate_bmi)
        self.back_button_window = self.canvas.create_window(
            250, 660, anchor="center", window=self.calculate_button)

        self.root.mainloop()

        # Function of caluclating BMI
    def calculate_bmi(self):
        '''Get the weight and height from the entry widget,
        the height and weight value can be decimal values because of float point number
        if the user didn't enter a postive number it will display an erro message,
        if the user didn't enter a number and the progarm will tell the user to enter a number'''
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            if height <= 0 or weight <= 0:
                self.result_label.config(
                    text="Invalid input. \nHeight and weight \nmust be positive numbers.",
                    font=self.small_custom_font)
            elif height > 1000 or weight > 1000:  # Add this condition to check for numbers over 1000
                self.result_label.config(
                text="Invalid input. \nHeight and weight \ncannot be over 1000.",
                font=self.small_custom_font)
            else:
                bmi = weight / ((height / 100) ** 2)
                self.result_label.config(
                    text=f"Your BMI: {bmi:.2f}",
                    font=self.custom_font)
        except ValueError:
            self.result_label.config(
                text="Invalid input. \nPlease enter valid numbers \nfor height and weight.",
                font=self.small_custom_font)

    # Function for the home button
    def home(self):
        '''Destory diet GUI and then import home GUI'''
        self.root.destroy()
        # Open home.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "home.py"])


# Check if is the script running the main progarm
if __name__ == "__main__":
    app = DietApp()
