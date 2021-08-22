from collections import Counter
import functools

with open("input.txt") as f: 
    lines = [l.strip() for l in f.readlines()]

all_count = {2:0, 3:0}

for l in lines:   
    a = Counter(l)
    print(a)
    for c in list(set(a.values())):
        if c in [2,3]:
            all_count[c] += 1
    
print(all_count)

sol_a = all_count[2]*all_count[3]

#sol_a = functools.reduce(lambda a,b: a*b if a!=0 else b, all_count)

print(sol_a)
