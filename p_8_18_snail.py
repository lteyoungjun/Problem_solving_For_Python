import numpy as np

MAX_N = 100

n = int(input("우물은 총 몇 m인가요:"))
m = int(input("몇 일 안에 올라가야 하나요:"))

cache = -1*np.ones((MAX_N,2*MAX_N+1))

def climb(days, climbed):

    if days == m:
        if climbed >= n:
            return 1
        else:
            return 0

    ret = cache[days][climbed]

    if ret != -1:
        return ret

    ret = 0.75*climb(days+1,climbed+1) + 0.25*climb(days+1,climbed+2)
    #ret = climb(days+1,climbed+1) + climb(days+1,climbed+2)

    cache[days][climbed] += ret

    return ret

print(climb(0,0))
