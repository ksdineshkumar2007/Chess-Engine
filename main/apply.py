def apply_move(board, move, castling_rights, en_passant):
    (from_r, from_c), (to_r, to_c) = move
    piece = board[from_r][from_c]
    captured = board[to_r][to_c]
    prev_castling = {
        "white": dict(castling_rights["white"]),
        "black": dict(castling_rights["black"])
    }
    prev_ep = en_passant[0]

    board[to_r][to_c] = piece
    board[from_r][from_c] = 0

    # En passant capture
    ep_captured_pos = None
    if abs(piece) == 1 and (to_r, to_c) == prev_ep:
        ep_r = from_r
        board[ep_r][to_c] = 0
        ep_captured_pos = (ep_r, to_c)

    # Set new en passant target
    if abs(piece) == 1 and abs(to_r - from_r) == 2:
        en_passant[0] = ((from_r + to_r) // 2, to_c)
    else:
        en_passant[0] = None

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

    return captured, piece, prev_castling, ep_captured_pos

def undo_move(board, move, captured, piece, castling_rights, prev_castling, en_passant, prev_ep, ep_captured_pos):
    (from_r, from_c), (to_r, to_c) = move
    board[from_r][from_c] = piece
    board[to_r][to_c] = captured

    # Restore en passant captured pawn
    if ep_captured_pos:
        ep_r, ep_c = ep_captured_pos
        board[ep_r][ep_c] = -1 if piece == 1 else 1
        board[to_r][to_c] = 0

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
    en_passant[0] = prev_ep