import re
with open('input.txt') as f:
    lines = [l.rstrip() for l in f]

inp = [re.split('contain |, ',l) for l in lines]

def find_number(s):    
    ans = re.findall(r'\d+|no', s)
    if 'no' in ans :
        return 0
    return [int(i) for i in ans][0]

bags = {}
for i in inp: 
    head = i[0].strip()
    options = []
    for bag in i[1:]:
        bag_num = find_number(bag)
        bag = " ".join(bag.replace('.', '').split(' ')[1:])
        if bag_num == 1:
            bag += 's'
        options.append((bag_num, bag))

    bags[head] = options

def find(name, bags):
    check = []
    nums = []
    for b, o in bags.items():
        here = False
        for i in o:         
            if name == i[1]:
                here = True
                nums.append(i[0])        
        if here: 
            check.append(b)
    return check, nums

has_checked = []
to_check, nums = find('shiny gold bags', bags)  

while len(to_check)>0:
    for c in to_check:
        res, nums = find(c, bags)        
        has_checked.append(c)
        to_check.remove(c)
        for r in res: 
            if r not in has_checked:
                to_check.append(r)    
    
print('ans: ', len(set(has_checked)))

def count_bags(search, bags):
    res = 1
    for o in bags[search]:
        if 'other bags' == o[1]:
            return 1
        else: 
            res += o[0]*count_bags(o[1], bags)
    return res

res = count_bags('shiny gold bags', bags)
print('ans task 2',res)
