# Dice logic
import random

class Dice:
    def __init__(self, faces=6):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)
