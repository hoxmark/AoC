"""Day nine of advent of code 2023 https://adventofcode.com/2023 """
# %%
import copy
from collections import Counter

data = open("input.txt", encoding="utf-8").read().splitlines()
data = [list(row) for row in data]


def spin_north(data):
    for _ in range(10000):
        changes = 0
        for row_id in range(1, len(data)):
            for col_id in range(len(data[row_id])):
                if data[row_id][col_id] == "O" and data[row_id - 1][col_id] == ".":
                    data[row_id - 1][col_id] = "O"
                    data[row_id][col_id] = "."
                    changes += 1

        # print(changes)
        if changes == 0:
            return data


def spin_south(data):
    for _ in range(10000):
        changes = 0
        for row_id in range(len(data) - 2, -1, -1):
            for col_id in range(len(data[row_id])):
                if data[row_id][col_id] == "O" and data[row_id + 1][col_id] == ".":
                    data[row_id + 1][col_id] = "O"
                    data[row_id][col_id] = "."
                    changes += 1

        # print(changes)
        if changes == 0:
            return data


def spin_west(data):
    for _ in range(10000):
        changes = 0
        for row_id in range(len(data)):
            for col_id in range(1, len(data[row_id])):
                if data[row_id][col_id] == "O" and data[row_id][col_id - 1] == ".":
                    data[row_id][col_id - 1] = "O"
                    data[row_id][col_id] = "."
                    changes += 1

        # print(changes)
        if changes == 0:
            return data


def spin_east(data):
    for _ in range(1000):
        changes = 0
        for row_id in range(len(data)):
            for col_id in range(len(data[row_id]) - 2, -1, -1):
                if data[row_id][col_id] == "O" and data[row_id][col_id + 1] == ".":
                    data[row_id][col_id + 1] = "O"
                    data[row_id][col_id] = "."
                    changes += 1

        # print(changes)
        if changes == 0:
            return data


def get_score(data):
    sum = 0
    for i, row in enumerate(data):
        c = Counter(row)
        sum += (len(data) - i) * c["O"]
    return sum


def to_str(grid):
    return "".join(["".join(grid[i]) for i in range(len(grid))])


def run(data):
    runs = 1000000000
    d = {}
    idx = 1
    while True:
        data = spin_north(data)
        data = spin_west(data)
        data = spin_south(data)
        data = spin_east(data)

        x = to_str(data)
        if x in d:
            cyclen = idx - d[x][0]
            for a, b in d.values():
                if a >= d[x][0] and a % cyclen == runs % cyclen:
                    return b
            break
        d[x] = (idx, get_score(data))
        idx += 1


task1 = get_score(spin_north(copy.deepcopy(data)))
print(task1)

task2 = run(data)
print(task2)
assert task2 == 102509
