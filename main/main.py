from board_file import create_board
from bishop_moves import bishop_move
def main():
    board=create_board()
    print(bishop_move(board, 4, 4, "white"))

if __name__=="__main__":
    main()