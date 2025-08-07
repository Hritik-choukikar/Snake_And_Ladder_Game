# Player class
class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.position = 0
        self.score = 0

    def increment_score(self):
        self.score += 1
