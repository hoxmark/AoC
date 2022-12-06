"""6nd day of advent of code 2022 https://adventofcode.com/2022 """

#%% import data
FILE_NAME = "input.txt"

data = list(open(FILE_NAME).read())


def find_start(data, L=4):
    stack = []
    while True:
        stack.append(data.pop(0))

        if len(stack) > L - 1:
            last_digitst = set(stack[-L:])
            if len(list(last_digitst)) == L:
                return len(stack)


# %%
print("Task 1, ", find_start(data, 4))
print("Task 2, ", find_start(data, 14))
# %%
