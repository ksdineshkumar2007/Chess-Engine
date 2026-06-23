def king_move(board, row, col, color):
    offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),
               (0,1),(1,-1),(1,0),(1,1)]
    moves = []
    for dr, dc in offsets:
        new_r, new_c = row+dr, col+dc
        if 0 <= new_r < 8 and 0 <= new_c < 8:
            target = board[new_r][new_c]
            if (color == "white" and target <= 0) or (color == "black" and target >= 0):
                moves.append((new_r, new_c))
    return moves