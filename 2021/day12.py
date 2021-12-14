#%%
import numpy as np

with open('data/input12.txt') as f:
    cave = [list(map(lambda x: x, l.strip().split('-'))) for l in f]

from collections import defaultdict
cave_rules = defaultdict(list)

for c_pair in cave: 
    cave_rules[c_pair[0]].append(c_pair[1])
    cave_rules[c_pair[1]].append(c_pair[0])

cave_rules

q = [['start']]
found = 0

while q:
    path = q.pop(0)
    #print(path)
    last_seen = path[-1]
    for c in cave_rules[last_seen]:
        if c == 'end':
            found = found + 1
        
        # add to queue if large cave or if not yet visitid small cave
        elif c.isupper() or c not in path:
            q.append(path + [c])

print('answer task 1: ', found)

#%%
q = [['start']]
found = 0

while q:
    path = q.pop(0)
    #print(path)
    last_seen = path[-1]
    for c in cave_rules[last_seen]:
        been_here_before = c.islower() and c in path

        if c == 'end':
            found = found + 1
               
        elif c != 'start' and not (path[0] == 'MARK' and been_here_before):
            if been_here_before:
                q.append(['MARK']+path+[c])
            else: 
                q.append(path+[c])
            

print('answer task 2: ', found)

# %%
