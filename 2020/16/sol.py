### Task 1 
from collections import defaultdict
import pandas as pd
import re
from functools import reduce


def find_number(s):  
    ans = re.findall(r'\d+', s)    
    return [int(i) for i in ans][0]

with open('input.txt') as f:
    inp = [l for l in f.read().split("\n\n")]    
    restrictions = {
        x.split(':')[0]: (
            [int(i) for i in x.split(':')[1].split('or')[0].split('-')],
            [int(i) for i in x.split(':')[1].split('or')[1].split('-')]
        ) for x in inp[0].split('\n')}        
    your_ticket = inp[1].split('\n')[1].split(',')
    nearby_ticket = [x.split(',') for x in inp[2].split('\n')[1:]]

def check_valid(inp, rule):
    return rule[0] <= inp <= rule[1]

def check_place(name, inp):    
    first_rule, second_rule = restrictions[name]
    return any([check_valid(inp,first_rule), check_valid(inp,second_rule)])

def check_number(inp):
    return [check_place(name, inp) for name in restrictions.keys()]

def return_unvalid_number(inp):
    if not any([check_place(name, inp) for name in restrictions.keys()]):
        return inp
    else: 
        return 0

res = [return_unvalid_number(int(item)) for sublist in nearby_ticket for item in sublist]
print('ans1',sum(res))

valid_nearby_tickets = []
for ticket in nearby_ticket:
    ticket_valids = []
    for number in ticket: 
        ticket_valids.append(any(check_number(int(number))))    
    if all(ticket_valids):
        ticket = [int(n) for n in ticket]
        valid_nearby_tickets.append(ticket)

df = pd.DataFrame(valid_nearby_tickets)
csp = {}
for name in restrictions.keys():
    applied_restriction = df.applymap(lambda x: check_place(name,x))
    res = applied_restriction.apply(lambda c: all(c),axis=0)

    csp[name] = list(res[res].index)
safe = {}

def get_the_one_with_only_one(l):
    for k,v in l.items():
        if len(v) == 1:
            return (k,v)
        
print(csp)
while len(csp)>0:
    found = get_the_one_with_only_one(csp)    
    new_csp = {}
    index = found[1][0]
    safe[index] = found[0]
    for k,v in csp.items():    
        if k != found[0]:
            if index in v: v.remove(index)        
            new_csp[k]=v
    
    csp = new_csp 
        
sol = pd.DataFrame([your_ticket,your_ticket])
sol.rename(safe, axis='columns', inplace=True)
sol = sol[['departure location','departure station','departure platform','departure track','departure date','departure time']]
for i, j in sol.iterrows(): 
    product = reduce((lambda x, y: x * y), [int(x) for x in j])
    print(product)
    print('ans2',product)