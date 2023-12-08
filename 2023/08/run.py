"""Day six of advent of code 2023 https://adventofcode.com/2023 """
# %%

from itertools import cycle
from math import lcm

data = open("input.txt", encoding="utf-8").read().splitlines()
instructions = data[0]
instructions

d = {d[:3]: (d[7:10], d[12:15]) for d in data[2:]}
d

# %% task 1
c = 0
current = "AAA"
for i in cycle(instructions):
    f = 1 if i == "R" else 0
    current = d[current][f]
    c += 1
    if current == "ZZZ":
        break
print("task1", c)

# %% task 2

starting_points = [i for i in d.keys() if i[2] == "A"]


hits = []
for sp in starting_points:
    c = 0
    current = sp
    for i in cycle(instructions):
        f = 1 if i == "R" else 0
        current = d[current][f]
        c += 1
        if current[2] == "Z":
            hits.append(c)
            break
print(c)

# to find the synchronization point of different cycles:
lcm(*hits)
