from tkinter import *

#class UIHandler:
#    def __init__(self):
#        print ("UI initialized")

def clicked():
    label.configure(text="you clicked, yay")

window = Tk()
window.title("Invisible Man")
label = Label(window, text="Invisible Man", font=("Times New Roman", 30))
label.grid(column=0, row=0)
window.geometry("350x200")
bt = Button(window, text="Enter", font=("Arial Bold", 25), command=clicked)
bt.grid(column=1, row= 0)
window.mainloop()

