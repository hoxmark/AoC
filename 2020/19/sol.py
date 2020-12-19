### Task 1 
from collections import defaultdict
import re
import types
import copy

def find_number(s):  
    ans = re.findall(r'\d+', s)    
    return [int(i) for i in ans][0]

with open('input.txt') as f:
    inp = [l for l in f.read().split("\n\n")]    
    rules = {int(x.split(':')[0]): x.split(':')[1].strip() for x in inp[0].split('\n')}        
    messages = inp[1].split('\n')    

formatted_rules = {}
for num, rule in rules.items():
    rule = [r.strip() for r in rule.split('|')]
    if rule[0][0]=='"':formatted_rules[num]=('1', rule[0][1])
    else:         
        if len(rule)>1:
            formatted_rules[num] = ('or', [ [int(i) for i in r.split(' ')] for r in rule])
        else:
            formatted_rules[num] = ('0', [ [int(i) for i in r.split(' ')] for r in rule])

print(formatted_rules)
print(messages)

def unwind_rules(rules):    
    matches = []
    def get_rule(sub_rules):
        nonlocal matches
        if sub_rules[0]=='1':            
            matches.append(sub_rules[1])
            return

        elif sub_rules[0]=='0':
            if not any(isinstance(i, list) for i in sub_rules[1]): 
                for num in sub_rules[1]:
                    get_rule(rules[num])
            else:  
                for num in sub_rules[1][0]:
                    get_rule(rules[num])
        
        elif sub_rules[0]=='or':  
            
            matches.append('(')
            for i in sub_rules[1][0]:
                get_rule(rules[i])
            matches.append('|')
            for i in sub_rules[1][1]:
                get_rule(rules[i])
            matches.append(')')
        else:
            print("WHAT= Why else")
        
        return matches
    return get_rule

find = unwind_rules(formatted_rules)
eq = find((formatted_rules[0]))

reg = "".join(eq)

count_not_none = []
for m in messages:
    overlap = re.fullmatch(reg, m)
    if overlap:
        count_not_none.append(overlap)
    
print(len(count_not_none))


