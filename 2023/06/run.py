"""Day six of advent of code 2023 https://adventofcode.com/2023 """
import math


# %%
def solve(time, dist):
    all_possible_win = []
    for best_time, best_distance in zip(time, dist):
        possible_win = []
        for start_speed in range((best_distance // best_time) + 1, best_time):
            time_left = best_time - start_speed
            distance_traveled = start_speed * time_left
            if distance_traveled > best_distance:
                possible_win.append(start_speed)

        all_possible_win.append(possible_win)
    return math.prod([len(x) for x in all_possible_win])


## task 1
time = [44, 89, 96, 91]
dist = [277, 1136, 1890, 1768]

solve(time, dist)
# %% task 2
time = [44899691]
dist = [277113618901768]

solve(time, dist)
