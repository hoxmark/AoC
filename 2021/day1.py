with open('Input1.txt') as f:
    lines = [int(l) for l in f]


def find_num_of_increase(lines):
    res = []
    for i,v in enumerate(lines):
        #print(lines[i], lines[i-1])
        is_larger = lines[i]>lines[i-1]
        res.append(is_larger)
    return sum(res)



print(find_num_of_increase(lines))

#seq=[199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
seq=lines
window_size = 3

lines2 = []
for i in range(len(seq) - window_size + 1):
    s = seq[i: i + window_size]
    lines2.append(sum(s))
print(lines2)
print(find_num_of_increase(lines2))

