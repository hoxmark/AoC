import itertools

with open("input.txt") as f: 
    lines = [l.strip() for l in f.readlines()]

def findEqualWithOneError(s1,s2):
    num_errors=0
    index_error=-1
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            index_error = i
            num_errors+=1
        if num_errors>1: return -1
    return index_error

combs = itertools.combinations(lines,2)

for c in combs:
    res = findEqualWithOneError(*c)
    if res>0:
        print(c[0])
        print(c[1])
        print(c[0][:res]+c[0][res+1:])
        break

