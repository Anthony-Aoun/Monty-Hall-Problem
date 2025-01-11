# Monty Hall Problem Simulation

This Python program simulates the Monty Hall problem, a probability puzzle based on a game show scenario. The simulation allows for an arbitrary number of doors and evaluates the player's strategy of either switching or staying with their initial choice after the host reveals non-prize doors.

## Overview

The Monty Hall problem involves:
1. A prize hidden behind one of several doors.
2. The player selecting a door.
3. The host revealing non-prize doors.
4. The player deciding to switch to another door or stick with their original choice.

This simulation analyzes how the switching strategy affects the player's chances of winning.

## Features
- Customizable number of doors.
- Choice to simulate switching or staying strategies.
- Visualization of cumulative winning rates compared to theoretical probabilities.

## Installation

1. Clone this repository or download the script.
2. Install the required packages:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

Run the script using Python:
```bash
python monty_hall_simulation.py
```

By default, the simulation runs 1,000 games with 3 doors, both with and without the switching strategy.

## Code Structure

### Class: `MontyHallGame`

Simulates a single game of the Monty Hall problem.

#### `__init__(self, num_doors: int, switch: bool = True)`
- Initializes the game with a specified number of doors.
- **Parameters:**
  - `num_doors`: Total number of doors in the game.
  - `switch`: If `True`, the player will switch their choice after doors are revealed.

#### `reset(self)`
- Resets the game state by:
  - Randomly placing the prize behind a door.
  - Randomly selecting the player's initial choice.
  - Clearing the list of opened doors.

#### `play(self) -> bool`
- Simulates one round of the game.
- **Returns:**
  - `True` if the player wins.
  - `False` if the player loses.

### Function: `simulate_games(num_games: int, num_doors: int, switch: bool)`
- Runs multiple simulations and visualizes the results.
- **Parameters:**
  - `num_games`: Number of games to simulate.
  - `num_doors`: Number of doors in each game.
  - `switch`: Player's strategy (`True` for switching, `False` for staying).
- **Output:**
  - Prints win statistics.
  - Plots the cumulative winning rate against theoretical probability.

### Example Output

```
Using 3 doors with switch strategy
Player won 669/1000 games (66.90%)

Using 3 doors without switch strategy
Player won 334/1000 games (33.40%)
```

## Customization

You can customize the number of games and doors by modifying the `NUM_GAMES` and `NUM_DOORS` variables in the `__main__` block:

```python
NUM_GAMES = 5000  # Number of games to simulate
NUM_DOORS = 5     # Number of doors in the game
```

## License
This project is licensed under the MIT License.

## Author
© 2025 [Anthony Aoun](https://github.com/Anthony-Aoun). All rights reserved.

This project is open-source and free to use for educational purpouses only.


