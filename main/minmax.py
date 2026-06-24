from apply import apply_move, undo_move
from evaluate_piece import evaluate
from get_all_moves import get_allmoves
def minimax(board,color,depth):
    if depth==0:
        return evaluate(board)
    best = -999999 if color == "white" else 999999
    for move in get_allmoves(board,color):
        captured=apply_move(board,move)
        score=minimax(board,"black" if color == "white" else "white",depth-1)
        undo_move(board,move,captured)
        if color=="white":
            best=max(best,score)
        else:
            best=min(best,score)
    return best
