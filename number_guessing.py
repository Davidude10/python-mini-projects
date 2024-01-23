import tkinter as tk
import random
def start():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="")
    guess_entry.delete(0, 'end')
def my_guess():
    guess = guess_entry.get()
    
    try:
        guess = int(guess)
        if guess == secret_number:
            result_label.config(text="Congratulations! You guessed the number!")
        elif guess < secret_number:
            result_label.config(text="Try a higher number.")
            odd_even()
        else:
            result_label.config(text="Try a lower number.")
            prime()
    except ValueError:
        result_label.config(text="Please enter a valid number.")
def prime():
    count=0
    for i in range(2,secret_number):
        if(secret_number%i==0):
            count+=1
    if count==0:
        prime_label.config(text="Hint : it is a prime number 😎")
    else:
        prime_label.config(text="Hint : it is not a prime number 😎")
def odd_even():
    if ((secret_number%2)==0):
        oddeven_label.config(text="Hint : it is an even number 😎")
    else:
        oddeven_label.config(text="Hint : it is an odd number 😎")
a = tk.Tk()
a.title("Number Guessing Game")

title_label = tk.Label(a, text="Guess the Number Game", font=("roboto", 18),foreground="red")
title_label.pack(pady=10)


start_button = tk.Button(a, text="Start New Game", command=start,height=3,background="green",foreground="yellow")
start_button.place(x=200,y=50)

prime_label=tk.Label(a, text="", font=("roboto", 12),background="sky blue",foreground="blue")
prime_label.place(x=120,y=120)

oddeven_label=tk.Label(a, text="", font=("roboto", 12),background="sky blue",foreground="black")
oddeven_label.place(x=120,y=160)

guess_entry = tk.Entry(a)
guess_entry.place(x=180,y=270)

check_button = tk.Button(a, text="Check Guess", command=my_guess,height=3,background="white",foreground="blue")
check_button.place(x=200,y=300)


result_label = tk.Label(a, text="", font=("roboto", 12),background="sky blue",foreground="red")
result_label.place(x=120,y=380)

start()

a.geometry("500x500")
a.configure(background="sky blue")
a.mainloop()
