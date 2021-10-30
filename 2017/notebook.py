#!/usr/bin/env python
# coding: utf-8

# # Advent of code 2017
# for tasks visit: https://adventofcode.com/2017/day/1

# In[1]:

from __future__ import annotations
from collections import Counter, defaultdict, namedtuple, deque
from itertools import permutations, combinations, product, chain
from functools import lru_cache
from typing import Dict, Tuple, Set, List, Iterator, Optional, Union

import numpy as np
import operator
import math
import ast
import sys
import re


# In[2]:


def data(day: int, parser=str, sep='\n', test=None) -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    if (sections := test) == None:
        sections = open(f'data/input{day}.txt').read().rstrip().split(sep)
    return [parser(section) for section in sections]


def do(day, *answers) -> Dict[int, int]:
    "E.g., do(3) returns {1: day3_1(in3), 2: day3_2(in3)}. Verifies `answers` if given."
    g = globals()
    got = []
    for part in (1, 2):
        fname = f'day{day}_{part}'
        if fname in g:
            got.append(g[fname](g[f'in{day}']))
            if len(answers) >= part:
                assert got[-1] == answers[part - 1], (
                    f'{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}')
    return got


# In[3]:


def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))


def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def rest(sequence) -> object: return sequence[1:]


def multimap(items: Iterable[Tuple]) -> dict:
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def prod(numbers) -> float:  # Will be math.prod in Python 3.8, but I'm in 3.7
    "The product of an iterable of numbers."
    result = 1
    for n in numbers:
        result *= n
    return result


def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return tuple(map(int, re.findall('-?[0-9]+', text)))


def atoms(text: str, ignore=r'', sep=None) -> Tuple[Union[int, str]]:
    "Parse text into atoms (numbers or strs), possibly ignoring a regex."
    if ignore:
        text = re.sub(ignore, '', text)
    return tuple(map(atom, text.split(sep)))


def atom(text: str) -> Union[float, int, str]:
    "Parse text into a single float or int or str."
    try:
        val = float(text)
        return round(val) if round(val) == val else val
    except ValueError:
        return text


def dotproduct(A, B) -> float: return sum(a * b for a, b in zip(A, B))


def mapt(fn, *args):
    "map(fn, *args) and return the result as a tuple."
    return tuple(map(fn, *args))

def minus(a,b):return tuple(map(lambda i, j: i - j, a, b))

cat = ''.join
flatten = chain.from_iterable
Char = str  # Type used to indicate a single character

# In[4]:
in1 = mapt(int, data(1)[0])

# In[5]:

def day1_1(digits):
    N = len(digits)
    return sum(digits[i]
               for i in range(N) if digits[i] == digits[i-1]
               )

def day1_2(digits):
    N = len(digits)
    steps = int(N/2)
    return sum(digits[i]
               for i in range(N) if digits[i] == digits[(i+steps) % N]
               )

do(1)

# In[120]:
in2 = data(2, sep='\n', parser=lambda x: mapt(int, x.split('\t')))
#in2 = data(2, test=[['5', '1', '9', '5'], [7, 5, 3], [2, 4, 6, 8]], parser=lambda x: mapt(int, x))

def day2_1(digits):
    return sum(
        max(i) - min(i)
        for i in digits
    )

def day2_2(rows):
    return sum(int(i/j)
               for row in rows
               for i, j in permutations(row, 2)
               if i % j == 0)

do(2)
# In[103]:
def make_square(iterations):
    def go_up(x):return (x[0]-1, x[1])
    def go_down(x):return (x[0]+1, x[1])
    def go_left(x):return (x[0], x[1]-1)
    def go_right(x):return (x[0], x[1]+1)
    def is_free(x):
        if grid[x] == 0: return True
        else: return False
    
    size = int(math.sqrt(iterations))*3
    grid = np.zeros((size,size))    
    origo = (int(size/2), int(size/2))
        
    counter_int = 2
    grid[origo] = 1
    counter = (origo[0]+0, origo[1]+1)
    grid[counter] = 2
    
    while counter_int < iterations:
        counter_int+=1
        if is_free(go_right(counter))  and is_free(go_up(counter)) and not is_free(go_left(counter)): #is_free(go_down(counter))
            counter = go_up(counter)
            grid[counter] = counter_int 

        elif is_free(go_right(counter)) and not is_free(go_down(counter)) and is_free(go_up(counter)) and is_free(go_left(counter)):
            counter = go_left(counter)
            grid[counter] = counter_int 
        
        elif not is_free(go_right(counter)) and not is_free(go_down(counter)) and is_free(go_up(counter)) and is_free(go_left(counter)):
            counter = go_left(counter)
            grid[counter] = counter_int 
        
        elif not is_free(go_right(counter)) and is_free(go_down(counter)) and is_free(go_left(counter)): #
            counter = go_down(counter)
            grid[counter] = counter_int 
        
        elif is_free(go_right(counter)) and is_free(go_down(counter)) and not is_free(go_up(counter)) : #is_free(go_left(counter))
            counter = go_right(counter)
            grid[counter] = counter_int 
       
    return grid, origo

# In[116]:
def day3_1(value):  
    grid, origo = make_square(value)    
    x,y = minus(origo, np.where(grid==value))
    return abs(int(x))+abs(int(y))

in3 = 325489
# day3_1(325489)
do(3)

# In[114]:


# 
