"""8nd day of advent of code 2022 https://adventofcode.com/2022 """
"""10nd day of advent of code 2022 https://adventofcode.com/2022 """
# %% import data
from itertools import accumulate

import numpy as np


def f(x):
    return int(x) if x[-1].isdigit() else 0


FILE_NAME = "input.txt"
FILE_NAME = "test2.txt"

data = [*map(f, open(FILE_NAME).read().split())]
data = list(accumulate([1] + data))

task1 = 0
task2 = ""

for i, x in enumerate(data, 1):
    print(i, x)
    if i % 40 == 20:
        task1 += i * x
    if (i - 1) % 40 - x in [-1, 0, 1]:
        task2 += "# "
    else:
        task2 += "  "

print("ans part1,", task1)
print(task2)
# READ FZBPBFZF


# %%
