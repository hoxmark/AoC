"""4. day of advent of code 2022 https://adventofcode.com/2022/leaderboard """
#%% import data

FILE_NAME = "input.txt"
with open(FILE_NAME, encoding="utf-8") as f:
    data = [[tuple(map(int, i.split("-"))) for i in l.strip().split(",")] for l in f]


def is_between(a, b):
    """Checks if a is between first and second value in b"""
    return (a >= b[0]) and (a <= b[1])


#%% task 1
fm, pm = 0, 0
for pairs in data:
    a, b = pairs

    if a[0] >= b[0] and a[1] <= b[1]:
        fm += 1
    elif b[0] >= a[0] and b[1] <= a[1]:
        fm += 1
print("fully overlap", fm)

# %%
for pairs in data:
    a, b = pairs

    c = any(
        [
            is_between(a[0], b),
            is_between(a[1], b),
            is_between(b[0], a),
            is_between(b[1], a),
        ]
    )
    if c:
        pm += 1
# %%
print("partally overlap", pm)
# %%
