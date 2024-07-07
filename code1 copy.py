import tkinter as tk
from PIL import ImageTK, Image
import os
import pyttsx3

engine = pyttsx3.init()


window = tk.Tk()
window.title("About Indian Islands")
window.configure(background="black")

head_img = tk.PhotoImage(file="imag1.png")