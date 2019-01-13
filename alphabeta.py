import math
from constants import GAME_NO_WINNER, MAX_PLAYER, MIN_PLAYER

def alphabeta(state, max_depth, player, score = None, done = None, successor = None,
              alpha = -math.inf, beta = math.inf, depth = 1):

    if depth >= max_depth or done(state) != GAME_NO_WINNER:
        return state, score(state)

    s = None
    kwargs = {'score': score, 'done': done, 'successor': successor}

    if player == MAX_PLAYER:
        v = -math.inf
        for n in successor(state, player):

            kwargs = {**kwargs, **{'alpha': alpha, 'beta': beta, 'depth': depth + 1}}
            alpha_state, alpha_score = alphabeta(n, max_depth, MIN_PLAYER, **kwargs)

            if v < alpha_score:
                v = alpha_score
                s = n

            alpha = max(alpha, v)

            if beta <= alpha:
                break
    else:
        v = math.inf
        for n in successor(state, player):

            kwargs = {**kwargs, **{'alpha': alpha, 'beta': beta, 'depth': depth + 1}}
            beta_state, beta_score = alphabeta(n, max_depth, MAX_PLAYER, **kwargs)
            
            if v > beta_score:
                v = beta_score
                s = n

            beta = min(beta, v)

            if beta <= alpha:
                break

    return s, v
