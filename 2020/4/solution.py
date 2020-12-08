### Task 1 
import re
from functools import reduce
import pandas as pd

with open('input.txt') as f:
    lines = f.read()

credentials = [l.replace('\n', ' ') for l in lines.split("\n\n")]

users = []
for c in credentials:
    user = {}
    for at in c.split(" "):        
        k,v = list(at.split(":"))
        user[k] = v
    users.append(user)

df = pd.DataFrame(users)
df.cid = df.cid.fillna(-1)
tinkered = df.dropna()
print(len(tinkered))

# task 2 There must be a better way to solve this. 
#tinkered 

#byr
d = tinkered[tinkered.byr.str.len() == 4]
d.byr = pd.to_numeric(d.byr, errors='coerce').fillna(-1)
accepted_byr = (d.byr.le(2002)) & (d.byr.ge(1920))
d = d[accepted_byr]

#iyr
d = d[d.iyr.str.len() == 4]
d.iyr = pd.to_numeric(d.iyr, errors='coerce').fillna(-1)
accepted_iyr = (d.iyr.le(2020)) & (d.iyr.ge(2010))
d = d[accepted_iyr]

#eyr
d = d[d.eyr.str.len() == 4]
d.eyr = pd.to_numeric(d.eyr, errors='coerce').fillna(-1)
accepted_eyr = (d.eyr.le(2030)) & (d.eyr.ge(2020))
d = d[accepted_eyr]

#hgt
def check_hight(text_in):
    if 'cm' in text_in:
        val = int(text_in[:-2])
        if (150 <= val <= 193):
            return True

    if 'in' in text_in:
        val = int(text_in[:-2])
        if (59 <= val <= 76):
            return True    

    return False    

d = d[d.hgt.map(check_hight)]
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
d = d[d.hcl.str.match('#[a-z|0-9]')]

#eye color
color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
d = d[d.ecl.isin(color)]

#pid (Passport ID) - a nine-digit number, including leading zeroes.
d = d[d.pid.str.len() == 9]

print(d)
print(len(d))