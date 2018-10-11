import numpy as np

MOD = 1000000007
cache = -1*np.ones((101))

def tiling(width):

    if width <= 1:
        return 1
    ret = cache[width]

    if ret != -1:
        return ret

    ret = tiling(width-1) + tiling(width-2)
    cache[width] = ret
    return ret

