
from functools import reduce

with open('input.txt') as f:
    lines = [l.rstrip().split(' ') for l in f]

def get_val_num(val_str):
    if val_str[:1] == '+':
        return int(val_str[1:])
    else: 
        return -int(val_str[1:])

def nop_func(counter, acc,val):
    counter =counter+1
    return counter, acc
 
def acc_func(counter, acc, val):
    acc = acc+get_val_num(val)
    counter =counter+1
    return counter, acc

def jmp_func(counter, acc,val):    
    counter = counter + get_val_num(val)
    return counter, acc
 
def eval(counter, opcode, acc, val):
    switcher = {
        'nop': nop_func,
        'acc': acc_func,
        'jmp': jmp_func,
    }
    
    func = switcher.get(opcode, lambda: "Invalid agrument")
    return func(counter, acc,val)
    
debug_history = {}
def infinite_loop_debugger(counter, opcode, variation):
    if counter == variation:        
        debug_history[counter] = opcode
        if opcode == 'nop':
            return counter, 'jmp'        
        if opcode == 'jmp':        
            return counter, 'nop'
        if opcode == 'acc':
            return counter, 'acc'
    else: 
        return counter, opcode

def run_task1():
    history = []
    counter = 0
    acc = 0
    while True:        
        opcode, val = lines[counter] 
        counter, acc = eval(counter, opcode, acc, val)
        
        if counter in history:
            #print(f'breaking at counter: {counter}, acc: {acc}')
            return acc             
        else:
            history.append(counter)

ans_task1 = run_task1()
print('ans_task1', ans_task1)

def run(variation):    
    history = []
    counter = 0
    acc = 0
    while counter<len(lines):        
        opcode, val = lines[counter]        
        counter, opcode = infinite_loop_debugger(counter, opcode, variation)    

        counter, acc = eval(counter, opcode,acc, val)
        if counter in history:
            #print(f"breaking at counter: {counter}, acc: {acc}")
            return False, counter, acc
        else:
            history.append(counter)
    return True, counter, acc

i = 0
while i < len(lines):
    res, counter, acc = run(i)    
    if res: 
        print('acc', acc)
        break
    i = i+1