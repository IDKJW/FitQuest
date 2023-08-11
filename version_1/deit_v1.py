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
        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = font.Font(weight="bold")
        self.small_custom_font = font.Font(family="Helvetica", size=17)

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


        # Create text for intructions for back button
        self.canvas.create_text(
            247,
            450,
            text="Click here to go back to the home screen",
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

        self.root.mainloop()

    # Function for the home button
    def home(self):
        '''Destory diet GUI and then import home GUI'''
        self.root.destroy()
        # Open home.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "design/home.py"])

# Check if is the script running the main progarm
if __name__ == "__main__":
    app = DietApp()
