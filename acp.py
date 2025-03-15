import tkinter as tk
from tkinter import messagebox
import random 

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choices)


    result = ""
    if user_choice == computer_choice:
        result = f"It's a tie! Both chose {user_choice}."
    elif(user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Paper" and computer_choice == "Rock") or \
        (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! {user_choice} beats {computer_choice}"
    else:
        result = f"You lose! {computer_choice} beats {user_choice}"

    # Update the result label
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Function to reset the game
    def reset_game():
        result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissor game")
root.geometry("400x300")
root.configure(bg="lightgray")

# Label for instruction 
instruction_label = tk.Label(root, text="Choose Rock, Paper or Scissors:", font=("Arial", 14), bg="lightgray")
instruction_label.pack(pady=10)

# Buttons for user choices 
rock_button = tk.Button(root, text='Rock', font=("Arial", 12), width=10, command=lambda: determine_winner("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text='Paper', font=("Arial", 12), width=10, command=lambda: determine_winner("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text='Scissors', font=("Arial", 12), width=10, command=lambda: determine_winner("Scissors"))
scissors_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
result_label.pack(pady=20)

# Button to reset the game
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), width=10)
reset_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

    

    