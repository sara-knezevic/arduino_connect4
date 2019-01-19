from copy import deepcopy
import serial
import sys

from alphabeta import alphabeta
from connect4 import State, done, score, successor
from constants import *

ser = serial.Serial()
ser.timeout = 1
ser.port = '/dev/ttyACM0' 
ser.open()

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
        sys.stdout.write('You win!\n')
    elif status == GAME_MAX_WINNER:
        sys.stdout.write('Algorithm wins!\n')
    elif status == GAME_DRAW:
        sys.stdout.write('It\s a draw!\n')

    sys.exit(1)
    
def update_game(current_state):
    status = done(current_state)

    sys.stdout.write(str(current_state) + '\n')
    
    if status != GAME_NO_WINNER:
        end_game(status, current_state)

def human_vs_computer():
    current_state = State(width = 5, height = 5)

    while True:

        # Human Turn
        sys.stdout.write('\n')
        print(current_state)
        options = get_play_options(current_state)
        for i in range(0, current_state.width):
            sys.stdout.write(' ' + str(i + 1) + ' ')
        sys.stdout.write('\n ')

        while True:
            ard = ser.readline().decode().strip('\r\n')

            if (ard != ''):
                break

        col = int(ard) - 1
        # col = int(input()) - 1 

        for i, j in options:
            if col != j: continue
            current_state.board[i][j] = MIN_PLAYER

        update_game(current_state)
        
        # AI Turn
        current_state, _score = alphabeta(current_state, 5, MAX_PLAYER, score, done, successor)
        update_game(current_state)

    
if __name__ == '__main__':
    human_vs_computer()
