### Task 1 
import re

with open('input.txt') as f:
    lines = [re.split('[- :]', l.rstrip()) for l in f]

res = len([ password for (minimum, maximum, letter, _, password) in lines if int(minimum) <= password.count(letter) <= int(maximum)])
print(res)

res2 = len([ password for (first, second, letter, _, password) in lines if (password[int(first)-1]==letter) != (password[int(second)-1]==letter)])
print(res2)
