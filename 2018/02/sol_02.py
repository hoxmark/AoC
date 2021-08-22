from collections import Counter
import functools

with open("input.txt") as f: 
    lines = [l.strip() for l in f.readlines()]

all_count = {2:0, 3:0}

for l in lines:   
    counted_id = Counter(l)
    for c in list(set(counted_id.values())):
        if c in [2,3]: all_count[c] += 1
    
sol_a = all_count[2]*all_count[3]
print(sol_a)    
