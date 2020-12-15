### Task 1 
from collections import defaultdict

def elf_game(init, get_number):
    spoken = defaultdict(list)
    for i in range(0,get_number):
        if i%1000000==0:
            print(i)    
        turn = i+1

        if len(init)>i and init[i] != None:
            number = init[i]        
            spoken[number]=[]
        else:             
            #print("number last spoken is now: ", number)
            if number in spoken.keys() and len(spoken[number])<=1 :
                number = 0
            else: 
                number = spoken[number][-1]-spoken[number][-2]

        spoken[number].append(turn)
    return number

ans1 = elf_game([6,4,12,1,20,0,16], 2020)
print(ans1)
ans2 = elf_game([6,4,12,1,20,0,16], 30000000)
print(ans2)