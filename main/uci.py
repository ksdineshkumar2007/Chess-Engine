import sys
from board_file import create_board
from apply import apply_move
from get_best_move import get_best_move

def uci_to_move(uci_str):
    col_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    from_c = col_map[uci_str[0]]
    from_r = 8 - int(uci_str[1])
    to_c = col_map[uci_str[2]]
    to_r = 8 - int(uci_str[3])
    return ((from_r, from_c), (to_r, to_c))

def move_to_uci(move):
    col_map = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
    (from_r, from_c), (to_r, to_c) = move
    return col_map[from_c] + str(8-from_r) + col_map[to_c] + str(8-to_r)

def uci_loop():
    board = create_board()
    castling_rights = {
        "white": {"kingside": True, "queenside": True},
        "black": {"kingside": True, "queenside": True}
    }
    en_passant = [None]
    last_position = ""

    for line in sys.stdin:
        line = line.strip()

        if line == "uci":
            print("id name DineshEngine")
            print("id author Dinesh")
            print("uciok")

        elif line == "isready":
            print("readyok")

        elif line.startswith("position"):
            last_position = line
            board = create_board()
            castling_rights = {
                "white": {"kingside": True, "queenside": True},
                "black": {"kingside": True, "queenside": True}
            }
            en_passant = [None]
            
            parts = line.split()
            if "moves" in parts:
                moves_idx = parts.index("moves")
                moves = parts[moves_idx+1:]
                for uci_move in moves:
                    move = uci_to_move(uci_move)
                    apply_move(board, move, castling_rights, en_passant)

        elif line.startswith("go"):
            parts = line.split()
            depth = 3
            if "depth" in parts:
                depth = int(parts[parts.index("depth")+1])

            # figure out whose turn based on moves played
            try:
                moves_idx = last_position.split().index("moves")
                num_moves = len(last_position.split()) - moves_idx - 1
            except:
                num_moves = 0

            color = "white" if num_moves % 2 == 0 else "black"
            best_move = get_best_move(board, color, depth, castling_rights, en_passant)
            if best_move:
                print(f"bestmove {move_to_uci(best_move)}")
            else:
                print("bestmove 0000")

        elif line == "quit":
            break

        sys.stdout.flush()

if __name__ == "__main__":
    uci_loop()