import tkinter as tk
import random

# scores
cscore = 0
hscore = 0

def play(user):
    global cscore, hscore

    com = random.randint(1, 3)

    choices = {1: "Stone", 2: "Paper", 3: "Scissors"}
    
    result_text.set(f"You chose {choices[user]} | Computer chose {choices[com]}")

    if user == 1 and com == 3:
        hscore += 1
        msg.set("You won this round!")
    elif user == 2 and com == 1:
        hscore += 1
        msg.set("You won this round!")
    elif user == 3 and com == 2:
        hscore += 1
        msg.set("You won this round!")
    elif user == com:
        msg.set("It's a draw!")
    else:
        cscore += 1
        msg.set("Computer won this round!")

    score.set(f"You: {hscore}  |  Computer: {cscore}")

    # check winner
    if hscore == 5:
        msg.set("🎉 Congratulations! You won the game!")
        disable_buttons()
    elif cscore == 5:
        msg.set("💻 Computer won the game!")
        disable_buttons()

def disable_buttons():
    btn1.config(state="disabled")
    btn2.config(state="disabled")
    btn3.config(state="disabled")

# UI setup
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("400x300")

# variables
score = tk.StringVar(value="You: 0  |  Computer: 0")
result_text = tk.StringVar()
msg = tk.StringVar()

# labels
tk.Label(root, text="Stone Paper Scissors", font=("Arial", 16)).pack(pady=10)
tk.Label(root, textvariable=score, font=("Arial", 12)).pack()
tk.Label(root, textvariable=result_text).pack(pady=5)
tk.Label(root, textvariable=msg, fg="blue").pack(pady=5)

# buttons
btn1 = tk.Button(root, text="Stone", width=10, command=lambda: play(1))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Paper", width=10, command=lambda: play(2))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Scissors", width=10, command=lambda: play(3))
btn3.pack(pady=5)

root.mainloop()