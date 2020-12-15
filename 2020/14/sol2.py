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

bit_size=36

def find_all_possible(adr):
    new_adrs=[]
    num_of_iterations = np.count_nonzero(adr == -1)
    lst = [list(i) for i in itertools.product([0, 1], repeat=num_of_iterations)]
    itemindex = np.where(adr==-1)
    for l in lst:        
        tmp = adr.copy()        
        for i,j in zip(itemindex[0], l):            
            tmp[i]=j
        new_adrs.append(tmp)
    return new_adrs
        

def bin_to_dec(x):
    return int(''.join(map(lambda x: str(int(x)), x)), 2)

res = {}
for program in programs:    
    mask_1 = []
    mask_x = []
    for i in program['mask']:        
        if i == '0':
           mask_1.append(0)
           mask_x.append(0)
        elif i == '1':
            mask_1.append(1)
            mask_x.append(0)            
        else:
            mask_1.append(0)
            mask_x.append(1)

    mask_1=np.array(mask_1)
    mask_x=np.array(mask_x)

    for m,v in program['list']:
        adresse = padarray(dec_to_bin(m), bit_size)
        tmp=np.where(mask_1==1, 1, adresse)
        tmp=np.where(mask_x==1, -1, tmp)
        adrs = find_all_possible(tmp)
        for x in adrs:
            dec_adr = bin_to_dec(x)            
            res[dec_adr] = v

print(sum(res.values()))