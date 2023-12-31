# Conway's Game of Life in Python

## Description
This project is an implementation of Conway's Game of Life, a cellular automaton devised by British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input.

## Installation
To run this project, you need Python installed on your machine along with the following packages:
- NumPy
- Matplotlib

[Version without libraries](./vanilaVersion.md)

You can install these packages using pip:
```bash
pip install numpy matplotlib
```

## Code Explanation

For a detailed explanation view the [code explanation here](./codeExplanation.md)

## Usage
Run the script in a Python environment. The script will display an animation of the Game of Life in action.

## Rules of the Game
The game evolves in a grid of cells, each of which is in one of two possible states: alive (ON) or dead (OFF). The rules of the game are as follows:
1. Any live cell with fewer than two live neighbors dies, as if by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Initial Configuration
The initial state of the game is a random distribution of ON and OFF cells. The probability of a cell being ON is set to 20%, and OFF is set to 80%.

## Code Explanation
The script's logic is as follows:
- **Import Required Libraries**: `numpy` for handling arrays and `matplotlib` for visualization.
- **Function `update`**: This function is called for each frame in the animation. It applies the rules of the game to determine the next state of each cell.
- **Defining ON and OFF**: These constants represent the states of a cell (alive or dead).
- **Creating the Grid**: A grid of NxN cells is initialized with random states (ON or OFF).
- **Setting up Plotting**: Matplotlib is used to create an animation showing the evolution of the game.
- **Running the Animation**: The `FuncAnimation` function from matplotlib is used to create the animation, calling the `update` function for each frame.

## Contributions
Contributions are welcome. If you have ideas on how to improve this implementation or add new features, feel free to create a pull request.

## License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
