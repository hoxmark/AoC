#%%
from collections import Counter


def day6(days=80):
    n_times = 9
    with open('input6.txt') as f: 
        init_fish = [l for l in f.readline().split(',')]
        cf = Counter(int(x) for x in init_fish)
        counts = [cf[i] for i in range(n_times)] 

    def next_step(counts):
        counts2 =  [0 for i in range(n_times)]
        for i in range(1, n_times):
            counts2[i-1] = counts[i]
        counts2[6] += counts[0]
        counts2[n_times - 1] += counts[0]
        return counts2

    for i in range(days):
        counts = next_step(counts)    
    print(sum(counts))

#%% Task 1
day6()

#%% Task 2
day6(256)

# %%
