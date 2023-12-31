# Game of Life - Vanilla Version

[View the code here](./vanilla.py)

- **Grid Initialization**: The create_grid function creates an NxN grid, where each cell is randomly set to either ON (alive) or OFF (dead).

- **Printing the Grid**: The print_grid function prints the current state of the grid to the console, with spaces between cells for readability.

- **Counting Neighbors**: The count_neighbors function calculates the number of alive neighbors for a given cell.

- **Calculating the Next Generation**: The next_generation function applies the rules of Conway's Game of Life to produce the next state of the grid.

- **Running the Game**: The run_game function initializes the grid and then continuously updates and displays the grid, creating an ongoing simulation.

- **Clearing the Console**: The script uses `os.system('cls' if os.name == 'nt' else 'clear')` to clear the console screen between each generation, giving the appearance of animation.


## Detailed Code Explanation

### Importing Necessary Modules

```py
import time
import os
import random
```

-   **`time`**: Used to introduce a delay between each generation to simulate animation.
-   **`os`**: Helps in clearing the console screen to display each new generation cleanly.
-   **`random`**: Used to randomly initialize the grid.

### Defining Constants and Grid Size

```py
ON = 'O'  # Representation of an alive cell
OFF = '.' # Representation of a dead cell
N = 20    # Size of the grid (N x N)
```

-   `ON` and `OFF` are string representations of alive and dead cells, respectively.
-   `N` sets the size of the grid to 20x20 cells.

### Grid Initialization Function

```py
def create_grid(size):
    return [[ON if random.random() > 0.7 else OFF for _ in range(size)] for _ in range(size)]
```

-   This function creates an NxN grid.
-   Each cell is randomly assigned to be either `ON` (alive) or `OFF` (dead). The chance of a cell starting as `ON` is set by `random.random() > 0.7`, implying roughly 30% of cells will be alive initially.

### Printing the Grid

```py
def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print("\n")
```

-   Iterates through each row of the grid and prints it. Cells are separated by spaces for better visibility.
-   An extra newline is printed after the grid for visual separation between generations.

### Neighbor Count Function

```py
def count_neighbors(grid, row, col):
    ...
```

-   This function calculates the number of alive neighbors for a cell located at `row`, `col`.
-   It checks the eight adjacent cells (including diagonals) to count how many are alive (`ON`).

### Calculating the Next Generation

```py
def next_generation(grid):
    ...
```

-   This function applies the rules of Conway's Game of Life to generate the next state of the grid.
-   It creates a new grid of the same size and then determines the fate of each cell based on the number of alive neighbors.

### Game Loop

```py
def run_game():
    grid = create_grid(N)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)

```

-   Initializes the game with a random grid.
-   Enters an infinite loop where each iteration represents a generation.
-   Clears the console screen for each generation using `os.system('cls' if os.name == 'nt' else 'clear')`. This makes sure the new grid is printed at the same position as the old one, creating an animation effect.
-   Prints the current state of the grid.
-   Waits for 0.5 seconds before computing the next generation to make the changes observable.

### Running the Game

-   Finally, the `run_game` function is called to start the simulation. This will keep running until manually stopped (usually with Ctrl+C in the console).

This script provides a basic, text-based simulation of Conway's Game of Life. It demonstrates the core concepts of cellular automata and how complex behavior can emerge from simple rules.



## Usage
Run this script in a Python environment. It will display the evolving Game of Life in your console. You can stop the game by interrupting the execution (usually Ctrl+C in the console).

This implementation is a basic console-based version and will not have the smooth animation or visual appeal of a graphical version, but it does demonstrate the core logic of Conway's Game of Life.

