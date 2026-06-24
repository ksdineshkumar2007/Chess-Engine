from get_all_moves import get_allmoves
from apply import apply_move,undo_move
from minmax import minimax
def get_best_move(board, color, depth):
    best = -999999 if color == "white" else 999999
    best_move = None
    
    for move in get_allmoves(board, color):
        captured = apply_move(board, move)
        score = minimax(board, "black" if color == "white" else "white", depth-1, -999999, 999999)

        undo_move(board, move, captured)
        
        if color == "white" and score > best:
            best = score
            best_move = move
        elif color == "black" and score < best:
            best = score
            best_move = move
    
    return best_move
    