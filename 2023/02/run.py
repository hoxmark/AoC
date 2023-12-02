"""Day two of advent of code 2023 https://adventofcode.com/2023 """
# %% import data
import re
from functools import reduce

FILE_NAME = "input.txt"
data = open(FILE_NAME, encoding="utf-8").read().splitlines()


def parse_game(game):
    game_id = re.search(r"Game (\d+):", game).group(1)
    slist = []
    for s in game[game.index(":") + 1 :].split(";"):
        slist.append(
            {
                c.strip().split(" ")[1]: c.strip().split(" ")[0]
                for c in s.strip().split(",")
            }
        )
    return (game_id, slist)


games = {r[0]: r[1] for g in data if (r := parse_game(g))}


# %% # task 1
def max_count_in_game(game):
    return {color: max(int(set_.get(color, 0)) for set_ in game) for color in t.keys()}


def game_meets_threshold(game, threshold):
    max_counts = max_count_in_game(game)
    return all(threshold[color] >= count for color, count in max_counts.items())


t = {"red": 12, "green": 13, "blue": 14}
task_1 = [
    int(game_id) for game_id, game in games.items() if game_meets_threshold(game, t)
]

assert sum(task_1) == 2913

# %% task 2


def max_count_per_color(game_sets):
    return [max(map(lambda s: int(s.get(color, 1)), game_sets)) for color in t.keys()]


def product_of_max_counts(game):
    return reduce(lambda x, y: x * y, max_count_per_color(game))


task2 = [product_of_max_counts(g) for _, g in games.items()]
assert sum(task2) == 55593
