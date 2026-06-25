from get_all_moves import get_allmoves
from apply import apply_move, undo_move
from king_check import is_in_check

def get_legal_moves(board, color, castling_rights):
    legal = []
    for move in get_allmoves(board, color, castling_rights):
        captured, piece, prev_castling = apply_move(board, move, castling_rights)
        if not is_in_check(board, color, castling_rights):
            legal.append(move)
        undo_move(board, move, captured, piece, castling_rights, prev_castling)
    return legal