
from board_file import create_board
from print_b_file import print_board
from apply import apply_move, undo_move
from get_best_move import get_best_move

def play():
    board = create_board()
    while True:
        print_board(board)
        
        # Human move
        user_input = input("Enter move (e.g. 64 54): ")
        if user_input=="quit":
            break
        from_r, from_c = int(user_input[0]), int(user_input[1])
        to_r, to_c = int(user_input[3]), int(user_input[4])
        apply_move(board, ((from_r, from_c), (to_r, to_c)))
        
        print("\nEngine thinking...")
        engine_move = get_best_move(board, "black", 3)
        if engine_move:
            apply_move(board, engine_move)
            print(f"Engine played: {engine_move}")
        else:
            print("Engine has no moves!")
            break

if __name__ == "__main__":
    play()

