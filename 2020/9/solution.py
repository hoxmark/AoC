### Task 1 
import itertools

with open('input.txt') as f:
    lines = [int(l.rstrip()) for l in f]

def find_weakness(lookback = 25):
    for i in range(lookback+1,len(lines)):    
        seq = lines[i-(lookback+1):i]
        seq, main = seq[:-1],seq[-1]
        equals = [(i,k) for i,k in itertools.combinations(seq, 2) if i+k==main]       
        if len(equals)==0:
            return main

weakness = find_weakness()
print('ans1', weakness)

### Task 2
def find_sum_in_sub_list(l, s, m):       
    sum_sub_list = 0

    for i in range (len(l)-m + 1): 
        sum_sub_list = 0
        for j in range (i, i + m): 
            sum_sub_list += l[j] 

        if sum_sub_list == s:                         
            return [l[i] for i in list(range (i, i + m))]
    return False


for m in range(2,20):
    found = find_sum_in_sub_list(l=lines, s=weakness, m=m) 
    if found != False:        
        contigues_list = found 
        ans = max(contigues_list) + min(contigues_list)
        print('-----')
        print('ans2:', ans)
        break
