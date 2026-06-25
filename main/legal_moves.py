from get_all_moves import get_allmoves
from apply import apply_move, undo_move
from king_check import is_in_check

def get_legal_moves(board, color, castling_rights, en_passant):
    legal = []
    for move in get_allmoves(board, color, castling_rights, en_passant):
        captured, piece, prev_castling, ep_captured_pos = apply_move(board, move, castling_rights, en_passant)
        prev_ep = en_passant[0]
        if not is_in_check(board, color, castling_rights, en_passant):
            legal.append(move)
        undo_move(board, move, captured, piece, castling_rights, prev_castling, en_passant, prev_ep, ep_captured_pos)
    return legal