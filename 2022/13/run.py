"""13nd day of advent of code 2022 https://adventofcode.com/2022 """
#%%
import ast
import operator
from functools import cmp_to_key, partial, reduce

INPUT_NAME = "input.txt"
# INPUT_NAME = "test/.txt"


def split_pairs(x):
    left = ast.literal_eval(x[0])
    right = ast.literal_eval(x[1])
    return (left, right)


pairs = [split_pairs(x.split("\n")) for x in open(INPUT_NAME).read().split("\n\n")]


def compare(l, r):
    """compare"""
    for i in range(max([len(l), len(r)])):
        if i >= len(r):
            return False
        elif i >= len(l):
            return True

        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return True
            elif l[i] == r[i]:
                continue
            else:
                return False

        elif isinstance(l[i], list) and isinstance(r[i], list):
            res = compare(l[i], r[i])
            if res is None:
                continue
            else:
                return res
        else:
            if isinstance(l[i], int):
                res = compare([l[i]], r[i])
            elif isinstance(r[i], int):
                res = compare(l[i], [r[i]])
            else:
                res = None

            return res

    return None


# task1
assert sum([i if compare(l, r) else 0 for i, (l, r) in enumerate(pairs, 1)]) == 5605

# task2
dividers = [[[2]], [[6]]]
lp = [item for sublist in pairs for item in sublist] + dividers
cmp = lambda x, y: 1 if compare(x, y) else -1
r = sorted(lp, key=cmp_to_key(cmp), reverse=True)
assert reduce(operator.mul, [i + 1 for i, p in enumerate(r) if p in dividers]) == 24969

# %%
