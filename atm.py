from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=240, width=360, bg="#d0efff")

# Add widgets
# Add Label 
lbl1 = Label(frame, text = "Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text = "Email Id", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text = "Enter Password", bg="#3895D3", fg='white', width=12)
lbl4 = Label(frame, text = "ATM Pin", bg="#3895D3", fg='white', width=12)

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")
pin_entry = Entry(frame, show="*")
entry_widgets = [name_entry,email_entry, pass_entry, pin_entry]
textbox = Text(bg="#9B7070", fg="black")

# Function to display message
def display():
	name = name_entry.get()
	greet = "Hey "+name
	message =  "\nCongratulations for your new account!"
	pin = pin_entry.get()
	textbox.insert(END, greet)
	textbox.insert(END, message)
	textbox.insert(END, f"\nYour ATM Pin is: {pin}")

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text = "Create Account", command=display, bg="red")

# Arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
lbl4.place(x=20, y=200)
pin_entry.place(x=150, y=200)
btn.place(x=130, y=260)
textbox.place(y=300)

# Start the GUI event loop
root.mainloop()