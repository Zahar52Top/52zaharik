import numpy as np
from config import *

def new_grid():
    grid = np.zeros((ROWS, COLUMNS))
    return grid

print(np.flip(grid, 0))

We will describe the functions in the board.py module:

def is_valid_position(grid, col):
    return grid[ROWS - 1][col] == 0

def get_valid_position(grid):
    valid_position = []
    for col in range(COLUMNS):
        if is_valid_position(grid, col):
    valid_position.append(col)
    return valid_position