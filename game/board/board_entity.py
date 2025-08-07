# Abstract class for Snake and Ladder
class BoardEntity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def display(self):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError

