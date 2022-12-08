"""8nd day of advent of code 2022 https://adventofcode.com/2022 """
# %% import data
import numpy as np

FILE_NAME = "input.txt"
# FILE_NAME = "test.txt"
data = [list(map(int, list(x))) for x in open(FILE_NAME).read().split("\n")]


def is_visable(dirs, current_value):
    """True if it is visable from on direction"""
    for row in dirs:
        is_higher = [current_value > a for a in row]

        if all(is_higher):
            return True
    return False


def is_tree_visable(cord, grid):
    """True is thee is visable from a direction"""
    iy, ix = cord
    if (iy == 0) or (ix == 0) or (iy == grid.shape[0] - 1) or (ix == grid.shape[1] - 1):
        return False
    if (iy == 1) or (ix == 1) or (iy == grid.shape[0] - 2) or (ix == grid.shape[1] - 2):
        return True

    current_value = grid[iy, ix]

    up = grid[0:iy, ix]
    down = grid[iy + 1 : grid.shape[0], ix]
    left = grid[iy, 0:ix]
    right = grid[iy, ix + 1 : grid.shape[1]]

    dirs = [up, down, left, right]

    return is_visable(dirs, current_value)


def number_of_visable_trees(data):
    """iterate over all items in grid"""
    grid = np.pad(data, (1, 1), "constant", constant_values=0)
    return sum([is_tree_visable((iy, ix), grid) for iy, ix in np.ndindex(grid.shape)])


assert number_of_visable_trees(data) == 1854


# %%
def countView(trees, current_value):
    score = 0
    for x in trees:
        if current_value > x:
            score += 1
        else:
            score += 1
            return score
    return score


def calculate_view_score(cords):
    iy, ix = cords
    if (iy == 0) or (ix == 0) or (iy == grid.shape[0] - 1) or (ix == grid.shape[1] - 1):
        return 0

    current_value = grid[iy, ix]

    up = grid[0:iy, ix]
    up_score = countView(reversed(up), current_value)

    down = grid[iy + 1 : grid.shape[0], ix]
    down_score = countView(down, current_value)

    left = grid[iy, 0:ix]
    left_score = countView(reversed(left), current_value)

    right = grid[iy, ix + 1 : grid.shape[1]]
    right_score = countView(right, current_value)

    res = up_score * down_score * left_score * right_score

    return res


grid = np.array(data)
view_score = [calculate_view_score(cord) for cord in np.ndindex(grid.shape)]


assert max(view_score) == 527340
# %%
