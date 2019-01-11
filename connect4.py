from copy import deepcopy

from constants import *
import sys

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []

        for i in range(0, height):
            self.board.append([])
            for j in range(0, width):
                self.board[i].append(EMPTY_SLOT)

    def __str__(self):
        string = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j] == EMPTY_SLOT:
                    string += ' %d ' % self.board[i][j]
                else:
                    string += '%+d ' % self.board[i][j]
            string += '\n'
        return string

def done(state):

    # check rows
    for i in range(0, state.height):
        count_max, count_min = 0, 0
        for j in range(0, state.width):
            if state.board[i][j] == MIN_PLAYER: count_min += 1; count_max = 0
            if state.board[i][j] == MAX_PLAYER: count_max += 1; count_min = 0
            if state.board[i][j] == EMPTY_SLOT: count_max, count_min = 0, 0
            if count_max >= 4: return GAME_MAX_WINNER
            if count_min >= 4: return GAME_MIN_WINNER

    # check cols
    for j in range(0, state.width):
        count_max, count_min = 0, 0
        for i in range(0, state.height):
            if state.board[i][j] == MIN_PLAYER: count_min += 1; count_max = 0
            if state.board[i][j] == MAX_PLAYER: count_max += 1; count_min = 0
            if state.board[i][j] == EMPTY_SLOT: count_max, count_min = 0, 0
            if count_max >= 4: return GAME_MAX_WINNER
            if count_min >= 4: return GAME_MIN_WINNER

    # check diagonal descendent (col-indexed)
    for j in range(0, state.width - 3):
        count_max, count_min = 0, 0
        for i in range(0, state.height):
            if i + j >= state.width: break
            if state.board[i][i + j] == MIN_PLAYER: count_min += 1; count_max = 0
            if state.board[i][i + j] == MAX_PLAYER: count_max += 1; count_min = 0
            if state.board[i][i + j] == EMPTY_SLOT: count_max, count_min = 0, 0
            if count_max >= 4: return GAME_MAX_WINNER
            if count_min >= 4: return GAME_MIN_WINNER

    # check diagonal descendent (row-indexed)
    for i in range(1, state.height):
        count_max, count_min = 0, 0
        for j in range(0, state.width - i + 1):
            if i + j >= state.height: break
            if state.board[i + j][j] == MIN_PLAYER: count_min += 1; count_max = 0
            if state.board[i + j][j] == MAX_PLAYER: count_max += 1; count_min = 0
            if state.board[i + j][j] == EMPTY_SLOT: count_max, count_min = 0, 0
            if count_max >= 4: return GAME_MAX_WINNER
            if count_min >= 4: return GAME_MIN_WINNER

    # check diagonal ascendent (col-indexed)
    for j in range(1, state.width - 3):
        count_max, count_min = 0, 0
        for i in range(state.height - 1, j - 1, -1):
            if state.board[i][j + (state.width - 1 - i)] == MIN_PLAYER: count_min += 1; count_max = 0
            if state.board[i][j + (state.width - 1 - i)] == MAX_PLAYER: count_max += 1; count_min = 0
            if state.board[i][j + (state.width - 1 - i)] == EMPTY_SLOT: count_max, count_min = 0, 0
            if count_max >= 4: return GAME_MAX_WINNER
            if count_min >= 4: return GAME_MIN_WINNER

    # check diagonal ascendent (row-indexed)
    for i in range(state.height - 1, state.height - 5, -1):
        count_max, count_min = 0, 0
        for j in range(0, state.width):
            if i - j < 0: break
            if state.board[i - j][j] == MIN_PLAYER: count_min += 1; count_max = 0
            if state.board[i - j][j] == MAX_PLAYER: count_max += 1; count_min = 0
            if state.board[i - j][j] == EMPTY_SLOT: count_max, count_min = 0, 0
            if count_max >= 4: return GAME_MAX_WINNER
            if count_min >= 4: return GAME_MIN_WINNER

    # check draw
    has_empty_spot = False
    for i in range(0, state.height):
        for j in range(0, state.width):
            if state.board[i][j] == EMPTY_SLOT:
                has_empty_spot = True
                break

    return GAME_NO_WINNER if has_empty_spot else GAME_DRAW

def max_row_neighbors(state, player, i, j):
    count = 0
    for _j in range(j + 1, state.width):
        if state.board[i][_j] != player: break
        count += 1
    for _j in range(j - 1, -1, -1):
        if state.board[i][_j] != player: break
        count += 1
    return count

def max_col_neighbors(state, player, i, j):
    count = 0
    for _i in range(i + 1, state.height):
        if state.board[_i][j] != player: break
        count += 1
    return count

def diag_neighbors(state, player, i, j, find_max=True):
    total_count = 0
    count = 0

    # diagonal descendent downwards
    _i = i + 1
    _j = j + 1

    while _i < state.height and _j < state.width:
        if state.board[_i][_j] != player: break
        count += 1
        _i += 1
        _j += 1

    # diagonal descendent upwards
    _i = i - 1
    _j = j - 1

    while _i >= 0 and _j >= 0:
        if state.board[_i][_j] != player: break
        count += 1
        _i -= 1
        _j -= 1

    if find_max:
        total_count = max(total_count, count)
    else:
        total_count += count

    count = 0
    # diagonal ascendent upwards
    _i = i - 1
    _j = j + 1

    while _i >= 0 and _j < state.width:
        if state.board[_i][_j] != player: break
        count += 1
        _i -= 1
        _j += 1

    # diagonal ascendent downwards
    _i = i + 1
    _j = j - 1

    while _i < state.height and _j >= 0:
        if state.board[_i][_j] != player: break
        count += 1
        _i += 1
        _j -= 1

    if find_max:
        total_count = max(total_count, count)
    else:
        total_count += count

    return total_count


def _can_opponent_win(state, opponent, i, j):
    neighbors = [
        (i    , j + 1, i + 1, j + 1),
        (i - 1, j + 1, i    , j + 1),
        (i - 1, j    , i    , j    ),
        (i - 1, j - 1, i    , j - 1),
        (i    , j - 1, i + 1, j - 1)
    ]

    for _i, _j, _ii, _jj in neighbors:
        if (_j >= 0 and _j < state.width and _i >= 0 and _i < state.height) and\
            (state.board[_i][_j] == EMPTY_SLOT):
            if (_jj >= 0 and _jj < state.width and _ii >= 0 and _ii < state.height) and\
               (state.board[_ii][_jj] != EMPTY_SLOT):
                state.board[_i][_j] = opponent
                result = done(state)
                state.board[_i][_j] = EMPTY_SLOT
                if result in (GAME_MAX_WINNER, GAME_MIN_WINNER):
                    return True

    return False
        

def score(state):
    max_score = 0
    min_score = 0
    
    for j in range(0, state.width):
        for i in range(state.height - 1, -1, -1):
            if state.board[i][j] == EMPTY_SLOT:

                state.board[i][j] = MAX_PLAYER
                if done(state) == GAME_MAX_WINNER:
                    max_score += 50
                elif _can_opponent_win(state, MIN_PLAYER, i, j):
                    min_score += 50
                else:
                    max_score += max_row_neighbors(state, MAX_PLAYER, i, j)
                    max_score += max_col_neighbors(state, MAX_PLAYER, i, j)
                    max_score += diag_neighbors(state, MAX_PLAYER, i, j, False)

                state.board[i][j] = MIN_PLAYER
                if done(state) == GAME_MIN_WINNER:
                    min_score += 50
                elif _can_opponent_win(state, MAX_PLAYER, i, j):
                    max_score += 50
                else:
                    min_score += max_row_neighbors(state, MIN_PLAYER, i, j)
                    min_score += max_col_neighbors(state, MIN_PLAYER, i, j)
                    min_score += diag_neighbors(state, MIN_PLAYER, i, j, False)

                state.board[i][j] = EMPTY_SLOT
                break

    return max_score - min_score

def successor(state, player):
    states = []
    for j in range(0, state.width):
        for i in range(state.height - 1, -1, -1):
            if state.board[i][j] == EMPTY_SLOT:
                s = deepcopy(state)
                s.board[i][j] = player
                states.append(s)
                break
    return states
