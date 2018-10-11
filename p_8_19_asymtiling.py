from p_8_16_tiling import *

def asymtiling(width):

    if(width % 2 == 1):
        return (tiling(width) - tiling(width//2) + MOD)%MOD

    ret = tiling(width)

    ret = (ret - tiling(width//2) + MOD)%MOD
    ret = (ret - tiling(width//2-1) + MOD)%MOD

    return ret

print(asymtiling(5))