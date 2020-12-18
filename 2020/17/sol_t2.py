import functools
import itertools
import numpy as np
with open('input.txt') as f:
    seats = [ ['#'==x for x in list(l.rstrip())] for l in f]
print(seats)
z = np.array(seats)# set midle size
z_minus_1 = np.zeros(z.shape)
z_plus_1 = np.zeros(z.shape)

cube = np.stack((z_minus_1,z,z_plus_1), axis=0)
print(cube.shape)
hypercube = np.expand_dims(cube, axis=0)

print(hypercube)
print(hypercube.shape)
cube = hypercube
pad_size=10
cube=np.pad(cube, ((pad_size+1,pad_size+1), (pad_size,pad_size), (pad_size,pad_size), (pad_size,pad_size)), 'constant')
print(cube)
print(cube.shape)

#borrowed from the internett
def surrounding(x, idx, radius=1, fill=0):
    """ 
    Gets surrounding elements from a numpy array 

    Parameters: 
    x (ndarray of rank N): Input array
    idx (N-Dimensional Index): The index at which to get surrounding elements. If None is specified for a particular axis,
        the entire axis is returned.
    radius (array-like of rank N or scalar): The radius across each axis. If None is specified for a particular axis, 
        the entire axis is returned.
    fill (scalar or None): The value to fill the array for indices that are out-of-bounds.
        If value is None, only the surrounding indices that are within the original array are returned.

    Returns: 
    ndarray: The surrounding elements at the specified index
    """

    assert len(idx) == len(x.shape)

    if np.isscalar(radius): radius = tuple([radius for i in range(len(x.shape))])

    slices = []
    paddings = []
    for axis in range(len(x.shape)):
        if idx[axis] is None or radius[axis] is None:
            slices.append(slice(0, x.shape[axis]))
            paddings.append((0, 0))
            continue

        r = radius[axis]
        l = idx[axis] - r 
        r = idx[axis] + r

        pl = 0 if l > 0 else abs(l)
        pr = 0 if r < x.shape[axis] else r - x.shape[axis] + 1

        slices.append(slice(max(0, l), min(x.shape[axis], r+1)))
        paddings.append((pl, pr))

    if fill is None: return x[slices]
    return np.pad(x[slices], paddings, 'constant', constant_values=fill)



def check_idx_and_return(idx, cube):
    current_val = cube[idx]
    nearby_cube = surrounding(cube,idx)    
    res = np.sum(nearby_cube) - current_val #dont want to count the middle, its not an neighbour
    if current_val == 0:
        if res == 3:        
            return 1
    else:
        if res == 2 or res ==3:
            return 1
    
    return 0

from itertools import product
amin, amax = 0, cube.shape[0]
l = list(product(range(amin, amax), repeat=4))

for c in range(1,7):
    new_cube = cube.copy()
    check_id = functools.partial(check_idx_and_return, cube=cube)
    for i in l:        
        res = check_id(i)
        new_cube[i] = res
    s = np.sum(new_cube)
    print(f"After {c} cycle:")
    print(s)

    cube = new_cube.copy()
    