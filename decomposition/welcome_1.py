"""Import modules
This is the welcome page which is the frist page that the user will interact with"""
from tkinter import font, Tk, PhotoImage, Canvas, Button, CENTER
import subprocess
import sys
import customtkinter
from PIL import ImageTk, Image


# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class WelcomeApp:
    """This is where all the function will be store into thi class so that thye all work"""

    def __init__(self):
        """Creating the GUI to welcoem the users and store all the functions inside this class"""
        # Create the main application window
        self.root = Tk()
        self.root.geometry("500x800")
        self.root.resizable(False, False)
        self.root.title("Welcome to FitQuest")

        # Create a font
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        small_custom_font = font.Font(
            family="Helvetica", size=13, weight="bold")

        # Create a Canvas
        self.canvas = Canvas(self.root, width=500, height=800)
        self.canvas.pack(fill="both", expand=True)

        # Define image and output the background image
        self.background_image = PhotoImage(
            file="assets/pixel_welcome_g_0-transformed.png")
        self.canvas.create_image(
            0, 0, image=self.background_image, anchor="nw")

        # Create a skyblue background for the text
        self.background_rectangle = self.canvas.create_rectangle(
            100, 80, 400, 600, fill="#4B9CD3")

        # Create a text for Welcome to FitQuest
        self.canvas.create_text(
            250,
            100,
            text="Welcome to FitQuest",
            fill="black",
            font=custom_font)

        # Create a text for intruction
        self.canvas.create_text(
            250,
            550,
            text="1.Register is for creating a new account"
            "\n2.Login is sign in an account\nClick on any button to continue.",
            fill="black",
            font=small_custom_font)

        # Define the logo image
        self.logo = ImageTk.PhotoImage(Image.open(
            "assets/Logo.png").resize((200, 150), Image.ANTIALIAS))
        # Output the logo image
        self.logo_image = customtkinter.CTkButton(
            master=self.root,
            image=self.logo,
            text="",
            compound="left",
            hover=False,
            bg_color="#020202")
        self.canvas.create_window(250, 250, window=self.logo_image)

        # Define image_button
        self.image_button = PhotoImage(file='assets/button_image.png')

        # out putting Login button
        login_button = Button(
            self.root,
            image=self.image_button,
            text="Login",
            font=custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=250,
            compound=CENTER,
            command=self.login)
        self.login_button_window = self.canvas.create_window(
            250, 400, anchor="center", window=login_button)

        # Outputting Register button
        register_button = Button(
            self.root,
            image=self.image_button,
            text="Register",
            font=custom_font,
            bg="white",
            fg="black",
            borderwidth=0,
            highlightthickness=0,
            height=30,
            width=250,
            compound=CENTER,
            command=self.register)
        self.register_button_window = self.canvas.create_window(
            250, 470, anchor="center", window=register_button)

    # Function for the login button
    def login(self):
        """Destroy the home GUI and import login GUI"""
        self.root.destroy()
        # Open login.py using the Python interpreter
        subprocess.Popen([PYTHON_EXECUTABLE, "login.py"])


    def run(self):
        """Start the main loop"""
        self.root.mainloop()


# Check if is the script running the main progarm
if __name__ == "__main__":
    app = WelcomeApp()
    app.run()
