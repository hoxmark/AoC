#%% Day 17
from collections import namedtuple
import re

with open('data/input17.txt') as f:
    x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', f.readline()))

P = namedtuple('Point', ['x', 'y'])
Velocity = namedtuple('Velocity', ['x', 'y'])


def calc_drag(v: Velocity) -> P:
    """
    ue to drag, the probe's x velocity changes by 1 toward the value 0; 
    that is, it decreases by 1 if it is greater than 0, 
    increases by 1 if it is less than 0, or does not change if it is already 0.
    """
    new_v = Velocity(v.x, v.y)
    if v.x > 0:
        new_v = P(new_v.x - 1, new_v.y)
    elif v.x < 0:
        new_v = P(new_v.x + 1, new_v.y)

    return new_v


# x (forward) and y (upward, or downward if negative)
def step(c: P, v: Velocity):
    #The probe's x and y position increases by its x and y velocity.
    c = P((c.x + v.x), (c.y + v.y))

    v = calc_drag(v)

    #Due to gravity, the probe's y velocity decreases by 1.
    v = Velocity(v.x, v.y - 1)
    return c, v


def is_c_in_target(c: P) -> bool:
    if x1 <= c.x <= x2 and y1 <= c.y <= y2:
        return True


sp = P(0, 0)
lowest_point_worth_looking = min([y1, y2])
farthest_point_worth_looking = max([x1, x2])


def test_t(init_cord: P, init_v: Velocity):
    highest_y = 0
    c, v = init_cord, init_v
    for i in range(1, 10000):
        c, v = step(c, v)
        if c.y > highest_y: highest_y = c.y

        if is_c_in_target(c):
            return True, highest_y

        if c.y < lowest_point_worth_looking:
            return False, highest_y

        if c.x > farthest_point_worth_looking:
            return False, highest_y

    return False, highest_y


hits = {}
highest_y_all = 0
for i in range(0, (x2+1)):    
    for j in range(y1, 300):        

        init_v = Velocity(i, j)
        hit, hy = test_t(sp, init_v)

        if hit:
            hits[init_v] = hy

highest_init_v = max(hits, key=hits.get)
print(highest_init_v)
print('task1', hits[highest_init_v], highest_init_v)
print('task2', len(hits))


#%% for test case 
def tests():
    assert (test_t(sp, Velocity(7, 2))[0])
    assert (test_t(sp, Velocity(6, 3))[0])
    assert (test_t(sp, Velocity(9, 0))[0])
    assert ((False == test_t(sp, Velocity(17, -4))[0]))

tests()

# %% Later learnt
def task1():
    y = min([y1,y2])
    return abs(y) * (abs(y) - 1) / 2
task1()
# %%
