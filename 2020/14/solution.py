### Task 1 
import numpy as np
import numpy.ma as ma
import itertools
import re

programs = []
with open('input.txt') as f:
    lines = [l.rstrip().split(' ') for l in f]

def find_number(s):  
    ans = re.findall(r'\d+', s)    
    return [int(i) for i in ans][0]

for l in lines:     
    if l[0]=='mask':
        programs.append({'mask':l[2], 'list':[]})
    else : 
        programs[-1]['list'].append((find_number(l[0]), int(l[2])))

def dec_to_bin(x):
    return [int(i) for i in list(bin(x)[2:])]

def padarray(A, size):
    t = size - len(A)
    return np.pad(A, pad_width=(t, 0), mode='constant')

print(programs)
bit_size=36

res = {}
for program in programs:
    
    mask = []
    for i in program['mask']:
        if i in ['0','1']:
            mask.append(int(i))
        else:
            mask.append(-1)

    mask=np.array(mask)
    masked = np.where(mask==-1,0, 1)
    for m,v in program['list']:
        value = padarray(dec_to_bin(v), bit_size)
        res[m]=np.where(mask==-1, value, mask)

tot = [int(''.join(map(lambda x: str(int(x)), x)), 2) for x in res.values()]
print(sum(tot))