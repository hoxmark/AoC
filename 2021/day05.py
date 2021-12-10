#%% Day 5

with open('data/input5.txt') as f:
    lines = [list(map(lambda x: list(map(lambda x: int(x), tuple(x.split(',')))), tuple(l.strip().split(' -> ')))) for l in f]

def flatten(t):
    return [item for sublist in t for item in sublist]
all_points = flatten(flatten(lines))
max_h, max_v = max(all_points), 0
print(max_h, max_v)

grid = [[0]*max_h]*max_h


def hline(x,y, vertical):
    s = min([x,y])
    e = max([x,y])
    for i in range(s, e): 
        grid[i][vertical] +=1

def vline(x,y,horizontal): 
    s = min([x,y])
    e = max([x,y])
    for i in range(s,e): 
        grid[horizontal][i] +=1

def add_line(x, y): 
    if x[0]==y[0]: 
        hline(x[1], y[1], x[0])
    elif x[1] == y[1]: 
        vline(x[0], y[0], x[1]) 
        
for l in lines: 
    add_line(*l)
    
