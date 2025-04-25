import tkinter as tk
import random

# Function to determine the winner
def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Scissors" and computer == "Paper") or \
         (player == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = get_winner(choice, computer_choice)
    result_label.config(
        text=f"Your choice: {choice}\nComputer's choice: {computer_choice}\nResult: {result}"
    )

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x300")

# Instruction label
label = tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 14))
label.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Rock Button
rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

# Paper Button
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

# Scissors Button
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), pady=20)
result_label.pack()

# Run the GUI loop
root.mainloop()
