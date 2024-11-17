import tkinter as tk
from tkinter import messagebox
import random

# Game Logic
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "user"
    else:
        return "computer"

# Button click handler
def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        result_text = f"Both chose {user_choice}. It's a tie!"
    elif result == "user":
        user_score += 1
        result_text = f"You chose {user_choice}, Computer chose {computer_choice}. You win!"
    else:
        computer_score += 1
        result_text = f"You chose {user_choice}, Computer chose {computer_choice}. Computer wins!"
    
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")
    result_label.config(text=result_text)

# Exit game handler
def exit_game():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.resizable(False, False)

# Scores
user_score = 0
computer_score = 0

# Title Label
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Instructions
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors to play", font=("Arial", 12))
instructions.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="blue")
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 14, "bold"), fg="green")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), width=10, command=exit_game)
exit_button.pack(pady=10)

# Run the app
root.mainloop()
