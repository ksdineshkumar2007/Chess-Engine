def apply_move(board, move):
    (from_r, from_c), (to_r, to_c) = move
    piece = board[from_r][from_c]
    captured = board[to_r][to_c]
    board[to_r][to_c] = piece
    board[from_r][from_c] = 0
    return captured  # return so we can undo later

def undo_move(board, move, captured):
    (from_r, from_c), (to_r, to_c) = move
    board[from_r][from_c] = board[to_r][to_c]
    board[to_r][to_c] = captured