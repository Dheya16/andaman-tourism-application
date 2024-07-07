import tkinter as tk
import pyttsx3
import threading

engine = pyttsx3.init()

def click():
    def play_audio(message):
        engine.say(message)
        engine.startLoop()
    
    sen = "This is a sample program"
    x = threading.Thread(target=play_audio, args=(sen,))
    x.start()

window = tk.Tk()
window.title("Sample")
btn = tk.Button(window, text="Submit", bg="black", fg="white", command=click)
btn.grid(row=0, column=0, sticky=tk.W)
window.update()
window.mainloop()