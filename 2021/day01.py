#%% Day 1
with open('data/input1.txt') as f:
    lines = [int(l) for l in f]

def num_inc(l):
    return sum([l[i]>l[i-1] for i in range(1,len(l))])

def sum_window(l, size=3):
    return [sum(l[i:i+size])
            for i in range(len(l)-size + 1)]

def day1_1(l):
    return num_inc(lines)

def day1_2(l):
    return num_inc(sum_window(lines))

print(day1_1(lines))

print(day1_2(lines))


# %%
