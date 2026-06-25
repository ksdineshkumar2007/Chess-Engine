def king_move(board, row, col, color, castling_rights):
    offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),
               (0,1),(1,-1),(1,0),(1,1)]
    moves = []
    for dr, dc in offsets:
        new_r, new_c = row+dr, col+dc
        if 0 <= new_r < 8 and 0 <= new_c < 8:
            target = board[new_r][new_c]
            if (color == "white" and target <= 0) or (color == "black" and target >= 0):
                moves.append((new_r, new_c))

    # Castling
    if color == "white" and row == 7 and col == 4:
        if castling_rights["white"]["kingside"]:
            if board[7][5] == 0 and board[7][6] == 0:
                moves.append((7, 6))
        if castling_rights["white"]["queenside"]:
            if board[7][1] == 0 and board[7][2] == 0 and board[7][3] == 0:
                moves.append((7, 2))

    if color == "black" and row == 0 and col == 4:
        if castling_rights["black"]["kingside"]:
            if board[0][5] == 0 and board[0][6] == 0:
                moves.append((0, 6))
        if castling_rights["black"]["queenside"]:
            if board[0][1] == 0 and board[0][2] == 0 and board[0][3] == 0:
                moves.append((0, 2))

    return moves