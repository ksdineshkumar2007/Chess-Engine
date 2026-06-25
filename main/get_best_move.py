from get_all_moves import get_allmoves
from apply import apply_move, undo_move
from minmax import minimax

def get_best_move(board, color, depth, castling_rights):
    best = -999999 if color == "white" else 999999
    best_move = None
    
    for move in get_allmoves(board, color, castling_rights):
        captured, piece, prev_castling = apply_move(board, move, castling_rights)
        score = minimax(board, "black" if color == "white" else "white", depth-1, castling_rights, -999999, 999999)
        undo_move(board, move, captured, piece, castling_rights, prev_castling)
        
        if color == "white" and score > best:
            best = score
            best_move = move
        elif color == "black" and score < best:
            best = score
            best_move = move
    
    return best_move