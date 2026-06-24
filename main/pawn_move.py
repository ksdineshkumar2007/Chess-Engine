def pawn_move(board,row,col,color):
    valid_moves=[]
    if color=="white":
        if row==6:
            if board[row-1][col]==0 and board[row-2][col]==0:
                valid_moves.extend([(row-1,col),(row-2,col)])
            if board[row-1][col]==0 and board[row-2][col]!=0:
                valid_moves.append((row-1,col))
        if 0<row<7 and col!=7 and board[row-1][col+1]<0 :
            valid_moves.append((row-1,col+1))
        if 0<row<7 and col!=0 and board[row-1][col-1]<0 :
            valid_moves.append((row-1,col-1))
        if 0<row<6 and board[row-1][col]==0:
            valid_moves.append((row-1,col))
        if row==0:
            valid_moves.append((row-1,col)) 
    if color=="black":
        if row == 1:
            if board[row+1][col] == 0 and board[row+2][col] == 0:
                valid_moves.extend([(row+1,col),(row+2,col)])
            if board[row+1][col] == 0 and board[row+2][col] != 0:
                valid_moves.append((row+1,col))
        if 0 < row < 7 and col != 7 and board[row+1][col+1] > 0 :
            valid_moves.append((row+1,col+1))
        if 0 < row < 7 and col != 0 and board[row+1][col-1] > 0 :
            valid_moves.append((row+1,col-1))
        if 1 < row < 7 and board[row+1][col] == 0:
            valid_moves.append((row+1,col))
        if row == 7:
            valid_moves.append((row+1,col))
    return valid_moves         
