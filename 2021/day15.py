#%% Day 15
import numpy as np
from helper import Graph
with open('data/input15_test.txt') as f:
    cave = [list(map(lambda x: int(x), l.strip())) for l in f]
grid = np.array(cave)
largest_y, largest_x = grid.shape[0]-1,grid.shape[1]-1
print('x', largest_x, 'y', largest_y)

def get_adjesent_cords(cord,grid,largest_y,largest_x):
    up = (cord[0] - 1, cord[1])
    down = (cord[0] + 1, cord[1])
    left = (cord[0], cord[1] - 1)
    right = (cord[0], cord[1] + 1)    
    l = [tuple([f'{li[0]},{li[1]}', grid[li]]) for li in [up, down, left, right] if li[0]>=0 and li[1]>=0 and li[0]<=largest_y and li[1]<=largest_x]
    return l

gi = {}
for coord in np.ndindex(grid.shape):    
    gi[f'{coord[0]},{coord[1]}'] = get_adjesent_cords(coord, grid, largest_y, largest_x)

graph1 = Graph(gi)
route = graph1.a_star_algorithm('0,0', f'{largest_y},{largest_x}')

print('Task1')
sum([grid[(int(c.split(',')[0]),int(c.split(',')[1]))] for c in route][1:])

#%% Task 2
g0 = [grid]
current_tgrid = grid
for g in range(1,5):    
    tgrid = ((current_tgrid+1) % 10)    
    tgrid[tgrid == 0] = 1
    #print(tgrid[0,7])
    g0.append(tgrid)
    current_tgrid = tgrid.copy()

large_grid = np.concatenate(tuple(g0),axis=1)

gy0to5 = [large_grid]
current_tgrid = large_grid.copy()
for g in range(1,5):
    tgrid = ((current_tgrid+1) %10)    
    tgrid[tgrid == 0] = 1
    gy0to5.append(tgrid)
    current_tgrid = tgrid.copy()

large_grid = np.concatenate(tuple(gy0to5),axis=0)

#In test: assert(sum(sum(large_grid))==12845) 

#%%
large_grid
llargest_y, llargest_x = large_grid.shape[0]-1,large_grid.shape[1]-1
print('x', llargest_x, 'y', llargest_y)

gi = {}
for coord in np.ndindex(large_grid.shape):    
    gi[f'{coord[0]},{coord[1]}'] = get_adjesent_cords(coord, large_grid, llargest_y, llargest_x)

graph2 = Graph(gi)
print("Searching")
route = graph2.a_star_algorithm('0,0', f'{llargest_y},{llargest_x}')

print("Task2") 
sum([large_grid[(int(c.split(',')[0]),int(c.split(',')[1]))] for c in route][1:])

# %%
