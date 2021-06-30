from tkinter import *
from tkinter.messagebox import showinfo
import warnings

root = Tk()
root.title("Tic Tac Toe")
root.configure(background='#b22222')
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ""
x = 0
boards = ["board"] * 10


def result(boards, mark):
    return ((boards[1] == boards[2] == boards[3] == mark)
            or (boards[4] == boards[5] == boards[6] == mark)
            or (boards[7] == boards[8] == boards[9] == mark)
            or (boards[1] == boards[4] == boards[7] == mark)
            or (boards[2] == boards[5] == boards[8] == mark)
            or (boards[3] == boards[6] == boards[9] == mark)
            or (boards[1] == boards[5] == boards[9] == mark)
            or (boards[3] == boards[5] == boards[7] == mark))


def sign(n1):
    global x, y, n
    if n1 == 1 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y
        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b1.config(text=y)
        x = x + 1
        mark = y

        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 wins")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            showinfo("Result", "Player 2 wins")
            destroys()

    if n1 == 2 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y
        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b2.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            showinfo("Reuslt", "Player 2 Won")
            destroys()

    if n1 == 3 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y

        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y
        b3.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            showinfo("Result", "Player 2 Won")
            destroys()

    if n1 == 4 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y

        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y
        b4.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            showinfo("Result", "Player 2 Won")
            destroys()

    if n1 == 5 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y
        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b5.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, "O") and mark == 'O'):
            showinfo("Result", "Player 2 Won")
            destroys()

    if n1 == 6 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y
        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b6.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            showinfo("Result", "Player 2 Won")
            destroys()

    if n1 == 7 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y

        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b7.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            print("Player 2 Won")
            showinfo("Result", "Player 2 Won")
            destroys()

    if n1 == 8 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y

        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b8.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            print("Player 1 Won")
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, "O") and mark == 'O'):
            print("Player 2 Won")
            showinfo("Result", "Player 2 Won")
            destroys()
    if n1 == 9 and n1 in n:
        n.remove(n1)
        if x % 2 == 0:
            y = 'X'
            boards[n1] = y

        elif x % 2 != 0:
            y = 'O'
            boards[n1] = y

        b9.config(text=y)
        x = x + 1
        mark = y
        if (result(boards, mark) and mark == 'X'):
            showinfo("Result", "Player 1 Won")
            destroys()
        elif (result(boards, mark) and mark == 'O'):
            showinfo("Result", "Player 2 Won")
            destroys()

    if (x > 8 and result(boards, 'X') == False and result(boards, 'O') == False):
        showinfo("Result", "Match Tied")
        print("Play again")
        destroys()

def destroys():
    root.destroy()


Label(root, text="Player 1 : X", font="times 15", bg='#800000', fg='#ffff00').grid(row=0, column=1)

Label(root, text="Player 2 : O", font="times 15", bg='#800000', fg='#ffff00').grid(row=0, column=2)

b1 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(1))
b1.grid(row=1, column=1)
b2 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(2))
b2.grid(row=1, column=2)
b3 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(3))
b3.grid(row=1, column=3)
b4 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(4))
b4.grid(row=2, column=1)
b5 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(5))
b5.grid(row=2, column=2)
b6 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(6))
b6.grid(row=2, column=3)
b7 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(7))
b7.grid(row=3, column=1)
b8 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(8))
b8.grid(row=3, column=2)
b9 = Button(root, width=20, height=10, font=('arial', 10, 'bold'), bg='#832b19', fg='#f6f0f0', command=lambda: sign(9))
b9.grid(row=3, column=3)
root.mainloop()
# Removes  warnings from the output
warnings.filterwarnings('ignore')