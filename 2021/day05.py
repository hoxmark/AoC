#%% Day 5
with open('data/input5.txt') as f:
    lines = [
        list(
            map(lambda x: list(map(lambda x: int(x), tuple(x.split(',')))),
                tuple(l.strip().split(' -> ')))) for l in f
    ]


def make_grid(s):
    gridline = []
    for i in range(s):
        gridline.append(0)

    grid = []
    for i in range(s):
        grid.append(list(gridline))
    return grid


def flatten(t):
    return [item for sublist in t for item in sublist]


all_points = flatten(flatten(lines))
max_h, max_v = max(all_points) + 1, 0
print(max_h, max_v)

grid = make_grid(max_h)


def hline(x, y, vertical):
    s = min([x, y])
    e = max([x, y]) + 1
    for i in range(s, e):
        grid[i][vertical] += 1


def vline(x, y, horizontal):
    s = min([x, y])
    e = max([x, y]) + 1
    for i in range(s, e):
        grid[horizontal][i] += 1


def dline(p1, p2):
    #to right
    if p1[0] < p2[0] and p1[1] < p2[1]:
        current = p1
        while current != p2:
            grid[current[0]][current[1]] += 1
            current = [current[0] + 1, current[1] + 1]
        grid[p2[0]][p2[1]] += 1

    elif p1[0] < p2[0] and p1[1] > p2[1]:
        current = p1
        while current != p2:
            grid[current[0]][current[1]] += 1
            current = [current[0] + 1, current[1] - 1]
        grid[p2[0]][p2[1]] += 1
    elif p1[0] > p2[0] and p1[1] < p2[1]:
        current = p1
        while current != p2:
            grid[current[0]][current[1]] += 1
            current = [current[0] - 1, current[1] + 1]
        grid[p2[0]][p2[1]] += 1

    elif p1[0] > p2[0] and p1[1] > p2[1]:
        current = p1

        while current != p2:
            grid[current[0]][current[1]] += 1

            current = [current[0] - 1, current[1] - 1]

        grid[current[0]][current[1]] += 1
    else:
        assert (True), "Failed"

def add_line(p1, p2):
    if p1[0] == p2[0]:
        vline(p1[1], p2[1], p1[0])
    elif p1[1] == p2[1]:
        hline(p1[0], p2[0], p1[1])
    else:
        dline(p1, p2)


for l in lines:
    add_line(*l)

print('task1', len([x for x in flatten(grid) if x > 1]))
# %%
