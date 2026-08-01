from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
root.title('virus scanner')

def msg():
    messagebox.showwarning("Alert", "Stop! \n Virus Found.")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y = 80)
root.mainloop()