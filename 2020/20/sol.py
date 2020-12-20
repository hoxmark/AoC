### Task 1 
from collections import defaultdict

import re
from functools import reduce
import numpy as np

with open('input.txt') as f:
    inp = [l.split('\n') for l in f.read().split("\n\n")]  
    tiles = {}
    for tile_uncoded in inp:        
        num = int(tile_uncoded[0].split(' ')[1].rstrip()[:-1])
        tile = np.array([list(x.rstrip()) for x in tile_uncoded[1:]])
        tiles[num] = np.where(tile=='#', True, False)

tile_posibility = {k:{} for k,_ in tiles.items()}
for k,t in tiles.items(): 
    #print(k, t)
    tile_posibility[k]['TOP'] = (t[0,:], False)                    # TOP    
    tile_posibility[k]['TOP_REV'] = (np.flipud(t[0,:]), False)     # TOP REV
    tile_posibility[k]['BOTTOM'] = (t[-1,:], False)                # BOTTOM
    tile_posibility[k]['BOTTOM_REV'] = (np.flipud(t[-1,:]), False) # BOTTOM REV
    tile_posibility[k]['LEFT'] = (t[:, 0], False)                  # LEFT
    tile_posibility[k]['LEFT_REV'] = (np.flipud(t[:, 0]), False)   # LEFT REV
    tile_posibility[k]['RIGHT'] = (t[:, -1], False)                # RIGHT
    tile_posibility[k]['RIGHT_REV'] = (np.flipud(t[:, -1]), False) # RIGHT REV
    
tile_found={}
for num_a, tile_a in tile_posibility.items():
    for num_b, tile_b in tile_posibility.items():
        if num_a == num_b: 
            continue
        for key_a, pos_a in tile_a.items():
            for key_b, pos_b in tile_b.items():
                if np.array_equal(pos_a[0],pos_b[0]):                              
                    #print('Match:', num_a,key_a, num_b, key_b)
                    tile_posibility[num_a][key_a] = (tile_posibility[num_a][key_a][0], True)
                    tile_posibility[num_b][key_b] = (tile_posibility[num_a][key_a][0], True)

corner = []
for num, tile in tile_posibility.items():    
    count_missing = 0
    for key, pos in tile.items():
        if not pos[1]:      
            count_missing = count_missing+1
    print(num, count_missing)
    if count_missing==4:
        corner.append(num)

print(corner)
s = 1
for i in corner:
    s = s*i
print(s)