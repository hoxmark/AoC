"""14nd day of advent of code 2022 https://adventofcode.com/2022 """
#%%

INPUT_NAME = "input.txt"
# INPUT_NAME = "test.txt"


pairs = [
    [tuple(map(int, p.strip().split(","))) for p in x.split("->")]
    for x in open(INPUT_NAME).read().split("\n")
]

xma = max([item[0] for sublist in pairs for item in sublist])
xmi = min([item[0] for sublist in pairs for item in sublist])
yma = max([item[1] for sublist in pairs for item in sublist]) + 2
ymi = min([item[1] for sublist in pairs for item in sublist])
print("frame:", xma, xmi, yma, ymi)

grid = set()
for (x, y), *path in pairs:
    grid.add((x, y))
    for xp, yp in path:
        while (x != xp) or (y != yp):
            x = x + (xp > x) - (x > xp)
            y = y + (yp > y) - (y > yp)
            grid.add((x, y))


for x in range(500 - yma - 1, 500 + yma + 1):
    grid.add((x, yma))


task1 = 0
task2 = 0
counter = 0


while True:
    x = 500
    y = 0
    if (x, y) in grid:
        task2 = counter
        break

    while True:
        if not task1 and y >= yma - 1:
            task1 = counter

        if (x, y + 1) not in grid:
            y = y + 1
        elif (x - 1, y + 1) not in grid:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in grid:
            x, y = x + 1, y + 1
        else:
            grid.add((x, y))
            break
    counter += 1

print("Task1 ", task1)
assert task1 == 795
print("Task2 ", task2)
assert task2 == 30214


# %%
