"""5nd day of advent of code 2022 https://adventofcode.com/2022 """
#%%
import copy


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# %% import data
FILE_NAME = "input.txt"
# FILE_NAME = "test.txt"


data = open(FILE_NAME).read()
stacks, instructions = data.split("\n\n")

instructions = [
    (int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5]))
    for i in instructions.split("\n")
]

stacks = stacks.split("\n")

stack_index = [i for i in stacks[-1].strip() if i != " "]
stacks = stacks[:-1]

s = {int(s): [] for s in stack_index}


def append_s(l):
    for i, item in enumerate(chunks(l, 4), 1):
        item = item.strip()
        if item == "":
            continue
        s[i].append(item.strip())


for l in reversed(stacks):
    append_s(l)


def task1(s, instructions):
    def move(times, fr, to):
        for _ in range(times):
            item = s[fr].pop()
            s[to].append(item)

    for i in instructions:
        move(i[0], i[1], i[2])

    return "".join([v[-1][1] for k, v in s.items()])


print("Task 1, rateMover 9000", task1(copy.deepcopy(s), instructions))

#%%
def task2(s, instructions):
    def move_9001(times, fr, to):
        items = s[fr][-times:]
        s[fr] = s[fr][:-times]
        s[to] += items

    for i in instructions:
        move_9001(i[0], i[1], i[2])

    return "".join([v[-1][1] for k, v in s.items()])


print("Task 2, rateMover 9001", task2(s, instructions))

# %%
