import tkinter as tk
from PIL import ImageTk, Image 
import os
import pyttsx3
engine = pyttsx3.init()

def click():
    def andamanClick():
        # entered_text = textentry.get()
        def anclimateclick():
            anclm = "The climate is tropical, hot all year round, with a dry season from January to April and a rainy season from May to November due to the Indian monsoon.The temperatures are stable throughout the year, however, in March and April, the hottest time of the year occurs."
            img = ImageTk.PhotoImage(Image.open("image1.png")) 
            panel = tk.Label(window, image = img) 
            panel.grid(row=9,column=1,columnspan=4,sticky=tk.W) 
            engine.say(anclm)
            # output.delete(0.0,END)
            engine.runAndWait()

        def anhbtclick():
            anhbt = ""

        def anlocclick():
            anloc = "Andaman consists of 372 Islands with only 36 Inhabited, Havelock Island, Sentinel Island, Car Nicobar Islands. The North Sentinel Island is one of dangerous islands whihc contains the Tribal People and are hostile to outside world."
            engine.say(anloc)
            engine.runAndWait()
        
        climateBtn = tk.Button (window, text="Climate", width=10, command=anclimateclick)
        climateBtn.grid(row=6, column=0, sticky=tk.W)

        habitatBtn = tk.Button(window, text="Habitat", width=10, command=anhbtclick)
        habitatBtn.grid(row=6, column=1, sticky=tk.W)

        locationBtn = tk.Button(window, text="Location", width=10, command=anlocclick)
        locationBtn.grid(row=6, column=2, sticky=tk.W)

        islandsBtn = tk.Button(window, text="Islands", width=10, command=click)
        islandsBtn.grid(row=6, column=3, sticky=tk.W)

        
    def lakswadeepClick():
        clmBtn = tk.Button (window, text="Climate", width=15, command=click)
        clmBtn.grid(row=6, column=0, sticky=tk.W)
        hbtBtn = tk.Button (window, text="Habitat", width=15, command=click)
        hbtBtn.grid(row=6, column=1, sticky=tk.W)
        locBtn = tk.Button (window, text="Location", width=15, command=click)
        locBtn.grid(row=6, column=2, sticky=tk.W)
        ildBtn = tk.Button (window, text="Islands", width=15, command=click)
        ildBtn.grid(row=6, column=3, sticky=tk.W)

    text_entry="Welcome " + textentry.get()
    l2 = tk.Label(window, text=text_entry, bg="black",fg="white",font="ariel 12 bold")
    l2.grid(row=3, column=0 ,sticky=tk.W)

    l3 = tk.Label(window, text="CHOOSE AN ISLAND", bg="black",fg="white",font="none 12 bold")
    l3.grid(row=4, column=0 ,sticky=tk.W)

    andaman_button = tk.Button(window, text="Andaman And Nicobar Islands", width=40, command=andamanClick)
    andaman_button.grid(row=5, column=0, columnspan=2, sticky=tk.W)

    lakswadeep_button = tk.Button(window, text="Lakshadweep Islands", width=40, command=lakswadeepClick)
    lakswadeep_button.grid(row=5, column=2, columnspan=2, sticky=tk.W)
    
    




window = tk.Tk()
window.title("About Indian Islands")
window.configure(background = "black")

pho1 = tk.PhotoImage(file = 'image1.png')
tk.Label(window, image = pho1, bg = "black") .grid (row = 0, column = 0, columnspan=10, sticky = tk.W)
l1 = tk.Label(window, text="Please Enter Your Name", bg="black",fg="white",font="none 12 bold")
l1.grid(row=1, column=0 ,sticky=tk.W)

textentry = tk.Entry (window, width=20, bg="white", fg="black")
textentry.grid(row=2,column=0,sticky=tk.W, columnspan=4)
btn = tk.Button(window,text="Submit",width=6, command=click)
btn.grid(row=2,column=1,sticky=tk.W,columnspan=2)




window.update()
window.mainloop()

