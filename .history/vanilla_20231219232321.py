import time
import os
import random

# Settings
ON = 'O'  # Representation of an alive cell
OFF = '.' # Representation of a dead cell
N = 20    # Size of the grid (N x N)

def create_grid(size):
    return [[ON if random.random() > 0.7 else OFF for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print("\n")

def count_neighbors(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbor_count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == ON:
            neighbor_count += 1
    return neighbor_count

def next_generation(grid):
    new_grid = create_grid(N)
    for row in range(N):
        for col in range(N):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col] == ON and neighbors in [2, 3]:
                new_grid[row][col] = ON
            elif grid[row][col] == OFF and neighbors == 3:
                new_grid[row][col] = ON
            else:
                new_grid[row][col] = OFF
    return new_grid

def run_game():
    grid = create_grid(N)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)

run_game()
