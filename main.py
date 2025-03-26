import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")


curent_player = "X"
buttons = []

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



def on_click (row,col):
    global curent_player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = curent_player

    if check_win():
        messagebox.showinfo("Крестики-нолики", f"Победил игрок {buttons[row][col]['text']}")
        return

    curent_player = "O"if curent_player == "X" else "X"


    buttons[row][col].config(text=curent_player)


for i in range(3):
   row = []
   for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
   buttons.append(row)








window.mainloop()