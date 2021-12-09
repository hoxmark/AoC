from collections import defaultdict
with open('Input3.txt') as f:
    lines = [l.strip() for l in f]

import operator
import functools

def invert(s): return   ''.join(['1' if i == '0' else '0'
                         for i in most_common])

def fmc(lines ): 
    #rs = list(map(lambda l: list(map(lambda x: 1 if x==v else 0, l)), lines))
    #rs = list(map(operator.add, rs[0], rs[1]))
    rs = list(map(lambda l: list(map(lambda x: int(x), l)), lines))
    rs = functools.reduce(lambda x, y: map(operator.add,x,y), rs)
    #print(list(rs))
    rs = map(lambda x: 1 if x>=len(lines)/2 else 0, rs)
    
    return list(rs)

most_common = fmc(lines)
print(most_common)


def find_most_common(lines):
    ones = defaultdict(lambda :0)
    zeros = defaultdict(lambda :0)
    for l in lines:
        for i,b in enumerate(l): 
            if b == '1':
                ones[i] += 1
            elif b == '0':
                zeros[i] += 1

    most_common = []
    for i in range(len(lines[0])):
        b = 0 if zeros[i] > ones[i] else 1
        most_common.append(str(b))
    return most_common

most_common = find_most_common(lines)
most_common = "".join(most_common)

def invert(s): return   ''.join(['1' if i == '0' else '0'
                         for i in most_common])

epsilon_rate = invert(most_common)
epsilon_rate = int(epsilon_rate, 2)

gamma_rate = int(most_common, 2) 

print(epsilon_rate, gamma_rate, epsilon_rate*gamma_rate)
import functools

def fo(values, i, most_common): 
    return [x for x in values if x[i]== most_common[i]] 
   
def fc(values, i, most_common): 
    return [x for x in values if x[i] != most_common[i]]


def find_oxy():
    l =  list(lines)
    for i in range(len(lines[0])):
        mc = find_most_common(l)
        l = fo(l, i, mc)
        if len(l) < 2: 
            return int(l[0], 2)

def find_co2():
    l = list(lines)
    for i in range(len(lines[0])):
        mc = find_most_common(l)
        l = fc(l, i, mc)
        if len(l) < 2: 
            return int(l[0], 2)
print("most_common", most_common)
o = find_oxy()
print(o)

c = find_co2()
print(c)

print('res', c*o)


