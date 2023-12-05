"""Day four of advent of code 2023 https://adventofcode.com/2023 """
# %% import data

# %%

FILE_NAME = "input.txt"
data = open(FILE_NAME, encoding="utf-8").read().splitlines()

seeds = list(map(int, data[0][data[0].index(":") + 1 :].strip().split(" ")))

# %%task 1
maps = {}
current = None
for l in data[2:]:
    if ":" in l:
        current = l.split(" ")[0]
        maps[current] = []

    elif l == "":
        pass
    else:
        maps[current].append(list(map(int, l.strip().split(" "))))


def find_in_map(current, m):
    for v in m:
        dest, source, r = v
        if current >= source and current < (source + r):
            c = current + dest - source
            return c

    return current


r = []
for s in seeds:
    current = s
    for k, v in maps.items():
        current = find_in_map(current, v)
    r.append(current)

min(r)
# %% task2

seeds = [(seed, seed + r) for seed, r in zip(seeds[::2], seeds[1::2])]

for m in maps.values():
    ranges = m
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
assert 37806486 == min(seeds)[0]
