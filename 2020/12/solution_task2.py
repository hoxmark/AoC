### Task 1 
import itertools
import math
import numpy as np

with open('input.txt') as f:
    lines = [(l[0], int(l[1:].rstrip())) for l in f]

def rotate(p, origin=(0, 0), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T-o.T) + o.T).T)

y, x = 0.0,0.0
north_unit, east_unit = 1, 10
for d, v in lines:
    if d=='N':
        north_unit = north_unit + v
    if d=='E':
        east_unit = east_unit + v
    if d=='S':
        north_unit = north_unit - v
    if d=='W':
        east_unit = east_unit - v
    if d=='L':                
        new_point = rotate((north_unit, east_unit), degrees=-v)    
        north_unit, east_unit = new_point[0], new_point[1]
    if d=='R':        
        new_point = rotate((north_unit, east_unit), degrees=v)            
        north_unit, east_unit = new_point[0], new_point[1]
    if d=='F':
        print(v,north_unit, east_unit)
        y = y+(v*north_unit)
        x = x+(v*east_unit)
    
print(x,y)
print('dist:', abs(x)+ abs(y))
