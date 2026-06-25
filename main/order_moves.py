def order_moves(board, moves):
    scored = []
    for move in moves:
        (from_r, from_c), (to_r, to_c) = move
        score = 0
        target = board[to_r][to_c]
        attacker = abs(board[from_r][from_c])
        
        PIECE_VALUES = {1: 100, 2: 500, 3: 330, 4: 320, 5: 900, 6: 20000}
        
        if target != 0:
            score = PIECE_VALUES[abs(target)] - PIECE_VALUES[attacker]
        
        scored.append((move, score))
    
    scored.sort(key=lambda x: x[1], reverse=True)
    return [move for move, score in scored]