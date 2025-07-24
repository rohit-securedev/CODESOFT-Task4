import tkinter as tk
import random

choices = ['Rock', 'Paper', 'Scissors']
emoji_map = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂️'}

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    user_display.config(text=f"{emoji_map[user_choice]} {user_choice}")
    comp_display.config(text=f"{emoji_map[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        result_display.config(text="It's a Tie! 🤝", fg="gold")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        user_score += 1
        result_display.config(text="You Win! 🎉", fg="green")
    else:
        computer_score += 1
        result_display.config(text="You Lose! 😞", fg="red")

    score_display.config(text=f"You: {user_score}  |  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_display.config(text="🧑 Your Choice:")
    comp_display.config(text="🤖 Computer Chose:")
    result_display.config(text="📢 Result:")
    score_display.config(text="You: 0  |  Computer: 0")

def quit_game():
    root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.config(bg="#f0f8ff")
root.geometry("500x450")

tk.Label(root, text="🪨 📄 ✂️ Rock-Paper-Scissors Game", font=("Helvetica", 18, "bold"), bg="#f0f8ff").pack(pady=10)

user_display = tk.Label(root, text="🧑 Your Choice:", font=("Helvetica", 14), bg="#f0f8ff")
user_display.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack()

for choice in choices:
    btn = tk.Button(btn_frame, text=f"{emoji_map[choice]} {choice}", font=("Helvetica", 12, "bold"), width=12,
                    command=lambda c=choice: play(c), bg="#e6e6fa", activebackground="#add8e6")
    btn.pack(side=tk.LEFT, padx=10, pady=5)

comp_display = tk.Label(root, text="🤖 Computer Chose:", font=("Helvetica", 14), bg="#f0f8ff")
comp_display.pack(pady=10)

result_display = tk.Label(root, text="📢 Result:", font=("Helvetica", 14, "bold"), bg="#f0f8ff")
result_display.pack(pady=10)

score_display = tk.Label(root, text="You: 0  |  Computer: 0", font=("Helvetica", 13), bg="#f0f8ff")
score_display.pack(pady=10)

bottom_frame = tk.Frame(root, bg="#f0f8ff")
bottom_frame.pack(pady=15)

tk.Button(bottom_frame, text="Play Again 🔄", font=("Helvetica", 12), command=reset_game,
          bg="#d4f1f9", width=15).pack(side=tk.LEFT, padx=10)

tk.Button(bottom_frame, text="Quit ❌", font=("Helvetica", 12), command=quit_game,
          bg="#f9d4d4", width=15).pack(side=tk.LEFT, padx=10)

root.mainloop()
