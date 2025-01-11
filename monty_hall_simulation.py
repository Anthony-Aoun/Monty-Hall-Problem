import numpy as np
import matplotlib.pyplot as plt
from random import randint, choice


class MontyHallGame:
    """
    Simulates the Monty Hall problem with an arbitrary number of doors.
    A prize is hidden behind one of the doors, and the player chooses one.
    The host opens non-prize doors, offering the player a chance to switch.
    """
    def __init__(self, num_doors: int, switch: bool = True):
        """
        Initializes the game with the specified number of doors and switch strategy.
        
        :param num_doors: Total number of doors in the game.
        :param switch: Boolean indicating if the player will switch their choice.
        """
        self.num_doors = num_doors
        self.switch = switch
        self.reset()

    def reset(self):
        """
        Resets the game by randomly placing the prize and making an initial player choice.
        """
        self.prize_door = randint(0, self.num_doors - 1)
        self.player_choice = randint(0, self.num_doors - 1)
        self.opened_doors = []

    def play(self) -> bool:
        """
        Plays one round of the game according to the switch strategy.
        
        :return: True if the player wins, False otherwise.
        """
        # Host opens doors that are neither the player's choice nor the prize door
        while len(self.opened_doors) < self.num_doors - 2:
            available_doors = [i for i in range(self.num_doors)
                               if i not in self.opened_doors and
                               i != self.player_choice and
                               i != self.prize_door]
            opened_door = choice(available_doors)
            self.opened_doors.append(opened_door)
        
        # Switch choice if the strategy requires it
        if self.switch:
            remaining_doors = [i for i in range(self.num_doors)
                               if i not in self.opened_doors and i != self.player_choice]
            self.player_choice = remaining_doors[0]
        
        return self.player_choice == self.prize_door


def simulate_games(num_games: int, num_doors: int, switch: bool) -> None:
    """
    Simulates multiple games and visualizes the cumulative winning rate.
    
    :param num_games: Number of games to simulate.
    :param num_doors: Number of doors in each game.
    :param switch: Whether the player switches their choice.
    """
    game = MontyHallGame(num_doors, switch)
    wins = 0
    winning_rates = []
    
    for game_id in range(1, num_games + 1):
        game.reset()
        if game.play():
            wins += 1
        winning_rates.append(wins / game_id)
    
    strategy = "with switch" if switch else "without switch"
    print(f"\nUsing {num_doors} doors {strategy} strategy")
    print(f"Player won {wins}/{num_games} games ({(wins / num_games) * 100:.2f}%)")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_games + 1), winning_rates, color='g', label='Cumulative Winning Rate')
    plt.axhline(1 / num_doors, linestyle='--', color='r', label='Theoretical Probability')
    plt.xlabel("Number of Games Played")
    plt.ylabel("Winning Rate")
    plt.title(f"Monty Hall Simulation ({strategy})")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    NUM_GAMES = 1000
    NUM_DOORS = 3

    # Simulation with switching strategy
    simulate_games(NUM_GAMES, NUM_DOORS, switch=True)
    
    # Simulation without switching strategy
    simulate_games(NUM_GAMES, NUM_DOORS, switch=False)
