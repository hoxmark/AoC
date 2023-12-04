"""Day two of advent of code 2023 https://adventofcode.com/2023 """
# %% import data
import math as m

FILE_NAME = "input.txt"
data = open(FILE_NAME, encoding="utf-8").read().splitlines()

flatten = lambda l: [item for sublist in l for item in sublist]


def find_all_legal_adjacent(loc):
    i, j = loc

    offsets = [(-1, -1), (-1, 0), (-1, 1), 
               (0, -1),           (0, 1), 
               (1, -1), (1, 0), (1, 1)]
    
    return [(i + di, j + dj) for di, dj in offsets]


all_num = []
all_num_loc = []
symb_loc = {}
for ir, r in enumerate(data):
    num_loc = []
    num = []
    for ii, i in enumerate(r + "."):  # ensure that we can find the last number
        if i.isdigit():
            num.append(i)
            num_loc.append((ir, ii))

        elif i != ".":
            symb_loc[(ir, ii)] = i

        if len(num) != 0 and (i.isdigit() == False):
            number = int("".join(num))

            all_num.append(number)
            all_num_loc.append(num_loc)
            num = []
            num_loc = []

OK = []

for num, loc in zip(all_num, all_num_loc):
    a_flat = set(flatten([find_all_legal_adjacent(l) for l in loc]))

    # overlap between a_flat and symb_loc
    overlap = a_flat.intersection(symb_loc.keys())

    if len(overlap) != 0:
        OK.append(num)

print(sum(OK))
assert sum(OK) == 553825

# %% task 2
task2 = 0
for loc, symb in symb_loc.items():
    nums = []
    if symb == "*":
        search_locs = set(find_all_legal_adjacent(loc))

        for num, ls in zip(all_num, all_num_loc):
            if len(search_locs.intersection(ls)):
                nums.append(num)

        if len(nums) > 1:
            task2 += m.prod(nums)
assert task2 == 93994191
