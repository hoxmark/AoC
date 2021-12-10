with open('input2.txt') as f:
    lines = [tuple(l.strip().split(" ")) for l in f]

    
print(lines)

d, v, aim = 0, 0, 0  
for (op, val) in lines:
    val = int(val)
    if op == "up":
        aim = aim-val
        d = d-val
    elif op == "down":
        aim = aim+val
        d = d+val
    elif op == "left": 
        v = v-val 
    elif op == "forward": 
        aim = aim 
        v = v+val


print(v, d, aim)
print(v*d)


d, h, aim = 0, 0, 0 
for (op, val) in lines:
    val = int(val)
    if op == "up":
        aim = aim-val
        #d = d-val
    elif op == "down":
        aim = aim+val
        #d = d+val
    elif op == "forward": 
        h = h+val 
        d = d+(aim*val)
            

print(h, d, aim)
print(h*d)
