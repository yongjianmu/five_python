from global_def import *


def can_draw(counter):
    return counter >= BOARD_ROW * BOARD_COL


def dfs(board, vis, x, y, color, counts):
    if counts >= FIVE:
        return True
    if x < 0 or x >= BOARD_ROW or\
       y < 0 or y >= BOARD_COL or\
       board[x][y] != color or vis[x][y]:
        return False
    vis[x][y] = True
    ret = dfs(board, vis, x + 1, y, color, counts + 1) or\
        dfs(board, vis, x - 1, y, color, counts + 1) or\
        dfs(board, vis, x, y + 1, color, counts + 1) or\
        dfs(board, vis, x, y - 1, color, counts + 1) or\
        dfs(board, vis, x + 1, y + 1, color, counts + 1) or\
        dfs(board, vis, x - 1, y - 1, color, counts + 1) or\
        dfs(board, vis, x + 1, y - 1, color, counts + 1) or\
        dfs(board, vis, x - 1, y + 1, color, counts + 1)
    vis[x][y] = False
    return ret


def can_win(board, x, y, color):
    vis = [[False]*BOARD_COL for i in range(BOARD_ROW)]  # used for dfs
    return dfs(board, vis, x, y, color, 0)
