import tkinter as tk
from tkinter import ttk

from PIL.Image import Image

SCREEN_HEIGHT = 1500
SCREEN_WIDTH = 2500

#class UIHandler:
#    def __init__(self):
#        print ("UI initialized")

        #pages
def loading_page():
    #all the other pages. pack_forget()
    #loading page shit .pack()
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


        #everything

    #window
window = tk.Tk(className = "Invisible Man")
window.configure(bg = '#B7B6B6')
window.geometry("2500x1500")

    #loading page
#label = Label(window, text="Invisible Man", font=("Times New Roman", 30)).pack()
#label.grid(column=0, row=0)

    #landing page

image1 = open('..\src\images\Logo.png', 'r+b')
display(image1)
#logo_photo = Image.l('..\src\images\Logo.png')
 #= tk.PhotoImage(file = "..\src\images\Logo.png")

bt = tk.Button(window, text="Start", bg = "#b7b6b6", command = clicked)
bt.config(width = 20, height = 2)
bt.place(x = 30, y = 50)
#bt.grid(column=3, row= 2)
window.mainloop()

