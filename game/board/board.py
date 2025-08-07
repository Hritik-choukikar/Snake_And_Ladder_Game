# Board class
class Board:
    def __init__(self, size):
        self.size = size * size
        self.snakes_and_ladders = []
        self.entity_map = {}

    def can_add_entity(self, position):
        return position not in self.entity_map

    def add_entity(self, entity):
        if self.can_add_entity(entity.start):
            self.snakes_and_ladders.append(entity)
            self.entity_map[entity.start] = entity

    def get_entity(self, position):
        return self.entity_map.get(position, None)

    def display(self):
        print("\n=== Board Configuration ===")
        print(f"Board Size: {self.size} cells")
        snakes = [e for e in self.snakes_and_ladders if e.name() == "SNAKE"]
        ladders = [e for e in self.snakes_and_ladders if e.name() == "LADDER"]

        print(f"\nSnakes: {len(snakes)}")
        for s in snakes:
            s.display()

        print(f"\nLadders: {len(ladders)}")
        for l in ladders:
            l.display()
        print("===========================\n")

