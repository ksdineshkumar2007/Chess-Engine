from rook_moves import rook_move
from bishop_moves import bishop_move
def queen_move(board, row, col, color):
    return rook_move(board, row, col, color) + bishop_move(board, row, col, color)