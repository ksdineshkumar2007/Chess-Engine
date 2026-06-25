from board_file import create_board
from print_b_file import print_board
from apply import apply_move, undo_move
from get_best_move import get_best_move
from king_check import is_in_check
from legal_moves import get_legal_moves

def play():
    board = create_board()
    castling_rights = {
        "white": {"kingside": True, "queenside": True},
        "black": {"kingside": True, "queenside": True}
    }
    en_passant = [None]

    while True:
        print_board(board)
        
        if not get_legal_moves(board, "white", castling_rights, en_passant):
            if is_in_check(board, "white", castling_rights, en_passant):
                print("Checkmate! Engine wins!")
            else:
                print("Stalemate! Draw!")
            break

        while True:
            user_input = input("Enter move (e.g. 64 54): ")
            if user_input == "quit":
                break
            from_r, from_c = int(user_input[0]), int(user_input[1])
            to_r, to_c = int(user_input[3]), int(user_input[4])
            move = ((from_r, from_c), (to_r, to_c))
            if move in get_legal_moves(board, "white", castling_rights, en_passant):
                apply_move(board, move, castling_rights, en_passant)
                break
            else:
                print("Illegal move! Try again.")

        if user_input == "quit":
            break

        print("\nEngine thinking...")
        engine_move = get_best_move(board, "black", 3, castling_rights, en_passant)
        if engine_move:
            apply_move(board, engine_move, castling_rights, en_passant)
            print(f"Engine played: {engine_move}")
        else:
            if is_in_check(board, "black", castling_rights, en_passant):
                print("Checkmate! You win!")
            else:
                print("Stalemate! Draw!")
            break

if __name__ == "__main__":
    play()