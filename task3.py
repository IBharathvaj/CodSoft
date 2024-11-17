import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Password length must be greater than 0.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    output_label.config(text=f"Generated Password: {password}")

def copy_to_clipboard():
    password = output_label.cget("text").replace("Generated Password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Now it stays on the clipboard after the app closes
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("No Password", "No password to copy!")

# Set up the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Entry for password length
length_label = tk.Label(root, text="Enter the desired password length:")
length_label.pack()

entry = tk.Entry(root, width=15, justify="center", font=("Arial", 12))
entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white", font=("Arial", 12))
generate_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
output_label.pack(pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white", font=("Arial", 12))
copy_button.pack(pady=10)

# Run the application
root.mainloop()
