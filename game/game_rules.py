# Game rules logic
class GameRules:
    def is_valid_move(self, pos, roll, size):
        return (pos + roll) <= size

    def calculate_new_position(self, pos, roll, board):
        new_pos = pos + roll
        entity = board.get_entity(new_pos)
        return entity.end if entity else new_pos

    def has_won(self, pos, size):
        return pos == size
