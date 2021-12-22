#%% Day 22
import re
from collections import defaultdict
with open('data/input22.txt') as f:
    cuboids= [(True if l[:2] == "on" else False, [int(i) for i in re.findall(r'[-]?\d+', l)])
          for l in f.readlines()]

cubes = defaultdict(bool)

def is_not_within_bounds(val): return not (-50 <=val <=50)

def turn(action, c):
    print(c)
    for xi in range(c[0], c[1]+1):
        if is_not_within_bounds(xi): return  
        for yi in range(c[2], c[3]+1):
            if is_not_within_bounds(yi): return  
            for zi in range(c[4], c[5]+1):
                if is_not_within_bounds(zi): return  
                #print(f"{xi},{yi},{zi}")
                cubes[f"{xi},{yi},{zi}"] = action

for action, c in cuboids: turn(action, c)
len(cubes), sum(cubes.values())
               
