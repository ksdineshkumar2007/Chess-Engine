from board_file import create_board
from get_best_move import get_best_move
def main():
    board=create_board()
    print(get_best_move(board, "white", 3))

if __name__=="__main__":
    main()