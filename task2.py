import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Labels and entry fields
tk.Label(root, text="Enter the first number:").pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12), justify="center")
entry1.pack(pady=5)

tk.Label(root, text="Enter the second number:").pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12), justify="center")
entry2.pack(pady=5)

# Dropdown menu for operations
tk.Label(root, text="Select an operation:").pack(pady=5)
operation_var = tk.StringVar(value="+")
operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operations_menu.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate, bg="green", fg="white", font=("Arial", 12))
calc_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result:", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()
