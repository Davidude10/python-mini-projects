import tkinter as tk

def play(row, col):
    global pl
    global game_over
    if board[row][col] == "" and not game_over:
        board[row][col] = pl
        buttons[row][col].config(text=pl)
        
        if check_winner(pl):
            label.config(text=f"player {pl} wins!")
            game_over = True
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            label.config(text="It's a draw!")
            game_over = True
        else:
            pl = "X" if pl == "O" else "O"

def check_winner(pl):
    for i in range(3):
        if all(board[i][j] == pl for j in range(3)):
            return True
        if all(board[j][i] == pl for j in range(3)):
            return True
    if all(board[i][i] == pl for i in range(3)) or all(board[i][2 - i] == pl for i in range(3)):
        return True
    return False

root = tk.Tk()
root.title("Tic-Tac-Toe")

pl = "X"
global game_over
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: play(i, j),background="light yellow",foreground="dark blue")
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

label = tk.Label(root, text="", font=("Helvetica", 16),background="light green",foreground="red")
label.grid(row=3, column=0, columnspan=3)
label.configure(background="light green")
root.mainloop()
