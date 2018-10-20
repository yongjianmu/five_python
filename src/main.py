import Tkinter as tk
import tkMessageBox

from global_def import *
import check_status


chess = [[ChessStatus.EMPTY]*BOARD_COL for i in range(BOARD_ROW)]
chess_button = [[None]*BOARD_COL for i in range(BOARD_ROW)]
counter = 0

root = tk.Tk()
root.title('Five')
root.geometry(str(FRAME_Width) + "x" + str(FRAME_Height) + "\
+" + str(FRAME_START_X) + "+" + str(FRAME_START_Y))
# http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
root.configure(background='goldenrod')
root.resizable(width=True, height=True)

canvas = tk.Canvas(root, width=FRAME_Width, height=FRAME_Height,
                   borderwidth=0, highlightthickness=0, bg='goldenrod')
canvas.pack()

# draw row and col
x_start, y_start = BOARD_MARGIN, BOARD_MARGIN
x_end, y_end = BOARD_MARGIN + (BOARD_ROW - 1) * GRID_SIDE_LEN,\
               BOARD_MARGIN + (BOARD_COL - 1) * GRID_SIDE_LEN
for i in range(0, BOARD_ROW):
    canvas.create_line(x_start, y_start + i * GRID_SIDE_LEN, x_end, y_start +
                       i * GRID_SIDE_LEN, fill="black")
    canvas.create_line(x_start + i * GRID_SIDE_LEN, y_start, x_start +
                       i * GRID_SIDE_LEN, y_end, fill="black")


# draw transparent button at first
def on_click(i, j, event):
    if ChessStatus.EMPTY != chess[i][j]:
        print 'Position[{}, {}] is not empty'.format(i, j)
        return
    global counter
    color = "white" if counter % 2 else "black"
    chess[i][j] = ChessStatus.WHITE if counter % 2 else ChessStatus.BLACK
    canvas.itemconfig(chess_button[i][j], fill=color)
    counter += 1
    if check_status.can_draw(counter):
        tkMessageBox.showinfo("Draw Game!")
        reset()
        return
    if check_status.can_win(chess, i, j, chess[i][j]):
        tkMessageBox.showinfo("You win!")
        reset()
        return


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

tk.Canvas.create_circle = _create_circle
for i in range(0, BOARD_ROW):
    for j in range(0, BOARD_COL):
        chess_button[i][j] = canvas.create_circle(x_start + i * GRID_SIDE_LEN,
                                                  y_start + j * GRID_SIDE_LEN,
                                                  CHESS_RIDIUM, width=0,
                                                  fill="systemTransparent")
        canvas.tag_bind(chess_button[i][j], '<Button-1>',
                        lambda e, i=i, j=j: on_click(i, j, e))


# draw a reset button
def on_reset(event):
    print 'on_reset'
    reset()

resetBtn = canvas.create_rectangle(650, 100, 750, 140, fill='gray')
canvas.create_text((700, 120), text="Reset")
canvas.tag_bind(resetBtn, '<Button-1>', lambda e: on_reset(e))


def reset():
    global counter
    counter = 0
    for i in range(0, BOARD_ROW):
        for j in range(0, BOARD_COL):
            canvas.itemconfig(chess_button[i][j], fill="systemTransparent")
            chess[i][j] = ChessStatus.EMPTY

# main()
root.mainloop()
