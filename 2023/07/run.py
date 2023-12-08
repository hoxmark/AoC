"""Day five of advent of code 2023 https://adventofcode.com/2023 """
# %% import data
from collections import Counter

FILE_NAME = "input.txt"
data = open(FILE_NAME, encoding="utf-8").read().splitlines()
d = [i.split(" ") for i in data]
d

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
order


# Five of a kind, where all five cards have the same label: AAAAA
def five_of_a_kind(c, js):
    if js == 5:
        return True
    if c[0][1] >= 5 - js:
        return True
    else:
        return False


# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
def four_of_a_kind(c, js):
    if c[0][1] >= 4 - js:
        return True
    else:
        return False


# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
def full_house(c, js):
    return c[0][1] + c[1][1] >= (5 - js)


# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
def three_of_a_kind(c, js):
    if c[0][1] >= 3 - js:
        return True
    else:
        return False


# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
def two_pair(c, js):
    return c[0][1] + c[1][1] >= (4 - js)


# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
def one_pair(c, js):
    return c[0][1] >= 2 - js


# High card, where all cards' labels are distinct: 23456
def is_first_best(h1, h2):
    for i in range(len(h1)):
        # print(h1[i][0], h2[i][0])
        # print(order.index(h1[i][0]), order.index(h2[i][0]))
        if order.index(h1[i][0]) < order.index(h2[i][0]):
            return 1
        elif order.index(h1[i][0]) == order.index(h2[i][0]):
            continue
        else:
            return -1
    assert False, "No winner"


def find_rank(hand):
    c = Counter(hand)
    js = c["J"]
    del c["J"]
    c = c.most_common()

    if five_of_a_kind(c, js):
        return 10
    if four_of_a_kind(c, js):
        return 9
    if full_house(c, js):
        return 8
    if three_of_a_kind(c, js):
        return 7
    if two_pair(c, js):
        return 6
    if one_pair(c, js):
        return 5
    else:
        return 1


assert find_rank("32T3K"), 5
assert find_rank("KK677"), 6


assert is_first_best("33332", "2AAAA") == True
assert is_first_best("77888", "77788") == True
assert is_first_best("JJJJ8", "JJJJJ") == 1


# %%
def compare_two_hands(h1, h2):
    v1 = find_rank(h1[0])
    v2 = find_rank(h2[0])
    # print(v1, v2)
    if v1 == v2:
        return is_first_best(h1[0], h2[0])
    elif v1 > v2:
        return 1
    else:
        return -1


assert compare_two_hands(["JKKK2"], ["QQQQ2"]) == -1
assert is_first_best("AAAAJ", "AAAAQ") == -1
assert compare_two_hands(["AAAAJ"], ["AAAAA"]) == -1
assert compare_two_hands(["JJJJ8"], ["JJJJJ"]) == 1

# %%
from functools import cmp_to_key

compare_key = cmp_to_key(compare_two_hands)

r = sorted(d, key=compare_key)
[(i, x) for i, x in enumerate(r, 1)]

assert sum([(int(i) * int(x[1])) for i, x in enumerate(r, 1)]) == 249138943
sum([(int(i) * int(x[1])) for i, x in enumerate(r, 1)])
