import numpy as np

MOD = 10*1000*1000

cache = -1*np.ones((101,101))

def poly(n,first):

    if n == first:
        return 1

    ret = cache[n][first]

    if ret != -1:
        return ret

    ret = 0

    for second in range(1, n - first +1):
        ret += (first + second -1)*poly(n-first, second)%MOD

    cache[n][first] = ret

    return ret

print(poly(2,1) + poly(2,2))
a = 0

for i in range(1,5):
    a += poly(4, i)

print(a)