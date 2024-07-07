# import tkinter as tk
# from PIL import ImageTk, Image   
  
# # creating main window 
# root = tk.Tk()   
  
# # arranging application parameters 
# canvas = tk.Canvas(root, width = 900, height = 500)   
  
# canvas.pack()   
  
# # loading the image 
# img = ImageTk.PhotoImage(Image.open("image1.png"))   
  
# # arranging image parameters  
# # in the application 
# canvas.create_image(300, 100, image = img)  
  
# # running the application 
# root.mainloop()  

import tkinter 
from PIL import ImageTk, Image 
import os 
  
# creating main window 
root = tkinter.Tk() 
  
# loading the image 
img = ImageTk.PhotoImage(Image.open("image1.png")) 
  
# reading the image 
panel = tkinter.Label(root, image = img) 
  
# setting the application 
panel.pack(side = "bottom", fill = "both", 
           expand = "yes") 
  
# running the application 
root.mainloop() 