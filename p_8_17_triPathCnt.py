import numpy as np
from p_8_9_trianglePath2 import *

cacheCount = -1*np.ones((100,100))

def count(y, x):

    if y == n-1:
        return 1

    ret = cacheCount[y][x]

    if ret != -1:
        return ret

    ret = 0

    if(path(y+1,x) >= path(y+1,x+1)):
        ret += count(y+1,x)

    if (path(y + 1, x) <= path(y + 1, x + 1)):
        ret += count(y + 1, x + 1)

    return ret

print(count(0,0))


