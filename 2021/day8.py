#%%
from collections import Counter, defaultdict

with open('input8.txt') as f: 
    data = [l.strip().split(' | ') for l in f]
    wires = [l[0].split(" ") for l in data] #
    digits = [l[1].split(" ") for l in data] 
print(wires)
def day8_1():
    times_appeared = Counter()
    for ws, ds in zip(wires, digits):
        ds_lens = [len(d) for d in ds]
        times_appeared.update(ds_lens)
    print(times_appeared)
    l = [2,3,4,7]
    day8_1_ans = sum([times_appeared[x] for x in l])
    print(day8_1_ans)
day8_1()

#%%
def day8_2():
    all_results = []
    for w, d in zip(wires, digits):
        known = defaultdict(str)
        for i in w: 
            if len(i) == 2:
                known['1'] = i
            elif len(i) == 4:
                known['4'] = i
            elif len(i) == 3:
                known['7'] = i
            elif len(i) == 7:
                known['8'] = i
        for i in w: 
            #6ere 
            if i in known.values():
                continue

            if len(i) == 6: 
                # Om 4 er i den, så er det 9. 
                if set(known['4']).issubset(set(i)):
                    known['9'] = i
                    
                # Om 7 går i den så er det 0
                elif set(known['7']).issubset(set(i)):
                    known['0'] = i                
                    
                else: 
                    known['6'] = i                
                    
            #5ere 
            elif len(i) == 5:
                # Om 7 går i den så er det 3
                if set(known['7']).issubset(set(i)):
                    known['3'] = i
                                
                # om det er 3 i overlapp mellom 4 og i, så er det 5
                elif len(set(known['4'])&(set(i)))==3:
                    known['5'] = i
                    
                else: 
                    known['2'] = i                
                
            else: 
                assert(True), 'what? something is wrong'
        answer = []
        for di in d:    
            for k,v in known.items():        
                if sorted(v)==sorted(di):                            
                    answer.append(k)
                    break
        all_results.append(int("".join(answer)))    

    return sum(all_results)

day8_2()
# %%
