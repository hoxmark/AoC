### Task 1 
import itertools
import numpy as np
with open('input.txt') as f:

    seats = [['.']+list(l.rstrip())+['.'] for l in f]

x_max, y_max = len(seats[0]), len(seats)
pad_y = ['.' for x in range(x_max)]

seats.insert(0,pad_y)
seats.append(pad_y)

x_max, y_max = len(seats[0]), len(seats)
grid = np.array(seats) 

masked_non_seats = np.where(grid== '.', 0, 1)
grid = np.where(grid== 'L', 0, 0)

def update(grid):
    newGrid = np.copy(grid)
    for i in range(y_max):
        for j in range(x_max):            
            if masked_non_seats[i,j] == 0:
                continue

            # compute 8-neghbor sum            
            total = int((grid[i, (j-1)] + grid[i, (j+1)] +
                         grid[(i-1), j] + grid[(i+1), j] +
                         grid[(i-1), (j-1)] + grid[(i-1), (j+1)] +
                         grid[(i+1), (j-1)] + grid[(i+1), (j+1)]))
                        
            if grid[i, j] == 0:                
                if (total == 0):
                    newGrid[i, j] = 1
            else:
                if total >= 4:
                    newGrid[i, j] = 0
    return newGrid

history = []
history.append(grid.sum())
sum_changes=True
while sum_changes:
    grid = update(grid)
    history.append(grid.sum())
    print(grid.sum())
    
    if history[-1]==history[-2]:    
        sum_changes = False