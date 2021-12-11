#%%
import numpy as np

with open('data/input11.txt') as f:
    lines = [list(map(lambda x: int(x), l.strip())) for l in f]


def init_grid(lines):
    grid = np.array(lines)
    size = grid.shape[0] * grid.shape[1]
    print(size)
    grid = np.pad(grid, ((1, 1), (1, 1)), 'constant', constant_values=11)
    return grid, size


def get_adjesent_cords(cord, grid):
    up = (cord[0] - 1, cord[1])
    down = (cord[0] + 1, cord[1])
    left = (cord[0], cord[1] - 1)
    right = (cord[0], cord[1] + 1)
    up_right = (cord[0] + 1, cord[1] + 1)
    up_left = (cord[0] + 1, cord[1] - 1)
    down_right = (cord[0] - 1, cord[1] + 1)
    down_left = (cord[0] - 1, cord[1] - 1)

    return [up, down, left, right, up_right, up_left, down_right, down_left]


def atleast_one_ready_to_flash(grid, has_flashed):
    for iy, ix in np.ndindex(grid.shape):
        if iy == 0 or ix == 0 or iy == grid.shape[0] - 1 or ix == grid.shape[1] - 1: continue
        fish_id = iy, ix
        if fish_id in has_flashed: continue
        if grid[fish_id] > 9:
            return True
    return False


def one_step(grid):
    has_flashed = set()

    # 1. the energy level of each octopus increases by 1.
    grid = grid + 1
    # 2. any octopus with an energy level greater than 9 flashes.
    while atleast_one_ready_to_flash(grid, has_flashed):
        for iy, ix in np.ndindex(grid.shape):
            if iy == 0 or ix == 0 or iy == grid.shape[
                    0] - 1 or ix == grid.shape[1] - 1:
                continue
            fish_id = iy, ix
            if fish_id in has_flashed: continue
            fish_level = grid[iy, ix]

            if fish_level > 9:
                has_flashed.add(fish_id)
                for coord in get_adjesent_cords(fish_id, grid):
                    grid[coord] += 1

    # 3 reset
    for fish_id in list(has_flashed):
        grid[fish_id] = 0

    return grid, len(has_flashed)


#%% Task1
def day11_1(grid):
    num_flashes = 0
    for _ in range(100):
        grid, l = one_step(grid)
        #print(grid, l)
        num_flashes += l
    return num_flashes


grid, size = init_grid(lines)
day11_1(grid)


#%% Task2
def day11_2(grid, size):
    l = 0
    counter = 0
    while l != 100:
        grid, l = one_step(grid)
        counter += 1
    print(counter)


grid, size = init_grid(lines)
day11_2(grid, size)

# %%
