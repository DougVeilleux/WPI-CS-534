# ====================================================================================================================
# --- Define Imports:

from typing import List
from copy import deepcopy
from random import choice
from Game import Game
from Players import Player
import random



# ====================================================================================================================
# --- Define Classes:
class TicTacToe(Game):
    """
    Tic Tac Toe game class.
    """

    def __init__(self, size=3):
        self.size = size
        self.moves = [(i, j) for i in range(size) for j in range(size)]
        self.players = ('X', 'O')
        self.winning_combinations = (
                [[(i, j) for i in range(size)] for j in range(size)]  # rows
                + [[(i, j) for j in range(size)] for i in range(size)]  # columns
                + [[(i, i) for i in range(size)]]  # diagonal
                + [[(i, size - i - 1) for i in range(size)]]  # anti-diagonal
        )
        self.initial = [[' ' for _ in range(size)] for _ in range(size)]

    def actions(self, state: List[List[str]]) -> List:
        return [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == ' ']

    def result(self, state: List[List[str]], move: tuple, player: str) -> List[List[str]]:
        state_copy = deepcopy(state)
        state_copy[move[0]][move[1]] = player
        return state_copy

    def winner(self, state: List[List[str]]) -> str:
        for player in self.players:
            for combination in self.winning_combinations:
                if all(state[i][j] == player for i, j in combination):
                    return player
        return None

    def terminal_test(self, state: List[List[str]]) -> bool:
        return self.winner(state) is not None or all(val != ' ' for row in state for val in row)

    def utility(self, state: List[List[str]], player: str) -> int:
        if self.winner(state) == player:
            return 1
        elif self.winner(state) == self.players[(self.players.index(player) + 1) % 2]:
            return -1
        else:
            return 0

    def display(self, state: List[List[str]]) -> None:
        for i in range(self.size):
            print(' | '.join(state[i]))
            if i < self.size - 1:
                print('---' * self.size)
        print()

    def to_move(self, state: List[List[str]]) -> str:
        num_X = sum(row.count('X') for row in state)
        num_O = sum(row.count('O') for row in state)
        if num_X == num_O:
            return 'X'
        else:
            return 'O'


class Human(Player):
    """
    Human player class.
    """

    def move(self, game: Game, state: List[List[str]]) -> tuple:
        print(f"Possible moves: {game.actions(state)}")
        move = input("Enter your move (i,j): ")
        return tuple(map(int, move.split(',')))


class AI(Player):
    """
    AI player class.
    """

    def __init__(self, name: str, algorithm: str):
        super().__init__(name)
        self.algorithm = algorithm

    # def move(self, game: Game, state: List[List[str]]) -> tuple:
    #     _, move = self.minimax(game, state) if self.algorithm == 'minimax' else self.alphabeta(game, state)
    #     return move
    def move(self, game: Game, state: List[List[str]]) -> tuple:
        if self.algorithm == 'minimax':
            _, move = self.minimax(game, state)
        elif self.algorithm == 'alphabeta':
            _, move = self.alphabeta(game, state)
        elif self.algorithm == 'random':
            move = self.random_player(game, state)
        return move

    def minimax(self, game: Game, state: List[List[str]], depth=1) -> tuple:
        player = game.to_move(state)
        if game.terminal_test(state):
            return game.utility(state, player), None
        scores = []
        for action in game.actions(state):
            new_state = game.result(state, action, player)
            score, _ = self.minimax(game, new_state, depth + 1)
            scores.append((-score, action))
        return max(scores)

    def alphabeta(self, game: Game, state: List[List[str]], depth=1, alpha=float('-inf'), beta=float('inf')) -> tuple:
        player = game.to_move(state)
        if game.terminal_test(state):
            return game.utility(state, player), None
        best_score, best_action = float('-inf'), None
        for action in game.actions(state):
            new_state = game.result(state, action, player)
            score, _ = self.alphabeta(game, new_state, depth + 1, -beta, -max(alpha, best_score))
            if -score > best_score:
                best_score, best_action = -score, action
            if best_score >= beta:
                break
        return best_score, best_action

    def random_player(self, game: Game, state):
        """A player that chooses a legal move at random."""
        return random.choice(game.actions(state)) if game.actions(state) else None