from get_all_moves import get_allmoves
from apply import apply_move, undo_move
from king_check import is_in_check

def get_legal_moves(board, color):
    legal = []
    for move in get_allmoves(board, color):
        captured,piece = apply_move(board, move)
        if not is_in_check(board, color):
            legal.append(move)
        undo_move(board, move, captured,piece)
    return legal