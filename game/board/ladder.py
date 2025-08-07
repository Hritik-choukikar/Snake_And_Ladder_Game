# Ladder entity
from board.board_entity import BoardEntity

class Ladder(BoardEntity):
    def __init__(self, start, end):
        super().__init__(start, end)
        if end <= start:
            print("Invalid ladder! End must be greater than start.")

    def display(self):
        print(f"Ladder: {self.start} -> {self.end}")

    def name(self):
        return "LADDER"

