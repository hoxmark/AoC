#%% Day 14
from collections import Counter, defaultdict

with open('data/input14.txt') as f:
    data = [l.strip() for l in f]
    p = data[data.index('') - 1]
    rules = {
        i.split(' -> ')[0]: i.split(' -> ')[1]
        for i in data[data.index('') + 1:]
    }
p, rules

#%% Task
def find_frequency(p):
    freq = defaultdict(int)
    for i in range(len(p) - 1): 
        freq[f"{p[i]}{p[i+1]}"] += 1
    return freq

def task(iterations, p):    
    freq = find_frequency(p)
    
    for i in range(iterations):
        next_freq = freq.copy()
        for key, value in freq.items():
            if value > 0:
                change = rules[key]
                next_freq[f"{key[0]}{change}"] += value
                next_freq[f"{change}{key[1]}"] += value
                next_freq[key] -= value
        freq = next_freq

    c = Counter({p[0], p[-1]})
    for k, v in freq.items():
        c[k[0]] += v
        c[k[1]] += v

    res = sorted([int(c[k]/2) for k in c.keys()])
    return print(res[-1]-res[0])

#%% TASK 1
task(10, p)

#%% TASK 2
task(40, p)

