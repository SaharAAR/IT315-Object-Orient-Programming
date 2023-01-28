# IT315 [579]
# Sahar Alrebdi 382216314
# Haifa AlRomaih 382214881

from tkinter import *
import random

# Global variables and properties
Margin = 20
s = 50  # side
rs = -1  # selected row
cs = -1  # selected column
random_x = list(range(9))
random_y = list(range(9))
random_nos = list(range(1, 10))

W = H = Margin * 2 + s * 9  # to set the window size '490'
grid = [[1] * 9 for v in range(9)]
displayed_tiles = [[0] * 9 for var in range(9)]
r = Tk()
r.title('SUDOKU')  # Window Title
canvas = Canvas(r, width=W, height=H, bg='white', relief="solid")  # Window properties
canvas.pack(fill=BOTH, s=TOP)  # Window size


def randomize():  # randomize function : all tiles in sudoku
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
            displayed_tiles[i][j] = 0
    random.shuffle(random_x)
    random.shuffle(random_y)
    random.shuffle(random_nos)


def issafe(row, col, num):
    for l in range(9):
        if grid[row][l] == num or grid[l][col] == num:
            return False
    st_r = row - (row % 3)
    st_c = col - (col % 3)
    for m in range(3):
        for n in range(3):
            if grid[st_r+m][st_c+n] == num:
                return False
    return True


def solve_sudoku(n):
    i = 0
    j = 0
    f2 = False
    for i in random_x:
        flag = False
        for j in random_y:
            if grid[i][j] == 0:
                flag = True
                f2 = True
                break
        if flag:
            break
    if not f2:
        return True
    for k in random_nos:
        if issafe(i, j, k):
            grid[i][j] = k
            if solve_sudoku(n) is True:
                return True
            grid[i][j] = 0
    return False


def random_game():  # randomize grid
    randomize()
    return solve_sudoku(9)


def hide_tiles(num):  # hides answers
    for i in num:
        grid[i[0]][i[1]] = 0
        displayed_tiles[i[0]][i[1]] = 1


def new_grid(num):  # sets conditions for reload and calls function to set values and hide answers
    indexes = []
    for i in range(9):
        for j in range(9):
            indexes.append([i, j])
    while True:
        if random_game():  # calls function to to use randomize() or return solve_Sudoku()
            break
    hide_tiles(random.sample(indexes, num))  # calls function to hide the answer cells value


def new_game():
    new_grid(40)  # calls function and uses '40' the number of cells to hide
    for i in range(10):  # grid lines properties
        color = "black" if i % 3 == 0 else "gray"
    # horizontal lines propeties
        a = Margin + i * s
        b = Margin
        c = Margin + i * s
        d = H - Margin
        canvas.create_line(a, b, c, d, fill=color)
    # Vertical lines properties
        a = Margin
        b = Margin + i * s
        c = W - Margin
        d = Margin + i * s
        canvas.create_line(a, b, c, d, fill=color)
    set_up_game()


# class to recognize input and display numbers
def set_up_game():
    canvas.delete("numbers")
    for i in range(9):
        for j in range(9):
            answer = grid[i][j]  # make sure the clicked is for answer
            if answer != 0:
                x = Margin + j * s + s / 2
                y = Margin + i * s + s / 2
                if displayed_tiles[i][j] == 1:
                    color = 'dark blue'  # color of input numbers
                else:  # Displayed numbers in board
                    color = 'black'
                canvas.create_text(x, y, text=answer, tags="numbers", fill=color, font=("Roboto", 13))


# to recognize input
def pressed(event):
    global rs, cs
    if rs >= 0 and cs >= 0 and event.char in "123456789":
        grid[rs][cs] = int(event.char)
        cs, rs = -1, -1
        set_up_game()


# For mouse click
def clicked(event):
    global rs, cs
    x, y = event.x, event.y
    if Margin < x < W - Margin and Margin < y < H - Margin:
        canvas.focus_set()
        row, col = int((y - Margin) / s), int((x - Margin) / s)
        if (row, col) == (rs, cs):
            rs, cs = -1, -1
        elif displayed_tiles[row][col] == 1:
            rs, cs = row, col


newgame_button = Button(r, text="Reload", command=new_game, bg="dark green", fg="white", font=("Roboto", 20))
newgame_button.pack(fill=BOTH, expand=True)
new_game()
canvas.bind("<Button-1>", clicked)
canvas.bind("<Key>", pressed)

r.mainloop()

# References:
# https://www.chegg.com/
# https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/
# https://www.reddit.com/r/Python/comments/ikvtbf/my_first_gui_a_complete_sudoku_game/
