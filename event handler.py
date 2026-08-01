from tkinter import *
window = Tk()
window.title('Event Handler')
window.geometry("100x100")

def handle_keypress(event):
    """Print the characters which are associated to the key pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nthe button was clicked!")


button = Button(text='Click Me!')
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()