import sys
from copy import deepcopy

from alphabeta import alphabeta
from connect4 import State, done, score, successor
from constants import (EMPTY_SLOT, GAME_DRAW, GAME_MAX_WINNER, GAME_MIN_WINNER,
                       GAME_NO_WINNER, MAX_PLAYER)


def get_play_options(state):
    options = []
    for j in range(0, state.width):
        for i in range(state.height - 1, -1, -1):
            if state.board[i][j] != EMPTY_SLOT: continue
            options.append((i, j))
            break
    return options

def end_game(status, current_state):
    if status == GAME_MIN_WINNER:
        sys.stdout.write('Human Win!\n')
    elif status == GAME_MAX_WINNER:
        sys.stdout.write('Computer Win!\n')
    elif status == GAME_DRAW:
        sys.stdout.write('Computer Win!\n')

    sys.exit(1)
    
def update_game(current_state):
    status = done(current_state)

    sys.stdout.write(str(current_state) + '\n')
    
    if status != GAME_NO_WINNER:
        end_game(status, current_state)

def human_vs_computer():
    current_state = State(width=5, height=5)

    while True:

        # Human Turn
        sys.stdout.write('\n')
        print(current_state)
        options = get_play_options(current_state)
        for i in range(0, current_state.width):
            sys.stdout.write(' ' + str(i) + ' ')
        sys.stdout.write('\n-> ')

        col = int(input())
        for i, j in options:
            if col != j: continue
            current_state.board[i][j] = -1

        update_game(current_state)
        
        # AI Turn
        current_state, _score = alphabeta(current_state, 5, MAX_PLAYER, score, done, successor)
        update_game(current_state)

    
if __name__ == '__main__':
    human_vs_computer()
