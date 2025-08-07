# Snake entity
from board.board_entity import BoardEntity

class Snake(BoardEntity):
    def __init__(self, start, end):
        super().__init__(start, end)
        if end >= start:
            print("Invalid snake! End must be less than start.")

    def display(self):
        print(f"Snake: {self.start} -> {self.end}")

    def name(self):
        return "SNAKE"
