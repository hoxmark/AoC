"""Day nine of advent of code 2023 https://adventofcode.com/2023 """
# %%
import numpy as np

data = open("input.txt", encoding="utf-8").read().splitlines()
data = np.array([list(x) for x in data])
data


def add_row_if_all_dots(data, T=False):
    res = []
    if T:
        data = data.T
    for row in range(len(data)):
        if all(data[row] == "."):
            res.append(row)

    return res


zero_row = add_row_if_all_dots(data)
zero_cols = add_row_if_all_dots(data, T=True)

print(zero_row, zero_cols)

space = data

num_hashes = np.count_nonzero(space == "#")
replacement_values = iter(range(1, num_hashes + 1))
space_int = np.zeros_like(space, dtype=int)

for i in range(space.shape[0]):
    for j in range(space.shape[1]):
        if space[i, j] == "#":
            space_int[i, j] = next(replacement_values)
        elif space[i, j] == ".":
            space_int[i, j] = 0

space = space_int

coords = {val: (i, j) for i, j, val in zip(*np.where(space != 0), space[space != 0])}
points = list(coords.values())


# %%
scale = 1_000_000
total = 0
for i, (r1, c1) in enumerate(points):
    for r2, c2 in points[:i]:
        for r in range(min(r1, r2), max(r1, r2)):
            total += scale if r in zero_row else 1
        for c in range(min(c1, c2), max(c1, c2)):
            total += scale if c in zero_cols else 1
total
