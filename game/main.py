# Entry point
from game_factory import GameFactory
from observer.console_notifier import ConsoleNotifier
from player.player import Player

def main():
    print("=== Welcome to Snake and Ladder ===")
    game = GameFactory.create_standard_game()
    game.add_observer(ConsoleNotifier())

    num = int(input("Enter number of players: "))
    for i in range(num):
        name = input(f"Enter name for player {i+1}: ")
        game.add_player(Player(i+1, name))

    game.play()

if __name__ == "__main__":
    main()

