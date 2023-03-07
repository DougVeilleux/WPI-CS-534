# ====================================================================================================================
# --- Define Imports:
from TicTacToeClass import TicTacToe, player, play_game, random_player, alphabeta_search, minimax_search



# Play the game:
def main():
    play_game(TicTacToe(), dict(X=random_player, O=player(alphabeta_search)), verbose=True).utility

if __name__ == '__main__':
    main()