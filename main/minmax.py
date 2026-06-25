from apply import apply_move, undo_move
from evaluate_piece import evaluate
from get_all_moves import get_allmoves

def minimax(board, color, depth, castling_rights, en_passant, alpha=-999999, beta=999999):
    if depth == 0:
        return evaluate(board)
    
    best = -999999 if color == "white" else 999999
    for move in get_allmoves(board, color, castling_rights, en_passant):
        if alpha >= beta:
            break
        captured, piece, prev_castling, ep_captured_pos = apply_move(board, move, castling_rights, en_passant)
        prev_ep = en_passant[0]
        score = minimax(board, "black" if color == "white" else "white", depth-1, castling_rights, en_passant, alpha, beta)
        undo_move(board, move, captured, piece, castling_rights, prev_castling, en_passant, prev_ep, ep_captured_pos)
        if color == "white":
            best = max(best, score)
            alpha = best
        else:
            best = min(best, score)
            beta = best
    return best