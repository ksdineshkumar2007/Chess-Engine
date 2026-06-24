def apply_move(board, move):
    (from_r, from_c), (to_r, to_c) = move
    piece = board[from_r][from_c]
    captured = board[to_r][to_c]
    board[to_r][to_c] = piece
    board[from_r][from_c] = 0
    if board[to_r][to_c] == 1 and to_r == 0:  # white pawn
        board[to_r][to_c] = 5
    if board[to_r][to_c] == -1 and to_r == 7:  # black pawn
        board[to_r][to_c] = -5

    return captured ,piece # return so we can undo later

def undo_move(board, move, captured,piece):
    (from_r, from_c), (to_r, to_c) = move
    board[from_r][from_c] = piece
    board[to_r][to_c] = captured