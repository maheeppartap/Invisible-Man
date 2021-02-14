import time
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageDraw, ImageTk

SCREEN_HEIGHT = 1920
SCREEN_WIDTH = 1080

#class UIHandler:
#    def __init__(self):
#        print ("UI initialized")

        #pages
def window_create():
    window = tk.Tk(className="Invisible Man")
    window.configure(bg='#B7B6B6')
    window.geometry("1920x1080")
    return window

def window_destroy():
    window_destroy()

def loading_page():
    load = Image.open('..\src\images\logo.png')
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render,bg = '#B7B6B6')
    panel.photo = render
    panel.place(relx=.4, rely=.2)
    return 0

def landing_page():
    #all the other pages .pack_forget()
    #landing page shit .pack()

    top_label = tk.Label(bg='#C4AB9B')
    top_label.place(relheight=0.12, relwidth=1)

    load = Image.open(r"..\src\images\minilogo.png")
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render, bg="#C4AB9B")
    panel.photo = render
    panel.place(relx=0, rely=0)

    load = Image.open(r"..\src\images\description.png")
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render, bg="#C4AB9B")
    panel.photo = render
    panel.place(relx=.25, rely=.75)

    load = Image.open('..\src\images\Submit.png')
    render = ImageTk.PhotoImage(load)
    panel = tk.Button(window, image=render, bg='#C4AB9B', activebackground='#C4AB9B',)
    panel.photo = render
    panel.place(relx=.45, rely=.6)

    load = Image.open('..\src\images\imb1.png')
    render = ImageTk.PhotoImage(load)
    panel = tk.Button(window, image=render, bg='#B7A091', activebackground='#B7A091')
    panel.photo = render
    panel.place(relx=.2, rely=.6)

    load = Image.open('..\src\images\imb2.png')
    render = ImageTk.PhotoImage(load)
    panel = tk.Button(window, image=render, bg='#B7A091', activebackground='#B7A091')
    panel.photo = render
    panel.place(relx=.575, rely=.6)

    return 0

def submitted_page():
    #all the other pages .pack_forget()
    #submitted page shit .pack()
    top_label = tk.Label(bg='#C4AB9B')
    top_label.place(relheight=0.12, relwidth=1)

    load = Image.open(r"..\src\images\miniLogo.png")
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render, bg="#C4AB9B")
    panel.photo = render
    panel.place(relx=0, rely=0)

    about_button = tk.Button(text="About", font=("DM Mono", 20), bg="#C4AB9B", fg="#384559", borderwidth=0)
    about_button.place(relheight=0.12, relwidth=0.1, relx=0.9)

    load = Image.open('..\src\images\Download.png')
    render = ImageTk.PhotoImage(load)
    panel = tk.Button(window, image=render, bg='#B7A091', activebackground='#B7A091')
    panel.photo = render
    panel.place(relx=.35, rely=.7)

    return 0

def about_page():
    #all the other pages .pack_forget()
    #about page shit .pack()
    top_label = tk.Label(bg='#C4AB9B')
    top_label.place(relheight=0.12, relwidth=1)

    load = Image.open(r"..\src\images\miniLogo.png")
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render, bg="#C4AB9B")
    panel.photo = render
    panel.place(relx=0, rely=0)

    about_button = tk.Button(text="About", font=("DM Mono", 20), bg="#C4AB9B", fg="#384559", borderwidth=0)
    about_button.place(relheight=0.12, relwidth=0.1, relx=0.9)

    load = Image.open('..\src\images\Screenshot_1.jpg')
    render = ImageTk.PhotoImage(load)
    panel = tk.Label(window, image=render, bg='#B7B6B6')
    panel.photo = render
    panel.place(relx=.1, rely=.1)


    return 0

#diff buttons clicked
def clicked():

    label = tk.Label()
    label.configure(text="you clicked, yay")
    label.pack()

#destroy command to reset window
window = window_create()
window.destroy()

window = window_create()
#submitted_page()
#landing_page()
about_page()

window.mainloop()


