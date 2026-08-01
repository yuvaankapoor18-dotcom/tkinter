from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("NUMBER PAD")

nums = [[1,2,3], [4,5,6], [7,8,9], ['#', 0, '*']]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=80)
    root.rowconfigure(i, weight=1, minsize=55)
    
    for j in range(0, 3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text = nums[i][j], bg = "#d0efff")
        label.pack(padx=3, pady=3)

root.mainloop()