
with open('input5.txt') as f:
    lines = [list(map(lambda x: list(map(lambda x: int(x), tuple(x.split(',')))), tuple(l.strip().split(' -> ')))) for l in f]

def make_grid(s): 
    gridline = []
    for i in range(s):
        gridline.append(0)

    grid = []
    for i in range(s):
        grid.append(list(gridline))
    return grid

def flatten(t):
    return [item for sublist in t for item in sublist]
all_points = flatten(flatten(lines))
max_h, max_v = max(all_points)+1, 0
print(max_h, max_v)

#grid = [[0]*max_h]*max_h
grid = make_grid(max_h)

def hline(x,y, vertical):
    s = min([x,y])
    e = max([x,y])+1
    for i in range(s, e): 
        #print(vertical, i)
        grid[vertical][i] +=1

def vline(x,y,horizontal): 
    #print(x,y,horizontal)
    s = min([x,y])
    e = max([x,y])+1
    #print(s,e)
    for i in range(s,e): 
        #print(horizontal, i)
        #print(grid[horizontal][i])
        grid[i][horizontal] +=1

def add_line(p1, p2): 
    if p1[0]==p2[0]: 
        vline(p1[1], p2[1], p1[0])
    elif p1[1] == p2[1]: 
        hline(p1[0], p2[0], p1[1]) 
        
for l in lines: 
    #print(l)
    add_line(*l)


#for i in range(max_h): 
    #print(i, grid[i])

print(len([x for x in flatten(grid) if x >1]))
