"""Day four of advent of code 2023 https://adventofcode.com/2023 """
# %% import data


FILE_NAME = "input.txt"
data = open(FILE_NAME, encoding="utf-8").read().splitlines()


# %%
def calculate_value(l):
    return 2 ** (len(l) - 1) if l else 0


def extrat_numers(nums):
    return set([int(x.strip()) for x in nums.strip().split(" ") if x != ""])


rs = []
for row in data:
    nums = row[row.index(":") + 1 :].split("|")
    wining_num = extrat_numers(nums[0])
    card_nums = extrat_numers(nums[1])
    overlap = wining_num & card_nums
    rs.append(calculate_value(overlap))
assert sum(rs) == 28538

# %%
copies = {k: 1 for k in range(len(data))}
rs = []
for card_id, row in enumerate(data):
    nums = row[row.index(":") + 1 :].split("|")
    wining_num = extrat_numers(nums[0])
    card_nums = extrat_numers(nums[1])
    overlap = wining_num & card_nums
    rs.append(calculcate_value(overlap))

    for x in range(copies[card_id]):
        for i in range(1, len(overlap) + 1):
            copies[card_id + i] += 1

assert sum(copies.values()) == 9425061
