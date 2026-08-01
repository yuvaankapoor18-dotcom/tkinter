from tkinter import *

root = Tk()
root.geometry("320x220")
root.title("USER LABEL")

frame = Frame(root, width=320, height=220, bg="#d4f1ff")
frame.pack(fill="both", expand=True, padx=10, pady=10)

lbl1 = Label(frame, text="Name:", bg="#d4f1ff", fg="black", width=14, anchor="w")
lbl2 = Label(frame, text="Gender:", bg="#d4f1ff", fg="black", width=14, anchor="w")

name_var = StringVar()
gender_var = StringVar()

name_entry = Entry(frame, textvariable=name_var, width=22)
gender_entry = Entry(frame, textvariable=gender_var, width=22)

result_frame = Frame(frame, bg="#d4f1ff")


def show_name():
    name = name_var.get().strip()
    gender = gender_var.get().strip()
    if name and gender:
        new_label = Label(result_frame, text=f"Name: {name} | Gender: {gender}", bg="#d4f1ff", fg="black", anchor="w")
        new_label.pack(anchor="w", pady=2)
        name_var.set("")
        gender_var.set("")
    else:
        Label(result_frame, text="Please enter both name and gender", bg="#d4f1ff", fg="black", anchor="w").pack(anchor="w", pady=2)


submit_button = Button(frame, text="Show Name", command=show_name)

lbl1.grid(row=0, column=0, padx=8, pady=8, sticky="w")
name_entry.grid(row=0, column=1, padx=8, pady=8)

lbl2.grid(row=1, column=0, padx=8, pady=8, sticky="w")
gender_entry.grid(row=1, column=1, padx=8, pady=8)

submit_button.grid(row=0, column=2, rowspan=2, padx=8, pady=8)
result_frame.grid(row=2, column=0, columnspan=3, padx=8, pady=8, sticky="w")

root.mainloop()