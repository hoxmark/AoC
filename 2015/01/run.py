"""Day two of advent of code 2021 https://adventofcode.com/2015 """
# %%
data = open("inp.txt").read()
# %%
print(data.count("(") - data.count(")"))
# %%
v = 0
for e, i in enumerate(data):
    if i == "(":
        v += 1
    elif i == ")":
        v -= 1

    if v == -1:
        print(e + 1)

# %%
