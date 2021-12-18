#%% Day 18
import re
import math

with open('data/input18_test2.txt') as f:
    fish = list(map(str.strip, f.readlines()))

fish


#%%
def add(a, b):
    if not a: return b
    return ['['] + a + [','] + b + [']']


convert = lambda f: [int(s) if s.isdigit() else s for s in f]
i_d = lambda x: isinstance(x, int)


def explode_on(ind, fi):
    left_num = fi[ind]
    right_num = fi[ind + 2]
    left = fi[:ind]
    right = fi[ind + 3:]

    rleft = list(reversed(left))
    for i in range(len(rleft)):
        if i_d(rleft[i]):
            rleft[i] += left_num
            break

    for i in range(len(right)):
        if i_d(right[i]):
            right[i] += right_num
            break

    return list(reversed(rleft))[:-1] + [0] + right[1:]


def test_explode():
    assert (find_and_explode(
        convert("[[[[[9,8],1],2],3],4]")) == "[[[[0,9],2],3],4]")
    assert (find_and_explode(
        convert("[7,[6,[5,[4,[3,2]]]]]")) == "[7,[6,[5,[7,0]]]]")
    assert (find_and_explode(
        convert("[[6,[5,[4,[3,2]]]],1]")) == "[[6,[5,[7,0]]],3]")
    assert (find_and_explode(convert("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
            == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
    assert (find_and_explode(convert("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")) ==
            "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")


def find_and_explode(fi):
    current_level = 0
    nums = []
    nums_id = []
    for ind, c in enumerate(fi):
        if c == '[': current_level += 1
        if c == ']': current_level -= 1
        if current_level == 5:
            if isinstance(c, int):
                nums.append(c)
                nums_id.append(ind)

    if len(nums) == 0:
        return fi
    res = explode_on(nums_id[0], fi)
    return res


def split_n(f):
    for i, c in enumerate(f):
        if i_d(c) and c > 9:
            l = math.floor(c / 2)
            r = math.ceil(c / 2)
            left = f[:i]
            right = f[i + 1:]
            return left + ['[', l, ',', r, ']'] + right
    return f


l2s = lambda l: "".join(map(str, l))


def reduce_number(fs):
    fs = [convert(f) for f in fs]
    fi = fs[0]
    fs = fs[1:]
    previus_iteration = None
    for _ in range(1000):

        for x in range(100):
            #EXPLODE
            for _ in range(100):
                fi_n = find_and_explode(fi)

                if fi_n == fi:
                    break
                fi = fi_n

            #SPLIT
            for _ in range(1):
                fi_n = split_n(fi)
                if fi_n == fi:
                    break
                fi = fi_n

        if previus_iteration == fi:
            #ADD
            if len(fs) > 0:
                next = fs[0]
                fs = fs[1:]
                fi = add(fi, next)

            else:
                return l2s(fi)

        else:
            previus_iteration = fi


res = reduce_number(fish)
res


def magnitude(a):
    a = convert(a)
    while len(a) > 1:
        for i in range(len(a)):
            if i_d(a[i]) and i_d(a[i + 2]):
                a = a[:i - 1] + [a[i] * 3 + a[i + 2] * 2] + a[i + 4:]
                break
    return a[0]


'task1', magnitude(res)
#%%

with open('data/input18.txt') as f:
    fish = list(map(str.strip, f.readlines()))


def part2(data):
    maxval = 0
    for a in data:
        for b in data:
            if a == b:
                continue
            val = magnitude(reduce_number([a, b]))
            if val > maxval:
                print(val)
                maxval = val
    return maxval


'task2', part2(fish)

#%%
fs = [
    "[1,1]",
    "[2,2]",
    "[3,3]",
    "[4,4]",
    "[5,5]",
]

reduce_number(fs)

assert (reduce_number([
    "[1,1]",
    "[2,2]",
    "[3,3]",
    "[4,4]",
    "[5,5]",
    "[6,6]",
]) == "[[[[5,0],[7,4]],[5,5]],[6,6]]")
