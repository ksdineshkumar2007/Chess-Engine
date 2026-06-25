def apply_move(board, move, castling_rights):
    (from_r, from_c), (to_r, to_c) = move
    piece = board[from_r][from_c]
    captured = board[to_r][to_c]
    prev_castling = {
        "white": dict(castling_rights["white"]),
        "black": dict(castling_rights["black"])
    }
    board[to_r][to_c] = piece
    board[from_r][from_c] = 0

    # Promotion
    if board[to_r][to_c] == 1 and to_r == 0:
        board[to_r][to_c] = 5
    if board[to_r][to_c] == -1 and to_r == 7:
        board[to_r][to_c] = -5

    # Castling rook move
    if abs(piece) == 6 and abs(to_c - from_c) == 2:
        if to_c == 6:
            board[from_r][5] = board[from_r][7]
            board[from_r][7] = 0
        elif to_c == 2:
            board[from_r][3] = board[from_r][0]
            board[from_r][0] = 0

    # Update castling rights
    if piece == 6:
        castling_rights["white"]["kingside"] = False
        castling_rights["white"]["queenside"] = False
    if piece == -6:
        castling_rights["black"]["kingside"] = False
        castling_rights["black"]["queenside"] = False
    if (from_r, from_c) == (7, 7): castling_rights["white"]["kingside"] = False
    if (from_r, from_c) == (7, 0): castling_rights["white"]["queenside"] = False
    if (from_r, from_c) == (0, 7): castling_rights["black"]["kingside"] = False
    if (from_r, from_c) == (0, 0): castling_rights["black"]["queenside"] = False

    return captured, piece, prev_castling

def undo_move(board, move, captured, piece, castling_rights, prev_castling):
    (from_r, from_c), (to_r, to_c) = move
    board[from_r][from_c] = piece
    board[to_r][to_c] = captured

    # Undo castling rook move
    if abs(piece) == 6 and abs(to_c - from_c) == 2:
        if to_c == 6:
            board[from_r][7] = board[from_r][5]
            board[from_r][5] = 0
        elif to_c == 2:
            board[from_r][0] = board[from_r][3]
            board[from_r][3] = 0

    castling_rights["white"] = prev_castling["white"]
    castling_rights["black"] = prev_castling["black"]