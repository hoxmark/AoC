### Task 2
import itertools
from collections import Counter, defaultdict

with open('input.txt') as f:
    lines = [int(l.rstrip()) for l in f]

lines.append(0)
lines.sort()
lines.append(max(lines)+3)

possibilities = defaultdict(int)
possibilities[0] = 1

for i in lines[1:]:
    # print(i)
    # print(possibilities[i-1])
    # print(possibilities[i-2])
    # print(possibilities[i-3])
    possibilities[i] = possibilities[i-1] + possibilities[i-2] + possibilities[i-3]

res = possibilities[max(lines)]
print(res)

