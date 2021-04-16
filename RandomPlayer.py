import sys
import chess
import random
import time
from Minimax import minimax

board = chess.Board()

### CONSTANTS ###
PLY = 2 # depth of each minimax search


# Player vs. Random Algorithm
'''
while not board.is_game_over():
    board.push(random.choice([move for move in board.legal_moves]))
    print(board)
    player_move = input('What move do you want to play? ')
    board.push_san(player_move)
'''
### COMPUTER VS. RANDOM ALGORITHM ###

# Start game #
print("STARTING GAME")
print(board, "\n\n")

move_count = 0
while not board.is_game_over():
    move_count+=1
    print("MOVE ", move_count, "\n")

    max_computer_score, computer_move = minimax(board)
    time.sleep(1)
    board.push(computer_move)
    print(board, "\n\n")

    random_move = random.choice([move for move in board.legal_moves])
    board.push(random_move)
    time.sleep(1)
    print(board, "\n\n\n\n")


### RANDOM VS. RANDOM ALGORITHM ###
"""
while not board.is_game_over():
    board.push(random.choice([move for move in board.legal_moves]))
    print(board)
"""

print(board.result())
