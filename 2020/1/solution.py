### Task 1 
##lines = [1721,979,366,299,675,1456]
import itertools

with open('input.txt') as f:
    lines = [int(l.rstrip()) for l in f]

ans = [i*k for i,k in itertools.combinations(lines, 2) if i+k==2020]
print('answer task 1:', ans[0])

### task 2 
ans = [i*k*j for i,k,j in itertools.combinations(lines, 3) if i+k+j==2020]
print('answer task 2:', ans[0])
