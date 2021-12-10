#%% Day 10
with open('data/input10.txt') as f:
    lines = [list(map(lambda x: x, l.strip())) for l in f]

illegal_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

pair = {')': '(', ']': '[', '}': '{', '>': '<'}

reversed_pair = {v: k for k, v in pair.items()}

complete_comp = {')': 1, ']': 2, '}': 3, '>': 4}


# %% Task 1, find number of corrupt
def find_corruption(l):
    stack = []
    for i, c in enumerate(l):
        if c in ["[", '{', "(", "<"]: stack.append(c)
        else:
            left = stack.pop()
            if left != pair[c]: return illegal_dict[c]
    return 0


print("task1: ", sum([find_corruption(l) for l in lines]))

# %% task2
incomplete_lines = [l for l in lines if 0 == find_corruption(l)]


def complete_lines(stack):
    score = 0
    while len(stack) > 0:
        score *= 5
        c = stack.pop()
        r_c = reversed_pair[c]
        score += complete_comp[r_c]
    return score


def traverse(l):
    stack = []
    for c in l:
        if c in ["[", '{', "(", "<"]: stack.append(c)
        else:
            left = stack.pop()
            if left != pair[c]: assert (False), "corruption"
    return complete_lines(stack)


def day10_2(lines):
    res = [traverse(l) for l in lines]

    #return middle of sorted res
    return sorted(res)[int(len(res) / 2)]


print('Task 2:' ,day10_2(incomplete_lines))


# %%
