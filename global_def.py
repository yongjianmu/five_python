from enum import Enum, unique


@unique
class ChessStatus(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

FRAME_START_X = 50
FRAME_START_Y = 50
FRAME_Width = 800
FRAME_Height = 600

BOARD_MARGIN = 20  # same margin for top, bottom, left, right
GRID_SIDE_LEN = 30  # each grid is 30 x 30
BOARD_ROW = 15
BOARD_COL = 15

CHESS_RIDIUM = 10

FIVE = 5
