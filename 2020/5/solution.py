### Task 5 
with open('input.txt') as f:
    lines = [(l.rstrip()[:7], l.rstrip()[7:]) for l in f]

def check_row(l, rows_left, splitter):
    half = int((len(rows_left)/2))
    if l[0] == splitter:    
        rows_to_return = rows_left[:half]        
    else:
        rows_to_return = rows_left[half:]

    if len(l)==1: return rows_to_return
    
    return check_row(l[1:],  rows_to_return, splitter)

def calc(rows,cols):
    row = check_row(rows, list(range(128)), 'F')
    col = check_row(cols, list(range(8)), 'L')
    return row[0]*8+col[0]
seat_ids = [calc(rows,cols) for rows,cols in lines]
print(max(seat_ids))

#task2
s = iter(sorted(seat_ids))
for i in s:
    if i+1 != next(s):
        print(i,next(s), 'ans:', i+1)

        