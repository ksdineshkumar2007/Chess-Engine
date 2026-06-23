def queen_move(board, row, col, color):
    return rook_move(board, row, col, color) + bishop_move(board, row, col, color)