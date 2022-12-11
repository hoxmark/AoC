"""11nd day of advent of code 2022 https://adventofcode.com/2022 """
#%%
import operator
from collections import namedtuple
from functools import partial, reduce

from tqdm import tqdm

Monkey = namedtuple("Monkey", ["num", "items", "op", "by", "test", "true", "false"])


def minus(a, b):
    return a - b


def mod(a, b):
    return a % b


def pow(a, b):
    return a**b


def parse_func(inp):
    """Str char to function"""
    old, val, in_b = inp

    match (val, in_b):
        case ("+", _):
            return partial(operator.add, int(in_b))
        case ("-", _):
            return partial(minus, b=int(in_b))
        case ("*", vb):
            if vb == "old":
                return partial(pow, b=2)
            else:
                return partial(operator.mul, int(in_b))
        case _:
            print("NOT FOUND")


def parse_monkey(m):
    """Parase monkey"""
    m = m.split("\n")
    num = int(m[0].split(" ")[1][0])
    items = [int(x.strip()) for x in m[1].split(":")[1].split(",")]
    operation = parse_func(m[2].split("=")[1].strip().split(" "))
    by = int(m[3].split("by")[1])
    test = lambda x: mod(x, by) == 0
    true = int(m[4].split("monkey")[1])
    false = int(m[5].split("monkey")[1])

    return Monkey(num, items, operation, by, test, true, false)


def iterate_over(monkey, reduction_func):
    """iterate over monkey"""
    # print(monkey)

    while True:
        if len((monkey.items)) < 1:
            return
        inspect_counter[monkey.num] += 1
        start = monkey.items.pop(0)
        val = monkey.op(start)

        val = reduction_func(val)
        # val = val // 3
        # val = val % mfmp

        if monkey.test(val):
            # print("TRUE, ", monkey.true)
            data[monkey.true].items.append(val)
        else:
            data[monkey.false].items.append(val)


def run(data, io, rounds):
    for _ in range(1, rounds):
        list(map(io, data))

    orded = sorted(inspect_counter.values())
    return orded[-1] * orded[-2]


INPUT_NAME = "test.txt"
INPUT_NAME = "input.txt"

# Task 1
data = list(map(parse_monkey, open(INPUT_NAME).read().split("\n\n")))
mfmp = reduce(operator.mul, [x.by for x in data])
inspect_counter = {i: 0 for i in range(len(data))}

inspect_counter = {i: 0 for i in range(len(data))}
io1 = partial(iterate_over, reduction_func=lambda x: x // 3)
inspect_counter = {i: 0 for i in range(len(data))}
assert run(data, io1, 21) == 182293

#%% Task 2
data = list(map(parse_monkey, open(INPUT_NAME).read().split("\n\n")))
mfmp = reduce(operator.mul, [x.by for x in data])
inspect_counter = {i: 0 for i in range(len(data))}

inspect_counter = {i: 0 for i in range(len(data))}
io2 = partial(iterate_over, reduction_func=lambda x: x % mfmp)
assert run(data, io2, 10_001) == 54832778815

# %%
