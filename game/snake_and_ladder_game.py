# Main game class
from collections import deque
from game_rules import GameRules
class SnakeAndLadderGame:
    def __init__(self, board, dice):
        
        self.board = board
        self.dice = dice
        self.rules = GameRules()
        self.players = deque()
        self.observers = []
        self.game_over = False

    def add_player(self, player):
        self.players.append(player)

    def add_observer(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

    def play(self):
        if len(self.players) < 2:
            print("At least two players required!")
            return

        self.notify("Game Started")
        self.board.display()

        while not self.game_over:
            current = self.players.popleft()
            input(f"\n{current.name}'s turn. Press Enter to roll the dice...")
            roll = self.dice.roll()
            print(f"{current.name} rolled a {roll}")

            if self.rules.is_valid_move(current.position, roll, self.board.size):
                intermediate = current.position + roll
                new_position = self.rules.calculate_new_position(current.position, roll, self.board)

                entity = self.board.get_entity(intermediate)
                if entity:
                    if entity.name() == "SNAKE":
                        print(f"Oh no! Snake at {intermediate}. Going down to {new_position}")
                    else:
                        print(f"Yay! Ladder at {intermediate}. Going up to {new_position}")
                else:
                    print(f"Moving to {new_position}")

                current.position = new_position
                self.notify(f"{current.name} is now at {new_position}")

                if self.rules.has_won(new_position, self.board.size):
                    print(f"\n🎉 {current.name} wins the game! 🎉")
                    current.increment_score()
                    self.game_over = True
                    self.notify(f"Game ended. Winner: {current.name}")
                    break
            else:
                print(f"{current.name} needs exact roll to finish.")

            self.players.append(current)

