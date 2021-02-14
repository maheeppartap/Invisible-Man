import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageDraw, ImageTk

SCREEN_HEIGHT = 1500
SCREEN_WIDTH = 2500

#class UIHandler:
#    def __init__(self):
#        print ("UI initialized")

        #pages
def loading_page():
    load = Image.open('..\src\images\logo.png')
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render)
    panel.photo = render
    panel.place(x=22, y=222)

    return 0

def landing_page():
    #all the other pages .pack_forget()
    #landing page shit .pack()
    return 0

def submitted_page():
    #all the other pages .pack_forget()
    #submitted page shit .pack()
    return 0

def about_page():
    #all the other pages .pack_forget()
    #about page shit .pack()
    return 0


        #diff buttons clicked
def clicked():

    label = tk.Label()
    label.configure(text="you clicked, yay")
    label.pack()

window = tk.Tk(className = "Invisible Man")
window.configure(bg = '#B7B6B6')
window.geometry("2500x1500")
loading_page()
window.mainloop()

