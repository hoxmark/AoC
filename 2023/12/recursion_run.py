# %%
from functools import lru_cache


@lru_cache(maxsize=None)
def count(config, nums):
    if config == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in config else 1

    result = 0

    if config[0] in ".?":
        result += count(config[1:], nums)

    if config[0] in "#?":
        if (
            nums[0] <= len(config)
            and "." not in config[: nums[0]]
            and (nums[0] == len(config) or config[nums[0]] != "#")
        ):
            result += count(config[nums[0] + 1 :], nums[1:])

    return result


total = 0

for line in open("input.txt"):
    print(line)
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    config = "?".join([config] * 5)
    nums *= 5
    total += count(config, nums)

print(total)

# %%
