#%% Day 9
import numpy as np
with open('data/input9.txt') as f:
    lines = [list(map(lambda x: int(x), l.strip())) for l in f]

grid = np.array(lines)
grid = np.pad(grid, ((1, 1), (1, 1)), 'constant', constant_values=10)
print(grid)


def get_adjesent_cords(cord):
    up = (cord[0] - 1, cord[1])
    down = (cord[0] + 1, cord[1])
    left = (cord[0], cord[1] - 1)
    right = (cord[0], cord[1] + 1)
    return [up, down, left, right]


def check_adjesent_cords(coord, ignore=set()):
    found = set([coord])
    current_value = grid[coord]
    all_a_cords = get_adjesent_cords(coord)
    cs = set([
        c for c in all_a_cords
        if (current_value < grid[c]) and (grid[c] not in [9, 10])
    ])
    found.update(cs)
    cs = cs - ignore
    if len(cs) == 0: return found

    for c in list(cs):        
        found.update(check_adjesent_cords(c, ignore=found))

    return found


basin = {}
basin_counter = 0
counter = 0
lowest_points = []

for iy, ix in np.ndindex(grid.shape):
    coord = iy, ix
    current_value = grid[iy, ix]
    if current_value == 10: continue
    all_a_cords = get_adjesent_cords((iy, ix))
    num_larger = sum([current_value < grid[c] for c in all_a_cords])
    if num_larger == 4:
        counter += (current_value + 1)
        lowest_points += (iy, ix)
        basin[basin_counter] = check_adjesent_cords(coord, set())
        basin_counter += 1

# %%
n_largest = sorted([len(x) for x in basin.values()])[-3:]
s = n_largest[0] * n_largest[1] * n_largest[2]
print("task1: ", counter)
print("task2: ", s)

# %%
