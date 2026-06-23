from board_file import create_board
from knight_moves import knight_move
def main():
    board=create_board()
    print(knight_move(board, 7, 1, "white")) 
if __name__=="__main__":
    main()