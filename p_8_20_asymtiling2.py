import numpy as np
from p_8_16_tiling import *
cache = -1*np.ones((101))

def asymtiling(width):
    if width <= 2:
        return 0

    ret = cache[width]
    if ret != -1:
        return ret

    ret = asymtiling(width-2)
    ret += asymtiling(width-4)
    ret += tiling(width-3)*2

    return ret

