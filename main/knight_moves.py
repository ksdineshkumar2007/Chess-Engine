def knight_move(board,row,col,color):
    offsets = [(-2,-1),(-2,+1),(-1,-2),(-1,+2),
           (+1,-2),(+1,+2),(+2,-1),(+2,+1)]

    moves = []

    for dr, dc in offsets:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 8 and 0 <= new_col < 8:
            target = board[new_row][new_col]

        
            if target <=0 and color=="white":
                moves.append((new_row, new_col))

      
            elif target>=0 and color=="black":
                moves.append((new_row, new_col))
    return moves
       