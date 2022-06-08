from tkinter import *
from tkinter import messagebox as mb

window = Tk()

x_turn, count = 1, 0

l = [Button() for _ in range(9)]
l = [0] + l

var_win = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
           (1, 4, 7), (2, 5, 8), (3, 6, 9),
           (1, 5, 9), (3, 5, 7)]


def restart_window(phrase):
    global count
    text = f'{phrase}\nDo you want to restart this game?'
    if mb.askyesno('Game over!', text):
        for i in range(1, len(l)):
            l[i].config(text=' ', bg='white')
            count= 0
    else:
        quit()


def abc(a, b, c, d='X'):
    winner = False
    if l[a]["text"] == l[b]["text"] == l[c]["text"] == d:
        for i in l[a], l[b], l[c]:
            i.config(bg="red")
        restart_window(f'Greatings! {d} wins!')
        winner = True
    return winner


def checkifwon():
    for i in range(len(var_win)):
        a, b, c = var_win[i]
        if abc(a, b, c) or abc(a, b, c, d='O'):
            break
    else:
        if count == 9:
            restart_window('No One Wins!')

    
def change_turn():
    global x_turn, count
    x_turn = not x_turn
    count += 1
    checkifwon()


def b_click(b):
    if b['text'] == ' ':
        b['text'] = ['X', 'O'][count % 2]
        change_turn()
        

for i in range(1, len(l)):
    l[i].config(text=' ', bg= 'white', font=('', 40), height=3, width=6,
                command=lambda i=i: b_click(l[i]))

idx = 1
for row in range(3):
    for column in range(3):
        l[idx].grid(row=row, column=column)
        idx += 1


window.mainloop()
