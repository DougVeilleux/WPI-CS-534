from TicTacToeClass import TicTacToe
from TicTacToeClass import AI
from TicTacToeClass import Human


def get_player_choice(player_name):
    choice = input(f"Enter the searching strategy for player {player_name} (random/alphabeta/minimax): ")
    while choice not in ['random', 'alphabeta', 'minimax']:
        choice = input(f"Invalid choice! Enter the searching strategy for player {player_name} (random/alphabeta/minimax): ")
    return choice


def main():
    play_again = True
    while play_again:
        size = int(input("Enter the size of the board: "))
        player1_choice = get_player_choice('X')
        player2_choice = get_player_choice('O')
        game = TicTacToe(size)
        player1 = AI('X', player1_choice)
        player2 = AI('O', player2_choice)
        state = game.initial
        print(game.display(state))
        while not game.terminal_test(state):
            player = game.to_move(state)
            if player == player1.name:
                move = player1.move(game, state)
            else:
                move = player2.move(game, state)
            state = game.result(state, move, player)
            print(f"{player} moves {move}")
            print(game.display(state))
        winner = game.winner(state)
        if winner is None:
            print("Tie!")
        else:
            print(f"{winner} won!")
        choice = input("Do you want to play again? (yes/no): ")
        while choice not in ['yes', 'no']:
            choice = input("Invalid choice! Do you want to play again? (yes/no): ")
        if choice == 'no':
            play_again = False
    print("Thank You for Playing Our Game")


if __name__ == "__main__":
    main()

