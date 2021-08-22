from collections import Counter
import functools

with open("file2.txt") as f: 
    lines = [l.strip() for l in f.readlines()]

print(lines)