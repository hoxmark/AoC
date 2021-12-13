#%% Day 13
from collections import Counter, defaultdict
import numpy as np

with open('data/input13_test.txt') as f:
    data = [l.strip() for l in f]
    dots = [tuple(map(int,i.split(','))) for i in data[:data.index('')]]
    folds = [(i.split('=')[0][-1],int(i.split('=')[1]))  for i in data[data.index('')+1:]]

for x,y in dots: 
    pass
largest_x = max(i[0] for i in dots)+1
largest_y = max(i[1] for i in dots)+1
'x', largest_x, 'y', largest_y

grid = np.zeros((largest_y, largest_x))

#fill grid wiht dots = 1, 
for iy, ix in np.ndindex(grid.shape):
    if (ix, iy) in dots: grid[iy, ix] = 1

def horizontal(y):
    
    for count, bottom_index in enumerate(range(y+1, largest_y)):        
        top_index = y-count-1
        grid[top_index] = grid[top_index]+grid[bottom_index] 
    return grid[:y]
    

def vertical(x):    
    for count, right_index in enumerate(range(x+1, largest_x)):
        left_index = x-count-1        
        grid[:,left_index] = grid[:,right_index]+grid[:,left_index]
    #
    return grid[:, :x]
def flip(fold):
    print('fold', fold)
    if fold[0]=='x': return vertical(fold[1])
    elif fold[0] == 'y': return horizontal(fold[1])
    else: assert(True), 'wrong input'

sums = []
for fold in folds:
    grid = flip(fold)
    grid[grid>0] = 1    
    sums.append(sum(sum(grid)))    
    largest_y,largest_x = grid.shape

def day13_1():
    return sums[0]
day13_1()

# %%
def day13_2():
    for i in grid:
        print(['#' if j>0 else '.' for j in i])
        #reduce the display size on text
day13_2()        
