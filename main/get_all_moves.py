from bishop_moves import bishop_move
from pawn_move import pawn_move
from queen_moves import queen_move
from rook_moves import rook_move
from king_moves import king_move
from knight_moves import knight_move

def get_allmoves(board, color, castling_rights, en_passant):
    moves = []
    piece_moves = {
        1: pawn_move, 2: rook_move, 3: bishop_move,
        4: knight_move, 5: queen_move, 6: king_move
    }
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if (color == "white" and piece > 0) or (color == "black" and piece < 0):
                if abs(piece) == 6:
                    for move in king_move(board, i, j, color, castling_rights):
                        moves.append(((i,j), move))
                elif abs(piece) == 1:
                    for move in pawn_move(board, i, j, color, en_passant):
                        moves.append(((i,j), move))
                else:
                    move_fn = piece_moves[abs(piece)]
                    for move in move_fn(board, i, j, color):
                        moves.append(((i,j), move))
    return moves