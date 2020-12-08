### Task 1 
import re
from functools import reduce

with open('input.txt') as f:
    lines = [l for l in f]

x_len = len(lines[0])-1
y_len = len(lines)
print('x:', x_len)
print('y:', y_len)

def check_policy(x_policy,y_policy):
    go = True
    log = []
    x, y = 0,0
    while go:
        log.append(lines[y][x%x_len])
        x += x_policy
        y += y_policy
        if y >= len(lines):
            go= False

    print(log)
    return log.count("#")

policyes_to_check = [(1,1), (3,1), (5,1), (7,1), (1,2) ]
res = [check_policy(*x) for x in policyes_to_check]

result1 = reduce((lambda x, y: x * y), res)

print("--")
print(result1)