import chess
import sys
from BoardEvaluation import material_evaluation

PLY = 4


def mini(board, depth):
    if depth == 0:
        return material_evaluation(board)

    min_score = sys.maxsize
    min_move = any(board.legal_moves)

    # print(board.legal_moves.count(), " LEGAL MOVES.")
    for move in board.legal_moves:
        board.push(move)  # try a move
        score = maxi(board, depth - 1)  # recurse
        if score < min_score:
            min_score = score
            min_move = move
        board.pop()  # undo the move
    if depth == PLY:
        return min_score, min_move
    return min_score


def maxi(board, depth):
    if depth == 0:
        return material_evaluation(board)

    max_score = -sys.maxsize
    max_move = any(board.legal_moves)

    for move in board.legal_moves:
        board.push(move)  # try a move
        score = mini(board, depth - 1)  # recurse
        if score > max_score:
            max_score = score
            max_move = move
        board.pop()  # undo the move

    if depth == PLY:
        return max_score, max_move
    return max_score


def minimax(board):
    return maxi(board, PLY)
