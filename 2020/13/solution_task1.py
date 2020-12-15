### Task 1 
import itertools
import math

with open('input.txt') as f:    
    arival = int(f.readline().rstrip())
    bus_interval = [int(i) for i in f.readline().split(',') if i != 'x']

print(arival, bus_interval)

def calulate_allpossible(bus, max_time):
    time = math.floor(max_time/bus)
    return bus*(time+1)

times = {k:calulate_allpossible(k, arival) for k in bus_interval}
earliest = min(times, key=times.get)
wait = (times[earliest]-arival)
res = wait*earliest
print(res)