"""3. day of advent of code 2022 https://adventofcode.com/2022 """
#%%

# %% import data
FILE_NAME = "input.txt"
# FILE_NAME = "test.txt"
with open(FILE_NAME, encoding="utf-8") as f:
    data = [l.strip() for l in f]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


letters = "abcdefghijklmnopqrstuvwxyz"
letters = list(list(letters) + list([l.upper() for l in letters]))
l_n = {v: k for k, v in enumerate(letters, 1)}

# %% task 1
ps = []
for d in data:
    l = len(d)
    s_a = set(i for i in d[: int(l // 2)])
    s_b = set(i for i in d[int(l // 2) :])
    inter = s_a.intersection(s_b)
    c = list(inter)[0]
    ps.append(l_n[c])
print("task 1:", sum(ps))

# %% task 2

r_2 = []
for d in chunks(data, 3):
    d = list(set(list(i)) for i in d)
    r = d[0] & d[1] & d[2]
    r = list(r)[0]
    r_2.append(l_n[r])
print("task 2:", sum(r_2))
