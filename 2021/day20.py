#%% Day 20
import numpy as np


def to_int(l):
    return [1 if x == '#' else 0 for x in l]


with open('data/input20.txt') as f:
    data = [l.strip() for l in f]
    algo = data[0]
    grid = np.array(list(map(to_int, data[2:])))

print(len(algo))
algo = {i: True if x == '#' else False for i, x in enumerate(algo)}
print(algo[0], algo[511])


def pad(grid, val=0):
    return np.pad(grid, 3, constant_values=val)


def get_adjesent_cords(cord, grid):
    up_left = (cord[0] - 1, cord[1] - 1)
    up = (cord[0] - 1, cord[1])
    up_right = (cord[0] - 1, cord[1] + 1)
    left = (cord[0], cord[1] - 1)
    right = (cord[0], cord[1] + 1)
    down_left = (cord[0] + 1, cord[1] - 1)
    down = (cord[0] + 1, cord[1])
    down_right = (cord[0] + 1, cord[1] + 1)

    return [
        up_left, up, up_right, left, cord, right, down_left, down, down_right
    ]


def on_iteration(grid, pad_val=0):
    grid = pad(grid, pad_val)

    if pad_val == 0:
        next_grid = np.zeros(grid.shape, dtype=np.uint8)
    else:
        next_grid = np.ones(grid.shape, dtype=np.uint8)

    for iy, ix in np.ndindex(grid.shape):
        if iy in [0, 1, grid.shape[0] - 1, grid.shape[0] - 2]: continue
        if ix in [0, 1, grid.shape[1] - 1, grid.shape[1] - 2]: continue

        part_of_grid = get_adjesent_cords((iy, ix), grid)

        bin = "".join([str(grid[x]) for x in part_of_grid])
        dec = int(bin, 2)

        next_grid[(iy, ix)] = int(algo[dec])

    return next_grid[2:-2, 2:-2]


def task(grid, times=2):
    for i in range(times):
        val = (i % 2 == 1) # padding fluxes between 1 and 0
        grid = on_iteration(grid, pad_val=val) 
    return np.sum(grid, axis=(0, 1))


print('task1', task(grid))

# %%
print('task2', task(grid, times=50))

