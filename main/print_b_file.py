symbols = {
    0:'.', 
    1:'P', 2:'R', 3:'B', 4:'N', 5:'Q', 6:'K',
   -1:'p',-2:'r',-3:'b',-4:'n',-5:'q',-6:'k'
}
def print_board(board):
    for i in range(0,8):
        for j in range(0,8):
            print(symbols[board[i][j]],end=' ')
        print()
    