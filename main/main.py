from board_file import create_board
from pawn_move import pawn_move
def main():
    board=create_board()
    print(pawn_move(board, 1, 0, "black"))   
    print(pawn_move(board, 5, 0, "white"))  
if __name__=="__main__":
    main()