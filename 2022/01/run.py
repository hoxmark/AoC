"""Day one of advent of code 2022 https://adventofcode.com/2022 """
#%% Day
# %% import data
data = open("input.txt", encoding="utf-8").read()[:-1].split("\n\n")
elfs = sorted([sum(map(int, x.split("\n"))) for x in data])
#%% task 1
print("largest", max(elfs))
#%% task 2
print("3 largest", elfs[-3:], "sum:", sum(elfs[-3:]))
