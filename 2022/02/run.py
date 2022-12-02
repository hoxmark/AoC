"""2nd day of advent of code 2022 https://adventofcode.com/2022/leaderboard """
# %% import data
FILE_NAME = "input.txt"
with open(FILE_NAME, encoding="utf-8") as f:
    data = [(l[0], l[2]) for l in f]

#%% task 1
# C : A for Rock, B for Paper, and C for Scissors
# me: X for Rock, Y for Paper, and Z for Scissors.
score = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}


def win(a: str, b: str):
    """Calculate score"""
    match (a, b):
        case ("A", "Y"):
            return 6
        case ("A", "Z"):
            return 0
        case ("B", "Z"):
            return 6
        case ("B", "X"):
            return 0
        case ("C", "Y"):
            return 0
        case ("C", "X"):
            return 6
        case _:
            return 3


def game(d):
    return win(d[0], d[1]) + score[d[1]]


total_score = sum([game(d) for d in data])
print(f"Task 1: {total_score}")

#%% Task 2
to_win = {"A": "B", "B": "C", "C": "A"}
to_lose = {v: k for k, v in to_win.items()}


def rig(a, your_goal):
    """
    X means you need to lose,
    Y means you need to end the round in a draw, and
    Z means you need to win. Good luck!"
    """
    if your_goal == "X":
        return 0 + score[to_lose[a]]

    if your_goal == "Y":
        return 3 + score[a]

    if your_goal == "Z":
        return 6 + score[to_win[a]]


total_score = sum([rig(d[0], d[1]) for d in data])
print(f"Task 2: {total_score}")
# %%
