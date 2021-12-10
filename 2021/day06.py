with open('input6_test.txt') as f: 
    init_fish = [int(l) for l in f.readline().split(',')]

print(init_fish)

print(f"Initial state:\t{init_fish}")

import functools

#@functools.lru_cache(maxsize=128)
def one_iteration(fs):
    new_fs = []
    for f in fs: 
        if f == 0: 
            new_fs.append(8)
            new_fs.append(6)
        else: 
            new_fs.append(f-1)
    return new_fs

dataset = list(init_fish)

number_of_days = 80
for i in range(1, number_of_days+1):
    dataset = one_iteration(dataset)
    print(f"After day {i} \t: {dataset} => {len(dataset)}")
    print(f"After day {i} \t: => {len(dataset)}")

len(dataset)

