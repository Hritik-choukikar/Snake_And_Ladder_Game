# Standard board setup
from strategy.board_setup_strategy import BoardSetupStrategy
from board.snake import Snake
from board.ladder import Ladder

class StandardBoardSetupStrategy(BoardSetupStrategy):
    def setup_board(self, board):
        if board.size != 100:
            print("Standard setup only works on 10x10 board!")
            return

        snake_positions = [(99, 54), (95, 75), (92, 88)]
        ladder_positions = [(2, 38), (7, 14), (8, 31)]

        for start, end in snake_positions:
            board.add_entity(Snake(start, end))
        for start, end in ladder_positions:
            board.add_entity(Ladder(start, end))

