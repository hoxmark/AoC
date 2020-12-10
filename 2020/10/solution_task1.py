### Task 1 
import itertools
import math

with open('input.txt') as f:
    lines = [int(l.rstrip()) for l in f]

lines.sort()

def find_jolts(l):
    val = 0
    l = l
    choises_diff = []    

    def choose(posibilites):
        #nonlocal val, l        
        return posibilites[0]


    def find_next_adapter():
        nonlocal val, l, choises_diff
        posibilites = list(filter(lambda x: abs(val - x) <= 3, l) )
        next_val = choose(posibilites)
        diff = abs(val - next_val)
        choises_diff.append(diff)
        val = next_val
        l.remove(val)
        if len(l)==0:
            choises_diff.append(3) #LAST RULE
            return False, choises_diff
        return True, choises_diff
    return find_next_adapter

a = find_jolts(lines)
a()

continue_search, v = a()
while continue_search:
    continue_search, v = a()

print(v.count(1)*v.count(3))
    