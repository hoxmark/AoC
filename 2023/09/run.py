"""Day nine of advent of code 2023 https://adventofcode.com/2023 """
# %%
data = open("input.txt", encoding="utf-8").read().splitlines()
data = [list(map(int, d.split(" "))) for d in data]


def get_first(n):
    n[-1].insert(0, 0)
    for i in range(len(n) - 2, -1, -1):
        a = n[i + 1][0]
        b = n[i][0]
        n[i].insert(0, b - a)
    return n[0][0]


def get_last(n):
    n[-1].append(0)
    for i in range(len(n) - 2, -1, -1):
        a = n[i + 1][-1]
        b = n[i][-1]
        n[i].append(a + b)
    return n[0][-1]


def extend(n):
    n, count = [n], 0

    while not all((i == 0 for i in n[count])):
        new_list = []
        for i in range(1, len(n[count])):
            new_list.append(n[count][i] - n[count][i - 1])
        n.append(new_list)
        count += 1
    return n


def extrapolate(n, front=False):
    n = extend(n)
    return get_first(n) if front else get_last(n)


assert 1708206096 == sum([extrapolate(d) for d in data])
assert 1050 == sum([extrapolate(d, front=True) for d in data])
