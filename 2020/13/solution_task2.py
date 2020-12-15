### Task 1 
import itertools
import math

with open('input.txt') as f:    
    arival = int(f.readline().rstrip())
    bus_interval = [i for i in f.readline().split(',')]

l = bus_interval
busses = {int(b):i for i, b in enumerate(l) if b!='x'}

def check_valid(t, busses):
    accepted = []    
    for i, (buss_id, offset) in enumerate(busses.items()):
        if (t+offset)%buss_id != 0:             
            return False, accepted
        
        accepted.append(buss_id)        
    return True, accepted

found, iterate_value, t = False,  1, 1
longest_accepted = []
last_second_found = 0
counter=0
found_best = 0
while not found:
    counter+=1    
    found, accepted = check_valid(t, busses)
    
    if found:
        print("DONE: ")        
        print(t, accepted)
        break

    #if len(accepted)>1:
    if len(accepted)>len(longest_accepted):    
        print(t, accepted)
        if last_second_found == 0:
            last_second_found = t
        else:
            iterate_value = t-last_second_found
            print('iterate_value', iterate_value)
            longest_accepted = accepted
            last_second_found = 0

    t = t + iterate_value

print('ans: ', t)
print('counter', counter)