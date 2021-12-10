#%% Day 4
with open('data/input4.txt') as f:
    rand_numbers = [num for num in f.readline().strip().split(",")]
    f.readline()
    lines = [l.split() for l in f]
    boards = []
    board = []

    for l in lines: 
        if len(l)==0:
            boards.append(board)
            board = []
        else: 
            board.append(l)

    boards.append(board)
found_board = []
print(rand_numbers)
def see_board():
    for b in boards: 
        for l in b:  print(l)
        print("\n")

def check_line(l):
    return sum([i=='x' for i in l])==5

def get_horizontal(lines, i):
    return [l[i] for l in lines]

def check_board(b, num):
   #final = [i+j for i in first for j in second] 
   horisontal_found = [check_line(v) for v in b]
   vertical_found = [ check_line(get_horizontal(b, i)) for i in range(len(b))]
   if any(horisontal_found) or any(vertical_found):
       print("BINGO")
       print(board)
       found_board = sum_numbers(b)
       print(found_board)
       print(found_board*int(num))
       return True

    
   else : 
       False, -1

def sum_numbers(b): 
    return sum([int(x) for i in b for x in i if x != 'x'])

def add_number(num): 
    for i_b, b in enumerate(boards):
        for i_l, l in enumerate(b):
            for i_n, n in enumerate(l):
                if n == num:
                    boards[i_b][i_l][i_n] = "x"

black_list = []
        

for num in rand_numbers: 
    add_number(num)
    for i, b in enumerate(boards):
        if i in black_list: 
            continue
    

        if check_board(b,num):
            black_list.append(i)
            



# %%
