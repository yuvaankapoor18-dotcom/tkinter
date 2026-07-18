from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started With Widgets')
root.geometry('500x500')

lbl = Label(text= "Hey There!", fg= "White", bg= "Blue", height=1, width=300)

name_lbl = Label(text= "Full Name", bg="orange")
name_entry = Entry()

def display():

    name = name_entry.get()

    global message
    message = "Welcome to the Application! Happy Birthday! \nToday's date is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)


btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg= "White")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()