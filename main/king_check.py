from get_all_moves import get_allmoves

def is_in_check(board, color, castling_rights, en_passant):
    king = 6 if color == "white" else -6
    king_pos = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                king_pos = (i, j)
    
    enemy = "black" if color == "white" else "white"
    for from_pos, to_pos in get_allmoves(board, enemy, castling_rights, en_passant):
        if to_pos == king_pos:
            return True
    return False