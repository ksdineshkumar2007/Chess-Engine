def rook_move(board, row, col, color):
    moves = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    
    for dr, dc in directions:
        new_row, new_col = row+dr, col+dc
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            target = board[new_row][new_col]
            if target == 0:
                moves.append((new_row, new_col))
            elif (color == "white" and target < 0) or (color == "black" and target > 0):
                moves.append((new_row, new_col))  # capture enemy
                break
            else:
                break  # friendly piece, stop
            new_row += dr
            new_col += dc
    return moves