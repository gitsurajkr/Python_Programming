import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def selectionOfWinner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "\nIt's tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "\nYou win!"
    else:
        return "\nComputer wins!"

def play(player_choice):
    computer_choice = get_computer_choice()
    result = selectionOfWinner(player_choice, computer_choice)
    result_label.config(text=f"Computer choice: {computer_choice}. {result}")

window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("350x250")
instructions = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
instructions.pack()
button_width = 15
button_height = 2
rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"), width=button_width, height=button_height)
paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"), width=button_width, height=button_height)
scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"), width=button_width, height=button_height)
rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
