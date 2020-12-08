### Task 5 
from functools import reduce

with open('input.txt') as f:
    lines = f.read()

inp = [l.split('\n') for l in lines.split("\n\n")]
#print(inp)
def count_list(i):
    group = [set(list(x)) for x in i]
    #print(group)
    res = reduce((lambda x, y: x | y), group)
    return len(res)

ans = sum([count_list(i) for i in inp])

print(ans)

# TODO remove last from inp
#TASK 2

def count_all_in_list(i):
    group = [set(list(x)) for x in i]
    print(group)
    res = reduce((lambda x, y: x & y), group)
    return len(res)

ans = sum([count_all_in_list(i) for i in inp])
print(ans)