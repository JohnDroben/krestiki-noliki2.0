import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")
game_active = True
scores = {"X": 0, "O": 0, "Draw": 0}

current_player = "X"
buttons = []


def create_widgets():
    reset_btn = tk.Button(window, text="Новая игра", font=("Arial", 14), command=reset_game)
    reset_btn.grid(row=3, column=0, columnspan=3, pady=10)

    global score_label
    score_label = tk.Label(window,
                         text=f"Игрок X: {scores['X']} | Игрок O: {scores['O']} | Ничьи: {scores['Draw']}",
                         font=("Arial", 12))
    score_label.grid(row=4, column=0, columnspan=3)

    # Исправлено: вынесено из глобальной области видимости
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(window, text="", font=("Arial", 20),
                           width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
            btn.grid(row=i, column=j)
            row.append(btn)
        buttons.append(row)

def update_score_display():
    score_label.config(text=f"Игрок X: {scores['X']} | Игрок O: {scores['O']} | Ничьи: {scores['Draw']}")

def disable_buttons():
    for row in buttons:
        for btn in row:
            btn["state"] = "disabled"

def check_win():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True

# Исправлено: объединение дублированных функций
def on_click(row, col):
    global current_player, game_active

    if not game_active or buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player

    if check_win():
        scores[current_player] += 1
        messagebox.showinfo("Победа!", f"Победил игрок {current_player}!")
        game_active = False
        disable_buttons()
        update_score_display()
        return

    if check_draw():
        scores["Draw"] += 1
        messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
        game_active = False
        disable_buttons()
        update_score_display()
        return

    # Исправлено: правильная смена игрока
    current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, game_active
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"
    current_player = "X"
    game_active = True
    update_score_display()

create_widgets()
window.mainloop()