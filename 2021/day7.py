#%%
import statistics
with open('input7.txt') as f: 
    subs = [int(l) for l in f.readline().split(',')]

def day7_1(subs):
    new_loc = statistics.median(subs)
    print('median',new_loc)

    cost = int(sum([abs(s-new_loc) for s in subs]))
    print('day 7_1 answer:', cost)
    return cost

day7_1(subs)

#%% task2  Brut force solution, checking all. could check only ones near mean
def day7_2(subs):
    def move_crab(start, end):
        distance = abs(end-start)    
        l = [i for i in range(1, distance+1)]
        sub_cost = sum(l)
        return sub_cost

    results = {}
    for i in range(max(subs)):
        cost = sum([move_crab(s,i) for s in subs])    
        results[i] = cost
        print('counter', i)
    res = min(results, key=results.get)    
    print('res day 7:', res, results[res])

    return results[res]

day7_2(subs)