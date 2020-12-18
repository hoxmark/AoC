### Task 2
import itertools
import numpy as np
with open('input.txt') as f:
    seats = [['.']+list(l.rstrip())+['.'] for l in f]

x_max, y_max = len(seats[0]), len(seats)
pad_y = ['.' for x in range(x_max)]

seats.insert(0,pad_y)
seats.append(pad_y)
x_max, y_max = len(seats[0]), len(seats)
grid = np.array(seats)# set grid size
print(grid)

def occupied_seat_in_sight(debug, row):    
    if debug:
        print(row) 
    for thing in row:
        if thing == 'L':
            return False
        if thing == '#':
            return True
    return False

def number_of_seats_in_use(grid):
    return list(grid.flatten()).count('#')


def update(grid, debug=False):
    newGrid = np.copy(grid)
    print(grid)

    for i in range(y_max): #for y
        for j in range(x_max):   #for x
            if debug:
                print('i', i, 'j', j, 'val', grid[i,j])
            if grid[i,j]=='.':                
                continue
            
            n = min(i,j)
            m = min(*grid[i+1:, :j].shape)
            # compute 8-neghbor sum            
            total = np.array([
                occupied_seat_in_sight(debug, grid[i, :j][::-1]), # left
                occupied_seat_in_sight(debug, grid[i, j+1:]), # right
                occupied_seat_in_sight(debug, grid[i+1:, j]), # down
                occupied_seat_in_sight(debug, grid[:i, j][::-1]), # up
                occupied_seat_in_sight(debug, grid[i-n:i, j-n:j].diagonal(0)[::-1]), # left top 
                occupied_seat_in_sight(debug, np.flipud(grid[:i, j+1:]).diagonal()), # right top
                occupied_seat_in_sight(debug, grid[i+1:, j+1:].diagonal()), # down right
                occupied_seat_in_sight(debug, np.flipud(grid[i+1:i+1+m, j-m:j]).diagonal()[::-1]), #down left 
            ])
            
            total = total.astype(int).sum()
            if debug:
                print(total)
                print('------')
                             
            if grid[i, j] == 'L':                
                if (total == 0):
                    newGrid[i, j] = '#'
            else:
                if total >= 5:
                    newGrid[i, j] = 'L'
    return newGrid

num = number_of_seats_in_use(grid)
history = [num]
print(history)
sum_changes=True

while sum_changes:
    grid = update(grid)
    num = number_of_seats_in_use(grid)
    history.append(num)    

    print(grid)
    print(history)
    if history[-1]==history[-2]:    
        sum_changes = False