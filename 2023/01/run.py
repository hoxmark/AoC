"""Day one of advent of code 2023 https://adventofcode.com/2023 """
# %% import data
FILE_NAME = "input.txt"
# with open(FILE_NAME, encoding="utf-8") as f:
#     data = [l.strip() for l in f.readlines()]
# data
data = open(FILE_NAME, encoding="utf-8").read().splitlines()


# %% task 1
r = []

for d in data:
    vals = [x for x in d if x.isdigit()]
    r.append((int("".join([vals[0] + vals[-1]]))))
print(sum(r))
assert sum(r) == 53651
# %% task 2
rep = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def scan_string(data, rev):
    if rev:
        for i in range(1, len(data) + 1):
            for x, v in rep.items():
                if str(v) in data[(-i):]:
                    return v

            for x, v in rep.items():
                if x in data[-i:]:
                    return v

    else:
        for i in range(len(data) + 1):
            for x, v in rep.items():
                if str(v) in data[0:i]:
                    print(data[i - 1], x, v, data)
                    return v

            for x, v in rep.items():
                if x in data[0:i]:
                    return v


r = []
for d in data:
    i = []
    f = scan_string(d, False)
    l = scan_string(d, True)
    if f:
        i.append(str(f))
    if l:
        i.append(str(l))
    #  print(data)
    # print(f, l, int("".join(i)))
    r.append((int("".join(i))))

print(sum(r))
assert sum(r) == 53894
