# Factory for game creation
from board.board import Board
from strategy.standard_board_setup_strategy import StandardBoardSetupStrategy
from dice.dice import Dice
from snake_and_ladder_game import SnakeAndLadderGame

class GameFactory:
    @staticmethod
    def create_standard_game():
        board = Board(10)
        strategy = StandardBoardSetupStrategy()
        strategy.setup_board(board)
        dice = Dice(6)
        return SnakeAndLadderGame(board, dice)

    @staticmethod
    def create_random_game(difficulty):
        board = Board(10)
        strategy = StandardBoardSetupStrategy()
        strategy.setup_board(board)
        dice = Dice(6)
        return SnakeAndLadderGame(board, dice)

