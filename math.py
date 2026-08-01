from tkinter import *
import math

root = Tk()
root.title('SUM UP!')
root.geometry('500x500')

lbl = Label(text= "Hey There!", fg= "White", bg= "Blue", height=1, width=300)

name_lbl1 = Label(text= "Number 1", bg="orange")
name_entry1 = Entry()
name_lbl2 = Label(text= "Number 2", bg="orange")
name_entry2 = Entry()

def display():

    num1 = int(name_entry1.get())
    num2 = int(name_entry2.get())
    product = num1 * num2
    global message
    message = "Welcome to the Application! ",num1," + ", num2," = ",product,"\n"

    text_box.insert(END, message)

text_box = Text(height=3)


btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg= "White")

lbl.pack()
name_lbl1.pack()
name_entry1.pack()
name_lbl2.pack()
name_entry2.pack()
btn.pack()
text_box.pack()

root.mainloop()