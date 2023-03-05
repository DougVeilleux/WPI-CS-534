
from collections import namedtuple, Counter, defaultdict
import random
import math
import functools
cache = functools.lru_cache(10**6)

# --- Define Functions:
def random_player(game, state): return random.choice(list(game.actions(state)))

def player(search_algorithm):
    """A game player who uses the specified search algorithm"""
    return lambda game, state: search_algorithm(game, state)[1]


# Play the game:

play_game(TicTacToe(), dict(X=random_player, O=player(alphabeta_search)), verbose=True).utility

