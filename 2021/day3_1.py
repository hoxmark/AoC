from collections import defaultdict
with open('Input3.txt') as f:
    lines = [l.strip() for l in f]

print(lines)

lines = [
        '00100',
       '11110',
       '10110',
       '10111',
       '10101',
       '01111',
       '00111',
       '11100',
       '10000',
       '11001',
       '00010',
       '01010']

ones = defaultdict(lambda :0)
zeros = defaultdict(lambda :0)
for l in lines:
    for i,b in enumerate(l): 
        if b == '1':
            ones[i] += 1
        elif b == '0':
            zeros[i] += 1

most_common = []
for i in range(len(ones)): 
    b = 0 if zeros[i] > ones[i] else 1
    most_common.append(str(b))

print(most_common)
most_common = "".join(most_common)

epsilon_rate  =  ''.join(['1' if i == '0' else '0'
                         for i in most_common])

epsilon_rate = int(epsilon_rate, 2)

gamma_rate = int(most_common, 2) 


print(epsilon_rate, gamma_rate, epsilon_rate*gamma_rate)

    
lines = [
        '00100',
       '11110',
       '10110',
       '10111',
       '10101',
       '01111',
       '00111',
       '11100',
       '10000',
       '11001',
       '00010',
       '01010']

def fo(values, i): 
    return [x for x in values if x[i]== most_common[i]] 
   
def fc(values, i): 
    return [x for x in values if x[i] != most_common[i]]

def find_oxy():
    l =  list(lines)
    for i in range(len(ones)): 
        l = fo(l, i)
        print(l)
        if len(l) < 2: 
            return int(l[0], 2)

def find_co2():
    l = list(lines)
    for i in range(len(ones)):
        l = fc(l, i)
        if len(l) < 2: 
            return int(l[0], 2)
print("most_common", most_common)
o = find_oxy()
print(o)

c = find_co2()
print(c)

print('res', c*o)


