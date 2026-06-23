def bishop_move(board,row,col,color):
    offsets=[(1,1),(-1,-1),(1,-1),(-1,1)]
    moves=[]
    for dr,dc in offsets:
        new_r=dr+row
        new_c=dc+col
        while 0<=new_r<8 and 0<=new_c<8 :
            target=board[new_r][new_c]
            if target == 0:
                moves.append((new_r, new_c))
            elif (color == "white" and target < 0) or (color == "black" and target > 0):
                moves.append((new_r, new_c))  # capture enemy
                break
            else:
                break  # friendly piece, stop
            new_r += dr
            new_c += dc
    return moves