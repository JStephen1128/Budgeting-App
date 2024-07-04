import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def calcBudget(a, b):
    try:
        a = float(a)
        b = float(b)
        if a < 0 or b < 0:
            raise ValueError("Input values should be non-negative.")
        
        necc = a * 0.3
        want = a * 0.2
        debt = b / 2
        sav = (a * 0.5) - debt
        
        result_text = (
            f"Okay, so for necessities, you'd want to set aside ${necc:.2f}.\n"
            f"For your monthly debts, you want to take out ${debt:.2f} from this check.\n"
            f"For your savings, you should send ${sav:.2f} into that account.\n"
			f"So after that, the remaining ${want:.2f} is your spending limit for anything you want!\n"
			f"Thank you for listening!"
        )
        
        result_label.config(text=result_text)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def on_calculate():
    pay = pay_entry.get()
    obl = obl_entry.get()
    calcBudget(pay, obl)

def on_quit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Budgetting App")

# Load and place the image
image = PhotoImage(file="FLLweXJXMAM2RfU.png")  # Replace with the path to your image file
image_label = tk.Label(root, image=image)
image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Define a custom font
custom_font = ("EarthMommaRegular-ZGrK", 14)
title_font = ("EarthMommaRegular-ZGrK", 14)

# Create and place the widgets with custom fonts
tk.Label(root, text="Hello, good afternoon! Welcome to the Wealth Advisory! Please take a seat!", font=title_font).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Please, input the amount you made over these past two weeks:", font=custom_font).grid(row=2, column=0, padx=10, pady=5)
pay_entry = tk.Entry(root, font=custom_font)
pay_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Now input the sum of any monthly obligations:", font=custom_font).grid(row=3, column=0, padx=10, pady=5)
obl_entry = tk.Entry(root, font=custom_font)
obl_entry.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Budget", command=on_calculate, font=custom_font)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left", font=custom_font)
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

quit_button = tk.Button(root, text="Leave Office", command=on_quit, font=custom_font)
quit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
