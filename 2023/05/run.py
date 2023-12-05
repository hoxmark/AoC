"""Day four of advent of code 2023 https://adventofcode.com/2023 """
# %% import data

# %%

FILE_NAME = "input.txt"
data = open(FILE_NAME, encoding="utf-8").read().splitlines()

seeds = list(map(int, data[0][data[0].index(":") + 1 :].strip().split(" ")))
seeds

# %%
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
maps


# %%
def find_in_map(current, m):
    for v in m:
        # print("v", v)
        dest, source, r = v
        # print("dest", dest, "source", source, "current", current)

        if current >= source and current < (source + r):
            c = current + dest - source
            return c

    return current


r = []
for s in seeds:
    print("seed", s)
    current = s

    for k, v in maps.items():
        # print(k, v)
        current = find_in_map(current, v)
        # print(current)
    print("end:", current)
    r.append(current)

min(r)
# %%
