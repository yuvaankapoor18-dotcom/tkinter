import tkinter as tk
from tkinter import messagebox
from datetime import date
from calendar import monthrange


def calculate_age():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter integer values for year, month and day.")
        return

    today = date.today()

    if year > today.year or year < 0:
        messagebox.showerror("Invalid year", "Impossible birth year.")
        return
    if month < 1 or month > 12:
        messagebox.showerror("Invalid month", "Birth month must be between 1 and 12.")
        return

    # validate day against actual days in that month/year
    max_day = monthrange(year, month)[1]
    if day < 1 or day > max_day:
        messagebox.showerror("Invalid day", f"Day must be between 1 and {max_day} for the given month.")
        return

    # Compute age
    age_years = today.year - year
    age_months = today.month - month
    age_days = today.day - day

    if age_days < 0:
        prev_month = today.month - 1
        prev_year = today.year
        if prev_month == 0:
            prev_month = 12
            prev_year -= 1
        days_in_prev_month = monthrange(prev_year, prev_month)[1]
        age_days += days_in_prev_month
        age_months -= 1

    if age_months < 0:
        age_months += 12
        age_years -= 1

    result_text = f"Age: {age_years} years, {age_months} months, {age_days} days"
    label_result.config(text=result_text)


root = tk.Tk()
root.title("Age Checker")
# Allow maximizing / resizing
root.resizable(True, True)

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill='both', expand=True)

tk.Label(frame, text="Birth Year:").grid(row=0, column=6, sticky="e")
entry_year = tk.Entry(frame, width=10)
entry_year.grid(row=0, column=1, padx=6, pady=4)

tk.Label(frame, text="Birth Month:").grid(row=1, column=6, sticky="e")
entry_month = tk.Entry(frame, width=10)
entry_month.grid(row=1, column=1, padx=6, pady=4)

tk.Label(frame, text="Birth Day:").grid(row=2, column=0, sticky="e")
entry_day = tk.Entry(frame, width=10)
entry_day.grid(row=2, column=1, padx=6, pady=4)

btn_calc = tk.Button(frame, text="Calculate Age", command=calculate_age)
btn_calc.grid(row=3, column=0, columnspan=2, pady=(8, 4))

label_result = tk.Label(frame, text="Age: ", font=(None, 11, "bold"))
label_result.grid(row=4, column=0, columnspan=2, pady=(6, 0))

root.mainloop()
