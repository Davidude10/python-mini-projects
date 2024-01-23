import tkinter as tk
import random

def determine_winner(player):
    computer = random.choice(["Rock", "Paper", "Scissors"])
    computer_label.place(x=60, y=40)
    computer_label.config(text="Computer: ")
    computer_label2.place(x=170, y=40)
    computer_label2.config(text=computer)
    if player == computer:
        result_label.config(text="It's a tie!")
    elif (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")
    result_label.place(x=140, y=120)

def rock():
    determine_winner("Rock")

def paper():
    determine_winner("Paper")

def scissor():
    determine_winner("Scissors")

a = tk.Tk()
a.title("Rock Paper Scissors")
clr1='#daf4b9'

player_label = tk.Label(a, text="Your choice: ", relief=tk.RAISED, borderwidth=2,background=clr1)
player_label.place(x=170, y=180)

computer_label = tk.Label(a, text="Computer: ",font=("poppins", 12), foreground="blue")
computer_label2 = tk.Label(a, text="", relief=tk.RAISED, borderwidth=2, font=("poppins", 16), foreground="black")
result_label = tk.Label(a, text="",font=("poppins", 18), foreground="red")

rock_button = tk.Button(a, text="Rock", command=rock, width=10, height=6, background="yellow", relief=tk.RAISED, borderwidth=2)
rock_button.place(x=70, y=220)

paper_button = tk.Button(a, text="Paper", command=paper, width=10, height=6, background="yellow", relief=tk.RAISED, borderwidth=2)
paper_button.place(x=170, y=220)

scissors_button = tk.Button(a, text="Scissors", command=scissor, width=10, height=6, background="yellow", relief=tk.RAISED, borderwidth=2)
scissors_button.place(x=270, y=220)

a.geometry("400x400")
a.mainloop()
