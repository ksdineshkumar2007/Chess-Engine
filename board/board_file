def create_board():
    pawn,rook,bishop,knight,queen,king=1,2,3,4,5,6
    base=[rook,knight,bishop,queen,king,bishop,knight,rook]
    base_p=[pawn,pawn,pawn,pawn,pawn,pawn,pawn,pawn]
    board=[[0]*8 for _ in range(8)]
    for i in range(0,8):
         for j in range(0,8):
            if i==0:
                board[i][j]=-base[j]
            elif i==7:
                board[i][j]=base[j]
            elif i==1:
                board[i][j]=-base_p[j]
            elif i==6:
                board[i][j]=base_p[j]
    return board    