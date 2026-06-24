def evaluate(board):
    score = 0
    for i in range(8):
        for j in range(8):
            score += board[i][j]
    return score