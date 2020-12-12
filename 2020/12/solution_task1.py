### Task 1 
import itertools
import math
with open('input.txt') as f:
    lines = [(l[0], int(l[1:].rstrip())) for l in f]

def manhatten_distance(x_value,  x_goal,y_value,y_goal):
    return abs(x_value - x_goal) + abs(y_value - y_goal)
print(lines)

y, x = 0.0,0.0 
degree = 90

for d, v in lines:
    
    if d=='N':
        y = y-v
    if d=='E':
        x = x+v
    if d=='S':
        y = y+v
    if d=='W':
        x = x-v
    if d=='L':
        degree = (degree - v) % 360
    if d=='R':
        degree = (degree + v) % 360
    if d=='F':
        if degree == 90:            
            x = x+v
        elif degree == 180:
            y = y+v
        elif degree == 270:            
            x = x-v
        elif degree == 0:
            y = y-v
        else: 
            print(degree, v)
print(x,y)
dist = manhatten_distance(x,0,y,0)
print(dist)
