import tkinter as tk
from tkinter import ttk
#class UIHandler:
#    def __init__(self):
#        print ("UI initialized")

def clicked():
    label = tk.Label()
    label.configure(text="you clicked, yay")
    label.pack()

window = tk.Tk(className = "Invisible Man")
window.configure(bg = '#B7B6B6')
window.geometry("3500x2000")


#label = Label(window, text="Invisible Man", font=("Times New Roman", 30)).pack()
#label.grid(column=0, row=0)


#button_photo = PhotoImage(file = r"C:\Users\kimia\OneDrive\Documents\GitHub\Invisible-Man\src\images\Logo.png")

bt = tk.Button(window, text="Start", bg = "#b7b6b6", command = clicked)
bt.config(width = 20, height = 2)
bt.pack()
#bt.grid(column=3, row= 2)
window.mainloop()

