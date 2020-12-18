import re
with open('input.txt') as f:equations = [eq.rstrip() for eq in f.readlines()]

def find_last_index(s, value):
    s_i = list(s)
    s_i.reverse()
    i = s_i.index(value)    
    return s[:-(i+1)], s[-i:]

def all_list(eq):
    temp = 0
    plus_evaluated = False
    evaluate_later = []
    while len(eq)>0:
        HEAD, TAIL = eq[0], eq[1:]
        if HEAD == '+': operator = HEAD
        elif HEAD == '*':
            if plus_evaluated: operator = HEAD
            else:
                evaluate_later += [temp, HEAD]
                temp = 0
        else: 
            if temp == 0:temp = HEAD
            elif operator in ['+', '*']:temp = evaluate(temp, operator, HEAD)                                   
            
        if len(TAIL)==0 and not plus_evaluated:
            eq=evaluate_later+[temp]
            plus_evaluated, temp = True,0                
        else:
            eq=TAIL
    return temp
        
def add_left2right(eq):
    temp = 0
    while len(eq)>0:
        HEAD, TAIL = eq[0], eq[1:]
        if HEAD in ['+', '*']:
            operator = HEAD
        else: 
            if temp == 0: temp = HEAD
            else: temp = evaluate(temp, operator, HEAD)                   
        eq=TAIL
    return temp
        
def evaluate(num_b,operator, num_a):    
    if operator == '+': return num_b+num_a
    elif operator == '*': return num_b*num_a

number= [f"{i}" for i in range(0,10)]
answers = []
def calculate(precedence):
    for eq in equations:    
        stack = []
        while len(eq)>0:
            HEAD, TAIL = eq[0], eq[1:]
            if HEAD==')':
                stack, vals = find_last_index(stack,'(')    
                res = precedence(vals)
                stack.append(res)        
            elif HEAD in['(','+', '*']:
                stack.append(HEAD)
            elif HEAD in number:
                stack.append(int(HEAD))
            elif HEAD==' ':pass
            eq=TAIL        
        res = precedence(stack)
        answers.append(res)
    print(sum(answers))

calculate(precedence=add_left2right)
calculate(precedence=all_list)