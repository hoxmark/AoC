"""7nd day of advent of code 2022 https://adventofcode.com/2022 """
# %% import data
FILE_NAME = "input.txt"
data = [x.split(" ") for x in open(FILE_NAME).read().split("\n")]

all_dirs = {}
stack_dirs = []

for d in data:
    if d[0] == "$":
        if d[1] == "cd":
            if d[2] == "..":
                stack_dirs.pop()
            else:
                stack_dirs.append(d[2])

    elif d[0].isdigit():
        p = "_".join(stack_dirs)
        if p in all_dirs:
            all_dirs[p].append(int(d[0]))
        else:
            all_dirs[p] = [int(d[0])]


def get_longest_(ks):
    return max([x.count("_") for x in ks])


all_collapesed_folder = []

while True:
    if len(all_dirs) == 1:
        break
    longest = get_longest_(all_dirs.keys())

    to_del = []
    to_create = []
    for k, v in all_dirs.items():
        if k.count("_") == longest:
            new_loc = "_".join(k.split("_")[:-1])

            to_del.append(k)
            to_create.append((new_loc, sum(v)))

    for (k, v) in to_create:
        if k in all_dirs:
            all_dirs[k].append(v)
        else:
            all_dirs[k] = [v]

    for k in to_del:
        all_collapesed_folder.append(sum(all_dirs[k]))
        del all_dirs[k]

# task1
assert sum([x for x in all_collapesed_folder if x < 100000]) == 2031851

# task2
FILE_SYSTEM = 70000000
used = sum(all_dirs["/"])
NEEDED = 30000000
now = FILE_SYSTEM - used
need_to_free = NEEDED - now

assert min([i for i in all_collapesed_folder if i > need_to_free]) == 2568781
