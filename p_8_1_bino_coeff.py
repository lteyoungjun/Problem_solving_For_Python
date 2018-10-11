import numpy as np

cache = -1*np.ones((30,30))

def bino(n, r):
    if(r == 0 or n == r):
        return 1
    if cache[n][r] != -1:
        return cache[n][r]


    cache[n][r] = bino(n-1,r) + bino(n-1, r-1)
    return cache[n][r]

print(bino(5,2))


